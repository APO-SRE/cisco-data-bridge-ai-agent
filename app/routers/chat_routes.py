################################################################################
## cisco-data-bridge-domain-index/routers/chat_routes.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import os
import json
import logging
from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# LLM modules
from app.llm.function_dispatcher import dispatch_function_call
from app.llm.llm_factory import get_llm_client
from app.llm.prompt_templates import (
    BASE_SYSTEM_PROMPT_DOCS_ONLY,
    BASE_SYSTEM_PROMPT_GENERAL,
    BASE_SYSTEM_PROMPT_EVENT,
    BASE_SYSTEM_PROMPT_LOB,
    USER_PROMPT_TEMPLATE,
    HTML_MERAKI_APS_WITH_MESSAGE_PROMPT
)
from app.llm.function_definitions import FUNCTION_DEFINITIONS

# Retrievers
from retrievers.azure_search_retriever import AzureSearchRetriever
from retrievers.chroma_retriever import ChromaRetriever
from retrievers.elastic_retriever import ElasticRetriever
from retrievers.null_retriever import NullRetriever

# ------------------------------------------------------------------------------
# Import the CiscoSpacesClient so we can optionally download floor plan images
# ------------------------------------------------------------------------------
from cisco_integrations.cisco_spaces_client import CiscoSpacesClient

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Load environment variables
load_dotenv()

router = APIRouter()

# -----------------------------------------------------
# Environment / Config
# -----------------------------------------------------
RAG_TYPE = os.getenv("RAG_TYPE", "azure_search")
TOP_K = int(os.getenv("AZURE_SEARCH_TOP_K", "5"))
ENABLE_IN_DOMAIN = os.getenv("AZURE_SEARCH_ENABLE_IN_DOMAIN", "false").lower() == "true"

# Catalyst environment variables
CATALYST_USERNAME = os.getenv("CISCO_CATALYST_USERNAME", "")
CATALYST_PASSWORD = os.getenv("CISCO_CATALYST_PASSWORD", "")
CATALYST_URL = os.getenv("CISCO_CATALYST_URL", "https://sandboxdnac.cisco.com:443")
CATALYST_VERSION = os.getenv("CISCO_CATALYST_VERSION", "2.3.7.6")
print("CATAYLYST USERNAME", CATALYST_USERNAME)
print("CATALYST PASSWORD", CATALYST_PASSWORD)
print("CATALYST URL", CATALYST_URL)

# Meraki environment variables
MERAKI_API_KEY = os.getenv("CISCO_MERAKI_API_KEY", "")
SPACES_TOKEN = os.getenv("CISCO_SPACES_API_KEY", "")
WEBEX_TOKEN = os.getenv("CISCO_WEBEX_TOKEN", "")

# Check booleans to see if the platform is “enabled”
ENABLE_CATALYST_CENTER = os.getenv("ENABLE_CATALYST_CENTER", "false").lower() == "true"
ENABLE_MERAKI = os.getenv("ENABLE_MERAKI", "false").lower() == "true"
print("ENABLE CATALYST CENTER", ENABLE_CATALYST_CENTER)
SPACES_TOKEN = os.getenv("CISCO_SPACES_API_KEY", "")
WEBEX_TOKEN = os.getenv("CISCO_WEBEX_TOKEN", "")


# -----------------------------------------------------
# Pydantic model for user input
# -----------------------------------------------------
class UserQuery(BaseModel):
    message: str
    lob_index: str = ""


# -----------------------------------------------------
# A central dictionary for all LOB keywords
# -----------------------------------------------------
LOB_KEYWORDS_MAP = {
    "lob-agriculture": [
        "soil", "sandy", "clay", "ph", "cover crop", "crop rotation",
        "pest", "rootworm", "alfalfa", "soybeans", "wheat", "sulfur application",
        "livestock", "cows", "goats", "barn", "milk", "harvest", "hay",
        "water retention", "irrigation", "flooding", "hail damage", "orchard",
        "farm", "pasture", "fields", "crop cycle", "organic spray", "cutworm"
    ],

    "lob-automotive": [
        "production line", "battery supply", "EV", "electric vehicle", "hybrid",
        "sedan", "truck", "SUV", "infotainment", "warranty", "recall",
        "diesel", "towing", "emission", "maintenance records", "dealership feedback",
        "factory ramp", "chassis", "over-the-air updates", "fast-charging",
        "crossover", "fuel efficiency", "model specs", "hydrogen concept",
        "service center"
    ],

    "lob-biotechnology": [
        "CRISPR", "CAR-T", "mRNA", "scaffolding", "lab experiments",
        "clinical trials", "off-target edits", "immune response", "gene editing",
        "research project", "distribution strategy", "adverse findings", "pre-IND",
        "therapeutic", "lymphoma", "inflammation", "lab data", "biosafety",
        "regulatory submission", "exemption request", "probiotic", "microbiome"
    ],

    "lob-construction": [
        "foundation", "framing", "piling", "geotechnical", "concrete",
        "materials inventory", "crew scheduling", "building codes",
        "steel erection", "warehouse expansion", "school renovation",
        "project phases", "drywall", "rebar", "inspection", "subcontractor",
        "LEED-compliant", "fire-rated", "excavation", "basement"
    ],

    "lob-consumer-electronics": [
        "smartphone", "smartwatch", "wireless earbuds", "4K TV", "gaming console",
        "RMA", "warranty", "accidental coverage", "battery drain", "sales invoice",
        "promotional discount", "earbuds", "repair ticket", "bundle deal",
        "customer feedback", "invoice", "TV upgrade event"
    ],

    "lob-cybersecurity": [
        "phishing", "ransomware", "LockBox", "SQL injection", "DDoS", "APT",
        "zero-day", "threat intel", "incident", "remediation", "compromise",
        "firewall", "endpoint security", "MSSP coverage", "malware",
        "botnet", "intrusion", "breach", "SOC", "IR retainer", "spam filter",
        "threat detection", "vulnerability scanning"
    ],

    "lob-e-commerce": [
        "order", "cart", "refund", "coupon", "promo code", "discount",
        "bulk purchase", "shipping", "inventory", "SKU", "fulfillment",
        "payment", "logistics", "tracking", "delivery", "checkout",
        "returns", "RMA", "priority shipping", "customer feedback"
    ],

    "lob-education": [
        "course enrollment", "faculty", "exam schedule", "syllabus",
        "student advising", "academic probation", "lab practical",
        "bio 310", "math 201", "office hours", "professor", "tutoring",
        "essay", "incomplete course", "minor", "cs 420", "gpa"
    ],

    "lob-energy-utilities": [
        "plant outage", "maintenance_outages", "battery storage", "wind farm",
        "transmission line", "time-of-use tariff", "coal station", "net metering",
        "renewables", "capacity reduction", "power factor", "grid infrastructure",
        "hydro upgrade", "turbine", "solar farm", "kWh", "battery pilot",
        "emissions retrofit", "billing"
    ],

    "lob-entertainment-media": [
        "streaming", "season", "episode", "reality show", "viewership",
        "movie", "post-production", "children's show", "documentary",
        "music festival", "concert series", "venue", "advertising campaign",
        "licensing", "talent roster", "brand sponsor", "ticket vendor",
        "broadcast", "box office", "merchandise"
    ],

    "lob-financial": [
        "investment portfolio", "equities", "bonds", "municipal bonds", "wire transfer",
        "AML", "compliance checks", "Q4 earnings", "profit margin", "revenue",
        "crypto", "BTC", "ETH", "retirement contributions", "mortgage",
        "loans", "interest-only", "cost-cutting", "operational expense",
        "merger", "due diligence", "shareholders meeting", "corporate report",
        "high-yield", "KYC", "dividends", "asset allocation", "rebalance"
    ],

    "lob-food-and-beverage": [
        "menu item", "cheeseburger", "vegan wrap", "IPA beer", "organic salad",
        "cheesecake", "supplier", "food safety", "salmonella test", "keg",
        "catering order", "production record", "beef patties", "GreenLeaf produce",
        "strawberry", "dessert trays", "brew master", "batches", "sales orders"
    ],

    "lob-gaming": [
        "fantasy rpg", "co-op", "level cap", "arcade flight sim", "leaderboard",
        "futuristic fps", "clan territory", "sandbox building", "turn-based strategy",
        "patch notes", "in-game transactions", "skin bundle", "mod expansions",
        "wizard", "battlequest", "skyracer", "cyberstrike", "citycraft",
        "tactical legends", "tournament", "clan war", "e-sports"
    ],

    "lob-government-national-security": [
        "extremist activity", "sector", "cyber threat", "redcipher", "maritime security",
        "bomb threat", "capitol complex", "smuggling", "defense appropriations",
        "special operations", "firewallnext", "agency operations", "security events",
        "border security", "top secret", "national broadcasting continuity",
        "data privacy", "bill", "legislation", "task force", "strategic plan", "ops code"
    ],

    "lob-healthcare": [
        "patient", "appointment", "physician", "nurse", "lab test", "cardiology",
        "pediatrics", "hematology", "billing codes", "policy on cancellations",
        "allergy appointment", "fasting", "diabetes follow-up", "neurology",
        "blood pressure", "A1C", "vaccine updates", "medical record",
        "pending confirmation", "hospital", "clinic", "doctor", "nurse"
    ],

    "lob-hospitality": [
        "conference hall", "booking", "housekeeping", "inn", "family suite",
        "ski package", "airport suite", "loyalty tier", "spa facility",
        "wedding block", "complaint", "property listings", "meeting room discount",
        "silver tier", "basic tier", "housekeeping schedule", "off-season closure",
        "corporate booking", "post-event cleanup"
    ],

    "lob-human-resources": [
        "employee", "manager", "performance review", "recent hires", "finance department",
        "sales commission", "training", "hr analytics", "referral applicant",
        "leadership essentials", "payroll", "recruitment", "applicant",
        "performance rating", "salary", "base salary", "stock options",
        "interview feedback"
    ],

    "lob-information-technology-and-services": [
        "managed it", "cloud migration", "devops pipeline", "cybersecurity assessment",
        "data analytics", "etl pipeline", "BI dashboards", "service offerings",
        "compliance audits", "iso 27001", "pci-dss", "aws architecture",
        "azure baseline", "rmm", "patch scheduling", "project tasks",
        "pen testing", "vulnerability scanning"
    ],

    "lob-insurance": [
        "policy", "coverage limit", "claims", "deductible", "premium payment",
        "homeowners", "auto coverage", "collision claim", "life insurance",
        "commercial property", "underwriting rules", "storm damage", "health plan",
        "out-of-pocket", "claim timeline", "complaint about claims", "kitchen fire",
        "policy renewal", "term life", "premium", "oop limit", "feedback on claim"
    ],

    "lob-legal-services": [
        "case records", "contract dispute", "estate probate", "personal injury",
        "mergers and acquisitions", "patent infringement", "retainer agreement",
        "court filings", "client_contracts", "motion to compel", "compliance policies",
        "billing_invoices", "flat fee", "contingency", "probate", "demand letter"
    ],

    "lob-manufacturing": [
        "injection molding", "metal stamping", "welding run", "assembly line",
        "paint defects", "quality inspections", "production plans", "supplier invoices",
        "maintenance schedules", "inventory records", "defect rate", "robotic welding",
        "resin pellets", "spot welds", "conveyor", "drip marks"
    ],

    "lob-marketing-and-advertising": [
        "digital ads campaign", "tv spot", "email campaign", "direct mail",
        "influencer collaboration", "billboards", "client budget", "creative assets",
        "ad spend invoices", "performance metrics", "brand recall", "CTR", "ROI",
        "comedic angle", "social media push", "out-of-home ads"
    ],

    "lob-mining-and-natural-resources": [
        "iron ore project", "open-pit copper", "coal mining", "gold project",
        "rare earth", "tailings pond", "equipment maintenance", "environmental audits",
        "drill rig", "haul truck", "extraction site", "deep boreholes", "borehole",
        "methane ventilation", "water discharge permit"
    ],

    "lob-non-profit": [
        "fundraising_campaigns", "donor records", "corporate pledge", "food drive",
        "scholarship fund", "clean water initiative", "volunteer activities",
        "impact_reports", "community health fair", "winter coat drive",
        "project_funding", "monthly donor", "bulk food", "coats distribution"
    ],

    "lob-oil-and-gas": [
        "offshore exploration", "onshore exploration", "shalepeak", "arctic shelf",
        "sour gas", "HSE", "production field", "drilling rig", "top drive overhaul",
        "fracking pump", "NGL shipment", "BOP test", "condensate", "ice management",
        "wellhead inspection"
    ],

    "lob-pharmaceuticals": [
        "neocure", "viraxin", "analge-patch", "generic antibiotic", "phase ii",
        "adverse_events", "distribution_logistics", "production_batches",
        "regulatory_submissions", "injectable device", "glucose monitor",
        "IND application", "ANDA", "stability data", "patch reformulation"
    ],

    "lob-professional-services": [
        "management consulting", "financial advisory", "HR talent solutions",
        "IT & digital transformation", "marketing & brand advisory",
        "compliance_standards", "ISO 9001", "peer review", "client deliverables",
        "M&A due diligence", "org design", "valuation model", "recruitment strategy"
    ],

    "lob-real-estate": [
        "property listing", "tenant records", "commercial unit", "condo",
        "luxury penthouse", "maintenance requests", "property sales", "lease",
        "rent invoice", "HVAC repair", "suburban house", "downtown apartment",
        "partial rent payment", "property listing id"
    ],

    "lob-retail": [
        "men’s running shoes", "yoga pants", "headphones", "smartwatch",
        "store inventory", "loyalty tier", "sales transactions", "returns_exchanges",
        "cash purchase", "promotions", "defective item", "discount code",
        "refund", "platinum loyalty", "unisex hoodie"
    ],

    "lob-social-services": [
        "youth mentorship", "elderly assistance", "job training", "homeless outreach",
        "family counseling", "intake forms", "outcome_reports", "client_cases",
        "staff_records", "volunteer activities", "academic challenges",
        "daily meal distribution", "case coordinator"
    ],

    "lob-state-local-government": [
        "neighborhood safety", "council_meetings", "permits_licenses",
        "small business growth", "public transportation", "community health outreach",
        "public projects", "resident_records", "ward", "green energy initiative",
        "solar permit", "road widening", "city council"
    ],

    "lob-telecommunications": [
        "mobile plan", "family plan", "fiber internet", "business broadband",
        "unlimited data", "combined billing", "network outages", "support ticket",
        "LTE upgrade", "international calls", "invoice", "bundling discount",
        "late payment", "overseas call glitch"
    ],

    "lob-transportation-and-logistics": [
        "truck route", "van shuttle", "rail freight", "ship cargo", "air cargo flight",
        "shipment id", "freight invoice", "warehouse inventory", "maintenance records",
        "port terminal", "distribution center", "driver", "fleet schedules",
        "cargo hub", "daily express packages"
    ]
}


# -----------------------------------------------------
# Helper: get_retriever
# -----------------------------------------------------
def get_retriever() -> object:
    """
    Choose a retriever class based on RAG_TYPE env var.
    """
    logging.info(f"RAG_TYPE set to: {RAG_TYPE}")
    if RAG_TYPE == "azure_search":
        return AzureSearchRetriever()
    elif RAG_TYPE == "chroma":
        return ChromaRetriever()
    elif RAG_TYPE == "elastic":
        return ElasticRetriever()
    else:
        return NullRetriever()


# -----------------------------------------------------
# Helper: create_messages (general doc-based RAG)
# -----------------------------------------------------
def create_messages(user_input: str, retrieved_docs: List[dict], use_general_knowledge: bool = False) -> List[dict]:
    logging.debug(f"Retrieved documents: {retrieved_docs}")
    if retrieved_docs and not use_general_knowledge:
        docs_str = "\n\n".join([doc.get("content", "") for doc in retrieved_docs])
        system_content = f"{BASE_SYSTEM_PROMPT_DOCS_ONLY}\n\nYou have access to the following documents:\n{docs_str}"
    elif use_general_knowledge:
        system_content = BASE_SYSTEM_PROMPT_GENERAL
    else:
        system_content = BASE_SYSTEM_PROMPT_DOCS_ONLY

    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": USER_PROMPT_TEMPLATE.format(user_query=user_input)},
    ]


# -----------------------------------------------------
# Helper: create_messages_for_events
# -----------------------------------------------------
def create_messages_for_events(user_input: str, retrieved_docs: List[dict]) -> List[dict]:
    doc_texts = []
    for doc in retrieved_docs:
        content_str = doc.get("content", "")
        additional_info = doc.get("additional_info", {})
        if additional_info:
            content_str += "\n\nAdditional Info JSON:\n" + json.dumps(additional_info, indent=2)
        doc_texts.append(content_str)

    docs_str = "\n\n".join(doc_texts)
    system_content = f"""{BASE_SYSTEM_PROMPT_EVENT}

You have access to the following event documents:
{docs_str}
"""
    user_content = USER_PROMPT_TEMPLATE.format(user_query=user_input)
    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ]


# -----------------------------------------------------
# Helper: create_messages_for_lob
# -----------------------------------------------------
def create_messages_for_lob(user_input: str, retrieved_docs: List[dict]) -> List[dict]:
    doc_texts = []
    for doc in retrieved_docs:
        content_str = doc.get("content", "")
        metadata_str = doc.get("metadata", "")
        if metadata_str:
            content_str += "\n\nAdditional Metadata:\n" + metadata_str
        doc_texts.append(content_str)

    docs_str = "\n\n".join(doc_texts)
    system_content = f"""{BASE_SYSTEM_PROMPT_LOB}

You have access to the following LOB documents:
{docs_str}
"""
    user_content = USER_PROMPT_TEMPLATE.format(user_query=user_input)
    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ]


# -----------------------------------------------------
# Helper: finalize Meraki AP data with message
# -----------------------------------------------------
def finalize_meraki_aps_with_message(llm_client: AzureOpenAIClient, function_result: dict) -> str:
    """
    This helper uses the specialized HTML_MERAKI_APS_WITH_MESSAGE_PROMPT
    to produce HTML output that includes 'message' and 'access_points'.
    """
    # Convert dict to JSON for the user input
    json_str = json.dumps(function_result, indent=2)

    second_messages = [
        {
            "role": "system",
            "content": HTML_MERAKI_APS_WITH_MESSAGE_PROMPT
        },
        {
            "role": "user",
            "content": json_str
        }
    ]

    response = llm_client.call_llm(second_messages)
    final_html = response.choices[0].message.get("content", "").strip()
    return final_html


# -----------------------------------------------------
# Main chat route (with second LLM call for final summary)
# -----------------------------------------------------
@router.post("/")
async def chat_route(query: UserQuery, request: Request):
    logging.info(f"Received user query: {query.message}")

    # ------------------------------------------------------------------
    # A) Check if user wants to "download floor plan" (Spaces image)
    #    (simple keyword detection—example only)
    # ------------------------------------------------------------------
    user_text_lower = query.message.lower()
    if "download" in user_text_lower and "floor plan" in user_text_lower:
        # Hard-coded example: parse or set the tenant_id, image_path, etc.
        tenant_id = "15650"
        image_path = (
            "mapservices/floor/1740f8692294427345852f81db601f9b7067447c76ec874b964edf1136c8ed6b/"
            "6b2a502d16ce911514e030964b55e2f9"
        )
        image_type = "png"
        local_filename = "floor_sjc12_1.png"

        spaces_client = CiscoSpacesClient()
        result = spaces_client.get_floor_image(
            tenant_id=tenant_id,
            image_path=image_path,
            image_type=image_type,
            save_local=True,  # <--- Key addition to store under app/assets/
            local_filename=local_filename
        )

        # If we got a dict with "error", return that
        if isinstance(result, dict) and "error" in result:
            return JSONResponse({
                "role": "assistant",
                "label": "Cisco AI",
                "response": f"Could not download the floor image: {result['error']}"
            })

        # Otherwise success
        msg = f"Floor plan downloaded & saved to app/assets/{local_filename}."
        logging.info(msg)
        return JSONResponse({
            "role": "assistant",
            "label": "Cisco AI",
            "response": msg
        })

    # --- Step B: Decide about Meraki / Catalyst usage ---
    user_text = query.message.lower()
    mentions_meraki = "meraki" in user_text
    mentions_catalyst = ("catalyst" in user_text) or ("dna center" in user_text)
    both_enabled = (ENABLE_MERAKI and ENABLE_CATALYST_CENTER)

    extra_instructions = []
    if mentions_meraki and not mentions_catalyst:
        if not ENABLE_MERAKI:
            extra_instructions.append(
                "User asks for Meraki but it is disabled. Attempt fallback or respond with not available."
            )
        else:
            extra_instructions.append(
                "User specifically requests Meraki. Use Meraki-based function calls only."
            )
    elif mentions_catalyst and not mentions_meraki:
        if not ENABLE_CATALYST_CENTER:
            extra_instructions.append(
                "User asks for Catalyst but it is disabled. Attempt fallback or respond with not available."
            )
        else:
            extra_instructions.append(
                "User specifically requests Catalyst. Use Catalyst-based function calls only."
            )
    else:
        # Neither specifically requested or possibly both
        if both_enabled:
            extra_instructions.append(
                "Both Meraki and Catalyst are enabled. Feel free to call either or both to answer the query."
            )
        elif ENABLE_MERAKI:
            extra_instructions.append("Only Meraki is enabled. Catalyst is not.")
        elif ENABLE_CATALYST_CENTER:
            extra_instructions.append("Only Catalyst is enabled. Meraki is not.")
        else:
            extra_instructions.append("No major integrations are enabled. Only fallback solutions are possible.")

    # -----------------------------------------------------
    # 1) Perform RAG retrieval or fallback
    # -----------------------------------------------------
    retriever = get_retriever()
    llm_client = get_llm_client()

    logging.info(f"retriever.lob_index (from ENV) => '{retriever.lob_index}'")

    # If user didn't provide a lob_index, default to the retriever's
    effective_lob_index = query.lob_index.strip().lower()
    if not effective_lob_index:
        effective_lob_index = retriever.lob_index.strip().lower()
        logging.info(f"No lob_index provided; defaulting => '{effective_lob_index}'")

    logging.info(f"Final effective_lob_index => {effective_lob_index}")

    # Simple check: does user mention 'event'?
    is_event_query = "event" in query.message.lower()

    # Check if recognized LOB
    is_lob_query = False
    if effective_lob_index and effective_lob_index in LOB_KEYWORDS_MAP:
        query_lower = query.message.lower()
        possible_keywords = LOB_KEYWORDS_MAP[effective_lob_index]
        matched_keywords = [kw for kw in possible_keywords if kw in query_lower]
        if matched_keywords:
            is_lob_query = True
            logging.info(f"LOB keywords matched: {matched_keywords}")

    # 2) Retrieve relevant docs (event, LOB, or fallback domain)
    if is_event_query:
        logging.info("Route branch: event-based retrieval")
        retrieved_docs = retriever.retrieve_event_info(query.message)
        messages = create_messages_for_events(query.message, retrieved_docs)

    elif is_lob_query:
        logging.info(f"LOB query => Using index: {effective_lob_index}")
        if hasattr(retriever, "lob_index"):
            logging.info(f"Setting retriever.lob_index => {effective_lob_index}")
            retriever.lob_index = effective_lob_index
        retrieved_docs = retriever.retrieve_lob_info(query.message)
        messages = create_messages_for_lob(query.message, retrieved_docs)

    else:
        logging.info("Route branch: fallback domain-based retrieval")
        if ENABLE_IN_DOMAIN:
            logging.info("In-domain retrieval only.")
            retrieved_docs = retriever.retrieve_domain_info(query.message)
            messages = create_messages(query.message, retrieved_docs, use_general_knowledge=False)
        else:
            logging.info("Domain info + possible API docs retrieval.")
            domain_docs = retriever.retrieve_domain_info(query.message)
            platform_names = [doc.get("platform", "") for doc in domain_docs if "platform" in doc]
            retrieved_docs = retriever.retrieve_api_docs(query.message, platform_names)
            messages = create_messages(query.message, retrieved_docs, use_general_knowledge=True)

    logging.info(f"Retrieved {len(retrieved_docs)} documents.")
    logging.debug(f"Constructed system prompt: {messages[0]['content']}")

    # ----- Insert extra_instructions as a system message at the front -----
    if extra_instructions:
        combined_text = "\n".join(extra_instructions)
        messages.insert(0, {"role": "system", "content": combined_text})

    # -----------------------------------------------------
    # 3) First LLM call (with function definitions)
    # -----------------------------------------------------
    try:
        response = llm_client.call_llm(messages, functions=FUNCTION_DEFINITIONS)
        logging.debug(f"LLM Response: {response}")
    except Exception as e:
        logging.error(f"Error calling LLM: {e}")
        return JSONResponse({"response": "An error occurred while processing your request."}, status_code=500)

    choice_msg = response.choices[0].message

    # -----------------------------------------------------
    # 4) If the LLM wants to call a function, do it
    # -----------------------------------------------------
    if choice_msg.get("function_call"):
        func_name = choice_msg["function_call"]["name"]
        func_args = json.loads(choice_msg["function_call"]["arguments"] or "{}")

        # Dispatch the function
        function_result_response = dispatch_function_call(func_name, func_args)
        if not function_result_response.body:
            return function_result_response

        # Convert the JSONResponse body to string
        raw_json_str = function_result_response.body.decode("utf-8")

        # Attempt to parse into a dict
        try:
            function_result_dict = json.loads(raw_json_str)
        except json.JSONDecodeError as err:
            logging.error(f"Failed to parse function JSON: {err}")
            function_result_dict = {}

        # If it includes "access_points" & "message" => specialized Meraki AP helper
        if "access_points" in function_result_dict and "message" in function_result_dict:
            final_answer = finalize_meraki_aps_with_message(llm_client, function_result_dict)
        else:
            # Otherwise do a standard second prompt
            second_messages = [
                {
                    "role": "system",
                    "content": (
                        "You just called a Cisco function and obtained this JSON result. "
                        "Please produce your final answer in a well-structured HTML format. "
                        "If the JSON includes arrays of items (e.g. devices), create an HTML table with columns. "
                        "Otherwise, provide bullet-lists or paragraphs. No triple backticks."
                    )
                },
                {
                    "role": "user",
                    "content": raw_json_str
                }
            ]
            second_response = llm_client.call_llm(second_messages)
            final_answer = second_response.choices[0].message.get("content", "").strip()

        return JSONResponse({
            "role": "assistant",
            "label": "Cisco AI",
            "response": final_answer
        })

    else:
        # -----------------------------------------------------
        # 5) No function call => final text answer
        # -----------------------------------------------------
        final_answer = choice_msg.get("content", "").strip()
        logging.info(f"Final Answer: {final_answer}")

        return JSONResponse({
            "role": "assistant",
            "label": "Cisco AI",
            "response": final_answer
        })

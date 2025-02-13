![Cisco Data Bridge Banner](app/assets/banner3.png)

The Cisco Data Bridge AI Agent integrates large language model intelligence with multiple Cisco technologies, offering scalable access to network and collaboration resources. Its layered structure separates front-end, back-end, retrieval, and integration logic, making it adaptable and easy to maintain.

**This repo is part of the [Cisco Data Bridge Project Suite](https://github.com/APO-SRE/cisco-data-bridge-project-suite).**

---

### High-Level Architecture Overview

```mermaid

flowchart TB

%% FRONT-END (TOP)
subgraph FE["Front-End"]
    FE1["Client Browser\nHTML/JS\nChart.js in /static"]
end

%% FASTAPI & ROUTERS (MIDDLE) - all inner boxes (except Vectors) have the same blue background
subgraph FA["FastAPI\n(app/main.py)"]
    direction TB

    %% Routers
    subgraph Routers["Routers\n(app/routers)"]
        direction TB
        R1["chat_routes.py"]
        R2["catalyst_routes.py"]
        R3["meraki_routes.py"]
        R4["spaces_routes.py"]
        R5["webex_routes.py"]
    end

    %% Optional RAG: Retrievers and Vector Databases
    subgraph RAG["Optional RAG\n(retrievers/ + Vector DBs)"]
        direction TB

        %% Retrievers
        subgraph Retrievers["Retrievers"]
            direction TB
            RT1["azure_search_retriever.py"]
            RT2["chroma_retriever.py"]
            RT3["elastic_retriever.py"]
            RT4["null_retriever.py"]
        end

        %% Connect Retrievers to Vector Databases to force vertical stacking
        Retrievers --> Vectors

        %% Vector Databases (white background), directly under Retrievers
        subgraph Vectors["Vector Databases"]
            direction TB
            V1["domain_summaries"]
            V2["api_docs"]
            V3["events"]
            V4["LOB"]
        end
    end

    %% LLM Integration
    subgraph LLM["LLM Integration\n(app/llm)"]
        direction TB
        L1["azure_openai.py"]
        L2["llama3.py"]
        L3["base_llm.py"]
        L4["prompt_templates.py"]
        L5["function_definitions.py"]
        L6["function_dispatcher.py"]
    end
end

%% CISCO INTEGRATIONS (BOTTOM)
subgraph CI["Unified Service + Clients\n(cisco_integrations/)"]
    direction TB
    CI1["unified_service.py"]

    subgraph Clients["Specialized Clients"]
        direction TB
        C1["cisco_catalyst_client.py"]
        C2["cisco_meraki_client.py"]
        C3["cisco_spaces_client.py"]
        C4["cisco_webex_client.py"]
        C5["base_client.py"]
        C6["etc..."]
    end
end

%% ARROWS (TOP TO BOTTOM FLOW)
FE1 -->|"User request\n(e.g. chat or command)"| R1
R1 -->|"If user query triggers\nRAG"| RT1
R1 -->|"Send query + docs +\nfunction_defs to LLM"| L1
L1 -->|"LLM sees\nfunction_definitions"| L5
L1 -->|"LLM might produce\nfunction_call"| L6
L6 -->|"Dispatch function_call\nto Unified Service"| CI1
CI1 -->|"Invokes...\nSpecialized Clients"| C1
L6 -->|"Return JSON\n-> optional 2nd LLM call"| L1
R1 -->|"Send final response\nto user"| FE1

%% STYLES

%% Front-End style (using a light lavender color)
style FE fill:#D3D3FF,stroke:#333,stroke-width:2px

%% FastAPI container style (blue background for inner boxes except Vectors)
style FA fill:#ADD8E6,stroke:#333,stroke-width:2px
style Routers fill:#ADD8E6,stroke:#333,stroke-width:1px
style RAG fill:#ADD8E6,stroke:#333,stroke-width:1px
style Retrievers fill:#ADD8E6,stroke:#333,stroke-width:1px
style LLM fill:#ADD8E6,stroke:#333,stroke-width:1px

%% Vector Databases style (white background)
style Vectors fill:#FFFFFF,stroke:#333,stroke-width:1px

%% Unified Service + Clients style (using a light green color)
style CI fill:#D1FFD1,stroke:#333,stroke-width:2px

%% Specialized Clients style (matching Unified Service color)
style Clients fill:#D1FFD1,stroke:#333,stroke-width:2px
```

---

### Key Architectural Highlights

#### Front-End (Static HTML/JS)
- **Location**: `static/` folder  
- **Purpose**: Demonstrates the agent’s functionality with a simple UI for chatting and optional visualizations.  
- **Communication**: Interacts with the FastAPI endpoints via REST calls.  
- **Flexibility**: Can be replaced or expanded for production deployments.

#### Back-End (FastAPI)
- **Definition**: Found in `app/main.py` and multiple routers in `app/routers/`. Examples include:
  - `catalyst_routes.py`
  - `chat_routes.py`
  - `meraki_routes.py`
  - `spaces_routes.py`
  - `webex_routes.py`
- **Responsibilities**:  
  1. Receives requests from the front-end  
  2. Optionally performs retrieval-augmented generation (RAG) by pulling relevant documents from various vector databases (`retrievers/`)  
  3. Passes user queries and relevant docs to the LLM  
  4. If the LLM decides to invoke a Cisco function, `chat_routes.py` delegates the request to a **function dispatcher** for actual execution  
  5. Returns the final response to the client  
- **Scalability**: Easily containerized for Docker or Kubernetes.

#### LLM Integration (`app/llm/`)
- **Logic Storage**: Contains code that communicates with large language models (e.g., Azure OpenAI).  
- **Prompt Templates & Function Definitions**:  
  - **Prompt Templates** guide how context is provided to the LLM.  
  - **function_definitions.py** defines each “tool” or “function” the LLM can call, specifying the name, description, and JSON schema for parameters.  
- **Function Dispatcher**:  
  - When the LLM returns a structured `function_call`, the dispatcher executes the correct method in `unified_service.py` to retrieve real data from Cisco APIs.

#### Retrieval Layer (`retrievers/`)
- **RAG Functionality**: Implements *retrieval-augmented generation* by fetching relevant data from enterprise sources *before* each LLM query, if needed.  
- **Multiple Options**: Azure Search, Elastic, or Chroma can be used to vectorize and search domain documents.

#### Cisco Integrations (`cisco_integrations/`)
- **Specialized Clients**: Classes like `cisco_catalyst_client.py`, `cisco_meraki_client.py`, `cisco_spaces_client.py`, `cisco_webex_client.py` handle the respective Cisco product’s REST APIs.  
- **Base Class Inheritance**: All clients extend `BaseCiscoClient` for consistent error handling, authentication, and retries.  
- **Unified Service**: `unified_service.py` orchestrates calls to each specialized client, providing a single interface for the rest of the application.

---

### Why This Architecture?

1. **LLM & Retrieval Separation**  
   The main application *decides* whether to retrieve domain data, while the LLM focuses on *using* that data. This cleanly isolates large language model usage from enterprise search concerns.

2. **Function Dispatcher**  
   The dispatcher pattern streamlines how function calls from the LLM are executed in Python. Instead of crowding `chat_routes.py` with “if function == X, call Y,” each function is declared in **function_definitions.py** (the “schema”), and the dispatcher runs the correct code in `unified_service.py` or the specialized Cisco clients.

3. **Unified Cisco Service**  
   All Cisco product interactions pass through `unified_service.py`, ensuring consistent authentication, logging, and error handling. Each product (Catalyst, Meraki, Spaces, Webex) can be swapped or extended without breaking the rest of the application.

4. **Front/Back-End Split**  
   The UI is decoupled from the LLM and Cisco integrations. You can update the front-end independently (a React dashboard, a CLI tool, or a new web app), while the back-end logic and integration remain stable.

Overall, the **two-step function-calling approach** (LLM → function call → dispatcher → summary) and **modular retrieval** give teams a stable, enterprise-ready foundation that can scale to new data sources, new Cisco products, or advanced AI usage scenarios.
```
## Getting Started

If you’re a first-time user or new to Git/Python, please see our [Beginner’s Guide](./GETTING_STARTED.md) for step-by-step instructions.
 
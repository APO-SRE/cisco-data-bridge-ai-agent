################################################################################
## cisco-data-bridge-domain-index/llm/function_disptahcer.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import os
import logging
from fastapi.responses import JSONResponse
from cisco_integrations.unified_service import CiscoUnifiedService

# Configure logging at the INFO level.
logging.basicConfig(level=logging.INFO)

FUNCTION_WARNINGS = {
    "get_all_access_points": "Heads up! Retrieving all APs can take a few seconds..."
    # Add more flagged functions here if desired
}


def dispatch_function_call(func_name: str, func_args: dict):
    logging.info(f"Dispatching function call: {func_name} with arguments: {func_args}")

    # Create the CiscoUnifiedService instance
    service = CiscoUnifiedService(
        catalyst_username=os.getenv("CISCO_CATALYST_USERNAME", ""),
        catalyst_password=os.getenv("CISCO_CATALYST_PASSWORD", ""),
        catalyst_url=os.getenv("CISCO_CATALYST_URL", "https://sandboxdnac.cisco.com:443"),
        catalyst_version=os.getenv("CISCO_CATALYST_VERSION", "2.3.7.6"),
        meraki_api_key=os.getenv("CISCO_MERAKI_API_KEY", ""),
        spaces_token=os.getenv("CISCO_SPACES_API_KEY", ""),
        webex_token=os.getenv("CISCO_WEBEX_TOKEN", "")
    )

    # Check if there's a standard warning for this function
    preemptive_msg = None
    if func_name in FUNCTION_WARNINGS:
        preemptive_msg = FUNCTION_WARNINGS[func_name]


    # --- Cisco Spaces functions ---


 # Cisco Spaces: Floor details
    if func_name == "get_spaces_floor_details":
        floor_id = func_args.get("floor_id")
        result = service.get_spaces_floor_details(floor_id)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    # Cisco Spaces: Location hierarchy
    elif func_name == "get_spaces_location_hierarchy":
        tenant_id = func_args.get("tenant_id")
        result = service.get_spaces_location_hierarchy(tenant_id)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    # Cisco Spaces: Floor image
    elif func_name == "get_spaces_floor_image":
        tenant_id = func_args.get("tenant_id")
        image_path = func_args.get("image_path")
        image_type = func_args.get("image_type")
        result = service.get_spaces_floor_image(tenant_id, image_path, image_type)
        # Typically raw bytes. We'll just return base64 or hex if needed?
        # For now, just wrap in JSON. You might do base64 encoding, etc.
        return JSONResponse({
            "function": func_name,
            "arguments": func_args,
            "result": "Binary image data (bytes). Length = {}".format(len(result))
        })
    
    # Cisco Spaces: /devices
    elif func_name == "get_spaces_devices":
        # We accept all possible query arguments as **kwargs
        result = service.get_spaces_devices(**func_args)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    # Cisco Spaces: /devices/count
    elif func_name == "get_spaces_devices_count":
        result = service.get_spaces_devices_count(**func_args)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    # Cisco Spaces: /devices/floors
    elif func_name == "get_spaces_devices_floors":
        result = service.get_spaces_devices_floors()
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    # Cisco Spaces: Export history CSV
    elif func_name == "export_history_csv":
        # Returns raw CSV bytes
        csv_bytes = service.export_history_csv(**func_args)
        return JSONResponse({
            "function": func_name,
            "arguments": func_args,
            "result": f"CSV data returned. Byte length={len(csv_bytes)}"
        })
    
    # Cisco Spaces: Export history GZ
    elif func_name == "export_history_gz":
        gz_bytes = service.export_history_gz(**func_args)
        return JSONResponse({
            "function": func_name,
            "arguments": func_args,
            "result": f"GZ data returned. Byte length={len(gz_bytes)}"
        })
    
    # Cisco Spaces: /history/record/count
    elif func_name == "get_history_record_count":
        result = service.get_history_record_count(**func_args)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    # Cisco Spaces: /history/devices
    elif func_name == "get_history_devices":
        result = service.get_history_devices(**func_args)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    # Cisco Spaces: /history/device/{deviceId}
    elif func_name == "get_spaces_device_history":
        # deviceId must be present
        device_id = func_args.pop("deviceId", None)  # required
        if not device_id:
            return JSONResponse({
                "function": func_name,
                "arguments": func_args,
                "error": "Missing required deviceId"
            })
        result = service.get_history_for_device(device_id, **func_args)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_spaces_location_subtree":
        location_id = func_args.get("location_id")
        result = service.get_spaces_location_subtree(location_id)
        return JSONResponse({
            "function": func_name,
            "arguments": func_args,
            "result": result
        })

    # --- Cisco Catalyst Center functions ---
    elif func_name == "get_all_catalyst_devices":
        result = service.get_all_catalyst_devices()
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_catalyst_device_by_id":
        device_id = func_args.get("device_id")
        result = service.get_catalyst_device_by_id(device_id)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "run_cli_command_on_catalyst_device":
        device_id = func_args.get("device_id")
        command = func_args.get("command")
        result = service.run_cli_command_on_catalyst_device(device_id, command)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_catalyst_task_status_by_id":
        task_id = func_args.get("task_id")
        result = service.get_catalyst_task_status_by_id(task_id)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_cli_command_output":
        file_id = func_args.get("file_id")
        result = service.get_command_output(file_id)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_all_sites":
        result = service.get_all_sites()
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_site_details":
        site_id = func_args.get("site_id")
        result = service.get_site_details(site_id)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_all_ssids":
        result = service.get_all_ssids()
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_aps_by_site":
        site_id = func_args.get("site_id")  # Optional: may be None
        result = service.get_aps_by_site(site_id)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_ap_details":
        ap_id = func_args.get("ap_id")
        result = service.get_ap_details(ap_id)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_all_clients":
        result = service.get_all_clients()
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_client_details":
        mac_address = func_args.get("mac_address")
        result = service.get_client_details(mac_address)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_catalyst_system_info":
        result = service.get_catalyst_system_info()
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_dnac_packages_summary":
        result = service.get_dnac_packages_summary()
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_all_interfaces":
        result = service.get_all_interfaces()
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_device_interfaces":
        device_id = func_args.get("device_id")
        result = service.get_device_interfaces(device_id)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_interfaces_by_ip":
        ip_address = func_args.get("ip_address")
        result = service.get_interfaces_by_ip(ip_address)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "initiate_path_trace":
        source_ip = func_args.get("source_ip")
        destination_ip = func_args.get("destination_ip")
        result = service.initiate_path_trace(source_ip, destination_ip)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_path_trace_result":
        flow_analysis_id = func_args.get("flow_analysis_id")
        result = service.get_path_trace_result(flow_analysis_id)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "delete_path_trace":
        flow_analysis_id = func_args.get("flow_analysis_id")
        result = service.delete_path_trace(flow_analysis_id)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_catalyst_device_list":
        result = service.get_catalyst_device_list_direct()
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "get_catalyst_device_detail_by_name":
        device_name = func_args.get("device_name")
        result = service.get_catalyst_device_detail_by_name(device_name)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({
            "function": func_name,
            "arguments": func_args,
            "result": result
        })

    elif func_name == "get_catalyst_device_detail_by_mac_address":
        mac_address = func_args.get("mac_address")
        result = service.get_catalyst_device_detail_by_mac_address(mac_address)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({
            "function": func_name,
            "arguments": func_args,
            "result": result
    })

    elif func_name == "get_site_by_name":
        site_name = func_args.get("site_name")
        result = service.get_site_by_name(site_name)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({
            "function": func_name,
            "arguments": func_args,
            "result": result
        })

    # --- Meraki functions ---
    elif func_name == "get_meraki_networks":
        result = service.get_meraki_networks()
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_meraki_network_by_id":
        network_id = func_args.get("network_id")
        result = service.get_meraki_network_by_id(network_id)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_organization":
        # Do not pass organization_id – the method uses the env variable automatically.
        result = service.get_organization()
        logging.info(f"Dispatching function call: {func_name} with arguments: {func_args}")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "get_organization_networks":
        result = service.get_organization_networks()
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_organization_inventory_devices":
        result = service.get_organization_inventory_devices()
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "list_all_clients_in_org":
        timespan = func_args.get("timespan", 60 * 60 * 24 * 14)
        result = service.list_all_clients_in_org(timespan)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "list_all_clients_in_org_by_name":
        name_substring = func_args.get("name_substring")
        timespan = func_args.get("timespan", 60 * 60 * 24 * 14)
        result = service.list_all_clients_in_org_by_name(name_substring, timespan)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "get_organization_licenses_overview":
        result = service.get_organization_licenses_overview()
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    # --- Meraki Network-Level Details & Analytics ---
    elif func_name == "get_network_alerts_history":
        network_id = func_args.get("network_id")
        result = service.get_network_alerts_history(network_id)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_network_clients":
        network_id = func_args.get("network_id")
        result = service.get_network_clients(network_id)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_organization_wireless_ssids":
        result = service.get_organization_wireless_ssids()
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    # --- Meraki Device-Level ---
    elif func_name == "get_organization_inventory_device":
        device_id = func_args.get("device_id")
        result = service.get_organization_inventory_device(device_id)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})


    # --- New: Security & Alerts ---
    
    elif func_name == "get_organization_login_security":
        result = service.get_organization_login_security()
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "get_meraki_network_devices":
        network_id = func_args.get("network_id")
        result = service.get_meraki_network_devices(network_id)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "get_meraki_device_switch_ports":
        serial = func_args.get("serial")
        result = service.get_meraki_device_switch_ports(serial)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "get_meraki_network_wireless_ssids":
        network_id = func_args.get("network_id")
        result = service.get_meraki_network_wireless_ssids(network_id)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "list_all_devices_in_org":
        result = service.list_all_devices_in_org()
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "get_all_access_points":
        result = service.get_all_access_points()
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "warning": preemptive_msg, "result": result})
    # Meraki switches
    elif func_name == "list_all_switches_in_org":
        result = service.list_all_switches_in_org()
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    #MEraki cameras
    elif func_name == "list_all_cameras_in_org":
        result = service.list_all_cameras_in_org()
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    # --- Webex functions ---
    elif func_name == "get_webex_meetings":
        result = service.get_webex_meetings()
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_webex_meeting_by_id":
        meeting_id = func_args.get("meeting_id")
        result = service.get_webex_meeting_by_id(meeting_id)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    # --- Unknown / Unimplemented function ---
    else:
        logging.info(f"Function {func_name} is not implemented.")
        return JSONResponse({
            "function": func_name,
            "arguments": func_args,
            "error": f"Function '{func_name}' not implemented yet."
        })
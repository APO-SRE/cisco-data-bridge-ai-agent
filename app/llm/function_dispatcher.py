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


####################################################
# Cisco Spaces Functions
####################################################

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

####################################################
# Cisco Catalyst Center Functions
####################################################

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

#####################################################
# Cisco Catalyst Center SDK Functions
####################################################

    elif func_name == "getsAllTheVersionsOfAGivenTemplate":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.gets_all_the_versions_of_a_given_template(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getMulticastVirtualNetworks":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_multicast_virtual_networks(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceControllabilitySettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_controllability_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getChassisDetailsForDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_chassis_details_for_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getsABuilding":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.gets_a_building(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getCountOfAllDiscoveryJobs":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_count_of_all_discovery_jobs(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getViewsForAGivenViewGroup":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_views_for_a_given_view_group(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveImageDistributionServers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_image_distribution_servers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveBannerSettingsForASite":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_banner_settings_for_a_site(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSiteAssignedNetworkDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_site_assigned_network_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkDevicesCredentialsSyncStatus":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_devices_credentials_sync_status(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSoftwareImageDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_software_image_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAnycastGateways":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_anycast_gateways(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTagMembersById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_tag_members_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricSiteCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_site_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesAllTheValidationSets":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_all_the_validation_sets(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricDevicesLayer2HandoffsCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_devices_layer2_handoffs_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "countOfEventSubscriptions":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.count_of_event_subscriptions(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDetailsOfASingleAssuranceEvent":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_details_of_a_single_assurance_event(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveTelemetrySettingsForASite":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_telemetry_settings_for_a_site(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFloorSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_floor_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTheTotalNumberOfIssuesForGivenSetOfFilters":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_the_total_number_of_issues_for_given_set_of_filters(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTag":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_tag(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getLayer2VirtualNetworks":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_layer2_virtual_networks(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricZoneCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_zone_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getWebhookDestination":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_webhook_destination(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveTimeZoneSettingsForASite":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_time_zone_settings_for_a_site(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getApplicationPolicyQueuingProfile":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_application_policy_queuing_profile(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSyslogDestination":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_syslog_destination(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSyncResultForVirtualAccount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_sync_result_for_virtual_account(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getApplicationPolicyDefault":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_application_policy_default(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getModuleInfoById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_module_info_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricDevicesLayer3HandoffsWithSdaTransit":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_devices_layer3_handoffs_with_sda_transit(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricDevicesLayer3HandoffsWithIpTransit":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_devices_layer3_handoffs_with_ip_transit(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "countOfNotifications":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.count_of_notifications(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAScheduledReport":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_a_scheduled_report(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSiteHealth":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_site_health(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSitesCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_sites_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesTheListOfValidationWorkflows":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_the_list_of_validation_workflows(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSiteCountV2":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_site_count_v2(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getExtranetPolicies":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_extranet_policies(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFlexibleReportScheduleByReportId":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_flexible_report_schedule_by_report_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getPortChannels":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_port_channels(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getsTheTemplatesAvailable":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.gets_the_templates_available(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSyslogSubscriptionDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_syslog_subscription_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getListOfScheduledReports":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_list_of_scheduled_reports(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getClientDetail":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_client_detail(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "countTheNumberOfEvents":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.count_the_number_of_events(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTagMemberCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_tag_member_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceInterfacesBySpecifiedRange":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_interfaces_by_specified_range(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getPollingIntervalForAllDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_polling_interval_for_all_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceList":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_list(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getQosDeviceInterfaceInfo":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_qos_device_interface_info(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceFamilyIdentifiers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_family_identifiers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTaskCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_task_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesValidationDetailsForAValidationSet":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_validation_details_for_a_validation_set(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSmartAccountList":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_smart_account_list(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getLayer3VirtualNetworks":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_layer3_virtual_networks(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getListOfAvailableNamespaces":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_list_of_available_namespaces(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveNetworkDeviceProductName":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_network_device_product_name(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getExecutionIdByReportId":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_execution_id_by_report_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getMobilityGroupsCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_mobility_groups_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAdvisoriesList":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_advisories_list(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getListOfFiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_list_of_files(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveSpecificImageDistributionServer":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_specific_image_distribution_server(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getApplicationPolicy":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_application_policy(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getWorkflowById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_workflow_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAdvisoriesSummary":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_advisories_summary(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTagResourceTypes":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_tag_resource_types(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getPortAssignmentCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_port_assignment_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDiscoveriesByRange":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_discoveries_by_range(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getsAnArea":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.gets_an_area(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getExtranetPolicyCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_extranet_policy_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getResyncIntervalForTheNetworkDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_resync_interval_for_the_network_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getInterfaces":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_interfaces(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAllViewGroups":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_all_view_groups(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getEvents":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_events(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getEmailEventSubscriptions":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_email_event_subscriptions(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getEmailSubscriptionDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_email_subscription_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAllGlobalCredentialsV2":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_all_global_credentials_v2(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkDevicesFromDiscovery":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_devices_from_discovery(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSites":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_sites(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getEventSubscriptions":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_event_subscriptions(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getPlannedAccessPointsForFloor":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_planned_access_points_for_floor(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDiscoveryById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_discovery_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getConfigurationArchiveDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_configuration_archive_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAdvisoriesPerDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_advisories_per_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesTheCountOfValidationWorkflows":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_the_count_of_validation_workflows(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getComplianceDetailCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_compliance_detail_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOverallClientHealth":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_overall_client_health(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getLinecardDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_linecard_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getWirelessProfilesCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_wireless_profiles_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTagById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_tag_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAuditLogSummary":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_audit_log_summary(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getsAListOfProjects":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.gets_a_list_of_projects(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAuthenticationAndPolicyServers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_authentication_and_policy_servers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getProvisionedDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_provisioned_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesAllPreviousPathtracesSummary":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_all_previous_pathtraces_summary(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCredentialSettingsForASite":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_credential_settings_for_a_site(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceInterfaceCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_interface_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getLayer2VirtualNetworkCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_layer2_virtual_network_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesTheCountOfNetworkProfilesForSites":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_the_count_of_network_profiles_for_sites(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricDevicesLayer2Handoffs":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_devices_layer2_handoffs(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSyslogEventSubscriptions":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_syslog_event_subscriptions(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSiteV2":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_site_v2(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTasksCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_tasks_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getsAFloor":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.gets_a_floor(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricZones":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_zones(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getVirtualAccountList":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_virtual_account_list(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getQosDeviceInterfaceInfoCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_qos_device_interface_info_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "countOfEvents":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.count_of_events(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkDeviceImageUpdates":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_device_image_updates(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTransitNetworks":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_transit_networks(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getStackDetailsForDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_stack_details_for_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getApplicationSetCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_application_set_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getWorkflowCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_workflow_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesPreviousPathtrace":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_previous_pathtrace(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOverallNetworkHealth":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_overall_network_health(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getServiceProviderDetailsV2":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_service_provider_details_v2(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getWirelessProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_wireless_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getConfigTaskDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_config_task_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getMulticastVirtualNetworkCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_multicast_virtual_network_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTagCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_tag_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSummary":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_summary(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAuthenticationProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_authentication_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAllFlexibleReportSchedules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_all_flexible_report_schedules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFunctionalCapabilityById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_functional_capability_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricSites":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_sites(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getWorkflows":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_workflows(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceConfigById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_config_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationListForMeraki":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_list_for_meraki(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getPollingIntervalById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_polling_interval_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNotifications":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_notifications(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceConfigCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_config_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveANetworkProfileForSitesById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_a_network_profile_for_sites_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAuditLogRecords":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_audit_log_records(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSupervisorCardDetail":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_supervisor_card_detail(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveImageDistributionSettingsForASite":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_image_distribution_settings_for_a_site(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getEventArtifacts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_event_artifacts(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesValidationWorkflowDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_validation_workflow_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getModuleCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_module_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTransitNetworksCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_transit_networks_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAllExecutionDetailsForAGivenReport":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_all_execution_details_for_a_given_report(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getPortChannelCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_port_channel_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAuditLogParentRecords":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_audit_log_parent_records(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveDNSSettingsForASite":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_d_n_s_settings_for_a_site(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getEmailDestination":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_email_destination(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveLicenseSetting":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_license_setting(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getMulticast":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_multicast(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricDevicesCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_devices_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getLayer3VirtualNetworksCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_layer3_virtual_networks_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDevicesDiscoveredById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_devices_discovered_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTaskById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_task_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDiscoveredDevicesByRange":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_discovered_devices_by_range(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesTheTotalCountOfClientsByApplyingBasicFiltering":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_the_total_count_of_clients_by_applying_basic_filtering(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesTheListOfNetworkDeviceProductNames":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_the_list_of_network_device_product_names(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getConnectedDeviceDetail":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_connected_device_detail(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDevicesThatAreAssignedToASite":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_devices_that_are_assigned_to_a_site(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getListOfDiscoveriesByDiscoveryId":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_list_of_discoveries_by_discovery_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getPhysicalTopology":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_physical_topology(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSiteTopology":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_site_topology(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveNTPSettingsForASite":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_n_t_p_settings_for_a_site(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "countOfNetworkDeviceImageUpdates":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.count_of_network_device_image_updates(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getPlannedAccessPointsForBuilding":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_planned_access_points_for_building(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "countOfNetworkProductNames":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.count_of_network_product_names(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAccessPointConfiguration":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_access_point_configuration(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceConfigForAllDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_config_for_all_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTopologyDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_topology_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricDevicesLayer3HandoffsWithIpTransitCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_devices_layer3_handoffs_with_ip_transit_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFabricDevicesLayer3HandoffsWithSdaTransitCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_fabric_devices_layer3_handoffs_with_sda_transit_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesTheListOfNetworkProfilesForSites":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_the_list_of_network_profiles_for_sites(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getFunctionalCapabilityForDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_functional_capability_for_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getPortAssignments":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_port_assignments(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSiteNotAssignedNetworkDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_site_not_assigned_network_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAccessPointRebootTaskResult":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_access_point_reboot_task_result(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceDetail":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_detail(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSiteNotAssignedNetworkDevicesCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_site_not_assigned_network_devices_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceBySerialNumber":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_by_serial_number(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getApplicationCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_application_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getComplianceStatusCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_compliance_status_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTasks":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_tasks(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getListOfChildEventsForTheGivenWirelessClientEvent":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_list_of_child_events_for_the_given_wireless_client_event(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getProvisioningSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_provisioning_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getInterfaceById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_interface_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getInterfaceInfoById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_interface_info_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTaskByOperationId":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_task_by_operation_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getL3TopologyDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_l3_topology_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAdvisoryDeviceDetail":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_advisory_device_detail(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getConnectorTypes":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_connector_types(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrieveDHCPSettingsForASite":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieve_d_h_c_p_settings_for_a_site(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAnycastGatewayCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_anycast_gateway_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkDeviceByPaginationRange":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_device_by_pagination_range(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSiteAssignedNetworkDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_site_assigned_network_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAllInterfaces":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_all_interfaces(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getWirelessLanControllerDetailsById":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_wireless_lan_controller_details_by_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDevicesPerAdvisory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_devices_per_advisory(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAccessPointConfigurationTaskResult":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_access_point_configuration_task_result(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getComplianceDetail":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_compliance_detail(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getGlobalCredentials":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_global_credentials(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getComplianceStatus":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_compliance_status(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getProvisionedDevicesCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_provisioned_devices_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getInterfacesCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_interfaces_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getModules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_modules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "retrievesTheCountOfAssignedNetworkDeviceProducts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.retrieves_the_count_of_assigned_network_device_products(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getApplicationPolicyQueuingProfileCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_application_policy_queuing_profile_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTaskTree":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_task_tree(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDiscoveredNetworkDevicesByDiscoveryId":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_discovered_network_devices_by_discovery_id(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSiteAssignedNetworkDevicesCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_site_assigned_network_devices_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkV2":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_v2(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceValuesThatMatchFullyOrPartiallyAnAttribute":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_values_that_match_fully_or_partially_an_attribute(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getApplications":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_applications(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetwork":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getTransitPeerNetworkInfo":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_transit_peer_network_info(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getApplicationSets":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_application_sets(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getApplicationsCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_applications_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getGlobalPool":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_global_pool(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getProvisionedWiredDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_provisioned_wired_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCredentialDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_credential_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getServiceProviderDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_service_provider_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSite":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_site(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getVirtualNetworkSummary":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_virtual_network_summary(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getWirelessProfile":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_wireless_profile(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getIssueEnrichmentDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_issue_enrichment_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getSiteCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_site_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getClientEnrichmentDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_client_enrichment_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getVirtualNetworkWithScalableGroups":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_virtual_network_with_scalable_groups(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDynamicInterface":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_dynamic_interface(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getApplicationSetsCount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_application_sets_count(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getUserEnrichmentDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_user_enrichment_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceEnrichmentDetails":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_enrichment_details(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getMembership":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_membership(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

####################################################
# Meraki Functions
####################################################


    elif func_name == "list_all_clients_in_org":
        timespan = func_args.get("timespan", 60 * 60 * 24 * 14)
        result = service.list_all_clients_in_org(timespan)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "list_all_clients_in_org_by_name":
        name_substring = func_args.get("name_substring")
        timespan = func_args.get("timespan", 60 * 60 * 24 * 14)
        result = service.list_all_clients_in_org_by_name(name_substring, timespan)
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})
    
    elif func_name == "get_network_alerts_history":
        network_id = func_args.get("network_id")
        result = service.get_network_alerts_history(network_id)
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
    #Meraki cameras
    elif func_name == "list_all_cameras_in_org":
        result = service.list_all_cameras_in_org()
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})


####################################################
# Meraki SDK Functions
####################################################


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


    # --- Meraki read-only functions ---

    elif func_name == "getAdministeredIdentitiesMe":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_administered_identities_me(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAdministeredIdentitiesMeApiKeys":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_administered_identities_me_api_keys(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAdministeredLicensingSubscriptionEntitlements":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_administered_licensing_subscription_entitlements(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAdministeredLicensingSubscriptionSubscriptions":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_administered_licensing_subscription_subscriptions(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_administered_licensing_subscription_subscriptions_compliance_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceApplianceDhcpSubnets":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_appliance_dhcp_subnets(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceAppliancePerformance":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_appliance_performance(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceAppliancePrefixesDelegated":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_appliance_prefixes_delegated(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceAppliancePrefixesDelegatedVlanAssignments":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_appliance_prefixes_delegated_vlan_assignments(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceApplianceRadioSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_appliance_radio_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceApplianceUplinksSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_appliance_uplinks_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraAnalyticsLive":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_analytics_live(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraAnalyticsOverview":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_analytics_overview(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraAnalyticsRecent":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_analytics_recent(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraAnalyticsZones":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_analytics_zones(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraAnalyticsZoneHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_analytics_zone_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraCustomAnalytics":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_custom_analytics(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraQualityAndRetention":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_quality_and_retention(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraSense":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_sense(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraSenseObjectDetectionModels":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_sense_object_detection_models(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraVideoSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_video_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraVideoLink":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_video_link(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCameraWirelessProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_camera_wireless_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCellularSims":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_cellular_sims(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCellularGatewayLan":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_cellular_gateway_lan(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceCellularGatewayPortForwardingRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_cellular_gateway_port_forwarding_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceClients":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_clients(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceLiveToolsArpTable":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_live_tools_arp_table(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceLiveToolsCableTest":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_live_tools_cable_test(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceLiveToolsLedsBlink":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_live_tools_leds_blink(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceLiveToolsPing":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_live_tools_ping(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceLiveToolsPingDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_live_tools_ping_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceLiveToolsThroughputTest":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_live_tools_throughput_test(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceLiveToolsWakeOnLan":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_live_tools_wake_on_lan(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceLldpCdp":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_lldp_cdp(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceLossAndLatencyHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_loss_and_latency_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceManagementInterface":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_management_interface(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSensorCommands":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_sensor_commands(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSensorCommand":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_sensor_command(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSensorRelationships":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_sensor_relationships(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSwitchPorts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_switch_ports(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSwitchPortsStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_switch_ports_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSwitchPortsStatusesPackets":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_switch_ports_statuses_packets(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSwitchPort":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_switch_port(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSwitchRoutingInterfaces":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_switch_routing_interfaces(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSwitchRoutingInterface":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_switch_routing_interface(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSwitchRoutingInterfaceDhcp":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_switch_routing_interface_dhcp(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSwitchRoutingStaticRoutes":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_switch_routing_static_routes(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSwitchRoutingStaticRoute":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_switch_routing_static_route(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceSwitchWarmSpare":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_switch_warm_spare(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceWirelessBluetoothSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_wireless_bluetooth_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceWirelessConnectionStats":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_wireless_connection_stats(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceWirelessElectronicShelfLabel":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_wireless_electronic_shelf_label(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceWirelessLatencyStats":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_wireless_latency_stats(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceWirelessRadioSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_wireless_radio_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getDeviceWirelessStatus":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_device_wireless_status(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetwork":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkAlertsHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_alerts_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkAlertsSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_alerts_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceClientSecurityEvents":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_client_security_events(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceConnectivityMonitoringDestinations":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_connectivity_monitoring_destinations(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceContentFiltering":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_content_filtering(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceContentFilteringCategories":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_content_filtering_categories(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallCellularFirewallRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_cellular_firewall_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallFirewalledServices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_firewalled_services(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallFirewalledService":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_firewalled_service(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallInboundCellularFirewallRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_inbound_cellular_firewall_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallInboundFirewallRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_inbound_firewall_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallL3FirewallRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_l3_firewall_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallL7FirewallRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_l7_firewall_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallL7FirewallRulesApplicationCategories":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_l7_firewall_rules_application_categories(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallOneToManyNatRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_one_to_many_nat_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallOneToOneNatRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_one_to_one_nat_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallPortForwardingRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_port_forwarding_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceFirewallSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_firewall_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkAppliancePorts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_ports(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkAppliancePort":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_port(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkAppliancePrefixesDelegatedStatics":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_prefixes_delegated_statics(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkAppliancePrefixesDelegatedStatic":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_prefixes_delegated_static(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceRfProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_rf_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceRfProfile":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_rf_profile(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceSecurityEvents":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_security_events(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceSecurityIntrusion":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_security_intrusion(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceSecurityMalware":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_security_malware(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceSingleLan":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_single_lan(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceSsids":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_ssids(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceSsid":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_ssid(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceStaticRoutes":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_static_routes(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceStaticRoute":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_static_route(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceTrafficShaping":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_traffic_shaping(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceTrafficShapingCustomPerformanceClasses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_traffic_shaping_custom_performance_classes(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceTrafficShapingCustomPerformanceClass":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_traffic_shaping_custom_performance_class(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceTrafficShapingRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_traffic_shaping_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceTrafficShapingUplinkBandwidth":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_traffic_shaping_uplink_bandwidth(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceTrafficShapingUplinkSelection":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_traffic_shaping_uplink_selection(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceUplinksUsageHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_uplinks_usage_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceVlans":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_vlans(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceVlansSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_vlans_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceVlan":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_vlan(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceVpnBgp":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_vpn_bgp(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceVpnSiteToSiteVpn":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_vpn_site_to_site_vpn(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkApplianceWarmSpare":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_appliance_warm_spare(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkBluetoothClients":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_bluetooth_clients(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkBluetoothClient":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_bluetooth_client(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkCameraQualityRetentionProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_camera_quality_retention_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkCameraQualityRetentionProfile":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_camera_quality_retention_profile(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkCameraSchedules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_camera_schedules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkCameraWirelessProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_camera_wireless_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkCameraWirelessProfile":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_camera_wireless_profile(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkCellularGatewayConnectivityMonitoringDestinations":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_cellular_gateway_connectivity_monitoring_destinations(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkCellularGatewayDhcp":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_cellular_gateway_dhcp(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkCellularGatewaySubnetPool":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_cellular_gateway_subnet_pool(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkCellularGatewayUplink":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_cellular_gateway_uplink(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkClients":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_clients(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkClientsApplicationUsage":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_clients_application_usage(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkClientsBandwidthUsageHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_clients_bandwidth_usage_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkClientsOverview":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_clients_overview(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkClientsUsageHistories":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_clients_usage_histories(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkClient":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_client(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkClientPolicy":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_client_policy(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkClientSplashAuthorizationStatus":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_client_splash_authorization_status(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkClientTrafficHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_client_traffic_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkClientUsageHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_client_usage_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkEvents":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_events(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkEventsEventTypes":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_events_event_types(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkFirmwareUpgrades":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_firmware_upgrades(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkFirmwareUpgradesStagedEvents":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_firmware_upgrades_staged_events(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkFirmwareUpgradesStagedGroups":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_firmware_upgrades_staged_groups(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkFirmwareUpgradesStagedGroup":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_firmware_upgrades_staged_group(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkFirmwareUpgradesStagedStages":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_firmware_upgrades_staged_stages(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkFloorPlans":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_floor_plans(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkFloorPlan":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_floor_plan(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkGroupPolicies":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_group_policies(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkGroupPolicy":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_group_policy(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkHealthAlerts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_health_alerts(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkInsightApplicationHealthByTime":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_insight_application_health_by_time(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkMerakiAuthUsers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_meraki_auth_users(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkMerakiAuthUser":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_meraki_auth_user(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkMqttBrokers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_mqtt_brokers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkMqttBroker":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_mqtt_broker(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkNetflow":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_netflow(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkNetworkHealthChannelUtilization":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_network_health_channel_utilization(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkPiiPiiKeys":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_pii_pii_keys(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkPiiRequests":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_pii_requests(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkPiiRequest":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_pii_request(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkPiiSmDevicesForKey":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_pii_sm_devices_for_key(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkPiiSmOwnersForKey":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_pii_sm_owners_for_key(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkPoliciesByClient":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_policies_by_client(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSensorAlertsCurrentOverviewByMetric":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sensor_alerts_current_overview_by_metric(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSensorAlertsOverviewByMetric":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sensor_alerts_overview_by_metric(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSensorAlertsProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sensor_alerts_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSensorAlertsProfile":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sensor_alerts_profile(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSensorMqttBrokers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sensor_mqtt_brokers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSensorMqttBroker":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sensor_mqtt_broker(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSensorRelationships":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sensor_relationships(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmBypassActivationLockAttempt":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_bypass_activation_lock_attempt(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDeviceCellularUsageHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_cellular_usage_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDeviceCerts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_certs(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDeviceConnectivity":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_connectivity(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDeviceDesktopLogs":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_desktop_logs(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDeviceDeviceCommandLogs":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_device_command_logs(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDeviceDeviceProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_device_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDeviceNetworkAdapters":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_network_adapters(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDevicePerformanceHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_performance_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDeviceRestrictions":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_restrictions(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDeviceSecurityCenters":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_security_centers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDeviceSoftwares":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_softwares(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmDeviceWlanLists":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_device_wlan_lists(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmTargetGroups":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_target_groups(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmTargetGroup":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_target_group(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmTrustedAccessConfigs":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_trusted_access_configs(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmUserAccessDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_user_access_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmUsers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_users(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmUserDeviceProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_user_device_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSmUserSoftwares":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_sm_user_softwares(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSnmp":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_snmp(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSplashLoginAttempts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_splash_login_attempts(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchAccessControlLists":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_access_control_lists(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchAccessPolicies":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_access_policies(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchAccessPolicy":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_access_policy(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchAlternateManagementInterface":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_alternate_management_interface(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchDhcpV4ServersSeen":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_dhcp_v4_servers_seen(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchDhcpServerPolicy":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_dhcp_server_policy(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchDscpToCosMappings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_dscp_to_cos_mappings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchLinkAggregations":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_link_aggregations(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchMtu":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_mtu(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchPortSchedules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_port_schedules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchQosRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_qos_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchQosRulesOrder":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_qos_rules_order(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchQosRule":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_qos_rule(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchRoutingMulticast":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_routing_multicast(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchRoutingMulticastRendezvousPoints":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_routing_multicast_rendezvous_points(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchRoutingMulticastRendezvousPoint":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_routing_multicast_rendezvous_point(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchRoutingOspf":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_routing_ospf(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchStacks":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_stacks(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchStack":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_stack(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchStackRoutingInterfaces":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_stack_routing_interfaces(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchStackRoutingInterface":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_stack_routing_interface(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchStackRoutingInterfaceDhcp":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_stack_routing_interface_dhcp(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchStackRoutingStaticRoutes":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_stack_routing_static_routes(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchStackRoutingStaticRoute":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_stack_routing_static_route(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchStormControl":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_storm_control(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSwitchStp":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_switch_stp(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkSyslogServers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_syslog_servers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkTopologyLinkLayer":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_topology_link_layer(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkTraffic":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_traffic(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkTrafficAnalysis":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_traffic_analysis(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkTrafficShapingApplicationCategories":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_traffic_shaping_application_categories(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkTrafficShapingDscpTaggingOptions":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_traffic_shaping_dscp_tagging_options(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkVlanProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_vlan_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkVlanProfilesAssignmentsByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_vlan_profiles_assignments_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkVlanProfile":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_vlan_profile(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWebhooksHttpServers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_webhooks_http_servers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWebhooksHttpServer":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_webhooks_http_server(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWebhooksPayloadTemplates":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_webhooks_payload_templates(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWebhooksPayloadTemplate":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_webhooks_payload_template(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWebhooksWebhookTest":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_webhooks_webhook_test(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessAirMarshal":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_air_marshal(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessAlternateManagementInterface":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_alternate_management_interface(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessBilling":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_billing(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessBluetoothSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_bluetooth_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessChannelUtilizationHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_channel_utilization_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessClientCountHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_client_count_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessClientsConnectionStats":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_clients_connection_stats(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessClientsLatencyStats":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_clients_latency_stats(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessClientConnectionStats":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_client_connection_stats(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessClientConnectivityEvents":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_client_connectivity_events(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessClientLatencyHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_client_latency_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessClientLatencyStats":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_client_latency_stats(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessConnectionStats":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_connection_stats(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessDataRateHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_data_rate_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessDevicesConnectionStats":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_devices_connection_stats(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessDevicesLatencyStats":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_devices_latency_stats(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessElectronicShelfLabel":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_electronic_shelf_label(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessElectronicShelfLabelConfiguredDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_electronic_shelf_label_configured_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessEthernetPortsProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ethernet_ports_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessEthernetPortsProfile":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ethernet_ports_profile(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessFailedConnections":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_failed_connections(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessLatencyHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_latency_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessLatencyStats":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_latency_stats(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessMeshStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_mesh_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessRfProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_rf_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessRfProfile":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_rf_profile(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSignalQualityHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_signal_quality_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsids":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssids(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsid":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidBonjourForwarding":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_bonjour_forwarding(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidDeviceTypeGroupPolicies":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_device_type_group_policies(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidEapOverride":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_eap_override(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidFirewallL3FirewallRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_firewall_l3_firewall_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidFirewallL7FirewallRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_firewall_l7_firewall_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidHotspot20":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_hotspot20(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidIdentityPsks":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_identity_psks(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidIdentityPsk":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_identity_psk(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidSchedules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_schedules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidSplashSettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_splash_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidTrafficShapingRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_traffic_shaping_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessSsidVpn":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_ssid_vpn(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getNetworkWirelessUsageHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_network_wireless_usage_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizations":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organizations(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganization":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationActionBatches":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_action_batches(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationActionBatch":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_action_batch(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAdaptivePolicyAcls":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_adaptive_policy_acls(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAdaptivePolicyAcl":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_adaptive_policy_acl(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAdaptivePolicyGroups":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_adaptive_policy_groups(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAdaptivePolicyGroup":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_adaptive_policy_group(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAdaptivePolicyOverview":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_adaptive_policy_overview(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAdaptivePolicyPolicies":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_adaptive_policy_policies(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAdaptivePolicyPolicy":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_adaptive_policy_policy(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAdaptivePolicySettings":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_adaptive_policy_settings(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAdmins":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_admins(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAlertsProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_alerts_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApiRequests":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_api_requests(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApiRequestsOverview":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_api_requests_overview(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApiRequestsOverviewResponseCodesByInterval":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_api_requests_overview_response_codes_by_interval(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApplianceSecurityEvents":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_appliance_security_events(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApplianceSecurityIntrusion":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_appliance_security_intrusion(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_appliance_traffic_shaping_vpn_exclusions_by_network(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApplianceUplinkStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_appliance_uplink_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApplianceUplinksStatusesOverview":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_appliance_uplinks_statuses_overview(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApplianceUplinksUsageByNetwork":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_appliance_uplinks_usage_by_network(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApplianceVpnStats":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_appliance_vpn_stats(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApplianceVpnStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_appliance_vpn_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApplianceVpnThirdPartyVPNPeers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_appliance_vpn_third_party_v_p_n_peers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationApplianceVpnVpnFirewallRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_appliance_vpn_vpn_firewall_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAssuranceAlerts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_assurance_alerts(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAssuranceAlertsOverview":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_assurance_alerts_overview(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAssuranceAlertsOverviewByNetwork":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_assurance_alerts_overview_by_network(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAssuranceAlertsOverviewByType":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_assurance_alerts_overview_by_type(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAssuranceAlertsOverviewHistorical":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_assurance_alerts_overview_historical(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationAssuranceAlert":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_assurance_alert(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationBrandingPolicies":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_branding_policies(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationBrandingPoliciesPriorities":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_branding_policies_priorities(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationBrandingPolicy":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_branding_policy(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCameraBoundariesAreasByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_camera_boundaries_areas_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCameraBoundariesLinesByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_camera_boundaries_lines_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCameraCustomAnalyticsArtifacts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_camera_custom_analytics_artifacts(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCameraCustomAnalyticsArtifact":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_camera_custom_analytics_artifact(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCameraDetectionsHistoryByBoundaryByInterval":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_camera_detections_history_by_boundary_by_interval(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCameraOnboardingStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_camera_onboarding_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCameraPermissions":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_camera_permissions(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCameraPermission":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_camera_permission(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCameraRoles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_camera_roles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCameraRole":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_camera_role(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCellularGatewayEsimsInventory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_cellular_gateway_esims_inventory(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCellularGatewayEsimsServiceProviders":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_cellular_gateway_esims_service_providers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCellularGatewayEsimsServiceProvidersAccounts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_cellular_gateway_esims_service_providers_accounts(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_cellular_gateway_esims_service_providers_accounts_communication_plans(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_cellular_gateway_esims_service_providers_accounts_rate_plans(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationCellularGatewayUplinkStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_cellular_gateway_uplink_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationClientsBandwidthUsageHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_clients_bandwidth_usage_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationClientsOverview":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_clients_overview(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationClientsSearch":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_clients_search(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationConfigTemplates":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_config_templates(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationConfigTemplate":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_config_template(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationConfigTemplateSwitchProfiles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_config_template_switch_profiles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationConfigTemplateSwitchProfilePorts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_config_template_switch_profile_ports(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationConfigTemplateSwitchProfilePort":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_config_template_switch_profile_port(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationConfigurationChanges":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_configuration_changes(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationDevicesAvailabilities":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_devices_availabilities(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationDevicesAvailabilitiesChangeHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_devices_availabilities_change_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationDevicesOverviewByModel":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_devices_overview_by_model(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationDevicesPowerModulesStatusesByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_devices_power_modules_statuses_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationDevicesProvisioningStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_devices_provisioning_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationDevicesStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_devices_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationDevicesStatusesOverview":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_devices_statuses_overview(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationDevicesUplinksAddressesByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_devices_uplinks_addresses_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationDevicesUplinksLossAndLatency":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_devices_uplinks_loss_and_latency(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationEarlyAccessFeatures":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_early_access_features(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationEarlyAccessFeaturesOptIns":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_early_access_features_opt_ins(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationEarlyAccessFeaturesOptIn":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_early_access_features_opt_in(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationFirmwareUpgrades":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_firmware_upgrades(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationFirmwareUpgradesByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_firmware_upgrades_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationFloorPlansAutoLocateDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_floor_plans_auto_locate_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationFloorPlansAutoLocateStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_floor_plans_auto_locate_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationInsightApplications":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_insight_applications(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationInsightMonitoredMediaServers":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_insight_monitored_media_servers(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationInsightMonitoredMediaServer":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_insight_monitored_media_server(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationInventoryDevices":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_inventory_devices(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationInventoryDevicesSwapsBulk":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_inventory_devices_swaps_bulk(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationInventoryDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_inventory_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationInventoryOnboardingCloudMonitoringImports":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_inventory_onboarding_cloud_monitoring_imports(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationInventoryOnboardingCloudMonitoringNetworks":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_inventory_onboarding_cloud_monitoring_networks(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationLicenses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_licenses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationLicensesOverview":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_licenses_overview(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationLicense":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_license(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationLicensingCotermLicenses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_licensing_coterm_licenses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationLoginSecurity":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_login_security(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationNetworks":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_networks(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationOpenapiSpec":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_openapi_spec(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationPolicyObjects":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_policy_objects(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationPolicyObjectsGroups":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_policy_objects_groups(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationPolicyObjectsGroup":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_policy_objects_group(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationPolicyObject":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_policy_object(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSaml":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_saml(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSamlIdps":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_saml_idps(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSamlIdp":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_saml_idp(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSamlRoles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_saml_roles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSamlRole":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_saml_role(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSensorReadingsHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_sensor_readings_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSensorReadingsLatest":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_sensor_readings_latest(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSmAdminsRoles":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_sm_admins_roles(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSmAdminsRole":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_sm_admins_role(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSmApnsCert":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_sm_apns_cert(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSmSentryPoliciesAssignmentsByNetwork":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_sm_sentry_policies_assignments_by_network(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSmVppAccounts":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_sm_vpp_accounts(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSmVppAccount":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_sm_vpp_account(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSnmp":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_snmp(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSplashAsset":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_splash_asset(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSplashThemes":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_splash_themes(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSummarySwitchPowerHistory":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_summary_switch_power_history(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSummaryTopAppliancesByUtilization":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_summary_top_appliances_by_utilization(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSummaryTopApplicationsByUsage":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_summary_top_applications_by_usage(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSummaryTopApplicationsCategoriesByUsage":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_summary_top_applications_categories_by_usage(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSummaryTopClientsByUsage":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_summary_top_clients_by_usage(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSummaryTopClientsManufacturersByUsage":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_summary_top_clients_manufacturers_by_usage(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSummaryTopDevicesByUsage":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_summary_top_devices_by_usage(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSummaryTopDevicesModelsByUsage":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_summary_top_devices_models_by_usage(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSummaryTopNetworksByStatus":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_summary_top_networks_by_status(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSummaryTopSsidsByUsage":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_summary_top_ssids_by_usage(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSummaryTopSwitchesByEnergyUsage":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_summary_top_switches_by_energy_usage(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSwitchPortsBySwitch":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_switch_ports_by_switch(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSwitchPortsClientsOverviewByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_switch_ports_clients_overview_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSwitchPortsOverview":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_switch_ports_overview(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSwitchPortsStatusesBySwitch":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_switch_ports_statuses_by_switch(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationSwitchPortsTopologyDiscoveryByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_switch_ports_topology_discovery_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationUplinksStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_uplinks_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWebhooksAlertTypes":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_webhooks_alert_types(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWebhooksCallbacksStatus":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_webhooks_callbacks_status(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWebhooksLogs":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_webhooks_logs(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessAirMarshalRules":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_air_marshal_rules(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessAirMarshalSettingsByNetwork":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_air_marshal_settings_by_network(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessClientsOverviewByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_clients_overview_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessDevicesChannelUtilizationByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_devices_channel_utilization_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessDevicesChannelUtilizationByNetwork":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_devices_channel_utilization_by_network(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_devices_channel_utilization_history_by_device_by_interval(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_devices_channel_utilization_history_by_network_by_interval(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessDevicesEthernetStatuses":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_devices_ethernet_statuses(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessDevicesPacketLossByClient":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_devices_packet_loss_by_client(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessDevicesPacketLossByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_devices_packet_loss_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessDevicesPacketLossByNetwork":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_devices_packet_loss_by_network(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessDevicesWirelessControllersByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_devices_wireless_controllers_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessRfProfilesAssignmentsByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_rf_profiles_assignments_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})

    elif func_name == "getOrganizationWirelessSsidsStatusesByDevice":
        logging.info(f"Dispatching LLM function call: {func_name} with args: {func_args}")
        result = service.get_organization_wireless_ssids_statuses_by_device(**func_args)
        logging.info(f"Executed {func_name} successfully.")
        return JSONResponse({"function": func_name, "arguments": func_args, "result": result})


####################################################
# WebEx Functions
####################################################
    # --- Webex functions
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
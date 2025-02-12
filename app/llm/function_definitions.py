################################################################################
## cisco-data-bridge-domain-index/llm/function_definitions.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################


#############################
# Cisco Spaces
#############################

# 1) Retrieve floor details from Cisco Spaces
get_spaces_floor_details_function = {
    "name": "get_spaces_floor_details",
    "description": "Fetch details for a specific floor (map details and location hierarchy) from Cisco Spaces.",
    "parameters": {
        "type": "object",
        "properties": {
            "floor_id": {
                "type": "string",
                "description": "The unique identifier for the floor."
            }
        },
        "required": ["floor_id"]
    }
}

# 2) Retrieve location hierarchy
get_spaces_location_hierarchy_function = {
    "name": "get_spaces_location_hierarchy",
    "description": "Retrieve the entire location hierarchy from Cisco Spaces (GET /map/locationhierarchy).",
    "parameters": {
        "type": "object",
        "properties": {
            "tenant_id": {
                "type": "string",
                "description": "Optional tenantId to specify if needed."
            }
        },
        "required": []
    }
}

# 3) Retrieve floor image
get_spaces_floor_image_function = {
    "name": "get_spaces_floor_image",
    "description": "Retrieve the floor image from Cisco Spaces (GET /map/floor/image). Returns raw image bytes.",
    "parameters": {
        "type": "object",
        "properties": {
            "tenant_id": {"type": "string", "description": "Unique client identifier."},
            "image_path": {"type": "string", "description": "The image path."},
            "image_type": {"type": "string", "description": "Type of image."}
        },
        "required": ["tenant_id", "image_path", "image_type"]
    }
}

# 4) Retrieve devices (with optional filters)
get_spaces_devices_function = {
    "name": "get_spaces_devices",
    "description": "Fetch devices from Cisco Spaces /v2/devices with optional query filters.",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceType": {"type": "string", "description": "CLIENT, TAG, BLE, ROGUE_AP, ROGUE_CLIENT, INTERFERER"},
            "deviceId": {"type": "string"},
            "ipAddress": {"type": "string"},
            "floorId": {"type": "string"},
            "buildingId": {"type": "string"},
            "campusId": {"type": "string"},
            "associated": {"type": "boolean"},
            "ssid": {"type": "string"},
            "apMacAddress": {"type": "string"},
            "manufacturer": {"type": "string"},
            "rogueApClients": {"type": "boolean"},
            "format": {"type": "string", "description": "geojson, etc."},
            "mapElementId": {"type": "string"},
            "mapElementLevel": {"type": "string", "description": "campus, building, floor"},
            "page": {"type": "string"},
            "limit": {"type": "string"},
            "username": {"type": "string"},
            "searchType": {"type": "string", "description": "wildcard, etc."}
        },
        "required": []
    }
}

# 5) Retrieve devices count
get_spaces_devices_count_function = {
    "name": "get_spaces_devices_count",
    "description": "Fetch a count of devices from Cisco Spaces /v2/devices/count with optional filters.",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceType": {"type": "string"},
            "deviceId": {"type": "string"},
            "ipAddress": {"type": "string"},
            "floorId": {"type": "string"},
            "buildingId": {"type": "string"},
            "campusId": {"type": "string"},
            "associated": {"type": "boolean"},
            "ssid": {"type": "string"},
            "apMacAddress": {"type": "string"},
            "rogueApClients": {"type": "boolean"},
            "manufacturer": {"type": "string"},
            "groupBy": {"type": "string"},
            "mapElementId": {"type": "string"},
            "mapElementLevel": {"type": "string"},
            "username": {"type": "string"}
        },
        "required": []
    }
}

# 6) Retrieve floors that have devices
get_spaces_devices_floors_function = {
    "name": "get_spaces_devices_floors",
    "description": "Fetch a list of floors (IDs) which currently have devices on them (GET /devices/floors).",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

# 7) Export history as CSV (max 50k records)
export_history_csv_function = {
    "name": "export_history_csv",
    "description": "Export client history records in CSV format (up to 50k). Returns raw CSV bytes.",
    "parameters": {
        "type": "object",
        "properties": {
            "formatType": {"type": "string", "description": "Should be 'csv'.", "default": "csv"},
            "limit": {"type": "number", "description": "Max items, up to 50000."},
            "format": {"type": "string"},
            "deviceId": {"type": "string"},
            "deviceType": {"type": "string"},
            "apMacAddress": {"type": "string"},
            "username": {"type": "string"},
            "ssid": {"type": "string"},
            "floorId": {"type": "string"},
            "campusId": {"type": "string"},
            "buildingId": {"type": "string"},
            "startTime": {"type": "string"},
            "endTime": {"type": "string"},
            "associated": {"type": "boolean"},
            "timeZone": {"type": "number"}
        },
        "required": []
    }
}

# 8) Export history as GZ (max 5 million records)
export_history_gz_function = {
    "name": "export_history_gz",
    "description": "Export client history records in gzipped format (up to 5 million). Returns raw gz bytes.",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string"},
            "deviceType": {"type": "string"},
            "apMacAddress": {"type": "string"},
            "username": {"type": "string"},
            "ssid": {"type": "string"},
            "floorId": {"type": "string"},
            "campusId": {"type": "string"},
            "buildingId": {"type": "string"},
            "startTime": {"type": "string"},
            "endTime": {"type": "string"},
            "associated": {"type": "boolean"},
            "timeZone": {"type": "number"}
        },
        "required": []
    }
}

# 9) Get history record count
get_history_record_count_function = {
    "name": "get_history_record_count",
    "description": "Get the count of history records within a given time range (up to 1 day).",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string"},
            "deviceType": {"type": "string"},
            "apMacAddress": {"type": "string"},
            "username": {"type": "string"},
            "ssid": {"type": "string"},
            "floorId": {"type": "string"},
            "campusId": {"type": "string"},
            "buildingId": {"type": "string"},
            "startTime": {"type": "string"},
            "endTime": {"type": "string"},
            "associated": {"type": "boolean"},
            "timeZone": {"type": "number"}
        },
        "required": []
    }
}

# 10) Get list of history devices
get_history_devices_function = {
    "name": "get_history_devices",
    "description": "Fetch the list of clients or devices seen in historical data (GET /history/devices).",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string"},
            "apMacAddress": {"type": "string"},
            "username": {"type": "string"},
            "ssid": {"type": "string"},
            "floorId": {"type": "string"},
            "campusId": {"type": "string"},
            "buildingId": {"type": "string"},
            "startTime": {"type": "string"},
            "endTime": {"type": "string"},
            "associated": {"type": "boolean"},
            "deviceType": {"type": "string"},
            "x": {"type": "number"},
            "y": {"type": "number"},
            "radius": {"type": "number"},
            "includeDetails": {"type": "boolean"},
            "timeZone": {"type": "number"}
        },
        "required": []
    }
}

# 11) Get history for a specific device
get_device_history_function = {
    "name": "get_spaces_device_history",
    "description": "Retrieve the historical data for a specific device (GET /history/device/{deviceId}).",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "Required device ID (MAC address)."},
            "apMacAddress": {"type": "string"},
            "username": {"type": "string"},
            "ssid": {"type": "string"},
            "floorId": {"type": "string"},
            "campusId": {"type": "string"},
            "buildingId": {"type": "string"},
            "startTime": {"type": "string"},
            "endTime": {"type": "string"},
            "associated": {"type": "boolean"},
            "timeZone": {"type": "number"},
            "deviceType": {"type": "string"},
            "x": {"type": "number"},
            "y": {"type": "number"},
            "radius": {"type": "number"},
            "includeDetails": {"type": "boolean"}
        },
        "required": ["deviceId"]
    }
}

get_spaces_location_subtree_function = {
    "name": "get_spaces_location_subtree",
    "description": "Retrieve the subtree of the Cisco Spaces location hierarchy for the given location_id.",
    "parameters": {
        "type": "object",
        "properties": {
            "location_id": {
                "type": "string",
                "description": "The unique ID of the location (as returned by /map/locationhierarchy)."
            }
        },
        "required": ["location_id"]
    }
}


#############################
# Cisco Catalyst Center (DNA Center)
#############################

# Retrieve all devices
get_all_catalyst_devices_function = {
    "name": "get_all_catalyst_devices",
    "description": "Fetch a list of all devices from Cisco Catalyst Center (DNA Center).",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

# Retrieve a single device by ID
get_catalyst_device_by_id_function = {
    "name": "get_catalyst_device_by_id",
    "description": "Fetch details of a single device by its device ID in Cisco Catalyst Center (DNA Center).",
    "parameters": {
        "type": "object",
        "properties": {
            "device_id": {
                "type": "string",
                "description": "The unique ID of the device in Cisco Catalyst Center."
            }
        },
        "required": ["device_id"]
    }
}

# Run a CLI command on a Catalyst device
run_cli_command_function = {
    "name": "run_cli_command_on_catalyst_device",
    "description": "Run a CLI command on a given Catalyst device.",
    "parameters": {
        "type": "object",
        "properties": {
            "device_id": {
                "type": "string",
                "description": "The ID of the Catalyst device."
            },
            "command": {
                "type": "string",
                "description": "The CLI command to run."
            }
        },
        "required": ["device_id", "command"]
    }
}

# Check the status of a DNA Center task by ID
get_catalyst_task_status_by_id_function = {
    "name": "get_catalyst_task_status_by_id",
    "description": "Check the status (and progress) of a DNA Center task by its task ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "task_id": {
                "type": "string",
                "description": "The unique ID of the DNA Center task."
            }
        },
        "required": ["task_id"]
    }
}

# Retrieve CLI Command Output by File ID
get_cli_command_output_function = {
    "name": "get_cli_command_output",
    "description": "Retrieve CLI command output by file ID from Catalyst Center.",
    "parameters": {
        "type": "object",
        "properties": {
            "file_id": {
                "type": "string",
                "description": "The ID of the file containing CLI command output."
            }
        },
        "required": ["file_id"]
    }
}

# Retrieve All Sites
get_all_sites_function = {
    "name": "get_all_sites",
    "description": "Fetch a list of all sites in DNA Center.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

# List All SSIDs
get_all_ssids_function = {
    "name": "get_all_ssids",
    "description": "List all wireless SSIDs in the environment.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

# Execute Path Trace
execute_path_trace_function = {
    "name": "execute_path_trace",
    "description": "Execute a path trace from a source IP to a destination IP.",
    "parameters": {
        "type": "object",
        "properties": {
            "source_ip": {
                "type": "string",
                "description": "The source IP address."
            },
            "destination_ip": {
                "type": "string",
                "description": "The destination IP address."
            }
        },
        "required": ["source_ip", "destination_ip"]
    }
}

# Retrieve Path Trace Result
get_path_trace_result_function = {
    "name": "get_path_trace_result",
    "description": "Retrieve the result of a path trace task by task ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "task_id": {
                "type": "string",
                "description": "The task ID of the path trace operation."
            }
        },
        "required": ["task_id"]
    }
}

get_catalyst_system_info_function = {
    "name": "get_catalyst_system_info",
    "description": "Retrieve Catalyst Center system information, including platform details.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

get_dnac_packages_summary_function = {
    "name": "get_dnac_packages_summary",
    "description": "Retrieve the summary of DNA Center packages, including their names and versions.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

# Retrieve all interfaces globally
get_all_interfaces_function = {
    "name": "get_all_interfaces",
    "description": "Retrieve all interfaces globally (up to 500 per request).",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

# Retrieve interfaces for a specific device
get_device_interfaces_function = {
    "name": "get_device_interfaces",
    "description": "Retrieve all interfaces for a specific device using its deviceId.",
    "parameters": {
        "type": "object",
        "properties": {
            "device_id": {
                "type": "string",
                "description": "The unique deviceId of the network device."
            }
        },
        "required": ["device_id"]
    }
}

# Retrieve interfaces for a specific management IP
get_interfaces_by_ip_function = {
    "name": "get_interfaces_by_ip",
    "description": "Retrieve interfaces for a specific management IP address.",
    "parameters": {
        "type": "object",
        "properties": {
            "ip_address": {
                "type": "string",
                "description": "The management IP address of the network device."
            }
        },
        "required": ["ip_address"]
    }
}

# Initiate Path Trace
initiate_path_trace_function = {
    "name": "initiate_path_trace",
    "description": "Initiate a path trace from a source IP to a destination IP.",
    "parameters": {
        "type": "object",
        "properties": {
            "source_ip": {
                "type": "string",
                "description": "The source IP address."
            },
            "destination_ip": {
                "type": "string",
                "description": "The destination IP address."
            }
        },
        "required": ["source_ip", "destination_ip"]
    }
}


# Get Path Trace Result
get_path_trace_result_function = {
    "name": "get_path_trace_result",
    "description": "Retrieve the result of a path trace using the flow analysis ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "flow_analysis_id": {
                "type": "string",
                "description": "The flow analysis ID of the path trace."
            }
        },
        "required": ["flow_analysis_id"]
    }
}


get_catalyst_device_list_function = {
    "name": "get_catalyst_device_list",
    "description": "Fetch the device list from DNA Center /dna/intent/api/v1/network-device using direct requests or dnacentersdk.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

get_device_detail_function = {
    "name": "get_device_detail",
    "description": "Retrieve a device’s detailed info by specifying an identifier type (e.g. ipaddress) and search value.",
    "parameters": {
        "type": "object",
        "properties": {
            "identifier": {
                "type": "string",
                "description": "The type of identifier to search by (e.g. macAddress, ipaddress, uuid, nwDeviceName)."
            },
            "search_by": {
                "type": "string",
                "description": "The actual value to match for the given identifier (e.g. 10.10.20.85)."
            }
        },
        "required": ["identifier", "search_by"]
    }
}

get_catalyst_device_detail_by_name_function = {
    "name": "get_catalyst_device_detail_by_name",
    "description": "Fetch device details from DNA Center by hostname (nwDeviceName).",
    "parameters": {
        "type": "object",
        "properties": {
            "device_name": {
                "type": "string",
                "description": "The DNS/hostname recognized by DNA Center (e.g. switch3.ciscotest.com)."
            }
        },
        "required": ["device_name"]
    }
}

get_catalyst_device_detail_by_mac_address_function = {
    "name": "get_catalyst_device_detail_by_mac_address",
    "description": "Fetch device details from DNA Center by MAC address.",
    "parameters": {
        "type": "object",
        "properties": {
            "mac_address": {
                "type": "string",
                "description": "The MAC address recognized by DNA Center (e.g. 52:54:00:01:c2:c0)."
            }
        },
        "required": ["mac_address"]
    }
}

get_site_by_name_function = {
    "name": "get_site_by_name",
    "description": "Retrieve a site's info from DNAC (v2) by specifying a site name hierarchy (groupNameHierarchy). E.g. Global/USA/CA.",
    "parameters": {
        "type": "object",
        "properties": {
            "site_name": {
                "type": "string",
                "description": "The site name hierarchy to look up (e.g. 'Global/USA/CA/San Jose')."
            }
        },
        "required": ["site_name"]
    }
}
 

get_all_devices_by_site_function = {
    "name": "get_all_devices_by_site",
    "description": "Retrieve all devices in a specific site from DNA Center by site ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "site_id": {
                "type": "string",
                "description": "The unique site ID in DNA Center (GUID)."
            }
        },
        "required": ["site_id"]
    }
}


#############################
# Meraki
#############################

# Retrieve all Meraki networks
get_meraki_networks_function = {
    "name": "get_meraki_networks",
    "description": "Fetch a list of Meraki networks for the authenticated organization.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

# Retrieve details of a single Meraki network by ID
get_meraki_network_by_id_function = {
    "name": "get_meraki_network_by_id",
    "description": "Fetch details of a single Meraki network by its network ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "network_id": {
                "type": "string",
                "description": "The unique ID of the Meraki network."
            }
        },
        "required": ["network_id"]
    }
}

get_organization_function = {
    "name": "get_organization",
    "description": "Retrieve details for a given organization by organization_id.",
    "parameters": {
        "type": "object",
        "properties": {
            "organization_id": {
                "type": "string",
                "description": "The unique identifier for the organization."
            }
        },
        "required": ["organization_id"]
    }
}

get_organization_networks_function = {
    "name": "get_organization_networks",
    "description": "Retrieve a list of networks in the organization.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

get_organization_inventory_devices_function = {
    "name": "get_organization_inventory_devices",
    "description": "Retrieve a list of all devices in the organization.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}



get_organization_licenses_overview_function = {
    "name": "get_organization_licenses_overview",
    "description": "Retrieve an overview summary of license usage and status.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

list_all_clients_in_org_function = {
    "name": "list_all_clients_in_org",
    "description": "Enumerate all clients across all networks in Meraki org, optionally filtering by timespan.",
    "parameters": {
        "type": "object",
        "properties": {
            "timespan": {
                "type": "number",
                "description": "Time range (in seconds) to look back, e.g. 86400 for 1 day. Default 14 days."
            }
        },
        "required": []
    }
}

list_all_clients_in_org_by_name_function = {
    "name": "list_all_clients_in_org_by_name",
    "description": "List Meraki clients whose name or hostname contains the specified substring, over a given timespan.",
    "parameters": {
        "type": "object",
        "properties": {
            "name_substring": {
                "type": "string",
                "description": "Case-insensitive substring to match against client description or hostname."
            },
            "timespan": {
                "type": "number",
                "description": "Look back timespan in seconds (default 14 days)."
            }
        },
        "required": ["name_substring"]  # 'timespan' is optional
    }
}

get_network_alerts_history_function = {
    "name": "get_network_alerts_history",
    "description": "Retrieve historical alerts for a specific network.",
    "parameters": {
        "type": "object",
        "properties": {
            "network_id": {
                "type": "string",
                "description": "The unique ID of the network."
            }
        },
        "required": ["network_id"]
    }
}

get_network_clients_function = {
    "name": "get_network_clients",
    "description": "Retrieve a list of clients connected to a given network.",
    "parameters": {
        "type": "object",
        "properties": {
            "network_id": {
                "type": "string",
                "description": "The network identifier."
            }
        },
        "required": ["network_id"]
    }
}


get_organization_wireless_ssids_function = {
    "name": "get_organization_wireless_ssids",
    "description": "Retrieve a list of wireless SSIDs configured in the organization.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

get_organization_inventory_device_function = {
    "name": "get_organization_inventory_device",
    "description": "Retrieve detailed information for a specific device by device_id.",
    "parameters": {
        "type": "object",
        "properties": {
            "device_id": {"type": "string", "description": "The unique device identifier."}
        },
        "required": ["device_id"]
    }
}

get_organization_login_security_function = {
    "name": "get_organization_login_security",
    "description": "Retrieve the login security settings for the organization.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}


get_meraki_network_devices_function = {
    "name": "get_meraki_network_devices",
    "description": "List all devices in a specific network (GET /networks/{networkId}/devices).",
    "parameters": {
        "type": "object",
        "properties": {
            "network_id": {
                "type": "string",
                "description": "The Meraki network identifier."
            }
        },
        "required": ["network_id"]
    }
}


get_meraki_device_switch_ports_function = {
    "name": "get_meraki_device_switch_ports",
    "description": "Retrieve switch port details for a switch device by serial (GET /devices/{serial}/switchPorts).",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {
                "type": "string",
                "description": "The Meraki switch device serial number."
            }
        },
        "required": ["serial"]
    }
}

get_meraki_network_wireless_ssids_function = {
    "name": "get_meraki_network_wireless_ssids",
    "description": "Retrieve the list of SSIDs configured for a wireless network (GET /networks/{networkId}/wireless/ssids).",
    "parameters": {
        "type": "object",
        "properties": {
            "network_id": {
                "type": "string",
                "description": "The Meraki network identifier."
            }
        },
        "required": ["network_id"]
    }
}

list_all_devices_in_org_function = {
    "name": "list_all_devices_in_org",
    "description": "Retrieve a list of all Meraki devices in the organization (inventory).",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

get_all_access_points_function = {
    "name": "get_all_access_points",
    "description": "Retrieve all Meraki access points in the organization (wireless controllers).",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

list_all_switches_in_org_function = {
    "name": "list_all_switches_in_org",
    "description": "List all switch devices (MS) in the Meraki organization’s inventory.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

list_all_cameras_in_org_function = {
    "name": "list_all_cameras_in_org",
    "description": "List all Meraki cameras in the organization by checking camera onboarding statuses.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

#############################
# Webex Control Hub
#############################

# Retrieve all meetings
get_webex_meetings_function = {
    "name": "get_webex_meetings",
    "description": "Fetch a list of upcoming or recorded Webex meetings for the authenticated user/organization.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

# Retrieve details of a single Webex meeting
get_webex_meeting_by_id_function = {
    "name": "get_webex_meeting_by_id",
    "description": "Fetch details of a specific Webex meeting by its meeting ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "meeting_id": {
                "type": "string",
                "description": "The unique ID of the Webex meeting."
            }
        },
        "required": ["meeting_id"]
    }
}

#############################
# Combine all function definitions
#############################
FUNCTION_DEFINITIONS = [

    # Cisco Spaces
    get_spaces_floor_details_function,
    get_spaces_location_hierarchy_function,
    get_spaces_floor_image_function,
    get_spaces_devices_function,
    get_spaces_devices_count_function,
    get_spaces_devices_floors_function,
    export_history_csv_function,
    export_history_gz_function,
    get_history_record_count_function,
    get_history_devices_function,
    get_device_history_function,
    get_spaces_location_subtree_function,
    # Cisco Catalyst Center
    get_all_catalyst_devices_function,
    get_catalyst_device_by_id_function,
    run_cli_command_function,
    get_catalyst_task_status_by_id_function,
    get_cli_command_output_function,
    get_all_sites_function,
    get_all_ssids_function,
    get_catalyst_system_info_function,
    get_dnac_packages_summary_function,
    get_all_interfaces_function,
    get_device_interfaces_function,
    get_interfaces_by_ip_function,
    initiate_path_trace_function,
    get_path_trace_result_function,
    get_catalyst_device_list_function,
    get_device_detail_function,
    get_catalyst_device_detail_by_name_function,
    get_catalyst_device_detail_by_mac_address_function,
    get_site_by_name_function,
    get_all_devices_by_site_function,
    
    # Meraki
    get_meraki_networks_function,
    get_meraki_network_by_id_function,
    get_organization_function,
    get_organization_networks_function,
    get_organization_inventory_devices_function,
    get_organization_licenses_overview_function,
    get_network_alerts_history_function,
    get_network_clients_function,
    get_organization_wireless_ssids_function,
    get_organization_inventory_device_function,
    get_organization_login_security_function,
    get_meraki_network_devices_function,
    get_meraki_device_switch_ports_function,
    get_meraki_network_wireless_ssids_function,
    list_all_clients_in_org_function,
    list_all_clients_in_org_by_name_function,
    list_all_devices_in_org_function,
    get_all_access_points_function,
    list_all_switches_in_org_function,
    list_all_cameras_in_org_function,
    
    # Webex
    get_webex_meetings_function,
    get_webex_meeting_by_id_function,
]
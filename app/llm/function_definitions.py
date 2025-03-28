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







##############################################
# Catalyst Center SDK (DNA Center) - Functions
##############################################

getsAllTheVersionsOfAGivenTemplate_function = {
    "name": "getsAllTheVersionsOfAGivenTemplate",
    "description": "Get all the versions of template by its id",
    "parameters": {
        "type": "object",
        "properties": {
            "templateId": {"type": "string", "description": "templateId(UUID) to get list of versioned templates"},
        },
        "required": ["templateId"]
    }
}

getMulticastVirtualNetworks_function = {
    "name": "getMulticastVirtualNetworks",
    "description": "Returns a list of multicast configurations for virtual networks that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric site where multicast is configured."},
            "virtualNetworkName": {"type": "string", "description": "Name of the virtual network associated to the multicast configuration."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getDeviceControllabilitySettings_function = {
    "name": "getDeviceControllabilitySettings",
    "description": "Device Controllability is a system-level process on Catalyst Center that enforces state synchronization for some device-layer features. Its purpose is to aid in the deployment of required network settings that Catalyst Center needs to manage devices. Changes are made on network devices during discovery, when adding a device to Inventory, or when assigning a device to a site. If changes are made to any settings that are under the scope of this process, these changes are applied to the network devices during the Provision and Update Telemetry Settings operations, even if Device Controllability is disabled. The following device settings will be enabled as part of Device Controllability when devices are discovered. - SNMP Credentials. - NETCONF Credentials. Subsequent to discovery, devices will be added to Inventory. The following device settings will be enabled when devices are added to inventory. - Cisco TrustSec (CTS) Credentials. The following device settings will be enabled when devices are assigned to a site. Some of these settings can be defined at a site level under Design > Network Settings > Telemetry & Wireless. - Wired Endpoint Data Collection Enablement. - Controller Certificates. - SNMP Trap Server Definitions. - Syslog Server Definitions. - Application Visibility. - Application QoS Policy. - Wireless Service Assurance (WSA). - Wireless Telemetry. - DTLS Ciphersuite. - AP Impersonation. If Device Controllability is disabled, Catalyst Center does not configure any of the preceding credentials or settings on devices during discovery, at runtime, or during site assignment. However, the telemetry settings and related configuration are pushed when the device is provisioned or when the update Telemetry Settings action is performed. Catalyst Center identifies and automatically corrects the following telemetry configuration issues on the device. - SWIM certificate issue. - IOS WLC NA certificate issue. - PKCS12 certificate issue. - IOS telemetry configuration issu",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getChassisDetailsForDevice_function = {
    "name": "getChassisDetailsForDevice",
    "description": "Returns chassis details for given device ID",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["deviceId"]
    }
}

getsABuilding_function = {
    "name": "getsABuilding",
    "description": "Gets a building in the network hierarchy.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Building Id"},
        },
        "required": ["id"]
    }
}

getCountOfAllDiscoveryJobs_function = {
    "name": "getCountOfAllDiscoveryJobs",
    "description": "Returns the count of all available discovery jobs",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getViewsForAGivenViewGroup_function = {
    "name": "getViewsForAGivenViewGroup",
    "description": "Gives a list of summary of all views in a viewgroup. Use \"Get all view groups\" API to get the viewGroupIds (required as a query param for this API) for available viewgroups.",
    "parameters": {
        "type": "object",
        "properties": {
            "viewGroupId": {"type": "string", "description": "viewGroupId of viewgroup."},
        },
        "required": ["viewGroupId"]
    }
}

getDeviceById_function = {
    "name": "getDeviceById",
    "description": "Returns device details specified by device id",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "id"},
        },
        "required": ["id"]
    }
}

retrieveImageDistributionServers_function = {
    "name": "retrieveImageDistributionServers",
    "description": "Retrieve the list of remote image distribution servers. There can be up to two remote servers.Product always acts as local distribution server, and it is not part of this API response.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

retrieveBannerSettingsForASite_function = {
    "name": "retrieveBannerSettingsForASite",
    "description": "Retrieve banner settings for a site; `null` values indicate that the setting will be inherited from the parent site; empty objects (`{}`) indicate that the setting is unset at a site.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Site Id"},
            "_inherited": {"type": "boolean", "description": "Include settings explicitly set for this site and settings inherited from sites higher in the site hierarchy; when `false`, `null` values indicate that the site inherits that setting from the parent site or a site higher in the site hierarchy."},
        },
        "required": ["id"]
    }
}

getSiteAssignedNetworkDevices_function = {
    "name": "getSiteAssignedNetworkDevices",
    "description": "Get all site assigned network devices. The items in the list are arranged in an order that corresponds with their internal identifiers.",
    "parameters": {
        "type": "object",
        "properties": {
            "siteId": {"type": "string", "description": "Site Id. It must be area Id or building Id or floor Id."},
            "offset": {"type": "number", "description": "The first record to show for this page; the first record is numbered 1."},
            "limit": {"type": "number", "description": "The number of records to show for this page."},
        },
        "required": ["siteId"]
    }
}

getNetworkDevicesCredentialsSyncStatus_function = {
    "name": "getNetworkDevicesCredentialsSyncStatus",
    "description": "Get network devices credentials sync status at a given site.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Site Id."},
        },
        "required": ["id"]
    }
}

getSoftwareImageDetails_function = {
    "name": "getSoftwareImageDetails",
    "description": "Returns software image list based on a filter criteria. For example: \"filterbyName = cat3k%\"",
    "parameters": {
        "type": "object",
        "properties": {
            "imageUuid": {"type": "string", "description": "imageUuid"},
            "name": {"type": "string", "description": "name"},
            "family": {"type": "string", "description": "family"},
            "applicationType": {"type": "string", "description": "applicationType"},
            "imageIntegrityStatus": {"type": "string", "description": "imageIntegrityStatus - FAILURE, UNKNOWN, VERIFIED"},
            "version": {"type": "string", "description": "software Image Version"},
            "imageSeries": {"type": "string", "description": "image Series"},
            "imageName": {"type": "string", "description": "image Name"},
            "isTaggedGolden": {"type": "boolean", "description": "is Tagged Golden"},
            "isCCORecommended": {"type": "boolean", "description": "is recommended from cisco.com"},
            "isCCOLatest": {"type": "boolean", "description": "is latest from cisco.com"},
            "createdTime": {"type": "integer", "description": "time in milliseconds (epoch format)"},
            "imageSizeGreaterThan": {"type": "integer", "description": "size in bytes"},
            "imageSizeLesserThan": {"type": "integer", "description": "size in bytes"},
            "sortBy": {"type": "string", "description": "sort results by this field"},
            "sortOrder": {"type": "string", "description": "sort order - 'asc' or 'des'. Default is asc"},
            "limit": {"type": "integer", "description": "limit"},
            "offset": {"type": "integer", "description": "offset"},
        },
        "required": []
    }
}

getAnycastGateways_function = {
    "name": "getAnycastGateways",
    "description": "Returns a list of anycast gateways that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "ID of the anycast gateway."},
            "fabricId": {"type": "string", "description": "ID of the fabric the anycast gateway is assigned to."},
            "virtualNetworkName": {"type": "string", "description": "Name of the virtual network associated with the anycast gateways."},
            "ipPoolName": {"type": "string", "description": "Name of the IP pool associated with the anycast gateways."},
            "vlanName": {"type": "string", "description": "VLAN name of the anycast gateways."},
            "vlanId": {"type": "number", "description": "VLAN ID of the anycast gateways. The allowed range for vlanId is [2-4093] except for reserved VLANs [1002-1005], 2046, and 4094."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getTagMembersById_function = {
    "name": "getTagMembersById",
    "description": "Returns tag members specified by id",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Tag ID"},
            "memberType": {"type": "string", "description": "Entity type of the member. Possible values can be retrieved by using /tag/member/type API"},
            "offset": {"type": "number", "description": "Used for pagination. It indicates the starting row number out of available member records"},
            "limit": {"type": "number", "description": "Used to Number of maximum members to return in the result"},
            "memberAssociationType": {"type": "string", "description": "Indicates how the member is associated with the tag. Possible values and description. 1) DYNAMIC : The member is associated to the tag through rules. 2) STATIC – The member is associated to the tag manually. 3) MIXED – The member is associated manually and also satisfies the rule defined for the tag"},
            "level": {"type": "string", "description": "level"},
        },
        "required": ["id", "memberType"]
    }
}

getFabricSiteCount_function = {
    "name": "getFabricSiteCount",
    "description": "Returns the count of fabric sites that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

retrievesAllTheValidationSets_function = {
    "name": "retrievesAllTheValidationSets",
    "description": "Retrieves all the validation sets and optionally the contained validations",
    "parameters": {
        "type": "object",
        "properties": {
            "view": {"type": "string", "description": "When the query parameter `view=DETAIL` is passed, all validation sets and associated validations will be returned. When the query parameter `view=DEFAULT` is passed, only validation sets metadata will be returned."},
        },
        "required": []
    }
}

retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo_function = {
    "name": "retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo",
    "description": "Retrieves the list of sites that the given network profile for sites is assigned to.  The list includes the sites the profile has been directly assigned to, as well as child sites that have inherited the profile.",
    "parameters": {
        "type": "object",
        "properties": {
            "profileId": {"type": "string", "description": "The `id` of the network profile, retrievable from `GET /intent/api/v1/networkProfilesForSites`"},
            "offset": {"type": "number", "description": "The first record to show for this page; the first record is numbered 1."},
            "limit": {"type": "number", "description": "The number of records to show for this page."},
        },
        "required": ["profileId"]
    }
}

getFabricDevicesLayer2HandoffsCount_function = {
    "name": "getFabricDevicesLayer2HandoffsCount",
    "description": "Returns the count of layer 2 handoffs of fabric devices that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric this device belongs to."},
            "networkDeviceId": {"type": "string", "description": "Network device ID of the fabric device."},
        },
        "required": ["fabricId"]
    }
}

countOfEventSubscriptions_function = {
    "name": "countOfEventSubscriptions",
    "description": "Returns the Count of EventSubscriptions",
    "parameters": {
        "type": "object",
        "properties": {
            "eventIds": {"type": "string", "description": "List of subscriptions related to the respective eventIds"},
        },
        "required": ["eventIds"]
    }
}

getDetailsOfASingleAssuranceEvent_function = {
    "name": "getDetailsOfASingleAssuranceEvent",
    "description": "API to fetch the details of an assurance event using event `id`. For detailed information about the usage of the API, please refer to the Open API specification document - https://github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceEvents-1.0.0-resolved.yaml",
    "parameters": {
        "type": "object",
        "properties": {
            "X-CALLER-ID": {"type": "string", "description": "Caller ID is used to trace the origin of API calls and their associated queries executed on the database. It's an optional header parameter that can be added to an API request."},
            "id": {"type": "string", "description": "Unique identifier for the event"},
            "attribute": {"type": "string", "description": "The list of attributes that needs to be included in the response. If this parameter is not provided, then basic attributes (`id`, `name`, `timestamp`, `details`, `messageType`, `siteHierarchyId`, `siteHierarchy`, `deviceFamily`, `networkDeviceId`, `networkDeviceName`, `managementIpAddress`) would be part of the response.  Examples:  `attribute=name` (single attribute requested)  `attribute=name&attribute=networkDeviceName` (multiple attribute requested)"},
            "view": {"type": "string", "description": "The list of events views. Please refer to `EventViews` for the supported list  Examples:  `view=network` (single view requested)  `view=network&view=ap` (multiple view requested)"},
        },
        "required": ["id"]
    }
}

retrieveTelemetrySettingsForASite_function = {
    "name": "retrieveTelemetrySettingsForASite",
    "description": "Retrieves telemetry settings for the given site. `null` values indicate that the setting will be inherited from the parent site.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Site Id, retrievable from the `id` attribute in `/dna/intent/api/v1/sites`"},
            "_inherited": {"type": "boolean", "description": "Include settings explicitly set for this site and settings inherited from sites higher in the site hierarchy; when `false`, `null` values indicate that the site inherits that setting from the parent site or a site higher in the site hierarchy."},
        },
        "required": ["id"]
    }
}

getFloorSettings_function = {
    "name": "getFloorSettings",
    "description": "Gets UI user preference for floor unit system.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getTheTotalNumberOfIssuesForGivenSetOfFilters_function = {
    "name": "getTheTotalNumberOfIssuesForGivenSetOfFilters",
    "description": "Returns the total number issues for given set of filters. If there is no start and/or end time, then end time will be defaulted to current time and start time will be defaulted to 24-hours ago from end time. https://github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-IssuesList-1.0.0-resolved.yaml",
    "parameters": {
        "type": "object",
        "properties": {
            "X-CALLER-ID": {"type": "string", "description": "Caller ID can be used to trace the caller for queries executed on database. The caller id is like a optional attribute which can be added to API invocation like ui, python, postman, test-automation etc"},
            "startTime": {"type": "number", "description": "Start time from which API queries the data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive.  If `startTime` is not provided, API will default to current time."},
            "endTime": {"type": "number", "description": "End time to which API queries the data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive."},
            "isGlobal": {"type": "boolean", "description": "Global issues are those issues which impacts across many devices, sites. They are also displayed on Issue Dashboard in Catalyst Center UI. Non-Global issues are displayed only on Client 360 or Device 360 pages. If this flag is 'true', only global issues are returned. If it if 'false', all issues are returned."},
            "priority": {"type": "string", "description": "Priority of the issue. Supports single priority and multiple priorities Examples: priority=P1 (single priority requested) priority=P1&priority=P2&priority=P3 (multiple priorities requested)"},
            "severity": {"type": "string", "description": "Severity of the issue. Supports single severity and multiple severities. Examples: severity=high (single severity requested) severity=high&severity=medium (multiple severities requested)"},
            "status": {"type": "string", "description": "Status of the issue. Supports single status and multiple statuses. Examples: status=active (single status requested) status=active&status=resolved (multiple statuses requested)"},
            "entityType": {"type": "string", "description": "Entity type of the issue. Supports single entity type and multiple entity types. Examples: entityType=networkDevice (single entity type requested) entityType=network device&entityType=client (multiple entity types requested)"},
            "category": {"type": "string", "description": "Categories of the issue. Supports single category and multiple categories. Examples: category=availability (single status requested) category=availability&category=onboarding (multiple categories requested)"},
            "deviceType": {"type": "string", "description": "Device Type of the device to which this issue belongs to. Supports single device type and multiple device types. Examples: deviceType=wireless controller (single device type requested) deviceType=wireless controller&deviceType=core (multiple device types requested)"},
            "name": {"type": "string", "description": "The name of the issue Examples: name=ap_down (single issue name requested) name=ap_down&name=wlc_monitor (multiple issue names requested) Issue names can be retrieved using the API - /data/api/v1/assuranceIssueConfigurations"},
            "issueId": {"type": "string", "description": "UUID of the issue Examples: issueId=e52aecfe-b142-4287-a587-11a16ba6dd26 (single issue id requested) issueId=e52aecfe-b142-4287-a587-11a16ba6dd26&issueId=864d0421-02c0-43a6-9c52-81cad45f66d8 (multiple issue ids requested)"},
            "entityId": {"type": "string", "description": "Id of the entity for which this issue belongs to. For example, it     could be mac address of AP or UUID of Sensor   example: 68:ca:e4:79:3f:20 4de02167-901b-43cf-8822-cffd3caa286f Examples: entityId=68:ca:e4:79:3f:20 (single entity id requested) entityId=68:ca:e4:79:3f:20&entityId=864d0421-02c0-43a6-9c52-81cad45f66d8 (multiple entity ids requested)"},
            "updatedBy": {"type": "string", "description": "The user who last updated this issue. Examples: updatedBy=admin (single updatedBy requested) updatedBy=admin&updatedBy=john (multiple updatedBy requested)"},
            "siteHierarchy": {"type": "string", "description": "The full hierarchical breakdown of the site tree starting from Global site name and ending with the specific site name. The Root site is named \"Global\" (Ex. `Global/AreaName/BuildingName/FloorName`)  This field supports wildcard asterisk (*) character search support. E.g. */San*, */San, /San*  Examples:  `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)  `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested)"},
            "siteHierarchyId": {"type": "string", "description": "The full hierarchy breakdown of the site tree in id form starting from Global site UUID and ending with the specific site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`)  This field supports wildcard asterisk (*) character search support. E.g. `*uuid*, *uuid, uuid*  Examples:  `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId requested)  `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested)"},
            "siteName": {"type": "string", "description": "The name of the site. (Ex. `FloorName`)  This field supports wildcard asterisk (*) character search support. E.g. *San*, *San, San*  Examples:  `?siteName=building1` (single siteName requested)  `?siteName=building1&siteName=building2&siteName=building3` (multiple siteNames requested)"},
            "siteId": {"type": "string", "description": "The UUID of the site. (Ex. `flooruuid`)  This field supports wildcard asterisk (*) character search support. E.g.*flooruuid*, *flooruuid, flooruuid*  Examples:  `?siteId=id1` (single id requested)  `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested)"},
            "fabricSiteId": {"type": "string", "description": "The UUID of the fabric site. (Ex. \"flooruuid\") Examples: fabricSiteId=e52aecfe-b142-4287-a587-11a16ba6dd26 (single id requested) fabricSiteId=e52aecfe-b142-4287-a587-11a16ba6dd26,864d0421-02c0-43a6-9c52-81cad45f66d8 (multiple ids requested)"},
            "fabricVnName": {"type": "string", "description": "The name of the fabric virtual network Examples: fabricVnName=name1 (single fabric virtual network name requested) fabricVnName=name1&fabricVnName=name2&fabricVnName=name3 (multiple fabric virtual network names requested)"},
            "fabricTransitSiteId": {"type": "string", "description": "The UUID of the fabric transit site. (Ex. \"flooruuid\") Examples: fabricTransitSiteId=e52aecfe-b142-4287-a587-11a16ba6dd26 (single id requested) fabricTransitSiteId=e52aecfe-b142-4287-a587-11a16ba6dd26&fabricTransitSiteId=864d0421-02c0-43a6-9c52-81cad45f66d8 (multiple ids requested)"},
            "networkDeviceId": {"type": "string", "description": "The list of Network Device Uuids. (Ex. `6bef213c-19ca-4170-8375-b694e251101c`)  Examples:  `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId requested)  `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple networkDeviceIds with & separator)"},
            "networkDeviceIpAddress": {"type": "string", "description": "The list of Network Device management IP Address. (Ex. `121.1.1.10`)  This field supports wildcard (`*`) character-based search.  Ex: `*1.1*` or `1.1*` or `*1.1`  Examples:  `networkDeviceIpAddress=121.1.1.10`  `networkDeviceIpAddress=121.1.1.10&networkDeviceIpAddress=172.20.1.10&networkDeviceIpAddress=10.10.20.10` (multiple networkDevice IP Address with & separator)"},
            "macAddress": {"type": "string", "description": "The macAddress of the network device or client This field supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or `*AB:AB:AB` Examples:  `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)  `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress requested)"},
            "aiDriven": {"type": "boolean", "description": "Flag whether the issue is AI driven issue"},
            "fabricDriven": {"type": "boolean", "description": "Flag whether the issue is related to a Fabric site, a virtual network or a transit."},
            "fabricSiteDriven": {"type": "boolean", "description": "Flag whether the issue is Fabric site driven issue"},
            "fabricVnDriven": {"type": "boolean", "description": "Flag whether the issue is Fabric Virtual Network driven issue"},
            "fabricTransitDriven": {"type": "boolean", "description": "Flag whether the issue is Fabric Transit driven issue"},
        },
        "required": []
    }
}

getTag_function = {
    "name": "getTag",
    "description": "Returns the tags for given filter criteria",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Tag name is mandatory when filter operation is used."},
            "additionalInfo.nameSpace": {"type": "string", "description": "nameSpace"},
            "additionalInfo.attributes": {"type": "string", "description": "attributeName"},
            "level": {"type": "string", "description": "levelArg"},
            "offset": {"type": "number", "description": "offset"},
            "limit": {"type": "number", "description": "limit"},
            "size": {"type": "string", "description": "size in kilobytes(KB)"},
            "field": {"type": "string", "description": "Available field names are :'name,id,parentId,type,additionalInfo.nameSpace,additionalInfo.attributes'"},
            "sortBy": {"type": "string", "description": "Only supported attribute is name. SortyBy is mandatory when order is used."},
            "order": {"type": "string", "description": "Available values are asc and des"},
            "systemTag": {"type": "string", "description": "systemTag"},
        },
        "required": []
    }
}

getLayer2VirtualNetworks_function = {
    "name": "getLayer2VirtualNetworks",
    "description": "Returns a list of layer 2 virtual networks that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "ID of the layer 2 virtual network."},
            "fabricId": {"type": "string", "description": "ID of the fabric the layer 2 virtual network is assigned to."},
            "vlanName": {"type": "string", "description": "The vlan name of the layer 2 virtual network."},
            "vlanId": {"type": "number", "description": "The vlan ID of the layer 2 virtual network."},
            "trafficType": {"type": "string", "description": "The traffic type of the layer 2 virtual network."},
            "associatedLayer3VirtualNetworkName": {"type": "string", "description": "Name of the associated layer 3 virtual network."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getFabricZoneCount_function = {
    "name": "getFabricZoneCount",
    "description": "Returns the count of fabric zones that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getWebhookDestination_function = {
    "name": "getWebhookDestination",
    "description": "Get Webhook Destination",
    "parameters": {
        "type": "object",
        "properties": {
            "webhookIds": {"type": "string", "description": "List of webhook configurations"},
            "offset": {"type": "number", "description": "The number of webhook configuration's to offset in the resultset whose default value 0"},
            "limit": {"type": "number", "description": "The number of webhook configuration's to limit in the resultset whose default value 10"},
            "sortBy": {"type": "string", "description": "SortBy field name"},
            "order": {"type": "string", "description": "order(asc/desc)"},
        },
        "required": []
    }
}

retrieveTimeZoneSettingsForASite_function = {
    "name": "retrieveTimeZoneSettingsForASite",
    "description": "Retrieve time zone settings for a site; `null` values indicate that the setting will be inherited from the parent site; empty objects (`{}`) indicate that the setting is unset at a site.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Site Id"},
            "_inherited": {"type": "boolean", "description": "Include settings explicitly set for this site and settings inherited from sites higher in the site hierarchy; when `false`, `null` values indicate that the site inherits that setting from the parent site or a site higher in the site hierarchy."},
        },
        "required": ["id"]
    }
}

getApplicationPolicyQueuingProfile_function = {
    "name": "getApplicationPolicyQueuingProfile",
    "description": "Get all or by name, existing application policy queuing profiles",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "queuing profile name"},
        },
        "required": []
    }
}

getSyslogDestination_function = {
    "name": "getSyslogDestination",
    "description": "Get Syslog Destination",
    "parameters": {
        "type": "object",
        "properties": {
            "configId": {"type": "string", "description": "Config id of syslog server"},
            "name": {"type": "string", "description": "Name of syslog server"},
            "protocol": {"type": "string", "description": "Protocol of syslog server"},
            "offset": {"type": "number", "description": "The number of syslog configuration's to offset in the resultset whose default value 0"},
            "limit": {"type": "number", "description": "The number of syslog configuration's to limit in the resultset whose default value 10"},
            "sortBy": {"type": "string", "description": "SortBy field name"},
            "order": {"type": "string", "description": "order(asc/desc)"},
        },
        "required": []
    }
}

getSyncResultForVirtualAccount_function = {
    "name": "getSyncResultForVirtualAccount",
    "description": "Returns the summary of devices synced from the given smart account & virtual account with PnP (Deprecated)",
    "parameters": {
        "type": "object",
        "properties": {
            "domain": {"type": "string", "description": "Smart Account Domain"},
            "name": {"type": "string", "description": "Virtual Account Name"},
        },
        "required": ["domain", "name"]
    }
}

getApplicationPolicyDefault_function = {
    "name": "getApplicationPolicyDefault",
    "description": "Get default application policy",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getModuleInfoById_function = {
    "name": "getModuleInfoById",
    "description": "Returns Module info by 'module id'",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Module id"},
        },
        "required": ["id"]
    }
}

getFabricDevicesLayer3HandoffsWithSdaTransit_function = {
    "name": "getFabricDevicesLayer3HandoffsWithSdaTransit",
    "description": "Returns a list of layer 3 handoffs with sda transit of fabric devices that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric this device belongs to."},
            "networkDeviceId": {"type": "string", "description": "Network device ID of the fabric device."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": ["fabricId"]
    }
}

getFabricDevicesLayer3HandoffsWithIpTransit_function = {
    "name": "getFabricDevicesLayer3HandoffsWithIpTransit",
    "description": "Returns a list of layer 3 handoffs with ip transit of fabric devices that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric this device belongs to."},
            "networkDeviceId": {"type": "string", "description": "Network device ID of the fabric device."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": ["fabricId"]
    }
}

countOfNotifications_function = {
    "name": "countOfNotifications",
    "description": "Get the Count of Published Notifications",
    "parameters": {
        "type": "object",
        "properties": {
            "eventIds": {"type": "string", "description": "The registered EventId should be provided"},
            "startTime": {"type": "number", "description": "Start Time in milliseconds"},
            "endTime": {"type": "number", "description": "End Time in milliseconds"},
            "category": {"type": "string", "description": "Category"},
            "type": {"type": "string", "description": "Type"},
            "severity": {"type": "string", "description": "Severity"},
            "domain": {"type": "string", "description": "Domain"},
            "subDomain": {"type": "string", "description": "Sub Domain"},
            "source": {"type": "string", "description": "Source"},
        },
        "required": []
    }
}

getAScheduledReport_function = {
    "name": "getAScheduledReport",
    "description": "Get scheduled report configuration by reportId",
    "parameters": {
        "type": "object",
        "properties": {
            "reportId": {"type": "string", "description": "reportId of report"},
        },
        "required": ["reportId"]
    }
}

getSiteHealth_function = {
    "name": "getSiteHealth",
    "description": "Returns Overall Health information for all sites",
    "parameters": {
        "type": "object",
        "properties": {
            "siteType": {"type": "string", "description": "site type: AREA or BUILDING (case insensitive)"},
            "offset": {"type": "number", "description": "Offset of the first returned data set entry (Multiple of 'limit' + 1)"},
            "limit": {"type": "number", "description": "Max number of data entries in the returned data set [1,50].  Default is 25"},
            "timestamp": {"type": "number", "description": "Epoch time(in milliseconds) when the Site Hierarchy data is required"},
        },
        "required": []
    }
}

getSitesCount_function = {
    "name": "getSitesCount",
    "description": "Get sites count.",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Site name."},
        },
        "required": []
    }
}

retrievesTheListOfValidationWorkflows_function = {
    "name": "retrievesTheListOfValidationWorkflows",
    "description": "Retrieves the workflows that have been successfully submitted and are currently available. This is sorted by `submitTime`",
    "parameters": {
        "type": "object",
        "properties": {
            "startTime": {"type": "number", "description": "Workflows started after the given time (as milliseconds since UNIX epoch)."},
            "endTime": {"type": "number", "description": "Workflows started before the given time (as milliseconds since UNIX epoch)."},
            "runStatus": {"type": "string", "description": "Execution status of the workflow. If the workflow is successfully submitted, runStatus is `PENDING`. If the workflow execution has started, runStatus is `IN_PROGRESS`. If the workflow executed is completed with all validations executed, runStatus is `COMPLETED`. If the workflow execution fails while running validations, runStatus is `FAILED`."},
            "offset": {"type": "number", "description": "The first record to show for this page; the first record is numbered 1."},
            "limit": {"type": "number", "description": "The number of records to show for this page."},
        },
        "required": []
    }
}

retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned_function = {
    "name": "retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned",
    "description": "Retrieves the count of profiles that the given site has been assigned.  These profiles may either be directly assigned to this site, or were assigned to a parent site and have been inherited.",
    "parameters": {
        "type": "object",
        "properties": {
            "siteId": {"type": "string", "description": "The `id` of the site, retrievable from `/dna/intent/api/v1/sites`"},
        },
        "required": ["siteId"]
    }
}

getSiteCountV2_function = {
    "name": "getSiteCountV2",
    "description": "Get the site count of the specified site's sub-hierarchy (inclusive of the provided site)",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Site instance UUID"},
        },
        "required": []
    }
}

getExtranetPolicies_function = {
    "name": "getExtranetPolicies",
    "description": "Returns a list of extranet policies that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "extranetPolicyName": {"type": "string", "description": "Name of the extranet policy."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getFlexibleReportScheduleByReportId_function = {
    "name": "getFlexibleReportScheduleByReportId",
    "description": "Get flexible report schedule by report id",
    "parameters": {
        "type": "object",
        "properties": {
            "Content-Type": {"type": "string", "description": "Request body content type"},
            "reportId": {"type": "string", "description": "Id of the report"},
        },
        "required": ["Content-Type", "reportId"]
    }
}

getPortChannels_function = {
    "name": "getPortChannels",
    "description": "Returns a list of port channels that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric the device is assigned to."},
            "networkDeviceId": {"type": "string", "description": "ID of the network device."},
            "portChannelName": {"type": "string", "description": "Name of the port channel."},
            "connectedDeviceType": {"type": "string", "description": "Connected device type of the port channel. The allowed values are [TRUNK, EXTENDED_NODE]."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getsTheTemplatesAvailable_function = {
    "name": "getsTheTemplatesAvailable",
    "description": "List the templates available",
    "parameters": {
        "type": "object",
        "properties": {
            "projectId": {"type": "string", "description": "Filter template(s) based on project UUID"},
            "softwareType": {"type": "string", "description": "Filter template(s) based software type"},
            "softwareVersion": {"type": "string", "description": "Filter template(s) based softwareVersion"},
            "productFamily": {"type": "string", "description": "Filter template(s) based on device family"},
            "productSeries": {"type": "string", "description": "Filter template(s) based on device series"},
            "productType": {"type": "string", "description": "Filter template(s) based on device type"},
            "filterConflictingTemplates": {"type": "boolean", "description": "Filter template(s) based on confliting templates"},
            "tags": {"type": "array", "description": "Filter template(s) based on tags"},
            "projectNames": {"type": "array", "description": "Filter template(s) based on project names"},
            "unCommitted": {"type": "boolean", "description": "Filter template(s) based on template commited or not"},
            "sortOrder": {"type": "string", "description": "Sort Order Ascending (asc) or Descending (des)"},
        },
        "required": []
    }
}

getSyslogSubscriptionDetails_function = {
    "name": "getSyslogSubscriptionDetails",
    "description": "Gets the list of subscription details for specified connectorType",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Name of the specific configuration"},
            "instanceId": {"type": "string", "description": "Instance Id of the specific configuration"},
            "offset": {"type": "number", "description": "The number of Syslog Subscription detail's to offset in the resultset whose default value 0"},
            "limit": {"type": "number", "description": "The number of Syslog Subscription detail's to limit in the resultset whose default value 10"},
            "sortBy": {"type": "string", "description": "SortBy field name"},
            "order": {"type": "string", "description": "order(asc/desc)"},
        },
        "required": []
    }
}

getListOfScheduledReports_function = {
    "name": "getListOfScheduledReports",
    "description": "Get list of scheduled report configurations.",
    "parameters": {
        "type": "object",
        "properties": {
            "viewGroupId": {"type": "string", "description": "viewGroupId of viewgroup for report"},
            "viewId": {"type": "string", "description": "viewId of view for report"},
        },
        "required": []
    }
}

getClientDetail_function = {
    "name": "getClientDetail",
    "description": "Returns detailed Client information retrieved by Mac Address for any given point of time.",
    "parameters": {
        "type": "object",
        "properties": {
            "macAddress": {"type": "string", "description": "MAC Address of the client"},
            "timestamp": {"type": "number", "description": "Epoch time(in milliseconds) when the Client health data is required"},
        },
        "required": ["macAddress"]
    }
}

countTheNumberOfEvents_function = {
    "name": "countTheNumberOfEvents",
    "description": "API to fetch the count of assurance events that match the filter criteria. Please refer to the 'API Support Documentation' section to understand which fields are supported. For detailed information about the usage of the API, please refer to the Open API specification document - https://github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceEvents-1.0.0-resolved.yaml",
    "parameters": {
        "type": "object",
        "properties": {
            "X-CALLER-ID": {"type": "string", "description": "Caller ID is used to trace the origin of API calls and their associated queries executed on the database. It's an optional header parameter that can be added to an API request."},
            "deviceFamily": {"type": "string", "description": "Device family. Please note that multiple families across network device type and client type is not allowed. For example, choosing `Routers` along with `Wireless Client` or `Unified AP` is not supported. Examples:  `deviceFamily=Switches and Hubs` (single deviceFamily requested)  `deviceFamily=Switches and Hubs&deviceFamily=Routers` (multiple deviceFamily requested)"},
            "startTime": {"type": "string", "description": "Start time from which API queries the data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive.  If `startTime` is not provided, API will default to current time minus 24 hours."},
            "endTime": {"type": "string", "description": "End time to which API queries the data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive.  If `endTime` is not provided, API will default to current time."},
            "messageType": {"type": "string", "description": "Message type for the event.  Examples:  `messageType=Syslog` (single messageType requested)  `messageType=Trap&messageType=Syslog` (multiple messageType requested)"},
            "severity": {"type": "string", "description": "Severity of the event between 0 and 6. This is applicable only for events related to network devices (other than AP) and `Wired Client` events.  | Value | Severity    | | ----- | ----------- | | 0     | Emergency   | | 1     | Alert       | | 2     | Critical    | | 3     | Error       | | 4     | Warning     | | 5     | Notice      | | 6     | Info        |  Examples:  `severity=0` (single severity requested)  `severity=0&severity=1` (multiple severity requested)"},
            "siteId": {"type": "string", "description": "The UUID of the site. (Ex. `flooruuid`)  Examples:  `?siteId=id1` (single siteId requested)  `?siteId=id1&siteId=id2&siteId=id3` (multiple siteId requested)"},
            "siteHierarchyId": {"type": "string", "description": "The full hierarchy breakdown of the site tree in id form starting from Global site UUID and ending with the specific site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`)  This field supports wildcard asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*`  Examples:  `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId requested)  `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyId requested)"},
            "networkDeviceName": {"type": "string", "description": "Network device name. This parameter is applicable for network device related families. This field supports wildcard (`*`) character-based search. Ex: `*Branch*` or `Branch*` or `*Branch` Examples:  `networkDeviceName=Branch-3-Gateway` (single networkDeviceName requested)  `networkDeviceName=Branch-3-Gateway&networkDeviceName=Branch-3-Switch` (multiple networkDeviceName requested)"},
            "networkDeviceId": {"type": "string", "description": "The list of Network Device Uuids. (Ex. `6bef213c-19ca-4170-8375-b694e251101c`)  Examples:  `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId requested)  `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple networkDeviceId requested)"},
            "apMac": {"type": "string", "description": "MAC address of the access point. This parameter is applicable for `Unified AP` and `Wireless Client` events.  This field supports wildcard (`*`) character-based search. Ex: `*50:0F*` or `50:0F*` or `*50:0F`  Examples:  `apMac=50:0F:80:0F:F7:E0` (single apMac requested)  `apMac=50:0F:80:0F:F7:E0&apMac=18:80:90:AB:7E:A0` (multiple apMac requested)"},
            "clientMac": {"type": "string", "description": "MAC address of the client. This parameter is applicable for `Wired Client` and `Wireless Client` events.  This field supports wildcard (`*`) character-based search. Ex: `*66:2B*` or `66:2B*` or `*66:2B`  Examples:  `clientMac=66:2B:B8:D2:01:56` (single clientMac requested)  `clientMac=66:2B:B8:D2:01:56&clientMac=DC:A6:32:F5:5A:89` (multiple clientMac requested)"},
        },
        "required": ["deviceFamily"]
    }
}

getTagMemberCount_function = {
    "name": "getTagMemberCount",
    "description": "Returns the number of members in a given tag",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Tag ID"},
            "memberType": {"type": "string", "description": "memberType"},
            "memberAssociationType": {"type": "string", "description": "memberAssociationType"},
        },
        "required": ["id", "memberType"]
    }
}

getDeviceInterfacesBySpecifiedRange_function = {
    "name": "getDeviceInterfacesBySpecifiedRange",
    "description": "Returns the list of interfaces for the device for the specified range",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "Device ID"},
            "startIndex": {"type": "integer", "description": "Start index"},
            "recordsToReturn": {"type": "integer", "description": "Number of records to return"},
        },
        "required": ["deviceId", "startIndex", "recordsToReturn"]
    }
}

getPollingIntervalForAllDevices_function = {
    "name": "getPollingIntervalForAllDevices",
    "description": "Returns polling interval of all devices",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getDeviceList_function = {
    "name": "getDeviceList",
    "description": "Returns list of network devices based on filter criteria such as management IP address, mac address, hostname, etc. You can use the .* in any value to conduct a wildcard search. For example, to find all hostnames beginning with myhost in the IP address range 192.25.18.n, issue the following request: GET /dna/intent/api/v1/network-device?hostname=myhost.*&managementIpAddress=192.25.18..*  If id parameter is provided with comma separated ids, it will return the list of network-devices for the given ids and ignores the other request parameters. You can also specify offset & limit to get the required list.",
    "parameters": {
        "type": "object",
        "properties": {
            "hostname": {"type": "array", "description": "hostname"},
            "managementIpAddress": {"type": "array", "description": "managementIpAddress"},
            "macAddress": {"type": "array", "description": "macAddress"},
            "locationName": {"type": "array", "description": "locationName"},
            "serialNumber": {"type": "array", "description": "serialNumber"},
            "location": {"type": "array", "description": "location"},
            "family": {"type": "array", "description": "family"},
            "type": {"type": "array", "description": "type"},
            "series": {"type": "array", "description": "series"},
            "collectionStatus": {"type": "array", "description": "collectionStatus"},
            "collectionInterval": {"type": "array", "description": "collectionInterval"},
            "notSyncedForMinutes": {"type": "array", "description": "notSyncedForMinutes"},
            "errorCode": {"type": "array", "description": "errorCode"},
            "errorDescription": {"type": "array", "description": "errorDescription"},
            "softwareVersion": {"type": "array", "description": "softwareVersion"},
            "softwareType": {"type": "array", "description": "softwareType"},
            "platformId": {"type": "array", "description": "platformId"},
            "role": {"type": "array", "description": "role"},
            "reachabilityStatus": {"type": "array", "description": "reachabilityStatus"},
            "upTime": {"type": "array", "description": "upTime"},
            "associatedWlcIp": {"type": "array", "description": "associatedWlcIp"},
            "license.name": {"type": "array", "description": "licenseName"},
            "license.type": {"type": "array", "description": "licenseType"},
            "license.status": {"type": "array", "description": "licenseStatus"},
            "module+name": {"type": "array", "description": "moduleName"},
            "module+equpimenttype": {"type": "array", "description": "moduleEqupimentType"},
            "module+servicestate": {"type": "array", "description": "moduleServiceState"},
            "module+vendorequipmenttype": {"type": "array", "description": "moduleVendorEquipmentType"},
            "module+partnumber": {"type": "array", "description": "modulePartNumber"},
            "module+operationstatecode": {"type": "array", "description": "moduleOperationStateCode"},
            "id": {"type": "string", "description": "Accepts comma separated ids and return list of network-devices for the given ids. If invalid or not-found ids are provided, null entry will be returned in the list."},
            "deviceSupportLevel": {"type": "string", "description": "deviceSupportLevel"},
            "offset": {"type": "integer", "description": "offset >= 1 [X gives results from Xth device onwards]"},
            "limit": {"type": "integer", "description": "1 <= limit <= 500 [max. no. of devices to be returned in the result]"},
        },
        "required": []
    }
}

getQosDeviceInterfaceInfo_function = {
    "name": "getQosDeviceInterfaceInfo",
    "description": "Get all or by network device id, existing qos device interface infos",
    "parameters": {
        "type": "object",
        "properties": {
            "networkDeviceId": {"type": "string", "description": "network device id"},
        },
        "required": []
    }
}

getDeviceFamilyIdentifiers_function = {
    "name": "getDeviceFamilyIdentifiers",
    "description": "API to get Device Family Identifiers for all Device Families that can be used for tagging an image golden.",
    "parameters": {
        "type": "object",
        "properties": {
            "Accept": {"type": "string", "description": "MIME type / MIME subtype"},
        },
        "required": []
    }
}

getTaskCount_function = {
    "name": "getTaskCount",
    "description": "Returns Task count",
    "parameters": {
        "type": "object",
        "properties": {
            "startTime": {"type": "string", "description": "This is the epoch start time from which tasks need to be fetched"},
            "endTime": {"type": "string", "description": "This is the epoch end time upto which audit records need to be fetched"},
            "data": {"type": "string", "description": "Fetch tasks that contains this data"},
            "errorCode": {"type": "string", "description": "Fetch tasks that have this error code"},
            "serviceType": {"type": "string", "description": "Fetch tasks with this service type"},
            "username": {"type": "string", "description": "Fetch tasks with this username"},
            "progress": {"type": "string", "description": "Fetch tasks that contains this progress"},
            "isError": {"type": "string", "description": "Fetch tasks ended as success or failure. Valid values: true, false"},
            "failureReason": {"type": "string", "description": "Fetch tasks that contains this failure reason"},
            "parentId": {"type": "string", "description": "Fetch tasks that have this parent Id"},
        },
        "required": []
    }
}

retrievesValidationDetailsForAValidationSet_function = {
    "name": "retrievesValidationDetailsForAValidationSet",
    "description": "Retrieves validation details for the given validation set id",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Validation set id"},
        },
        "required": ["id"]
    }
}

getSmartAccountList_function = {
    "name": "getSmartAccountList",
    "description": "Returns the list of Smart Account domains",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getLayer3VirtualNetworks_function = {
    "name": "getLayer3VirtualNetworks",
    "description": "Returns a list of layer 3 virtual networks that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "virtualNetworkName": {"type": "string", "description": "Name of the layer 3 virtual network."},
            "fabricId": {"type": "string", "description": "ID of the fabric the layer 3 virtual network is assigned to."},
            "anchoredSiteId": {"type": "string", "description": "Fabric ID of the fabric site the layer 3 virtual network is anchored at."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getListOfAvailableNamespaces_function = {
    "name": "getListOfAvailableNamespaces",
    "description": "Returns list of available namespaces",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

retrieveNetworkDeviceProductName_function = {
    "name": "retrieveNetworkDeviceProductName",
    "description": "Get the network device product name, its ordinal, and supported PIDs.",
    "parameters": {
        "type": "object",
        "properties": {
            "productNameOrdinal": {"type": "number", "description": "Product name ordinal is unique value for each network device product."},
        },
        "required": ["productNameOrdinal"]
    }
}

getExecutionIdByReportId_function = {
    "name": "getExecutionIdByReportId",
    "description": "Get Execution Id by Report Id",
    "parameters": {
        "type": "object",
        "properties": {
            "Content-Type": {"type": "string", "description": "Request body content type"},
            "reportId": {"type": "string", "description": "Id of the report"},
        },
        "required": ["Content-Type", "reportId"]
    }
}

getMobilityGroupsCount_function = {
    "name": "getMobilityGroupsCount",
    "description": "Retrieves count of mobility groups configured",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getAdvisoriesList_function = {
    "name": "getAdvisoriesList",
    "description": "Retrieves list of advisories on the network",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getListOfFiles_function = {
    "name": "getListOfFiles",
    "description": "Returns list of files under a specific namespace",
    "parameters": {
        "type": "object",
        "properties": {
            "nameSpace": {"type": "string", "description": "A listing of fileId's"},
        },
        "required": ["nameSpace"]
    }
}

retrieveSpecificImageDistributionServer_function = {
    "name": "retrieveSpecificImageDistributionServer",
    "description": "Retrieve image distribution server for the given server identifier",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Server identifier"},
        },
        "required": ["id"]
    }
}

getApplicationPolicy_function = {
    "name": "getApplicationPolicy",
    "description": "Get all existing application policies",
    "parameters": {
        "type": "object",
        "properties": {
            "policyScope": {"type": "string", "description": "policy scope name"},
        },
        "required": []
    }
}

getWorkflowById_function = {
    "name": "getWorkflowById",
    "description": "Returns a workflow specified by id",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "id"},
        },
        "required": ["id"]
    }
}

getAdvisoriesSummary_function = {
    "name": "getAdvisoriesSummary",
    "description": "Retrieves summary of advisories on the network.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getTagResourceTypes_function = {
    "name": "getTagResourceTypes",
    "description": "Returns list of supported resource types",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getPortAssignmentCount_function = {
    "name": "getPortAssignmentCount",
    "description": "Returns the count of port assignments that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric the device is assigned to."},
            "networkDeviceId": {"type": "string", "description": "Network device ID of the port assignment."},
            "interfaceName": {"type": "string", "description": "Interface name of the port assignment."},
            "dataVlanName": {"type": "string", "description": "Data VLAN name of the port assignment."},
            "voiceVlanName": {"type": "string", "description": "Voice VLAN name of the port assignment."},
        },
        "required": []
    }
}

getDiscoveriesByRange_function = {
    "name": "getDiscoveriesByRange",
    "description": "Returns the discoveries by specified range",
    "parameters": {
        "type": "object",
        "properties": {
            "startIndex": {"type": "integer", "description": "Starting index for the records"},
            "recordsToReturn": {"type": "integer", "description": "Number of records to fetch from the starting index"},
        },
        "required": ["startIndex", "recordsToReturn"]
    }
}

getsAnArea_function = {
    "name": "getsAnArea",
    "description": "Gets an area in the network hierarchy.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Area Id"},
        },
        "required": ["id"]
    }
}

getExtranetPolicyCount_function = {
    "name": "getExtranetPolicyCount",
    "description": "Returns the count of extranet policies that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getResyncIntervalForTheNetworkDevice_function = {
    "name": "getResyncIntervalForTheNetworkDevice",
    "description": "Fetch the reysnc interval for the given network device id.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "The id of the network device."},
        },
        "required": ["id"]
    }
}

getInterfaces_function = {
    "name": "getInterfaces",
    "description": "This API allows the user to get all Interfaces",
    "parameters": {
        "type": "object",
        "properties": {
            "limit": {"type": "number", "description": "Limit"},
            "offset": {"type": "number", "description": "Offset"},
        },
        "required": []
    }
}

getAllViewGroups_function = {
    "name": "getAllViewGroups",
    "description": "Gives a list of summary of all view groups.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getEvents_function = {
    "name": "getEvents",
    "description": "Gets the list of registered Events with provided eventIds or tags as mandatory",
    "parameters": {
        "type": "object",
        "properties": {
            "eventId": {"type": "string", "description": "The registered EventId should be provided"},
            "tags": {"type": "string", "description": "The registered Tags should be provided"},
            "offset": {"type": "number", "description": "The number of Registries to offset in the resultset whose default value 0"},
            "limit": {"type": "number", "description": "The number of Registries to limit in the resultset whose default value 10"},
            "sortBy": {"type": "string", "description": "SortBy field name"},
            "order": {"type": "string", "description": "order(asc/desc)"},
        },
        "required": ["tags"]
    }
}

getEmailEventSubscriptions_function = {
    "name": "getEmailEventSubscriptions",
    "description": "Gets the list of email Subscriptions's based on provided query params",
    "parameters": {
        "type": "object",
        "properties": {
            "eventIds": {"type": "string", "description": "List of email subscriptions related to the respective eventIds (Comma separated event ids)"},
            "offset": {"type": "number", "description": "The number of Subscriptions's to offset in the resultset whose default value 0"},
            "limit": {"type": "number", "description": "The number of Subscriptions's to limit in the resultset whose default value 10"},
            "sortBy": {"type": "string", "description": "SortBy field name"},
            "order": {"type": "string", "description": "order(asc/desc)"},
            "domain": {"type": "string", "description": "List of email subscriptions related to the respective domain"},
            "subDomain": {"type": "string", "description": "List of email subscriptions related to the respective sub-domain"},
            "category": {"type": "string", "description": "List of email subscriptions related to the respective category"},
            "type": {"type": "string", "description": "List of email subscriptions related to the respective type"},
            "name": {"type": "string", "description": "List of email subscriptions related to the respective name"},
        },
        "required": []
    }
}

getEmailSubscriptionDetails_function = {
    "name": "getEmailSubscriptionDetails",
    "description": "Gets the list of subscription details for specified connectorType",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Name of the specific configuration"},
            "instanceId": {"type": "string", "description": "Instance Id of the specific configuration"},
            "offset": {"type": "number", "description": "The number of Email Subscription detail's to offset in the resultset whose default value 0"},
            "limit": {"type": "number", "description": "The number of Email Subscription detail's to limit in the resultset whose default value 10"},
            "sortBy": {"type": "string", "description": "SortBy field name"},
            "order": {"type": "string", "description": "order(asc/desc)"},
        },
        "required": []
    }
}

getAllGlobalCredentialsV2_function = {
    "name": "getAllGlobalCredentialsV2",
    "description": "API to get device credentials' details. It fetches all global credentials of all types at once, without the need to pass any input parameters.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getNetworkDevicesFromDiscovery_function = {
    "name": "getNetworkDevicesFromDiscovery",
    "description": "Returns the devices discovered in the given discovery based on given filters. Discovery ID can be obtained using the \"Get Discoveries by range\" API.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Discovery ID"},
            "taskId": {"type": "string", "description": "taskId"},
            "sortBy": {"type": "string", "description": "Sort by field. Available values are pingStatus, cliStatus,snmpStatus, httpStatus and netconfStatus"},
            "sortOrder": {"type": "string", "description": "Order of sorting based on sortBy. Available values are 'asc' and 'des'"},
            "ipAddress": {"type": "array", "description": "IP Address of the device"},
            "pingStatus": {"type": "array", "description": "Ping status for the IP during the job run. Available values are 'SUCCESS', 'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED'"},
            "snmpStatus": {"type": "array", "description": "SNMP status for the IP during the job run. Available values are 'SUCCESS', 'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED'"},
            "cliStatus": {"type": "array", "description": "CLI status for the IP during the job run. Available values are 'SUCCESS', 'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED'"},
            "netconfStatus": {"type": "array", "description": "NETCONF status for the IP during the job run. Available values are 'SUCCESS', 'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED'"},
            "httpStatus": {"type": "array", "description": "HTTP staus for the IP during the job run. Available values are 'SUCCESS', 'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED'"},
        },
        "required": ["id"]
    }
}

getSites_function = {
    "name": "getSites",
    "description": "Get sites.",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Site name."},
            "nameHierarchy": {"type": "string", "description": "Site name hierarchy."},
            "type": {"type": "string", "description": "Site type."},
            "_unitsOfMeasure": {"type": "string", "description": "Floor units of measure"},
            "offset": {"type": "integer", "description": "The first record to show for this page; the first record is numbered 1."},
            "limit": {"type": "integer", "description": "The number of records to show for this page."},
        },
        "required": []
    }
}

getEventSubscriptions_function = {
    "name": "getEventSubscriptions",
    "description": "Gets the list of Subscriptions's based on provided offset and limit (Deprecated)",
    "parameters": {
        "type": "object",
        "properties": {
            "eventIds": {"type": "string", "description": "List of subscriptions related to the respective eventIds"},
            "offset": {"type": "number", "description": "The number of Subscriptions's to offset in the resultset whose default value 0"},
            "limit": {"type": "number", "description": "The number of Subscriptions's to limit in the resultset whose default value 10"},
            "sortBy": {"type": "string", "description": "SortBy field name"},
            "order": {"type": "string", "description": "order(asc/desc)"},
        },
        "required": []
    }
}

getPlannedAccessPointsForFloor_function = {
    "name": "getPlannedAccessPointsForFloor",
    "description": "Provides a list of Planned Access Points for the Floor it is requested for",
    "parameters": {
        "type": "object",
        "properties": {
            "floorId": {"type": "string", "description": "The instance UUID of the floor hierarchy element"},
            "limit": {"type": "number", "description": "The page size limit for the response, e.g. limit=100 will return a maximum of 100 records"},
            "offset": {"type": "number", "description": "The page offset for the response. E.g. if limit=100, offset=0 will return first 100 records, offset=1 will return next 100 records, etc."},
            "radios": {"type": "boolean", "description": "Whether to include the planned radio details of the planned access points"},
        },
        "required": ["floorId"]
    }
}

getDiscoveryById_function = {
    "name": "getDiscoveryById",
    "description": "Returns discovery by Discovery ID. Discovery ID can be obtained using the \"Get Discoveries by range\" API.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Discovery ID"},
        },
        "required": ["id"]
    }
}

getConfigurationArchiveDetails_function = {
    "name": "getConfigurationArchiveDetails",
    "description": "Returns the historical device configurations (running configuration , startup configuration , vlan if applicable) by specified criteria",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "comma separated device id for example cf35b0a1-407f-412f-b2f4-f0c3156695f9,aaa38191-0c22-4158-befd-779a09d7cec1 . if device id is not provided it will fetch for all devices"},
            "fileType": {"type": "string", "description": "Config File Type can be RUNNINGCONFIG or STARTUPCONFIG"},
            "createdTime": {"type": "string", "description": "Supported with logical filters GT,GTE,LT,LTE & BT : time in milliseconds (epoc format)"},
            "createdBy": {"type": "string", "description": "Comma separated values for createdBy - SCHEDULED, USER, CONFIG_CHANGE_EVENT, SCHEDULED_FIRST_TIME, DR_CALL_BACK, PRE_DEPLOY"},
            "offset": {"type": "number", "description": "offset"},
            "limit": {"type": "number", "description": "limit"},
        },
        "required": []
    }
}

getAdvisoriesPerDevice_function = {
    "name": "getAdvisoriesPerDevice",
    "description": "Retrieves list of advisories for a device",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "Device instance UUID"},
        },
        "required": ["deviceId"]
    }
}

retrievesTheCountOfValidationWorkflows_function = {
    "name": "retrievesTheCountOfValidationWorkflows",
    "description": "Retrieves the count of workflows that have been successfully submitted and are currently available.",
    "parameters": {
        "type": "object",
        "properties": {
            "startTime": {"type": "number", "description": "Workflows started after the given time (as milliseconds since UNIX epoch)."},
            "endTime": {"type": "number", "description": "Workflows started before the given time (as milliseconds since UNIX epoch)."},
            "runStatus": {"type": "string", "description": "Execution status of the workflow. If the workflow is successfully submitted, runStatus is `PENDING`. If the workflow execution has started, runStatus is `IN_PROGRESS`. If the workflow executed is completed with all validations executed, runStatus is `COMPLETED`. If the workflow execution fails while running validations, runStatus is `FAILED`."},
        },
        "required": []
    }
}

getComplianceDetailCount_function = {
    "name": "getComplianceDetailCount",
    "description": "Return  Compliance Count Detail",
    "parameters": {
        "type": "object",
        "properties": {
            "complianceType": {"type": "string", "description": "Specify \"Compliance type(s)\" separated by commas. The Compliance type can be 'APPLICATION_VISIBILITY', 'EOX', 'FABRIC', 'IMAGE', 'NETWORK_PROFILE', 'NETWORK_SETTINGS', 'PSIRT', 'RUNNING_CONFIG', 'WORKFLOW'."},
            "complianceStatus": {"type": "string", "description": "Specify \"Compliance status(es)\" separated by commas. The Compliance status can be 'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS', 'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'."},
        },
        "required": []
    }
}

getOverallClientHealth_function = {
    "name": "getOverallClientHealth",
    "description": "Returns Overall Client Health information by Client type (Wired and Wireless) for any given point of time",
    "parameters": {
        "type": "object",
        "properties": {
            "timestamp": {"type": "number", "description": "Epoch time(in milliseconds) when the Client health data is required"},
        },
        "required": []
    }
}

getLinecardDetails_function = {
    "name": "getLinecardDetails",
    "description": "Get line card detail for a given deviceuuid.  Response will contain serial no, part no, switch no and slot no.",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceUuid": {"type": "string", "description": "instanceuuid of device"},
        },
        "required": ["deviceUuid"]
    }
}

getWirelessProfilesCount_function = {
    "name": "getWirelessProfilesCount",
    "description": "This API allows the user to get count of all wireless profiles",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getTagById_function = {
    "name": "getTagById",
    "description": "Returns tag specified by Id",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Tag ID"},
        },
        "required": ["id"]
    }
}

getAuditLogSummary_function = {
    "name": "getAuditLogSummary",
    "description": "Get Audit Log Summary from the Event-Hub",
    "parameters": {
        "type": "object",
        "properties": {
            "parentInstanceId": {"type": "string", "description": "Parent Audit Log record's instanceID."},
            "isParentOnly": {"type": "boolean", "description": "Parameter to filter parent only audit-logs."},
            "instanceId": {"type": "string", "description": "InstanceID of the Audit Log."},
            "name": {"type": "string", "description": "Audit Log notification event name."},
            "eventId": {"type": "string", "description": "Audit Log notification's event ID."},
            "category": {"type": "string", "description": "Audit Log notification's event category. Supported values: INFO, WARN, ERROR, ALERT, TASK_PROGRESS, TASK_FAILURE, TASK_COMPLETE, COMMAND, QUERY, CONVERSATION"},
            "severity": {"type": "string", "description": "Audit Log notification's event severity. Supported values: 1, 2, 3, 4, 5."},
            "domain": {"type": "string", "description": "Audit Log notification's event domain."},
            "subDomain": {"type": "string", "description": "Audit Log notification's event sub-domain."},
            "source": {"type": "string", "description": "Audit Log notification's event source."},
            "userId": {"type": "string", "description": "Audit Log notification's event userId."},
            "context": {"type": "string", "description": "Audit Log notification's event correlationId."},
            "eventHierarchy": {"type": "string", "description": "Audit Log notification's event eventHierarchy. Example: \"US.CA.San Jose\" OR \"US.CA\" OR \"CA.San Jose\" - Delimiter for hierarchy separation is \".\"."},
            "siteId": {"type": "string", "description": "Audit Log notification's siteId."},
            "deviceId": {"type": "string", "description": "Audit Log notification's deviceId."},
            "isSystemEvents": {"type": "boolean", "description": "Parameter to filter system generated audit-logs."},
            "description": {"type": "string", "description": "String full/partial search - (Provided input string is case insensitively matched for records)."},
            "startTime": {"type": "number", "description": "Start Time in milliseconds since Epoch Eg. 1597950637211 (when provided endTime is mandatory)"},
            "endTime": {"type": "number", "description": "End Time in milliseconds since Epoch Eg. 1597961437211 (when provided startTime is mandatory)"},
        },
        "required": []
    }
}

getsAListOfProjects_function = {
    "name": "getsAListOfProjects",
    "description": "List the projects",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Name of project to be searched"},
            "sortOrder": {"type": "string", "description": "Sort Order Ascending (asc) or Descending (des)"},
        },
        "required": []
    }
}

getAuthenticationAndPolicyServers_function = {
    "name": "getAuthenticationAndPolicyServers",
    "description": "API to get Authentication and Policy Servers",
    "parameters": {
        "type": "object",
        "properties": {
            "isIseEnabled": {"type": "boolean", "description": "Valid values are : true, false"},
            "state": {"type": "string", "description": "Valid values are: ACTIVE, INACTIVE, RBAC_SUCCESS, RBAC_FAILURE, DELETED, FAILED, INPROGRESS"},
            "role": {"type": "string", "description": "Authentication and Policy Server Role (Example: primary, secondary)"},
        },
        "required": []
    }
}

retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo_function = {
    "name": "retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo",
    "description": "Retrieves the count of sites that the given network profile for sites is assigned to.",
    "parameters": {
        "type": "object",
        "properties": {
            "profileId": {"type": "string", "description": "The `id` of the network profile, retrievable from `GET /intent/api/v1/networkProfilesForSites`"},
        },
        "required": ["profileId"]
    }
}

getProvisionedDevices_function = {
    "name": "getProvisionedDevices",
    "description": "Returns the list of provisioned devices based on query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "ID of the provisioned device."},
            "networkDeviceId": {"type": "string", "description": "ID of the network device."},
            "siteId": {"type": "string", "description": "ID of the site hierarchy."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of devices to return."},
        },
        "required": []
    }
}

retrievesAllPreviousPathtracesSummary_function = {
    "name": "retrievesAllPreviousPathtracesSummary",
    "description": "Returns a summary of all flow analyses stored. Results can be filtered by specified parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "periodicRefresh": {"type": "boolean", "description": "Is analysis periodically refreshed?"},
            "sourceIP": {"type": "string", "description": "Source IP address"},
            "destIP": {"type": "string", "description": "Destination IP address"},
            "sourcePort": {"type": "number", "description": "Source port"},
            "destPort": {"type": "number", "description": "Destination port"},
            "gtCreateTime": {"type": "number", "description": "Analyses requested after this time"},
            "ltCreateTime": {"type": "number", "description": "Analyses requested before this time"},
            "protocol": {"type": "string", "description": "Protocol"},
            "status": {"type": "string", "description": "Status"},
            "taskId": {"type": "string", "description": "Task ID"},
            "lastUpdateTime": {"type": "number", "description": "Last update time"},
            "limit": {"type": "number", "description": "Number of resources returned"},
            "offset": {"type": "number", "description": "Start index of resources returned (1-based)"},
            "order": {"type": "string", "description": "Order by this field"},
            "sortBy": {"type": "string", "description": "Sort by this field"},
        },
        "required": []
    }
}

getDeviceCredentialSettingsForASite_function = {
    "name": "getDeviceCredentialSettingsForASite",
    "description": "Gets device credential settings for a site; `null` values indicate that the setting will be inherited from the parent site; empty objects (`{}`) indicate that the credential is unset, and that no credential of that type will be used for the site.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Site Id, retrievable from the `id` attribute in `/dna/intent/api/v1/sites`"},
            "_inherited": {"type": "boolean", "description": "Include settings explicitly set for this site and settings inherited from sites higher in the site hierarchy; when `false`, `null` values indicate that the site inherits that setting from the parent site or a site higher in the site hierarchy."},
        },
        "required": ["id"]
    }
}

getDeviceInterfaceCount_function = {
    "name": "getDeviceInterfaceCount",
    "description": "Returns the interface count for the given device",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["deviceId"]
    }
}

getLayer2VirtualNetworkCount_function = {
    "name": "getLayer2VirtualNetworkCount",
    "description": "Returns the count of layer 2 virtual networks that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric the layer 2 virtual network is assigned to."},
            "vlanName": {"type": "string", "description": "The vlan name of the layer 2 virtual network."},
            "vlanId": {"type": "number", "description": "The vlan ID of the layer 2 virtual network."},
            "trafficType": {"type": "string", "description": "The traffic type of the layer 2 virtual network."},
            "associatedLayer3VirtualNetworkName": {"type": "string", "description": "Name of the associated layer 3 virtual network."},
        },
        "required": []
    }
}

retrievesTheCountOfNetworkProfilesForSites_function = {
    "name": "retrievesTheCountOfNetworkProfilesForSites",
    "description": "Retrieves the count of network profiles for sites",
    "parameters": {
        "type": "object",
        "properties": {
            "type": {"type": "string", "description": "Filter the response to only count profiles of a given type"},
        },
        "required": []
    }
}

getDeviceCount_function = {
    "name": "getDeviceCount",
    "description": "Returns the count of network devices based on the filter criteria by management IP address, mac address, hostname and location name",
    "parameters": {
        "type": "object",
        "properties": {
            "hostname": {"type": "array", "description": "hostname"},
            "managementIpAddress": {"type": "array", "description": "managementIpAddress"},
            "macAddress": {"type": "array", "description": "macAddress"},
            "locationName": {"type": "array", "description": "locationName"},
        },
        "required": []
    }
}

getFabricDevicesLayer2Handoffs_function = {
    "name": "getFabricDevicesLayer2Handoffs",
    "description": "Returns a list of layer 2 handoffs of fabric devices that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric this device belongs to."},
            "networkDeviceId": {"type": "string", "description": "Network device ID of the fabric device."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": ["fabricId"]
    }
}

getSyslogEventSubscriptions_function = {
    "name": "getSyslogEventSubscriptions",
    "description": "Gets the list of Syslog Subscriptions's based on provided offset and limit",
    "parameters": {
        "type": "object",
        "properties": {
            "eventIds": {"type": "string", "description": "List of subscriptions related to the respective eventIds (Comma separated event ids)"},
            "offset": {"type": "number", "description": "The number of Subscriptions's to offset in the resultset whose default value 0"},
            "limit": {"type": "number", "description": "The number of Subscriptions's to limit in the resultset whose default value 10"},
            "sortBy": {"type": "string", "description": "SortBy field name"},
            "order": {"type": "string", "description": "order(asc/desc)"},
            "domain": {"type": "string", "description": "List of subscriptions related to the respective domain"},
            "subDomain": {"type": "string", "description": "List of subscriptions related to the respective sub-domain"},
            "category": {"type": "string", "description": "List of subscriptions related to the respective category"},
            "type": {"type": "string", "description": "List of subscriptions related to the respective type"},
            "name": {"type": "string", "description": "List of subscriptions related to the respective name"},
        },
        "required": []
    }
}

getSiteV2_function = {
    "name": "getSiteV2",
    "description": "API to get site(s) by site-name-hierarchy or siteId or type. List all sites if these parameters  are not given as an input.",
    "parameters": {
        "type": "object",
        "properties": {
            "groupNameHierarchy": {"type": "string", "description": "Site name hierarchy (E.g. Global/USA/CA)"},
            "id": {"type": "string", "description": "Site Id"},
            "type": {"type": "string", "description": "Site type (Acceptable values: area, building, floor)"},
            "offset": {"type": "string", "description": "Offset/starting index for pagination"},
            "limit": {"type": "string", "description": "Number of sites to be listed. Default and max supported value is 500"},
        },
        "required": []
    }
}

getFabricDevices_function = {
    "name": "getFabricDevices",
    "description": "Returns a list of fabric devices that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric this device belongs to."},
            "networkDeviceId": {"type": "string", "description": "Network device ID of the fabric device."},
            "deviceRoles": {"type": "string", "description": "Device roles of the fabric device. Allowed values are [CONTROL_PLANE_NODE, EDGE_NODE, BORDER_NODE, WIRELESS_CONTROLLER_NODE, EXTENDED_NODE]."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": ["fabricId"]
    }
}

getTasksCount_function = {
    "name": "getTasksCount",
    "description": "Returns the number of tasks that meet the filter criteria",
    "parameters": {
        "type": "object",
        "properties": {
            "startTime": {"type": "integer", "description": "This is the epoch millisecond start time from which tasks need to be fetched"},
            "endTime": {"type": "integer", "description": "This is the epoch millisecond end time upto which task records need to be fetched"},
            "parentId": {"type": "string", "description": "Fetch tasks that have this parent Id"},
            "rootId": {"type": "string", "description": "Fetch tasks that have this root Id"},
            "status": {"type": "string", "description": "Fetch tasks that have this status. Available values : PENDING, FAILURE, SUCCESS"},
        },
        "required": []
    }
}

getsAFloor_function = {
    "name": "getsAFloor",
    "description": "Gets a floor in the network hierarchy.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Floor Id"},
            "_unitsOfMeasure": {"type": "string", "description": "Floor units of measure"},
        },
        "required": ["id"]
    }
}

getFabricZones_function = {
    "name": "getFabricZones",
    "description": "Returns a list of fabric zones that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "ID of the fabric zone."},
            "siteId": {"type": "string", "description": "ID of the network hierarchy associated with the fabric zone."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getVirtualAccountList_function = {
    "name": "getVirtualAccountList",
    "description": "Returns list of virtual accounts associated with the specified smart account",
    "parameters": {
        "type": "object",
        "properties": {
            "domain": {"type": "string", "description": "Smart Account Domain"},
        },
        "required": ["domain"]
    }
}

getQosDeviceInterfaceInfoCount_function = {
    "name": "getQosDeviceInterfaceInfoCount",
    "description": "Get the number of all existing qos device interface infos group by network device id",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

countOfEvents_function = {
    "name": "countOfEvents",
    "description": "Get the count of registered events with provided eventIds or tags as mandatory",
    "parameters": {
        "type": "object",
        "properties": {
            "eventId": {"type": "string", "description": "The registered EventId should be provided"},
            "tags": {"type": "string", "description": "The registered Tags should be provided"},
        },
        "required": ["tags"]
    }
}

getNetworkDeviceImageUpdates_function = {
    "name": "getNetworkDeviceImageUpdates",
    "description": "Returns the list of network device image updates based on the given filter criteria",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Update id which is unique for each network device under the parentId"},
            "parentId": {"type": "string", "description": "Updates that have this parent id"},
            "networkDeviceId": {"type": "string", "description": "Network device id"},
            "status": {"type": "string", "description": "Status of the image update. Available values : FAILURE, SUCCESS, IN_PROGRESS, PENDING"},
            "imageName": {"type": "string", "description": "Software image name for the update"},
            "hostName": {"type": "string", "description": "Host name of the network device for the image update. Supports case-insensitive partial search"},
            "managementAddress": {"type": "string", "description": "Management address of the network device"},
            "startTime": {"type": "number", "description": "Image update started after the given time (as milliseconds since UNIX epoch)"},
            "endTime": {"type": "number", "description": "Image update started before the given time (as milliseconds since UNIX epoch)"},
            "sortBy": {"type": "string", "description": "A property within the response to sort by."},
            "order": {"type": "string", "description": "Whether ascending or descending order should be used to sort the response."},
            "offset": {"type": "number", "description": "The first record to show for this page; the first record is numbered 1."},
            "limit": {"type": "number", "description": "The number of records to show for this page."},
        },
        "required": []
    }
}

getTransitNetworks_function = {
    "name": "getTransitNetworks",
    "description": "Returns a list of transit networks that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "ID of the transit network."},
            "name": {"type": "string", "description": "Name of the transit network."},
            "type": {"type": "string", "description": "Type of the transit network. Allowed values are [IP_BASED_TRANSIT, SDA_LISP_PUB_SUB_TRANSIT, SDA_LISP_BGP_TRANSIT]."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getStackDetailsForDevice_function = {
    "name": "getStackDetailsForDevice",
    "description": "Retrieves complete stack details for given device ID",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["deviceId"]
    }
}

getApplicationSetCount_function = {
    "name": "getApplicationSetCount",
    "description": "Get the number of all existing application sets",
    "parameters": {
        "type": "object",
        "properties": {
            "scalableGroupType": {"type": "string", "description": "Scalable group type to retrieve, valid value APPLICATION_GROUP"},
        },
        "required": ["scalableGroupType"]
    }
}

getWorkflowCount_function = {
    "name": "getWorkflowCount",
    "description": "Returns the workflow count",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "array", "description": "Workflow Name"},
        },
        "required": []
    }
}

retrievesPreviousPathtrace_function = {
    "name": "retrievesPreviousPathtrace",
    "description": "Returns result of a previously requested flow analysis by its Flow Analysis id",
    "parameters": {
        "type": "object",
        "properties": {
            "flowAnalysisId": {"type": "string", "description": "Flow analysis request id"},
        },
        "required": ["flowAnalysisId"]
    }
}

getOverallNetworkHealth_function = {
    "name": "getOverallNetworkHealth",
    "description": "Returns Overall Network Health information by Device category (Access, Distribution, Core, Router, Wireless) for any given point of time",
    "parameters": {
        "type": "object",
        "properties": {
            "timestamp": {"type": "number", "description": "UTC timestamp of network health data in milliseconds"},
        },
        "required": []
    }
}

getServiceProviderDetailsV2_function = {
    "name": "getServiceProviderDetailsV2",
    "description": "API to get Service Provider details (QoS).",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getWirelessProfiles_function = {
    "name": "getWirelessProfiles",
    "description": "This API allows the user to get all Wireless Network Profiles",
    "parameters": {
        "type": "object",
        "properties": {
            "limit": {"type": "number", "description": "Limit"},
            "offset": {"type": "number", "description": "Offset"},
        },
        "required": []
    }
}

getConfigTaskDetails_function = {
    "name": "getConfigTaskDetails",
    "description": "Returns a config task result details by specified id",
    "parameters": {
        "type": "object",
        "properties": {
            "parentTaskId": {"type": "string", "description": "task Id"},
        },
        "required": ["parentTaskId"]
    }
}

getMulticastVirtualNetworkCount_function = {
    "name": "getMulticastVirtualNetworkCount",
    "description": "Returns the count of multicast configurations associated to virtual networks that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric site the multicast configuration is associated with."},
        },
        "required": []
    }
}

getTagCount_function = {
    "name": "getTagCount",
    "description": "Returns tag count",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "tagName"},
            "nameSpace": {"type": "string", "description": "nameSpace"},
            "attributeName": {"type": "string", "description": "attributeName"},
            "size": {"type": "string", "description": "size in kilobytes(KB)"},
            "systemTag": {"type": "string", "description": "systemTag"},
        },
        "required": []
    }
}

getDeviceSummary_function = {
    "name": "getDeviceSummary",
    "description": "Returns brief summary of device info such as hostname, management IP address for the given device Id",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Device ID"},
        },
        "required": ["id"]
    }
}

getAuthenticationProfiles_function = {
    "name": "getAuthenticationProfiles",
    "description": "Returns a list of authentication profiles that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric the authentication profile is assigned to."},
            "authenticationProfileName": {"type": "string", "description": "Return only the authentication profiles with this specified name. Note that 'No Authentication' is not a valid option for this parameter."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getAllFlexibleReportSchedules_function = {
    "name": "getAllFlexibleReportSchedules",
    "description": "Get all flexible report schedules",
    "parameters": {
        "type": "object",
        "properties": {
            "Content-Type": {"type": "string", "description": "Request body content type"},
        },
        "required": ["Content-Type"]
    }
}

getFunctionalCapabilityById_function = {
    "name": "getFunctionalCapabilityById",
    "description": "Returns functional capability with given Id",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Functional Capability UUID"},
        },
        "required": ["id"]
    }
}

getFabricSites_function = {
    "name": "getFabricSites",
    "description": "Returns a list of fabric sites that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "ID of the fabric site."},
            "siteId": {"type": "string", "description": "ID of the network hierarchy associated with the fabric site."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getWorkflows_function = {
    "name": "getWorkflows",
    "description": "Returns the list of workflows based on filter criteria. If a limit is not specified, it will default to return 50 workflows. Pagination and sorting are also supported by this endpoint",
    "parameters": {
        "type": "object",
        "properties": {
            "limit": {"type": "integer", "description": "Limits number of results"},
            "offset": {"type": "integer", "description": "Index of first result"},
            "sort": {"type": "array", "description": "Comma seperated lost of fields to sort on"},
            "sortOrder": {"type": "string", "description": "Sort Order Ascending (asc) or Descending (des)"},
            "type": {"type": "array", "description": "Workflow Type"},
            "name": {"type": "array", "description": "Workflow Name"},
        },
        "required": []
    }
}

getDeviceConfigById_function = {
    "name": "getDeviceConfigById",
    "description": "Returns the device config by specified device ID",
    "parameters": {
        "type": "object",
        "properties": {
            "networkDeviceId": {"type": "string", "description": "networkDeviceId"},
        },
        "required": ["networkDeviceId"]
    }
}

getOrganizationListForMeraki_function = {
    "name": "getOrganizationListForMeraki",
    "description": "Returns list of organizations for meraki dashboard",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Device Id"},
        },
        "required": ["id"]
    }
}

getPollingIntervalById_function = {
    "name": "getPollingIntervalById",
    "description": "Returns polling interval by device id",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Device ID"},
        },
        "required": ["id"]
    }
}

getNotifications_function = {
    "name": "getNotifications",
    "description": "Get the list of Published Notifications",
    "parameters": {
        "type": "object",
        "properties": {
            "eventIds": {"type": "string", "description": "The registered EventId should be provided"},
            "startTime": {"type": "number", "description": "Start Time in milliseconds"},
            "endTime": {"type": "number", "description": "End Time in milliseconds"},
            "category": {"type": "string", "description": "Category"},
            "type": {"type": "string", "description": "Type"},
            "severity": {"type": "string", "description": "Severity"},
            "domain": {"type": "string", "description": "Domain"},
            "subDomain": {"type": "string", "description": "Sub Domain"},
            "source": {"type": "string", "description": "Source"},
            "offset": {"type": "number", "description": "Start Offset"},
            "limit": {"type": "number", "description": "# of records"},
            "sortBy": {"type": "string", "description": "Sort By column"},
            "order": {"type": "string", "description": "Ascending/Descending order [asc/desc]"},
            "tags": {"type": "string", "description": "Tags"},
            "namespace": {"type": "string", "description": "Namespace"},
            "siteId": {"type": "string", "description": "Site Id"},
        },
        "required": []
    }
}

getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId_function = {
    "name": "getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId",
    "description": "Returns all the details and suggested actions of an issue for the given issue id. https://github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-IssuesList-1.0.0-resolved.yaml",
    "parameters": {
        "type": "object",
        "properties": {
            "Accept-Language": {"type": "string", "description": "This header parameter can be used to specify the language in which issue description and suggested actions need to be returned. Available options are - 'en' (English), 'ja' (Japanese), 'ko' (Korean), 'zh' (Chinese). If this parameter is not present the issue details are returned in English language."},
            "X-CALLER-ID": {"type": "string", "description": "Caller ID can be used to trace the caller for queries executed on database. The caller id is like a optional attribute which can be added to API invocation like ui, python, postman, test-automation etc"},
            "id": {"type": "string", "description": "The issue Uuid"},
            "view": {"type": "string", "description": "The name of the View. Each view represents a specific data set. Please refer to the `IssuesView` Model for supported views. View is predefined set of attributes supported by the API. Only the attributes related to the given view will be part of the API response along with default attributes. If multiple views are provided, then response will contain attributes from all those views. If no views are specified, all attributes will be returned.  | View Name | Included Attributes | | --- | --- | | `update` | updatedTime, updatedBy | | `site` | siteName, siteHierarchy, siteId, siteHierarchyId | Examples: `view=update` (single view requested) `view=update&view=site` (multiple views requested)"},
            "attribute": {"type": "string", "description": "List of attributes related to the issue. If these are provided, then only those attributes will be part of response along with the default attributes. Please refer to the `IssuesResponseAttribute` Model for supported attributes. Examples: `attribute=deviceType` (single attribute requested) `attribute=deviceType&attribute=updatedBy` (multiple attributes requested)"},
        },
        "required": ["id"]
    }
}

getDeviceConfigCount_function = {
    "name": "getDeviceConfigCount",
    "description": "Returns the count of device configs",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

retrieveANetworkProfileForSitesById_function = {
    "name": "retrieveANetworkProfileForSitesById",
    "description": "Retrieves a network profile for sites by id.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "The `id` of the network profile, retrievable from `GET /intent/api/v1/networkProfilesForSites`"},
        },
        "required": ["id"]
    }
}

getAuditLogRecords_function = {
    "name": "getAuditLogRecords",
    "description": "Get Audit Log Event instances from the Event-Hub",
    "parameters": {
        "type": "object",
        "properties": {
            "parentInstanceId": {"type": "string", "description": "Parent Audit Log record's instanceID."},
            "instanceId": {"type": "string", "description": "InstanceID of the Audit Log."},
            "name": {"type": "string", "description": "Audit Log notification event name."},
            "eventId": {"type": "string", "description": "Audit Log notification's event ID."},
            "category": {"type": "string", "description": "Audit Log notification's event category. Supported values: INFO, WARN, ERROR, ALERT, TASK_PROGRESS, TASK_FAILURE, TASK_COMPLETE, COMMAND, QUERY, CONVERSATION"},
            "severity": {"type": "string", "description": "Audit Log notification's event severity. Supported values: 1, 2, 3, 4, 5."},
            "domain": {"type": "string", "description": "Audit Log notification's event domain."},
            "subDomain": {"type": "string", "description": "Audit Log notification's event sub-domain."},
            "source": {"type": "string", "description": "Audit Log notification's event source."},
            "userId": {"type": "string", "description": "Audit Log notification's event userId."},
            "context": {"type": "string", "description": "Audit Log notification's event correlationId."},
            "eventHierarchy": {"type": "string", "description": "Audit Log notification's event eventHierarchy. Example: \"US.CA.San Jose\" OR \"US.CA\" OR \"CA.San Jose\" - Delimiter for hierarchy separation is \".\"."},
            "siteId": {"type": "string", "description": "Audit Log notification's siteId."},
            "deviceId": {"type": "string", "description": "Audit Log notification's deviceId."},
            "isSystemEvents": {"type": "boolean", "description": "Parameter to filter system generated audit-logs."},
            "description": {"type": "string", "description": "String full/partial search - (Provided input string is case insensitively matched for records)."},
            "offset": {"type": "number", "description": "Position of a particular Audit Log record in the data."},
            "limit": {"type": "number", "description": "Number of Audit Log records to be returned per page."},
            "startTime": {"type": "number", "description": "Start Time in milliseconds since Epoch Eg. 1597950637211 (when provided endTime is mandatory)"},
            "endTime": {"type": "number", "description": "End Time in milliseconds since Epoch Eg. 1597961437211 (when provided startTime is mandatory)"},
            "sortBy": {"type": "string", "description": "Sort the Audit Logs by certain fields. Supported values are event notification header attributes."},
            "order": {"type": "string", "description": "Order of the sorted Audit Log records. Default value is desc by timestamp. Supported values: asc, desc."},
        },
        "required": []
    }
}

getSupervisorCardDetail_function = {
    "name": "getSupervisorCardDetail",
    "description": "Get supervisor card detail for a given deviceuuid. Response will contain serial no, part no, switch no and slot no.",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceUuid": {"type": "string", "description": "instanceuuid of device"},
        },
        "required": ["deviceUuid"]
    }
}

retrieveImageDistributionSettingsForASite_function = {
    "name": "retrieveImageDistributionSettingsForASite",
    "description": "Retrieve image distribution settings for a site; `null` values indicate that the setting will be inherited from the parent site; empty objects (`{}`) indicate that the setting is unset at a site.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Site Id"},
            "_inherited": {"type": "boolean", "description": "Include settings explicitly set for this site and settings inherited from sites higher in the site hierarchy; when `false`, `null` values indicate that the site inherits that setting from the parent site or a site higher in the site hierarchy."},
        },
        "required": ["id"]
    }
}

getEventArtifacts_function = {
    "name": "getEventArtifacts",
    "description": "Gets the list of artifacts based on provided offset and limit",
    "parameters": {
        "type": "object",
        "properties": {
            "eventIds": {"type": "string", "description": "List of eventIds"},
            "tags": {"type": "string", "description": "Tags defined"},
            "offset": {"type": "number", "description": "Record start offset"},
            "limit": {"type": "number", "description": "# of records to return in result set"},
            "sortBy": {"type": "string", "description": "Sort by field"},
            "order": {"type": "string", "description": "sorting order (asc/desc)"},
            "search": {"type": "string", "description": "findd matches in name, description, eventId, type, category"},
        },
        "required": []
    }
}

retrievesValidationWorkflowDetails_function = {
    "name": "retrievesValidationWorkflowDetails",
    "description": "Retrieves workflow details for a workflow id",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Workflow id"},
        },
        "required": ["id"]
    }
}

getModuleCount_function = {
    "name": "getModuleCount",
    "description": "Returns Module Count",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "deviceId"},
            "nameList": {"type": "array", "description": "nameList"},
            "vendorEquipmentTypeList": {"type": "array", "description": "vendorEquipmentTypeList"},
            "partNumberList": {"type": "array", "description": "partNumberList"},
            "operationalStateCodeList": {"type": "array", "description": "operationalStateCodeList"},
        },
        "required": ["deviceId"]
    }
}

getTransitNetworksCount_function = {
    "name": "getTransitNetworksCount",
    "description": "Returns the count of transit networks that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "type": {"type": "string", "description": "Type of the transit network. Allowed values are [IP_BASED_TRANSIT, SDA_LISP_PUB_SUB_TRANSIT, SDA_LISP_BGP_TRANSIT]."},
        },
        "required": []
    }
}

getAllExecutionDetailsForAGivenReport_function = {
    "name": "getAllExecutionDetailsForAGivenReport",
    "description": "Get details of all executions for a given report",
    "parameters": {
        "type": "object",
        "properties": {
            "reportId": {"type": "string", "description": "reportId of report"},
        },
        "required": ["reportId"]
    }
}

getPortChannelCount_function = {
    "name": "getPortChannelCount",
    "description": "Returns the count of port channels that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric the device is assigned to."},
            "networkDeviceId": {"type": "string", "description": "ID of the network device."},
            "portChannelName": {"type": "string", "description": "Name of the port channel."},
            "connectedDeviceType": {"type": "string", "description": "Connected device type of the port channel. The allowed values are [TRUNK, EXTENDED_NODE]."},
        },
        "required": []
    }
}

getAuditLogParentRecords_function = {
    "name": "getAuditLogParentRecords",
    "description": "Get Parent Audit Log Event instances from the Event-Hub",
    "parameters": {
        "type": "object",
        "properties": {
            "instanceId": {"type": "string", "description": "InstanceID of the Audit Log."},
            "name": {"type": "string", "description": "Audit Log notification event name."},
            "eventId": {"type": "string", "description": "Audit Log notification's event ID."},
            "category": {"type": "string", "description": "Audit Log notification's event category. Supported values: INFO, WARN, ERROR, ALERT, TASK_PROGRESS, TASK_FAILURE, TASK_COMPLETE, COMMAND, QUERY, CONVERSATION"},
            "severity": {"type": "string", "description": "Audit Log notification's event severity. Supported values: 1, 2, 3, 4, 5."},
            "domain": {"type": "string", "description": "Audit Log notification's event domain."},
            "subDomain": {"type": "string", "description": "Audit Log notification's event sub-domain."},
            "source": {"type": "string", "description": "Audit Log notification's event source."},
            "userId": {"type": "string", "description": "Audit Log notification's event userId."},
            "context": {"type": "string", "description": "Audit Log notification's event correlationId."},
            "eventHierarchy": {"type": "string", "description": "Audit Log notification's event eventHierarchy. Example: \"US.CA.San Jose\" OR \"US.CA\" OR \"CA.San Jose\" - Delimiter for hierarchy separation is \".\"."},
            "siteId": {"type": "string", "description": "Audit Log notification's siteId."},
            "deviceId": {"type": "string", "description": "Audit Log notification's deviceId."},
            "isSystemEvents": {"type": "boolean", "description": "Parameter to filter system generated audit-logs."},
            "description": {"type": "string", "description": "String full/partial search - (Provided input string is case insensitively matched for records)."},
            "offset": {"type": "number", "description": "Position of a particular Audit Log record in the data."},
            "limit": {"type": "number", "description": "Number of Audit Log records to be returned per page."},
            "startTime": {"type": "number", "description": "Start Time in milliseconds since Epoch Eg. 1597950637211 (when provided endTime is mandatory)"},
            "endTime": {"type": "number", "description": "End Time in milliseconds since Epoch Eg. 1597961437211 (when provided startTime is mandatory)"},
            "sortBy": {"type": "string", "description": "Sort the Audit Logs by certain fields. Supported values are event notification header attributes."},
            "order": {"type": "string", "description": "Order of the sorted Audit Log records. Default value is desc by timestamp. Supported values: asc, desc."},
        },
        "required": []
    }
}

retrieveDNSSettingsForASite_function = {
    "name": "retrieveDNSSettingsForASite",
    "description": "Retrieve DNS settings for a site; `null` values indicate that the setting will be inherited from the parent site; empty objects (`{}`) indicate that the setting is unset at a site.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Site Id"},
            "_inherited": {"type": "boolean", "description": "Include settings explicitly set for this site and settings inherited from sites higher in the site hierarchy; when `false`, `null` values indicate that the site inherits that setting from the parent site or a site higher in the site hierarchy."},
        },
        "required": ["id"]
    }
}

getEmailDestination_function = {
    "name": "getEmailDestination",
    "description": "Get Email Destination",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

retrieveLicenseSetting_function = {
    "name": "retrieveLicenseSetting",
    "description": "Retrieves license setting - Default smart account id and virtual account id for auto registration of devices for smart license flow. If default smart account is not configured, 'defaultSmartAccountId' is 'null'. Similarly, if auto registration of devices for smart license flow is not enabled, 'autoRegistrationVirtualAccountId' is 'null'. For smart proxy connection mode, 'autoRegistrationVirtualAccountId' is always 'null'.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getMulticast_function = {
    "name": "getMulticast",
    "description": "Returns a list of multicast configurations at a fabric site level that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric site where multicast is configured."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getFabricDevicesCount_function = {
    "name": "getFabricDevicesCount",
    "description": "Returns the count of fabric devices that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric this device belongs to."},
            "networkDeviceId": {"type": "string", "description": "Network device ID of the fabric device."},
            "deviceRoles": {"type": "string", "description": "Device roles of the fabric device. Allowed values are [CONTROL_PLANE_NODE, EDGE_NODE, BORDER_NODE, WIRELESS_CONTROLLER_NODE, EXTENDED_NODE]."},
        },
        "required": ["fabricId"]
    }
}

getLayer3VirtualNetworksCount_function = {
    "name": "getLayer3VirtualNetworksCount",
    "description": "Returns the count of layer 3 virtual networks that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric the layer 3 virtual network is assigned to."},
            "anchoredSiteId": {"type": "string", "description": "Fabric ID of the fabric site the layer 3 virtual network is anchored at."},
        },
        "required": []
    }
}

getDevicesDiscoveredById_function = {
    "name": "getDevicesDiscoveredById",
    "description": "Returns the count of network devices discovered in the given discovery. Discovery ID can be obtained using the \"Get Discoveries by range\" API.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Discovery ID"},
            "taskId": {"type": "string", "description": "taskId"},
        },
        "required": ["id"]
    }
}

getTaskById_function = {
    "name": "getTaskById",
    "description": "Returns a task by specified id",
    "parameters": {
        "type": "object",
        "properties": {
            "taskId": {"type": "string", "description": "UUID of the Task"},
        },
        "required": ["taskId"]
    }
}

getDiscoveredDevicesByRange_function = {
    "name": "getDiscoveredDevicesByRange",
    "description": "Returns the network devices discovered for the given discovery and for the given range. The maximum number of records that can be retrieved is 500. Discovery ID can be obtained using the \"Get Discoveries by range\" API.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Discovery ID"},
            "startIndex": {"type": "integer", "description": "Starting index for the records"},
            "recordsToReturn": {"type": "integer", "description": "Number of records to fetch from the start index"},
            "taskId": {"type": "string", "description": "taskId"},
        },
        "required": ["id", "startIndex", "recordsToReturn"]
    }
}

retrievesTheTotalCountOfClientsByApplyingBasicFiltering_function = {
    "name": "retrievesTheTotalCountOfClientsByApplyingBasicFiltering",
    "description": "Retrieves the number of clients by applying basic filtering. For detailed information about the usage of the API, please refer to the Open API specification document - https://github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-clients1-1.0.0-resolved.yaml",
    "parameters": {
        "type": "object",
        "properties": {
            "X-CALLER-ID": {"type": "string", "description": "Caller ID is used to trace the origin of API calls and their associated queries executed on the database. It's an optional header parameter that can be added to an API request."},
            "startTime": {"type": "number", "description": "Start time from which API queries the data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive.  If `startTime` is not provided, API will default to current time."},
            "endTime": {"type": "number", "description": "End time to which API queries the data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive."},
            "type": {"type": "string", "description": "The client device type whether client is connected to network through Wired or Wireless medium."},
            "osType": {"type": "string", "description": "Client device operating system type. This field supports wildcard (`*`) character-based search. If the value contains the (`*`) character, please use the /query API for regex search.  Ex: `*iOS*` or `iOS*` or `*iOS` Examples:  `osType=iOS` (single osType requested)  `osType=iOS&osType=Android` (multiple osType requested)"},
            "osVersion": {"type": "string", "description": "Client device operating system version This field supports wildcard (`*`) character-based search. If the value contains the (`*`) character, please use the /query API for regex search.  Ex: `*14.3*` or `14.3*` or `*14.3` Examples:  `osVersion=14.3` (single osVersion requested)  `osVersion=14.3&osVersion=10.1` (multiple osVersion requested)"},
            "siteHierarchy": {"type": "string", "description": "The full hierarchical breakdown of the site tree starting from Global site name and ending with the specific site name. The Root site is named \"Global\" (Ex. \"Global/AreaName/BuildingName/FloorName\") This field supports wildcard (`*`) character-based search. If the value contains the (`*`) character, please use the /query API for regex search.  Ex: `*BuildingName*` or `BuildingName*` or `*BuildingName` Examples: `siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested) `siteHierarchy=Global/AreaName/BuildingName1/FloorName1&siteHierarchy=Global/AreaName/BuildingName1/FloorName2` (multiple siteHierarchy requested)"},
            "siteHierarchyId": {"type": "string", "description": "The full hierarchy breakdown of the site tree in id form starting from Global site UUID and ending with the specific site UUID. (Ex. \"globalUuid/areaUuid/buildingUuid/floorUuid\") This field supports wildcard (`*`) character-based search.  Ex: `*buildingUuid*` or `buildingUuid*` or `*buildingUuid` Examples: `siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid` (single siteHierarchyId requested) `siteHierarchyId=globalUuid/areaUuid/buildingUuid1/floorUuid1&siteHierarchyId=globalUuid/areaUuid/buildingUuid1/floorUuid2` (multiple siteHierarchyId requested)"},
            "siteId": {"type": "string", "description": "The site UUID without the top level hierarchy. (Ex.\"floorUuid\") Examples: `siteId=floorUuid` (single siteId requested) `siteId=floorUuid1&siteId=floorUuid2` (multiple siteId requested)"},
            "ipv4Address": {"type": "string", "description": "IPv4 Address of the network entity either network device or client This field supports wildcard (`*`) character-based search.  Ex: `*1.1*` or `1.1*` or `*1.1`  Examples:  `ipv4Address=1.1.1.1` (single ipv4Address requested)  `ipv4Address=1.1.1.1&ipv4Address=2.2.2.2` (multiple ipv4Address requested)"},
            "ipv6Address": {"type": "string", "description": "IPv6 Address of the network entity either network device or client This field supports wildcard (`*`) character-based search. Ex: `*2001:db8*` or `2001:db8*` or `*2001:db8`  Examples:  `ipv6Address=2001:db8:0:0:0:0:2:1` (single ipv6Address requested)  `ipv6Address=2001:db8:0:0:0:0:2:1&ipv6Address=2001:db8:85a3:8d3:1319:8a2e:370:7348` (multiple ipv6Address requested)"},
            "macAddress": {"type": "string", "description": "The macAddress of the network device or client This field supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or `*AB:AB:AB` Examples:  `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)  `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress requested)"},
            "wlcName": {"type": "string", "description": "Wireless Controller name that reports the wireless client. This field supports wildcard (`*`) character-based search. If the value contains the (`*`) character, please use the /query API for regex search. Ex: `*wlc-25*` or `wlc-25*` or `*wlc-25`  Examples:  `wlcName=wlc-25` (single wlcName requested)  `wlcName=wlc-25&wlc-34` (multiple wlcName requested)"},
            "connectedNetworkDeviceName": {"type": "string", "description": "Name of the neighbor network device that client is connected to. This field supports wildcard (`*`) character-based search. If the value contains the (`*`) character, please use the /query API for regex search. Ex: `*ap-25*` or `ap-25*` or `*ap-25`  Examples:  `connectedNetworkDeviceName=ap-25` (single connectedNetworkDeviceName requested)  `connectedNetworkDeviceName=ap-25&ap-34` (multiple connectedNetworkDeviceName requested)"},
            "ssid": {"type": "string", "description": "SSID is the name of wireless network to which client connects to. It is also referred to as WLAN ID - Wireless Local Area Network Identifier. This field supports wildcard (`*`) character-based search. If the value contains the (`*`) character, please use the /query API for regex search.  Ex: `*Alpha*` or `Alpha*` or `*Alpha`  Examples:  `ssid=Alpha` (single ssid requested)  `ssid=Alpha&ssid=Guest` (multiple ssid requested)"},
            "band": {"type": "string", "description": "WiFi frequency band that client or Access Point operates. Band value is represented in Giga Hertz - GHz Examples:  `band=5GHZ` (single band requested)  `band=2.4GHZ&band=6GHZ` (multiple band requested)"},
        },
        "required": []
    }
}

retrievesTheListOfNetworkDeviceProductNames_function = {
    "name": "retrievesTheListOfNetworkDeviceProductNames",
    "description": "Get the list of network device product names, their ordinal, and the support PIDs based on filter criteria.",
    "parameters": {
        "type": "object",
        "properties": {
            "productName": {"type": "string", "description": "Filter with network device product name. Supports partial case-insensitive search. A minimum of 3 characters are required for search"},
            "productId": {"type": "string", "description": "Filter with product ID (PID)"},
            "offset": {"type": "number", "description": "The first record to show for this page; the first record is numbered 1. The minimum value is 1."},
            "limit": {"type": "number", "description": "The number of records to show for this page. The minimum and maximum values are 1 and 500, respectively."},
        },
        "required": []
    }
}

getConnectedDeviceDetail_function = {
    "name": "getConnectedDeviceDetail",
    "description": "Get connected device detail for given deviceUuid and interfaceUuid",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceUuid": {"type": "string", "description": "instanceuuid of Device"},
            "interfaceUuid": {"type": "string", "description": "instanceuuid of interface"},
        },
        "required": ["deviceUuid", "interfaceUuid"]
    }
}

getDevicesThatAreAssignedToASite_function = {
    "name": "getDevicesThatAreAssignedToASite",
    "description": "API to get devices that are assigned to a site.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Site Id"},
            "offset": {"type": "string", "description": "Offset/starting index for pagination"},
            "limit": {"type": "string", "description": "Number of devices to be listed. Default and max supported value is 500"},
            "memberType": {"type": "string", "description": "Member type (This API only supports the 'networkdevice' type)"},
            "level": {"type": "string", "description": "Depth of site hierarchy to be considered to list the devices. If the provided value is -1, devices for all child sites will be listed."},
        },
        "required": ["id", "memberType"]
    }
}

retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned_function = {
    "name": "retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned",
    "description": "Retrieves the list of profiles that the given site has been assigned.  These profiles may either be directly assigned to this site, or were assigned to a parent site and have been inherited.  These assigments can be modified via the `/dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments` resources.",
    "parameters": {
        "type": "object",
        "properties": {
            "siteId": {"type": "string", "description": "The `id` of the site, retrievable from `/dna/intent/api/v1/sites`"},
            "offset": {"type": "number", "description": "The first record to show for this page; the first record is numbered 1."},
            "limit": {"type": "number", "description": "The number of records to show for this page."},
        },
        "required": ["siteId"]
    }
}

getListOfDiscoveriesByDiscoveryId_function = {
    "name": "getListOfDiscoveriesByDiscoveryId",
    "description": "Returns the list of discovery jobs for the given Discovery ID. The results can be optionally filtered based on IP. Discovery ID can be obtained using the \"Get Discoveries by range\" API.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Discovery ID"},
            "offset": {"type": "integer", "description": "Starting index for the records"},
            "limit": {"type": "integer", "description": "Number of records to fetch from the starting index"},
            "ipAddress": {"type": "string", "description": "Filter records based on IP address"},
        },
        "required": ["id"]
    }
}

getPhysicalTopology_function = {
    "name": "getPhysicalTopology",
    "description": "Returns the raw physical topology by specified criteria of nodeType",
    "parameters": {
        "type": "object",
        "properties": {
            "nodeType": {"type": "string", "description": "nodeType"},
        },
        "required": []
    }
}

getSiteTopology_function = {
    "name": "getSiteTopology",
    "description": "Returns site topology",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

retrieveNTPSettingsForASite_function = {
    "name": "retrieveNTPSettingsForASite",
    "description": "Retrieve NTP settings for a site; `null` values indicate that the setting will be inherited from the parent site; empty objects (`{}`) indicate that the setting is unset at a site.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Site Id"},
            "_inherited": {"type": "boolean", "description": "Include settings explicitly set for this site and settings inherited from sites higher in the site hierarchy; when `false`, `null` values indicate that the site inherits that setting from the parent site or a site higher in the site hierarchy."},
        },
        "required": ["id"]
    }
}

countOfNetworkDeviceImageUpdates_function = {
    "name": "countOfNetworkDeviceImageUpdates",
    "description": "Returns the count of network device image updates based on the given filter criteria",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Update id which is unique for each network device under the parentId"},
            "parentId": {"type": "string", "description": "Updates that have this parent id"},
            "networkDeviceId": {"type": "string", "description": "Network device id"},
            "status": {"type": "string", "description": "Status of the image update. Available values: FAILURE, SUCCESS, IN_PROGRESS, PENDING"},
            "imageName": {"type": "string", "description": "Software image name for the update"},
            "hostName": {"type": "string", "description": "Host name of the network device for the image update. Supports case-insensitive partial search."},
            "managementAddress": {"type": "string", "description": "Management address of the network device"},
            "startTime": {"type": "number", "description": "Image update started after the given time (as milliseconds since UNIX epoch)."},
            "endTime": {"type": "number", "description": "Image update started before the given time (as milliseconds since UNIX epoch)."},
        },
        "required": []
    }
}

getPlannedAccessPointsForBuilding_function = {
    "name": "getPlannedAccessPointsForBuilding",
    "description": "Provides a list of Planned Access Points for the Building it is requested for",
    "parameters": {
        "type": "object",
        "properties": {
            "buildingId": {"type": "string", "description": "The instance UUID of the building hierarchy element"},
            "limit": {"type": "number", "description": "The page size limit for the response, e.g. limit=100 will return a maximum of 100 records"},
            "offset": {"type": "number", "description": "The page offset for the response. E.g. if limit=100, offset=0 will return first 100 records, offset=1 will return next 100 records, etc."},
            "radios": {"type": "boolean", "description": "Whether to include the planned radio details of the planned access points"},
        },
        "required": ["buildingId"]
    }
}

countOfNetworkProductNames_function = {
    "name": "countOfNetworkProductNames",
    "description": "Count of product names based on filter criteria",
    "parameters": {
        "type": "object",
        "properties": {
            "productName": {"type": "string", "description": "Filter with network device product name. Supports partial case-insensitive search. A minimum of 3 characters are required for search"},
            "productId": {"type": "string", "description": "Filter with product ID (PID)"},
        },
        "required": []
    }
}

getAccessPointConfiguration_function = {
    "name": "getAccessPointConfiguration",
    "description": "Users can query the access point configuration information per device using the ethernet MAC address",
    "parameters": {
        "type": "object",
        "properties": {
            "key": {"type": "string", "description": "The ethernet MAC address of Access point"},
        },
        "required": ["key"]
    }
}

getDeviceConfigForAllDevices_function = {
    "name": "getDeviceConfigForAllDevices",
    "description": "Returns the config for all devices. This API has been deprecated and will not be available in a Cisco Catalyst Center release after Nov 1st 2024 23:59:59 GMT.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getTopologyDetails_function = {
    "name": "getTopologyDetails",
    "description": "Returns Layer 2 network topology by specified VLAN ID",
    "parameters": {
        "type": "object",
        "properties": {
            "vlanID": {"type": "string", "description": "Vlan Name for e.g Vlan1, Vlan23 etc"},
        },
        "required": ["vlanID"]
    }
}

getFabricDevicesLayer3HandoffsWithIpTransitCount_function = {
    "name": "getFabricDevicesLayer3HandoffsWithIpTransitCount",
    "description": "Returns the count of layer 3 handoffs with ip transit of fabric devices that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric this device belongs to."},
            "networkDeviceId": {"type": "string", "description": "Network device ID of the fabric device."},
        },
        "required": ["fabricId"]
    }
}

getFabricDevicesLayer3HandoffsWithSdaTransitCount_function = {
    "name": "getFabricDevicesLayer3HandoffsWithSdaTransitCount",
    "description": "Returns the count of layer 3 handoffs with sda transit of fabric devices that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric this device belongs to."},
            "networkDeviceId": {"type": "string", "description": "Network device ID of the fabric device."},
        },
        "required": ["fabricId"]
    }
}

retrievesTheListOfNetworkProfilesForSites_function = {
    "name": "retrievesTheListOfNetworkProfilesForSites",
    "description": "Retrieves the list of network profiles for sites.",
    "parameters": {
        "type": "object",
        "properties": {
            "offset": {"type": "number", "description": "The first record to show for this page; the first record is numbered 1."},
            "limit": {"type": "number", "description": "The number of records to show for this page."},
            "sortBy": {"type": "string", "description": "A property within the response to sort by."},
            "order": {"type": "string", "description": "Whether ascending or descending order should be used to sort the response."},
            "type": {"type": "string", "description": "Filter responses to only include profiles of a given type"},
        },
        "required": []
    }
}

getFunctionalCapabilityForDevices_function = {
    "name": "getFunctionalCapabilityForDevices",
    "description": "Returns the functional-capability for given devices",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "Accepts comma separated deviceid's and return list of functional-capabilities for the given id's. If invalid or not-found id's are provided, null entry will be returned in the list."},
            "functionName": {"type": "array", "description": "functionName"},
        },
        "required": ["deviceId"]
    }
}

getPortAssignments_function = {
    "name": "getPortAssignments",
    "description": "Returns a list of port assignments that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric the device is assigned to."},
            "networkDeviceId": {"type": "string", "description": "Network device ID of the port assignment."},
            "interfaceName": {"type": "string", "description": "Interface name of the port assignment."},
            "dataVlanName": {"type": "string", "description": "Data VLAN name of the port assignment."},
            "voiceVlanName": {"type": "string", "description": "Voice VLAN name of the port assignment."},
            "offset": {"type": "number", "description": "Starting record for pagination."},
            "limit": {"type": "number", "description": "Maximum number of records to return."},
        },
        "required": []
    }
}

getSiteNotAssignedNetworkDevices_function = {
    "name": "getSiteNotAssignedNetworkDevices",
    "description": "Get network devices that are not assigned to any site.",
    "parameters": {
        "type": "object",
        "properties": {
            "offset": {"type": "number", "description": "The first record to show for this page; the first record is numbered 1."},
            "limit": {"type": "number", "description": "The number of records to show for this page."},
        },
        "required": []
    }
}

getAccessPointRebootTaskResult_function = {
    "name": "getAccessPointRebootTaskResult",
    "description": "Users can query the access point reboot status using this intent API",
    "parameters": {
        "type": "object",
        "properties": {
            "parentTaskId": {"type": "string", "description": "task id of ap reboot request"},
        },
        "required": []
    }
}

getDeviceDetail_function = {
    "name": "getDeviceDetail",
    "description": "Returns detailed Network Device information retrieved by Mac Address, Device Name or UUID for any given point of time.",
    "parameters": {
        "type": "object",
        "properties": {
            "timestamp": {"type": "number", "description": "UTC timestamp of device data in milliseconds"},
            "identifier": {"type": "string", "description": "One of \"macAddress\", \"nwDeviceName\", \"uuid\" (case insensitive)"},
            "searchBy": {"type": "string", "description": "MAC Address, device name, or UUID of the network device"},
        },
        "required": ["identifier", "searchBy"]
    }
}

getSiteNotAssignedNetworkDevicesCount_function = {
    "name": "getSiteNotAssignedNetworkDevicesCount",
    "description": "Get network devices count that are not assigned to any site.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getDeviceBySerialNumber_function = {
    "name": "getDeviceBySerialNumber",
    "description": "Returns the network device with given serial number",
    "parameters": {
        "type": "object",
        "properties": {
            "serialNumber": {"type": "string", "description": "Device serial number"},
        },
        "required": ["serialNumber"]
    }
}

getApplicationCount_function = {
    "name": "getApplicationCount",
    "description": "Get the number of all existing applications",
    "parameters": {
        "type": "object",
        "properties": {
            "scalableGroupType": {"type": "string", "description": "scalable group type to retrieve, valid value APPLICATION"},
        },
        "required": ["scalableGroupType"]
    }
}

getComplianceStatusCount_function = {
    "name": "getComplianceStatusCount",
    "description": "Return Compliance Status Count",
    "parameters": {
        "type": "object",
        "properties": {
            "complianceStatus": {"type": "string", "description": "Specify \"Compliance status(es)\" separated by commas. The Compliance status can be 'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS', 'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'."},
        },
        "required": []
    }
}

getTasks_function = {
    "name": "getTasks",
    "description": "Returns task(s) based on filter criteria",
    "parameters": {
        "type": "object",
        "properties": {
            "offset": {"type": "integer", "description": "The first record to show for this page; the first record is numbered 1."},
            "limit": {"type": "integer", "description": "The number of records to show for this page."},
            "sortBy": {"type": "string", "description": "A property within the response to sort by."},
            "order": {"type": "string", "description": "Whether ascending or descending order should be used to sort the response."},
            "startTime": {"type": "integer", "description": "This is the epoch millisecond start time from which tasks need to be fetched"},
            "endTime": {"type": "integer", "description": "This is the epoch millisecond end time upto which task records need to be fetched"},
            "parentId": {"type": "string", "description": "Fetch tasks that have this parent Id"},
            "rootId": {"type": "string", "description": "Fetch tasks that have this root Id"},
            "status": {"type": "string", "description": "Fetch tasks that have this status. Available values : PENDING, FAILURE, SUCCESS"},
        },
        "required": []
    }
}

getListOfChildEventsForTheGivenWirelessClientEvent_function = {
    "name": "getListOfChildEventsForTheGivenWirelessClientEvent",
    "description": "Wireless client event could have child events and this API can be used to fetch the same using parent event `id` as the input. For detailed information about the usage of the API, please refer to the Open API specification document - https://github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceEvents-1.0.0-resolved.yaml",
    "parameters": {
        "type": "object",
        "properties": {
            "X-CALLER-ID": {"type": "string", "description": "Caller ID is used to trace the origin of API calls and their associated queries executed on the database. It's an optional header parameter that can be added to an API request."},
            "id": {"type": "string", "description": "Unique identifier for the event"},
        },
        "required": ["id"]
    }
}

getProvisioningSettings_function = {
    "name": "getProvisioningSettings",
    "description": "Returns provisioning settings",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getInterfaceById_function = {
    "name": "getInterfaceById",
    "description": "Returns the interface for the given interface ID",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Interface ID"},
        },
        "required": ["id"]
    }
}

getInterfaceInfoById_function = {
    "name": "getInterfaceInfoById",
    "description": "Returns list of interfaces by specified device",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["deviceId"]
    }
}

getTaskByOperationId_function = {
    "name": "getTaskByOperationId",
    "description": "Returns root tasks associated with an Operationid",
    "parameters": {
        "type": "object",
        "properties": {
            "operationId": {"type": "string", "description": "operationId"},
            "offset": {"type": "integer", "description": "Index, minimum value is 0"},
            "limit": {"type": "integer", "description": "The maximum value of {limit} supported is 500. <br/> Base 1 indexing for {limit}, minimum value is 1"},
        },
        "required": ["operationId", "offset", "limit"]
    }
}

getL3TopologyDetails_function = {
    "name": "getL3TopologyDetails",
    "description": "Returns the Layer 3 network topology by routing protocol",
    "parameters": {
        "type": "object",
        "properties": {
            "topologyType": {"type": "string", "description": "Type of topology(OSPF,ISIS,etc)"},
        },
        "required": ["topologyType"]
    }
}

getAdvisoryDeviceDetail_function = {
    "name": "getAdvisoryDeviceDetail",
    "description": "Retrieves advisory device details for a device",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "Device instance UUID"},
        },
        "required": ["deviceId"]
    }
}

getConnectorTypes_function = {
    "name": "getConnectorTypes",
    "description": "Get the list of connector types",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

retrieveDHCPSettingsForASite_function = {
    "name": "retrieveDHCPSettingsForASite",
    "description": "Retrieve DHCP settings for a site; `null` values indicate that the setting will be inherited from the parent site; empty objects (`{}`) indicate that the setting is unset at a site.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Site Id"},
            "_inherited": {"type": "boolean", "description": "Include settings explicitly set for this site and settings inherited from sites higher in the site hierarchy; when `false`, `null` values indicate that the site inherits that setting from the parent site or a site higher in the site hierarchy."},
        },
        "required": ["id"]
    }
}

getAnycastGatewayCount_function = {
    "name": "getAnycastGatewayCount",
    "description": "Returns the count of anycast gateways that match the provided query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "fabricId": {"type": "string", "description": "ID of the fabric the anycast gateway is assigned to."},
            "virtualNetworkName": {"type": "string", "description": "Name of the virtual network associated with the anycast gateways."},
            "ipPoolName": {"type": "string", "description": "Name of the IP pool associated with the anycast gateways."},
            "vlanName": {"type": "string", "description": "VLAN name of the anycast gateways."},
            "vlanId": {"type": "number", "description": "VLAN ID of the anycast gateways. The allowed range for vlanId is [2-4093] except for reserved VLANs [1002-1005], 2046, and 4094."},
        },
        "required": []
    }
}

getNetworkDeviceByPaginationRange_function = {
    "name": "getNetworkDeviceByPaginationRange",
    "description": "Returns the list of network devices for the given pagination range. The maximum number of records that can be retrieved is 500",
    "parameters": {
        "type": "object",
        "properties": {
            "startIndex": {"type": "integer", "description": "Start index [>=1]"},
            "recordsToReturn": {"type": "integer", "description": "Number of records to return [1<= recordsToReturn <= 500]"},
        },
        "required": ["startIndex", "recordsToReturn"]
    }
}

getSiteAssignedNetworkDevice_function = {
    "name": "getSiteAssignedNetworkDevice",
    "description": "Get site assigned network device. The items in the list are arranged in an order that corresponds with their internal identifiers.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Network Device Id."},
        },
        "required": ["id"]
    }
}

getAllInterfaces_function = {
    "name": "getAllInterfaces",
    "description": "Returns all available interfaces. This endpoint can return a maximum of 500 interfaces",
    "parameters": {
        "type": "object",
        "properties": {
            "offset": {"type": "integer", "description": "Offset"},
            "limit": {"type": "integer", "description": "Limit"},
            "lastInputTime": {"type": "string", "description": "Last Input Time"},
            "lastOutputTime": {"type": "string", "description": "Last Output Time"},
        },
        "required": []
    }
}

getWirelessLanControllerDetailsById_function = {
    "name": "getWirelessLanControllerDetailsById",
    "description": "Returns the wireless lan controller info with given device ID",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Device ID"},
        },
        "required": ["id"]
    }
}

getDevicesPerAdvisory_function = {
    "name": "getDevicesPerAdvisory",
    "description": "Retrieves list of devices for an advisory",
    "parameters": {
        "type": "object",
        "properties": {
            "advisoryId": {"type": "string", "description": "Advisory ID"},
        },
        "required": ["advisoryId"]
    }
}

getAccessPointConfigurationTaskResult_function = {
    "name": "getAccessPointConfigurationTaskResult",
    "description": "Users can query the access point configuration result using this intent API",
    "parameters": {
        "type": "object",
        "properties": {
            "task_id": {"type": "string", "description": "task id information of ap config"},
        },
        "required": ["task_id"]
    }
}

getComplianceDetail_function = {
    "name": "getComplianceDetail",
    "description": "Return Compliance Detail",
    "parameters": {
        "type": "object",
        "properties": {
            "complianceType": {"type": "string", "description": "Specify \"Compliance type(s)\" in commas. The Compliance type can be 'NETWORK_PROFILE', 'IMAGE', 'FABRIC', 'APPLICATION_VISIBILITY', 'FABRIC', RUNNING_CONFIG', 'NETWORK_SETTINGS', 'WORKFLOW' , 'EOX'."},
            "complianceStatus": {"type": "string", "description": "Specify \"Compliance status(es)\" in commas. The Compliance status can be 'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS', 'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'."},
            "deviceUuid": {"type": "string", "description": "Comma separated \"Device Id(s)\""},
            "offset": {"type": "number", "description": "offset/starting row"},
            "limit": {"type": "number", "description": "Number of records to be retrieved"},
        },
        "required": []
    }
}

getGlobalCredentials_function = {
    "name": "getGlobalCredentials",
    "description": "Returns global credential for the given credential sub type",
    "parameters": {
        "type": "object",
        "properties": {
            "credentialSubType": {"type": "string", "description": "Credential type as CLI / SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY / SNMPV3 / HTTP_WRITE / HTTP_READ / NETCONF"},
            "sortBy": {"type": "string", "description": "Field to sort the results by. Sorts by 'instanceId' if no value is provided"},
            "order": {"type": "string", "description": "Order of sorting. 'asc' or 'des'"},
        },
        "required": ["credentialSubType"]
    }
}

getComplianceStatus_function = {
    "name": "getComplianceStatus",
    "description": "Return compliance status of device(s).",
    "parameters": {
        "type": "object",
        "properties": {
            "complianceStatus": {"type": "string", "description": "Specify \"Compliance status(es)\" separated by commas. The Compliance status can be 'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS', 'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'."},
            "deviceUuid": {"type": "string", "description": "Comma separated 'Device Ids'"},
        },
        "required": []
    }
}

getProvisionedDevicesCount_function = {
    "name": "getProvisionedDevicesCount",
    "description": "Returns the count of provisioned devices based on query parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "siteId": {"type": "string", "description": "ID of the site hierarchy."},
        },
        "required": []
    }
}

getInterfacesCount_function = {
    "name": "getInterfacesCount",
    "description": "This API allows the user to get count of all interfaces",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getModules_function = {
    "name": "getModules",
    "description": "Returns modules by specified device id",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceId": {"type": "string", "description": "deviceId"},
            "limit": {"type": "integer", "description": "limit"},
            "offset": {"type": "integer", "description": "offset"},
            "nameList": {"type": "array", "description": "nameList"},
            "vendorEquipmentTypeList": {"type": "array", "description": "vendorEquipmentTypeList"},
            "partNumberList": {"type": "array", "description": "partNumberList"},
            "operationalStateCodeList": {"type": "array", "description": "operationalStateCodeList"},
        },
        "required": ["deviceId"]
    }
}

retrievesTheCountOfAssignedNetworkDeviceProducts_function = {
    "name": "retrievesTheCountOfAssignedNetworkDeviceProducts",
    "description": "Returns count of assigned network device product for a given image identifier. Refer `/dna/intent/api/v1/images` API for obtaining `imageId`",
    "parameters": {
        "type": "object",
        "properties": {
            "imageId": {"type": "string", "description": "Software image identifier. Refer `/dna/intent/api/v/images` API for obtaining `imageId`"},
            "productName": {"type": "string", "description": "Filter with network device product name. Supports partial case-insensitive search. A minimum of 3 characters are required for search."},
            "productId": {"type": "string", "description": "Filter with product ID (PID)"},
            "recommended": {"type": "string", "description": "Filter with recommended source. If `CISCO` then the network device product assigned was recommended by Cisco and `USER` then the user has manually assigned. Available values : CISCO, USER"},
            "assigned": {"type": "string", "description": "Filter with the assigned/unassigned, `ASSIGNED` option will filter network device products that are associated with the given image. The `NOT_ASSIGNED` option will filter network device products that have not yet been associated with the given image but apply to it. Available values: ASSIGNED, NOT_ASSIGNED"},
        },
        "required": ["imageId"]
    }
}

getDeviceHistory_function = {
    "name": "getDeviceHistory",
    "description": "Returns history for a specific device. Serial number is a required parameter",
    "parameters": {
        "type": "object",
        "properties": {
            "serialNumber": {"type": "string", "description": "Device Serial Number"},
            "sort": {"type": "array", "description": "Comma seperated list of fields to sort on"},
            "sortOrder": {"type": "string", "description": "Sort Order Ascending (asc) or Descending (des)"},
        },
        "required": ["serialNumber"]
    }
}

getApplicationPolicyQueuingProfileCount_function = {
    "name": "getApplicationPolicyQueuingProfileCount",
    "description": "Get the number of all existing  application policy queuing profile",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getTaskTree_function = {
    "name": "getTaskTree",
    "description": "Returns a task with its children tasks by based on their id",
    "parameters": {
        "type": "object",
        "properties": {
            "taskId": {"type": "string", "description": "UUID of the Task"},
        },
        "required": ["taskId"]
    }
}

getDiscoveredNetworkDevicesByDiscoveryId_function = {
    "name": "getDiscoveredNetworkDevicesByDiscoveryId",
    "description": "Returns the network devices discovered for the given Discovery ID. Discovery ID can be obtained using the \"Get Discoveries by range\" API.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Discovery ID"},
            "taskId": {"type": "string", "description": "taskId"},
        },
        "required": ["id"]
    }
}

getSiteAssignedNetworkDevicesCount_function = {
    "name": "getSiteAssignedNetworkDevicesCount",
    "description": "Get all network devices count under the given site in the network hierarchy.",
    "parameters": {
        "type": "object",
        "properties": {
            "siteId": {"type": "string", "description": "Site Id. It must be area Id or building Id or floor Id."},
        },
        "required": ["siteId"]
    }
}

getNetworkV2_function = {
    "name": "getNetworkV2",
    "description": "API to get SNMP, NTP, Network AAA, Client and Endpoint AAA, and/or DNS center server settings.",
    "parameters": {
        "type": "object",
        "properties": {
            "siteId": {"type": "string", "description": "Site Id to get the network settings associated with the site."},
        },
        "required": ["siteId"]
    }
}

getDeviceValuesThatMatchFullyOrPartiallyAnAttribute_function = {
    "name": "getDeviceValuesThatMatchFullyOrPartiallyAnAttribute",
    "description": "Returns the list of values of the first given required parameter. You can use the .* in any value to conduct a wildcard search. For example, to get all the devices with the management IP address starting with 10.10. , issue the following request: GET /dna/inten/api/v1/network-device/autocomplete?managementIpAddress=10.10..* It will return the device management IP addresses that match fully or partially the provided attribute. {[10.10.1.1, 10.10.20.2, …]}.",
    "parameters": {
        "type": "object",
        "properties": {
            "vrfName": {"type": "string", "description": "vrfName"},
            "managementIpAddress": {"type": "string", "description": "managementIpAddress"},
            "hostname": {"type": "string", "description": "hostname"},
            "macAddress": {"type": "string", "description": "macAddress"},
            "family": {"type": "string", "description": "family"},
            "collectionStatus": {"type": "string", "description": "collectionStatus"},
            "collectionInterval": {"type": "string", "description": "collectionInterval"},
            "softwareVersion": {"type": "string", "description": "softwareVersion"},
            "softwareType": {"type": "string", "description": "softwareType"},
            "reachabilityStatus": {"type": "string", "description": "reachabilityStatus"},
            "reachabilityFailureReason": {"type": "string", "description": "reachabilityFailureReason"},
            "errorCode": {"type": "string", "description": "errorCode"},
            "platformId": {"type": "string", "description": "platformId"},
            "series": {"type": "string", "description": "series"},
            "type": {"type": "string", "description": "type"},
            "serialNumber": {"type": "string", "description": "serialNumber"},
            "upTime": {"type": "string", "description": "upTime"},
            "role": {"type": "string", "description": "role"},
            "roleSource": {"type": "string", "description": "roleSource"},
            "associatedWlcIp": {"type": "string", "description": "associatedWlcIp"},
            "offset": {"type": "integer", "description": "offset"},
            "limit": {"type": "integer", "description": "limit"},
        },
        "required": []
    }
}

getApplications_function = {
    "name": "getApplications",
    "description": "Get applications by offset/limit or by name",
    "parameters": {
        "type": "object",
        "properties": {
            "offset": {"type": "number", "description": "The offset of the first application to be returned"},
            "limit": {"type": "number", "description": "The maximum number of applications to be returned"},
            "name": {"type": "string", "description": "Application's name"},
        },
        "required": []
    }
}

getNetwork_function = {
    "name": "getNetwork",
    "description": "API to get  DHCP and DNS center server details.",
    "parameters": {
        "type": "object",
        "properties": {
            "siteId": {"type": "string", "description": "Site id to get the network settings associated with the site."},
        },
        "required": []
    }
}

getTransitPeerNetworkInfo_function = {
    "name": "getTransitPeerNetworkInfo",
    "description": "Get Transit Peer Network Info from SD-Access",
    "parameters": {
        "type": "object",
        "properties": {
            "transitPeerNetworkName": {"type": "string", "description": "Transit or Peer Network Name"},
        },
        "required": ["transitPeerNetworkName"]
    }
}

getApplicationSets_function = {
    "name": "getApplicationSets",
    "description": "Get appllication-sets by offset/limit or by name",
    "parameters": {
        "type": "object",
        "properties": {
            "offset": {"type": "number", "description": ""},
            "limit": {"type": "number", "description": ""},
            "name": {"type": "string", "description": ""},
        },
        "required": []
    }
}

getApplicationsCount_function = {
    "name": "getApplicationsCount",
    "description": "Get the number of all existing applications",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getGlobalPool_function = {
    "name": "getGlobalPool",
    "description": "API to get the global pool.",
    "parameters": {
        "type": "object",
        "properties": {
            "offset": {"type": "number", "description": "Offset/starting row. Indexed from 1. Default value of 1."},
            "limit": {"type": "number", "description": "Number of Global Pools to be retrieved. Default is 25 if not specified."},
        },
        "required": []
    }
}

getProvisionedWiredDevice_function = {
    "name": "getProvisionedWiredDevice",
    "description": "Get Provisioned Wired Device",
    "parameters": {
        "type": "object",
        "properties": {
            "deviceManagementIpAddress": {"type": "string", "description": "deviceManagementIpAddress"},
        },
        "required": ["deviceManagementIpAddress"]
    }
}

getDeviceCredentialDetails_function = {
    "name": "getDeviceCredentialDetails",
    "description": "API to get device credential details. This API has been deprecated and will not be available in a Cisco DNA Center release after August 1st 2024 23:59:59 GMT. Please refer new Intent API : Get All Global Credentials V2",
    "parameters": {
        "type": "object",
        "properties": {
            "siteId": {"type": "string", "description": "Site id to retrieve the credential details associated with the site."},
        },
        "required": []
    }
}

getServiceProviderDetails_function = {
    "name": "getServiceProviderDetails",
    "description": "API to get service provider details (QoS).",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getSite_function = {
    "name": "getSite",
    "description": "Get site(s) by site-name-hierarchy or siteId or type. List all sites if these parameters are not given as an input.",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Site name hierarchy (E.g Global/USA/CA)"},
            "siteId": {"type": "string", "description": "Site Id"},
            "type": {"type": "string", "description": "Site type (Ex: area, building, floor)"},
            "offset": {"type": "integer", "description": "Offset/starting index for pagination. Indexed from 1."},
            "limit": {"type": "integer", "description": "Number of sites to be listed"},
        },
        "required": []
    }
}

getVirtualNetworkSummary_function = {
    "name": "getVirtualNetworkSummary",
    "description": "Get Virtual Network Summary",
    "parameters": {
        "type": "object",
        "properties": {
            "siteNameHierarchy": {"type": "string", "description": "Complete fabric siteNameHierarchy Path"},
        },
        "required": ["siteNameHierarchy"]
    }
}

getWirelessProfile_function = {
    "name": "getWirelessProfile",
    "description": "Gets either one or all the wireless network profiles if no name is provided for network-profile.",
    "parameters": {
        "type": "object",
        "properties": {
            "profileName": {"type": "string", "description": "Wireless Network Profile Name"},
        },
        "required": []
    }
}

getIssueEnrichmentDetails_function = {
    "name": "getIssueEnrichmentDetails",
    "description": "Enriches a given network issue context (an issue id or end user’s Mac Address) with details about the issue(s), impacted hosts and suggested actions for remediation",
    "parameters": {
        "type": "object",
        "properties": {
            "entity_type": {"type": "string", "description": "Issue enrichment details can be fetched based on either Issue ID or Client MAC address. This parameter value must either be issue_id/mac_address"},
            "entity_value": {"type": "string", "description": "Contains the actual value for the entity type that has been defined"},
            "__persistbapioutput": {"type": "boolean", "description": ""},
        },
        "required": ["entity_type", "entity_value"]
    }
}

getSiteCount_function = {
    "name": "getSiteCount",
    "description": "Get the site count of the specified site's sub-hierarchy (inclusive of the provided site)",
    "parameters": {
        "type": "object",
        "properties": {
            "siteId": {"type": "string", "description": "Site instance UUID"},
        },
        "required": []
    }
}

getClientEnrichmentDetails_function = {
    "name": "getClientEnrichmentDetails",
    "description": "Enriches a given network End User context (a network user-id or end user’s device Mac Address) with details about the user, the devices that the user is connected to and the assurance issues that the user is impacted by",
    "parameters": {
        "type": "object",
        "properties": {
            "entity_type": {"type": "string", "description": "Client enrichment details can be fetched based on either User ID or Client MAC address. This parameter value must either be network_user_id/mac_address"},
            "entity_value": {"type": "string", "description": "Contains the actual value for the entity type that has been defined"},
            "issueCategory": {"type": "string", "description": "The category of the DNA event based on which the underlying issues need to be fetched"},
            "__persistbapioutput": {"type": "boolean", "description": ""},
        },
        "required": ["entity_type", "entity_value"]
    }
}

getVirtualNetworkWithScalableGroups_function = {
    "name": "getVirtualNetworkWithScalableGroups",
    "description": "Get virtual network with scalable groups",
    "parameters": {
        "type": "object",
        "properties": {
            "virtualNetworkName": {"type": "string", "description": "virtualNetworkName"},
        },
        "required": ["virtualNetworkName"]
    }
}

getDynamicInterface_function = {
    "name": "getDynamicInterface",
    "description": "Get one or all dynamic interface(s)",
    "parameters": {
        "type": "object",
        "properties": {
            "__runsync": {"type": "boolean", "description": "Enable this parameter to execute the API and return a response synchronously"},
            "__timeout": {"type": "number", "description": "If __runsync is set to ‘true’, this defines the maximum time before which if the API completes its execution, then a synchronous response is returned.  If the time taken for the API to complete the execution, exceeds this time, then an asynchronous response is returned with an execution id, that can be used to get the status and response associated with the API execution"},
            "interface-name": {"type": "string", "description": "dynamic-interface name, if not specified all the existing dynamic interfaces will be retrieved"},
        },
        "required": []
    }
}

getApplicationSetsCount_function = {
    "name": "getApplicationSetsCount",
    "description": "Get the number of existing application-sets",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getUserEnrichmentDetails_function = {
    "name": "getUserEnrichmentDetails",
    "description": "Enriches a given network End User context (a network user-id or end user’s device Mac Address) with details about the user and devices that the user is connected to",
    "parameters": {
        "type": "object",
        "properties": {
            "entity_type": {"type": "string", "description": "User enrichment details can be fetched based on either User ID or Client MAC address. This parameter value must either be network_user_id/mac_address"},
            "entity_value": {"type": "string", "description": "Contains the actual value for the entity type that has been defined"},
            "__persistbapioutput": {"type": "boolean", "description": ""},
        },
        "required": ["entity_type", "entity_value"]
    }
}

getDeviceEnrichmentDetails_function = {
    "name": "getDeviceEnrichmentDetails",
    "description": "Enriches a given network device context (device id or device Mac Address or device management IP address) with details about the device and neighbor topology",
    "parameters": {
        "type": "object",
        "properties": {
            "entity_type": {"type": "string", "description": "Device enrichment details can be fetched based on either Device ID or Device MAC address or Device IP Address. This parameter value must either be device_id/mac_address/ip_address"},
            "entity_value": {"type": "string", "description": "Contains the actual value for the entity type that has been defined"},
            "__persistbapioutput": {"type": "boolean", "description": ""},
        },
        "required": ["entity_type", "entity_value"]
    }
}

getMembership_function = {
    "name": "getMembership",
    "description": "Getting the site children details and device details.",
    "parameters": {
        "type": "object",
        "properties": {
            "siteId": {"type": "string", "description": "Site id to retrieve device associated with the site."},
            "offset": {"type": "number", "description": "offset/starting row"},
            "limit": {"type": "number", "description": "Number of sites to be retrieved"},
            "deviceFamily": {"type": "string", "description": "Device family name"},
            "serialNumber": {"type": "string", "description": "Device serial number"},
        },
        "required": ["siteId"]
    }
}



#############################
# Meraki
#############################


list_all_clients_in_org = {
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

list_all_clients_in_org_by_name = {
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

get_network_alerts_history = {
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



list_all_devices_in_org = {
    "name": "list_all_devices_in_org",
    "description": "Retrieve a list of all Meraki devices in the organization (inventory).",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

get_all_access_points = {
    "name": "get_all_access_points",
    "description": "Retrieve all Meraki access points in the organization (wireless controllers).",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

list_all_switches_in_org = {
    "name": "list_all_switches_in_org",
    "description": "List all switch devices (MS) in the Meraki organization’s inventory.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

list_all_cameras_in_org = {
    "name": "list_all_cameras_in_org",
    "description": "List all Meraki cameras in the organization by checking camera onboarding statuses.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}



#############################
# Meraki SDK
#############################

getAdministeredIdentitiesMe = {
    "name": "getAdministeredIdentitiesMe",
    "description": "Returns the identity of the current user.",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getAdministeredIdentitiesMeApiKeys = {
    "name": "getAdministeredIdentitiesMeApiKeys",
    "description": "List the non-sensitive metadata associated with the API keys that belong to the user",
    "parameters": {
        "type": "object",
        "properties": {
        },
        "required": []
    }
}

getAdministeredLicensingSubscriptionEntitlements = {
    "name": "getAdministeredLicensingSubscriptionEntitlements",
    "description": "Retrieve the list of purchasable entitlements",
    "parameters": {
        "type": "object",
        "properties": {
            "skus": {"type": "array", "description": "Filter to entitlements with the specified SKUs"},
        },
        "required": []
    }
}

getAdministeredLicensingSubscriptionSubscriptions = {
    "name": "getAdministeredLicensingSubscriptionSubscriptions",
    "description": "List available subscriptions",
    "parameters": {
        "type": "object",
        "properties": {
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "subscriptionIds": {"type": "array", "description": "List of subscription ids to fetch"},
            "organizationIds": {"type": "array", "description": "Organizations to get associated subscriptions for"},
            "statuses": {"type": "array", "description": "List of statuses that returned subscriptions can have"},
            "productTypes": {"type": "array", "description": "List of product types that returned subscriptions need to have entitlements for."},
            "name": {"type": "string", "description": "Search for subscription name"},
            "startDate": {"type": "string", "description": "Filter subscriptions by start date, ISO 8601 format. To filter with a range of dates, use 'startDate[<option>]=?' in the request. Accepted options include lt, gt, lte, gte."},
            "endDate": {"type": "string", "description": "Filter subscriptions by end date, ISO 8601 format. To filter with a range of dates, use 'endDate[<option>]=?' in the request. Accepted options include lt, gt, lte, gte."},
        },
        "required": []
    }
}

getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses = {
    "name": "getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses",
    "description": "Get compliance status for requested subscriptions",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationIds": {"type": "array", "description": "Organizations to get subscription compliance information for"},
            "subscriptionIds": {"type": "array", "description": "Subscription ids"},
        },
        "required": ["organizationIds"]
    }
}

getDevice = {
    "name": "getDevice",
    "description": "Return a single device",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceApplianceDhcpSubnets = {
    "name": "getDeviceApplianceDhcpSubnets",
    "description": "Return the DHCP subnet information for an appliance",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceAppliancePerformance = {
    "name": "getDeviceAppliancePerformance",
    "description": "Return the performance score for a single MX. Only primary MX devices supported. If no data is available, a 204 error code is returned.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 30 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 14 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 30 minutes and be less than or equal to 14 days. The default is 30 minutes."},
        },
        "required": ["serial"]
    }
}

getDeviceAppliancePrefixesDelegated = {
    "name": "getDeviceAppliancePrefixesDelegated",
    "description": "Return current delegated IPv6 prefixes on an appliance.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceAppliancePrefixesDelegatedVlanAssignments = {
    "name": "getDeviceAppliancePrefixesDelegatedVlanAssignments",
    "description": "Return prefixes assigned to all IPv6 enabled VLANs on an appliance.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceApplianceRadioSettings = {
    "name": "getDeviceApplianceRadioSettings",
    "description": "Return the radio settings of an appliance",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceApplianceUplinksSettings = {
    "name": "getDeviceApplianceUplinksSettings",
    "description": "Return the uplink settings for an MX appliance",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceCameraAnalyticsLive = {
    "name": "getDeviceCameraAnalyticsLive",
    "description": "Returns live state from camera analytics zones",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceCameraAnalyticsOverview = {
    "name": "getDeviceCameraAnalyticsOverview",
    "description": "Returns an overview of aggregate analytics data for a timespan",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 365 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour."},
            "objectType": {"type": "string", "description": "[optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]."},
        },
        "required": ["serial"]
    }
}

getDeviceCameraAnalyticsRecent = {
    "name": "getDeviceCameraAnalyticsRecent",
    "description": "Returns most recent record for analytics zones",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "objectType": {"type": "string", "description": "[optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]."},
        },
        "required": ["serial"]
    }
}

getDeviceCameraAnalyticsZones = {
    "name": "getDeviceCameraAnalyticsZones",
    "description": "Returns all configured analytic zones for this camera",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceCameraAnalyticsZoneHistory = {
    "name": "getDeviceCameraAnalyticsZoneHistory",
    "description": "Return historical records for analytic zones",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "zoneId": {"type": "string", "description": "Zone ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 365 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 14 hours after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60."},
            "objectType": {"type": "string", "description": "[optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]."},
        },
        "required": ["serial", "zoneId"]
    }
}

getDeviceCameraCustomAnalytics = {
    "name": "getDeviceCameraCustomAnalytics",
    "description": "Return custom analytics settings for a camera",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceCameraQualityAndRetention = {
    "name": "getDeviceCameraQualityAndRetention",
    "description": "Returns quality and retention settings for the given camera",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceCameraSense = {
    "name": "getDeviceCameraSense",
    "description": "Returns sense settings for a given camera",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceCameraSenseObjectDetectionModels = {
    "name": "getDeviceCameraSenseObjectDetectionModels",
    "description": "Returns the MV Sense object detection model list for the given camera",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceCameraVideoSettings = {
    "name": "getDeviceCameraVideoSettings",
    "description": "Returns video settings for the given camera",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceCameraVideoLink = {
    "name": "getDeviceCameraVideoLink",
    "description": "Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "timestamp": {"type": "string", "description": "[optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time."},
        },
        "required": ["serial"]
    }
}

getDeviceCameraWirelessProfiles = {
    "name": "getDeviceCameraWirelessProfiles",
    "description": "Returns wireless profile assigned to the given camera",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceCellularSims = {
    "name": "getDeviceCellularSims",
    "description": "Return the SIM and APN configurations for a cellular device.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceCellularGatewayLan = {
    "name": "getDeviceCellularGatewayLan",
    "description": "Show the LAN Settings of a MG",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceCellularGatewayPortForwardingRules = {
    "name": "getDeviceCellularGatewayPortForwardingRules",
    "description": "Returns the port forwarding rules for a single MG.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceClients = {
    "name": "getDeviceClients",
    "description": "List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
        },
        "required": ["serial"]
    }
}

getDeviceLiveToolsArpTable = {
    "name": "getDeviceLiveToolsArpTable",
    "description": "Return an ARP table live tool job.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "arpTableId": {"type": "string", "description": "Arp table ID"},
        },
        "required": ["serial", "arpTableId"]
    }
}

getDeviceLiveToolsCableTest = {
    "name": "getDeviceLiveToolsCableTest",
    "description": "Return a cable test live tool job.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "id": {"type": "string", "description": "ID"},
        },
        "required": ["serial", "id"]
    }
}

getDeviceLiveToolsLedsBlink = {
    "name": "getDeviceLiveToolsLedsBlink",
    "description": "Return a blink LEDs job",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "ledsBlinkId": {"type": "string", "description": "Leds blink ID"},
        },
        "required": ["serial", "ledsBlinkId"]
    }
}

getDeviceLiveToolsPing = {
    "name": "getDeviceLiveToolsPing",
    "description": "Return a ping job. Latency unit in response is in milliseconds. Size is in bytes.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "id": {"type": "string", "description": "ID"},
        },
        "required": ["serial", "id"]
    }
}

getDeviceLiveToolsPingDevice = {
    "name": "getDeviceLiveToolsPingDevice",
    "description": "Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "id": {"type": "string", "description": "ID"},
        },
        "required": ["serial", "id"]
    }
}

getDeviceLiveToolsThroughputTest = {
    "name": "getDeviceLiveToolsThroughputTest",
    "description": "Return a throughput test job",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "throughputTestId": {"type": "string", "description": "Throughput test ID"},
        },
        "required": ["serial", "throughputTestId"]
    }
}

getDeviceLiveToolsWakeOnLan = {
    "name": "getDeviceLiveToolsWakeOnLan",
    "description": "Return a Wake-on-LAN job",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "wakeOnLanId": {"type": "string", "description": "Wake on lan ID"},
        },
        "required": ["serial", "wakeOnLanId"]
    }
}

getDeviceLldpCdp = {
    "name": "getDeviceLldpCdp",
    "description": "List LLDP and CDP information for a device",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceLossAndLatencyHistory = {
    "name": "getDeviceLossAndLatencyHistory",
    "description": "Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for MX, MG and Z devices.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 60 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60."},
            "uplink": {"type": "string", "description": "The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, wan3, cellular. The default is wan1."},
            "ip": {"type": "string", "description": "The destination IP used to obtain the requested stats. This is required."},
        },
        "required": ["serial", "ip"]
    }
}

getDeviceManagementInterface = {
    "name": "getDeviceManagementInterface",
    "description": "Return the management interface settings for a device",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceSensorCommands = {
    "name": "getDeviceSensorCommands",
    "description": "Returns a historical log of all commands",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "operations": {"type": "array", "description": "Optional parameter to filter commands by operation. Allowed values are disableDownstreamPower, enableDownstreamPower, cycleDownstreamPower, and refreshData."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "sortOrder": {"type": "string", "description": "Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'descending'."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 30 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 30 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 30 days. The default is 30 days."},
        },
        "required": ["serial"]
    }
}

getDeviceSensorCommand = {
    "name": "getDeviceSensorCommand",
    "description": "Returns information about the command's execution, including the status",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "commandId": {"type": "string", "description": "Command ID"},
        },
        "required": ["serial", "commandId"]
    }
}

getDeviceSensorRelationships = {
    "name": "getDeviceSensorRelationships",
    "description": "List the sensor roles for a given sensor or camera device.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceSwitchPorts = {
    "name": "getDeviceSwitchPorts",
    "description": "List the switch ports for a switch",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceSwitchPortsStatuses = {
    "name": "getDeviceSwitchPortsStatuses",
    "description": "Return the status for all the ports of a switch",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
        },
        "required": ["serial"]
    }
}

getDeviceSwitchPortsStatusesPackets = {
    "name": "getDeviceSwitchPortsStatusesPackets",
    "description": "Return the packet counters for all the ports of a switch",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 1 day from today."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day."},
        },
        "required": ["serial"]
    }
}

getDeviceSwitchPort = {
    "name": "getDeviceSwitchPort",
    "description": "Return a switch port",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "portId": {"type": "string", "description": "Port ID"},
        },
        "required": ["serial", "portId"]
    }
}

getDeviceSwitchRoutingInterfaces = {
    "name": "getDeviceSwitchRoutingInterfaces",
    "description": "List layer 3 interfaces for a switch. Those for a stack may be found under switch stack routing.",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceSwitchRoutingInterface = {
    "name": "getDeviceSwitchRoutingInterface",
    "description": "Return a layer 3 interface for a switch",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "interfaceId": {"type": "string", "description": "Interface ID"},
        },
        "required": ["serial", "interfaceId"]
    }
}

getDeviceSwitchRoutingInterfaceDhcp = {
    "name": "getDeviceSwitchRoutingInterfaceDhcp",
    "description": "Return a layer 3 interface DHCP configuration for a switch",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "interfaceId": {"type": "string", "description": "Interface ID"},
        },
        "required": ["serial", "interfaceId"]
    }
}

getDeviceSwitchRoutingStaticRoutes = {
    "name": "getDeviceSwitchRoutingStaticRoutes",
    "description": "List layer 3 static routes for a switch",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceSwitchRoutingStaticRoute = {
    "name": "getDeviceSwitchRoutingStaticRoute",
    "description": "Return a layer 3 static route for a switch",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "staticRouteId": {"type": "string", "description": "Static route ID"},
        },
        "required": ["serial", "staticRouteId"]
    }
}

getDeviceSwitchWarmSpare = {
    "name": "getDeviceSwitchWarmSpare",
    "description": "Return warm spare configuration for a switch",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceWirelessBluetoothSettings = {
    "name": "getDeviceWirelessBluetoothSettings",
    "description": "Return the bluetooth settings for a wireless device",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceWirelessConnectionStats = {
    "name": "getDeviceWirelessConnectionStats",
    "description": "Aggregated connectivity info for a given AP on this network",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 180 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information."},
            "ssid": {"type": "integer", "description": "Filter results by SSID"},
            "vlan": {"type": "integer", "description": "Filter results by VLAN"},
            "apTag": {"type": "string", "description": "Filter results by AP Tag"},
        },
        "required": ["serial"]
    }
}

getDeviceWirelessElectronicShelfLabel = {
    "name": "getDeviceWirelessElectronicShelfLabel",
    "description": "Return the ESL settings of a device",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceWirelessLatencyStats = {
    "name": "getDeviceWirelessLatencyStats",
    "description": "Aggregated latency info for a given AP on this network",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 180 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information."},
            "ssid": {"type": "integer", "description": "Filter results by SSID"},
            "vlan": {"type": "integer", "description": "Filter results by VLAN"},
            "apTag": {"type": "string", "description": "Filter results by AP Tag"},
            "fields": {"type": "string", "description": "Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string."},
        },
        "required": ["serial"]
    }
}

getDeviceWirelessRadioSettings = {
    "name": "getDeviceWirelessRadioSettings",
    "description": "Return the radio settings of a device",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getDeviceWirelessStatus = {
    "name": "getDeviceWirelessStatus",
    "description": "Return the SSID statuses of an access point",
    "parameters": {
        "type": "object",
        "properties": {
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["serial"]
    }
}

getNetwork = {
    "name": "getNetwork",
    "description": "Return a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkAlertsHistory = {
    "name": "getNetworkAlertsHistory",
    "description": "Return the alert history for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId"]
    }
}

getNetworkAlertsSettings = {
    "name": "getNetworkAlertsSettings",
    "description": "Return the alert configuration for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceClientSecurityEvents = {
    "name": "getNetworkApplianceClientSecurityEvents",
    "description": "List the security events for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clientId": {"type": "string", "description": "Client ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 791 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 791 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "sortOrder": {"type": "string", "description": "Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order."},
        },
        "required": ["networkId", "clientId"]
    }
}

getNetworkApplianceConnectivityMonitoringDestinations = {
    "name": "getNetworkApplianceConnectivityMonitoringDestinations",
    "description": "Return the connectivity testing destinations for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceContentFiltering = {
    "name": "getNetworkApplianceContentFiltering",
    "description": "Return the content filtering settings for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceContentFilteringCategories = {
    "name": "getNetworkApplianceContentFilteringCategories",
    "description": "List all available content filtering categories for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceFirewallCellularFirewallRules = {
    "name": "getNetworkApplianceFirewallCellularFirewallRules",
    "description": "Return the cellular firewall rules for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceFirewallFirewalledServices = {
    "name": "getNetworkApplianceFirewallFirewalledServices",
    "description": "List the appliance services and their accessibility rules",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceFirewallFirewalledService = {
    "name": "getNetworkApplianceFirewallFirewalledService",
    "description": "Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "service": {"type": "string", "description": "Service"},
        },
        "required": ["networkId", "service"]
    }
}

getNetworkApplianceFirewallInboundCellularFirewallRules = {
    "name": "getNetworkApplianceFirewallInboundCellularFirewallRules",
    "description": "Return the inbound cellular firewall rules for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceFirewallInboundFirewallRules = {
    "name": "getNetworkApplianceFirewallInboundFirewallRules",
    "description": "Return the inbound firewall rules for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceFirewallL3FirewallRules = {
    "name": "getNetworkApplianceFirewallL3FirewallRules",
    "description": "Return the L3 firewall rules for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceFirewallL7FirewallRules = {
    "name": "getNetworkApplianceFirewallL7FirewallRules",
    "description": "List the MX L7 firewall rules for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceFirewallL7FirewallRulesApplicationCategories = {
    "name": "getNetworkApplianceFirewallL7FirewallRulesApplicationCategories",
    "description": "Return the L7 firewall application categories and their associated applications for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceFirewallOneToManyNatRules = {
    "name": "getNetworkApplianceFirewallOneToManyNatRules",
    "description": "Return the 1:Many NAT mapping rules for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceFirewallOneToOneNatRules = {
    "name": "getNetworkApplianceFirewallOneToOneNatRules",
    "description": "Return the 1:1 NAT mapping rules for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceFirewallPortForwardingRules = {
    "name": "getNetworkApplianceFirewallPortForwardingRules",
    "description": "Return the port forwarding rules for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceFirewallSettings = {
    "name": "getNetworkApplianceFirewallSettings",
    "description": "Return the firewall settings for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkAppliancePorts = {
    "name": "getNetworkAppliancePorts",
    "description": "List per-port VLAN settings for all ports of a MX.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkAppliancePort = {
    "name": "getNetworkAppliancePort",
    "description": "Return per-port VLAN settings for a single MX port.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "portId": {"type": "string", "description": "Port ID"},
        },
        "required": ["networkId", "portId"]
    }
}

getNetworkAppliancePrefixesDelegatedStatics = {
    "name": "getNetworkAppliancePrefixesDelegatedStatics",
    "description": "List static delegated prefixes for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkAppliancePrefixesDelegatedStatic = {
    "name": "getNetworkAppliancePrefixesDelegatedStatic",
    "description": "Return a static delegated prefix from a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "staticDelegatedPrefixId": {"type": "string", "description": "Static delegated prefix ID"},
        },
        "required": ["networkId", "staticDelegatedPrefixId"]
    }
}

getNetworkApplianceRfProfiles = {
    "name": "getNetworkApplianceRfProfiles",
    "description": "List the RF profiles for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceRfProfile = {
    "name": "getNetworkApplianceRfProfile",
    "description": "Return a RF profile",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "rfProfileId": {"type": "string", "description": "Rf profile ID"},
        },
        "required": ["networkId", "rfProfileId"]
    }
}

getNetworkApplianceSecurityEvents = {
    "name": "getNetworkApplianceSecurityEvents",
    "description": "List the security events for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 365 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "sortOrder": {"type": "string", "description": "Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order."},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceSecurityIntrusion = {
    "name": "getNetworkApplianceSecurityIntrusion",
    "description": "Returns all supported intrusion settings for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceSecurityMalware = {
    "name": "getNetworkApplianceSecurityMalware",
    "description": "Returns all supported malware settings for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceSettings = {
    "name": "getNetworkApplianceSettings",
    "description": "Return the appliance settings for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceSingleLan = {
    "name": "getNetworkApplianceSingleLan",
    "description": "Return single LAN configuration",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceSsids = {
    "name": "getNetworkApplianceSsids",
    "description": "List the MX SSIDs in a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceSsid = {
    "name": "getNetworkApplianceSsid",
    "description": "Return a single MX SSID",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkApplianceStaticRoutes = {
    "name": "getNetworkApplianceStaticRoutes",
    "description": "List the static routes for an MX or teleworker network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceStaticRoute = {
    "name": "getNetworkApplianceStaticRoute",
    "description": "Return a static route for an MX or teleworker network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "staticRouteId": {"type": "string", "description": "Static route ID"},
        },
        "required": ["networkId", "staticRouteId"]
    }
}

getNetworkApplianceTrafficShaping = {
    "name": "getNetworkApplianceTrafficShaping",
    "description": "Display the traffic shaping settings for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceTrafficShapingCustomPerformanceClasses = {
    "name": "getNetworkApplianceTrafficShapingCustomPerformanceClasses",
    "description": "List all custom performance classes for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceTrafficShapingCustomPerformanceClass = {
    "name": "getNetworkApplianceTrafficShapingCustomPerformanceClass",
    "description": "Return a custom performance class for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "customPerformanceClassId": {"type": "string", "description": "Custom performance class ID"},
        },
        "required": ["networkId", "customPerformanceClassId"]
    }
}

getNetworkApplianceTrafficShapingRules = {
    "name": "getNetworkApplianceTrafficShapingRules",
    "description": "Display the traffic shaping settings rules for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceTrafficShapingUplinkBandwidth = {
    "name": "getNetworkApplianceTrafficShapingUplinkBandwidth",
    "description": "Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device's hardware capabilities.  For more information on your device's hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceTrafficShapingUplinkSelection = {
    "name": "getNetworkApplianceTrafficShapingUplinkSelection",
    "description": "Show uplink selection settings for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceUplinksUsageHistory = {
    "name": "getNetworkApplianceUplinksUsageHistory",
    "description": "Get the sent and received bytes for each uplink of a network.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 365 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60."},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceVlans = {
    "name": "getNetworkApplianceVlans",
    "description": "List the VLANs for an MX network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceVlansSettings = {
    "name": "getNetworkApplianceVlansSettings",
    "description": "Returns the enabled status of VLANs for the network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceVlan = {
    "name": "getNetworkApplianceVlan",
    "description": "Return a VLAN",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "vlanId": {"type": "string", "description": "Vlan ID"},
        },
        "required": ["networkId", "vlanId"]
    }
}

getNetworkApplianceVpnBgp = {
    "name": "getNetworkApplianceVpnBgp",
    "description": "Return a Hub BGP Configuration",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceVpnSiteToSiteVpn = {
    "name": "getNetworkApplianceVpnSiteToSiteVpn",
    "description": "Return the site-to-site VPN settings of a network. Only valid for MX networks.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkApplianceWarmSpare = {
    "name": "getNetworkApplianceWarmSpare",
    "description": "Return MX warm spare settings",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkBluetoothClients = {
    "name": "getNetworkBluetoothClients",
    "description": "List the Bluetooth clients seen by APs in this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 7 days from today."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "includeConnectivityHistory": {"type": "boolean", "description": "Include the connectivity history for this client"},
        },
        "required": ["networkId"]
    }
}

getNetworkBluetoothClient = {
    "name": "getNetworkBluetoothClient",
    "description": "Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "bluetoothClientId": {"type": "string", "description": "Bluetooth client ID"},
            "includeConnectivityHistory": {"type": "boolean", "description": "Include the connectivity history for this client"},
            "connectivityHistoryTimespan": {"type": "integer", "description": "The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used."},
        },
        "required": ["networkId", "bluetoothClientId"]
    }
}

getNetworkCameraQualityRetentionProfiles = {
    "name": "getNetworkCameraQualityRetentionProfiles",
    "description": "List the quality retention profiles for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkCameraQualityRetentionProfile = {
    "name": "getNetworkCameraQualityRetentionProfile",
    "description": "Retrieve a single quality retention profile",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "qualityRetentionProfileId": {"type": "string", "description": "Quality retention profile ID"},
        },
        "required": ["networkId", "qualityRetentionProfileId"]
    }
}

getNetworkCameraSchedules = {
    "name": "getNetworkCameraSchedules",
    "description": "Returns a list of all camera recording schedules.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkCameraWirelessProfiles = {
    "name": "getNetworkCameraWirelessProfiles",
    "description": "List the camera wireless profiles for this network.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkCameraWirelessProfile = {
    "name": "getNetworkCameraWirelessProfile",
    "description": "Retrieve a single camera wireless profile.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "wirelessProfileId": {"type": "string", "description": "Wireless profile ID"},
        },
        "required": ["networkId", "wirelessProfileId"]
    }
}

getNetworkCellularGatewayConnectivityMonitoringDestinations = {
    "name": "getNetworkCellularGatewayConnectivityMonitoringDestinations",
    "description": "Return the connectivity testing destinations for an MG network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkCellularGatewayDhcp = {
    "name": "getNetworkCellularGatewayDhcp",
    "description": "List common DHCP settings of MGs",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkCellularGatewaySubnetPool = {
    "name": "getNetworkCellularGatewaySubnetPool",
    "description": "Return the subnet pool and mask configured for MGs in the network.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkCellularGatewayUplink = {
    "name": "getNetworkCellularGatewayUplink",
    "description": "Returns the uplink settings for your MG network.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkClients = {
    "name": "getNetworkClients",
    "description": "List the clients that have used this network in the timespan. The data is updated at most once every five minutes.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 5000. Default is 10."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "statuses": {"type": "array", "description": "Filters clients based on status. Can be one of 'Online' or 'Offline'."},
            "ip": {"type": "string", "description": "Filters clients based on a partial or full match for the ip address field."},
            "ip6": {"type": "string", "description": "Filters clients based on a partial or full match for the ip6 address field."},
            "ip6Local": {"type": "string", "description": "Filters clients based on a partial or full match for the ip6Local address field."},
            "mac": {"type": "string", "description": "Filters clients based on a partial or full match for the mac address field."},
            "os": {"type": "string", "description": "Filters clients based on a partial or full match for the os (operating system) field."},
            "pskGroup": {"type": "string", "description": "Filters clients based on partial or full match for the iPSK name field."},
            "description": {"type": "string", "description": "Filters clients based on a partial or full match for the description field."},
            "vlan": {"type": "string", "description": "Filters clients based on the full match for the VLAN field."},
            "namedVlan": {"type": "string", "description": "Filters clients based on the partial or full match for the named VLAN field."},
            "recentDeviceConnections": {"type": "array", "description": "Filters clients based on recent connection type. Can be one of 'Wired' or 'Wireless'."},
        },
        "required": ["networkId"]
    }
}

getNetworkClientsApplicationUsage = {
    "name": "getNetworkClientsApplicationUsage",
    "description": "Return the application usage data for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clients": {"type": "string", "description": "A list of client keys, MACs or IPs separated by comma."},
            "ssidNumber": {"type": "integer", "description": "An SSID number to include. If not specified, eveusage histories application usagents for all SSIDs will be returned."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
        },
        "required": ["networkId", "clients"]
    }
}

getNetworkClientsBandwidthUsageHistory = {
    "name": "getNetworkClientsBandwidthUsageHistory",
    "description": "Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 30 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId"]
    }
}

getNetworkClientsOverview = {
    "name": "getNetworkClientsOverview",
    "description": "Return overview statistics for network clients",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 7200, 86400, 604800, 2592000. The default is 604800."},
        },
        "required": ["networkId"]
    }
}

getNetworkClientsUsageHistories = {
    "name": "getNetworkClientsUsageHistories",
    "description": "Return the usage histories for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clients": {"type": "string", "description": "A list of client keys, MACs or IPs separated by comma."},
            "ssidNumber": {"type": "integer", "description": "An SSID number to include. If not specified, events for all SSIDs will be returned."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
        },
        "required": ["networkId", "clients"]
    }
}

getNetworkClient = {
    "name": "getNetworkClient",
    "description": "Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clientId": {"type": "string", "description": "Client ID"},
        },
        "required": ["networkId", "clientId"]
    }
}

getNetworkClientPolicy = {
    "name": "getNetworkClientPolicy",
    "description": "Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clientId": {"type": "string", "description": "Client ID"},
        },
        "required": ["networkId", "clientId"]
    }
}

getNetworkClientSplashAuthorizationStatus = {
    "name": "getNetworkClientSplashAuthorizationStatus",
    "description": "Return the splash authorization for a client, for each SSID they've associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clientId": {"type": "string", "description": "Client ID"},
        },
        "required": ["networkId", "clientId"]
    }
}

getNetworkClientTrafficHistory = {
    "name": "getNetworkClientTrafficHistory",
    "description": "Return the client's network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide > General page. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clientId": {"type": "string", "description": "Client ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId", "clientId"]
    }
}

getNetworkClientUsageHistory = {
    "name": "getNetworkClientUsageHistory",
    "description": "Return the client's daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clientId": {"type": "string", "description": "Client ID"},
        },
        "required": ["networkId", "clientId"]
    }
}

getNetworkDevices = {
    "name": "getNetworkDevices",
    "description": "List the devices in a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkEvents = {
    "name": "getNetworkEvents",
    "description": "List the events for the network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "productType": {"type": "string", "description": "The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, wirelessController, and secureConnect"},
            "includedEventTypes": {"type": "array", "description": "A list of event types. The returned events will be filtered to only include events with these types."},
            "excludedEventTypes": {"type": "array", "description": "A list of event types. The returned events will be filtered to exclude events with these types."},
            "deviceMac": {"type": "string", "description": "The MAC address of the Meraki device which the list of events will be filtered with"},
            "deviceSerial": {"type": "string", "description": "The serial of the Meraki device which the list of events will be filtered with"},
            "deviceName": {"type": "string", "description": "The name of the Meraki device which the list of events will be filtered with"},
            "clientIp": {"type": "string", "description": "The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks."},
            "clientMac": {"type": "string", "description": "The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks."},
            "clientName": {"type": "string", "description": "The name, or partial name, of the client which the list of events will be filtered with"},
            "smDeviceMac": {"type": "string", "description": "The MAC address of the Systems Manager device which the list of events will be filtered with"},
            "smDeviceName": {"type": "string", "description": "The name of the Systems Manager device which the list of events will be filtered with"},
            "eventDetails": {"type": "string", "description": "The details of the event(Catalyst device only) which the list of events will be filtered with"},
            "eventSeverity": {"type": "string", "description": "The severity of the event(Catalyst device only) which the list of events will be filtered with"},
            "isCatalyst": {"type": "boolean", "description": "Boolean indicating that whether it is a Catalyst device. For Catalyst device, eventDetails and eventSeverity can be used to filter events."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId"]
    }
}

getNetworkEventsEventTypes = {
    "name": "getNetworkEventsEventTypes",
    "description": "List the event type to human-readable description",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkFirmwareUpgrades = {
    "name": "getNetworkFirmwareUpgrades",
    "description": "Get firmware upgrade information for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkFirmwareUpgradesStagedEvents = {
    "name": "getNetworkFirmwareUpgradesStagedEvents",
    "description": "Get the Staged Upgrade Event from a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkFirmwareUpgradesStagedGroups = {
    "name": "getNetworkFirmwareUpgradesStagedGroups",
    "description": "List of Staged Upgrade Groups in a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkFirmwareUpgradesStagedGroup = {
    "name": "getNetworkFirmwareUpgradesStagedGroup",
    "description": "Get a Staged Upgrade Group from a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "groupId": {"type": "string", "description": "Group ID"},
        },
        "required": ["networkId", "groupId"]
    }
}

getNetworkFirmwareUpgradesStagedStages = {
    "name": "getNetworkFirmwareUpgradesStagedStages",
    "description": "Order of Staged Upgrade Groups in a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkFloorPlans = {
    "name": "getNetworkFloorPlans",
    "description": "List the floor plans that belong to your network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkFloorPlan = {
    "name": "getNetworkFloorPlan",
    "description": "Find a floor plan by ID",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "floorPlanId": {"type": "string", "description": "Floor plan ID"},
        },
        "required": ["networkId", "floorPlanId"]
    }
}

getNetworkGroupPolicies = {
    "name": "getNetworkGroupPolicies",
    "description": "List the group policies in a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkGroupPolicy = {
    "name": "getNetworkGroupPolicy",
    "description": "Display a group policy",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "groupPolicyId": {"type": "string", "description": "Group policy ID"},
        },
        "required": ["networkId", "groupPolicyId"]
    }
}

getNetworkHealthAlerts = {
    "name": "getNetworkHealthAlerts",
    "description": "Return all global alerts on this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkInsightApplicationHealthByTime = {
    "name": "getNetworkInsightApplicationHealthByTime",
    "description": "Get application health by time",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "applicationId": {"type": "string", "description": "Application ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 7 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 3600, 86400. The default is 300."},
        },
        "required": ["networkId", "applicationId"]
    }
}

getNetworkMerakiAuthUsers = {
    "name": "getNetworkMerakiAuthUsers",
    "description": "List the authorized users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a MX network)",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkMerakiAuthUser = {
    "name": "getNetworkMerakiAuthUser",
    "description": "Return the Meraki Auth splash guest, RADIUS, or client VPN user",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "merakiAuthUserId": {"type": "string", "description": "Meraki auth user ID"},
        },
        "required": ["networkId", "merakiAuthUserId"]
    }
}

getNetworkMqttBrokers = {
    "name": "getNetworkMqttBrokers",
    "description": "List the MQTT brokers for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkMqttBroker = {
    "name": "getNetworkMqttBroker",
    "description": "Return an MQTT broker",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "mqttBrokerId": {"type": "string", "description": "Mqtt broker ID"},
        },
        "required": ["networkId", "mqttBrokerId"]
    }
}

getNetworkNetflow = {
    "name": "getNetworkNetflow",
    "description": "Return the NetFlow traffic reporting settings for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkNetworkHealthChannelUtilization = {
    "name": "getNetworkNetworkHealthChannelUtilization",
    "description": "Get the channel utilization over each radio for all APs in a network.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 600. The default is 600."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 100. Default is 10."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId"]
    }
}

getNetworkPiiPiiKeys = {
    "name": "getNetworkPiiPiiKeys",
    "description": "List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key \"0\" containing the applicable keys.  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/piiKeys ```",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "username": {"type": "string", "description": "The username of a Systems Manager user"},
            "email": {"type": "string", "description": "The email of a network user account or a Systems Manager device"},
            "mac": {"type": "string", "description": "The MAC of a network client device or a Systems Manager device"},
            "serial": {"type": "string", "description": "The serial of a Systems Manager device"},
            "imei": {"type": "string", "description": "The IMEI of a Systems Manager device"},
            "bluetoothMac": {"type": "string", "description": "The MAC of a Bluetooth client"},
        },
        "required": ["networkId"]
    }
}

getNetworkPiiRequests = {
    "name": "getNetworkPiiRequests",
    "description": "List the PII requests for this network or organization  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/requests ```",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkPiiRequest = {
    "name": "getNetworkPiiRequest",
    "description": "Return a PII request  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/requests/{requestId} ```",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "requestId": {"type": "string", "description": "Request ID"},
        },
        "required": ["networkId", "requestId"]
    }
}

getNetworkPiiSmDevicesForKey = {
    "name": "getNetworkPiiSmDevicesForKey",
    "description": "Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/smDevicesForKey ```",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "username": {"type": "string", "description": "The username of a Systems Manager user"},
            "email": {"type": "string", "description": "The email of a network user account or a Systems Manager device"},
            "mac": {"type": "string", "description": "The MAC of a network client device or a Systems Manager device"},
            "serial": {"type": "string", "description": "The serial of a Systems Manager device"},
            "imei": {"type": "string", "description": "The IMEI of a Systems Manager device"},
            "bluetoothMac": {"type": "string", "description": "The MAC of a Bluetooth client"},
        },
        "required": ["networkId"]
    }
}

getNetworkPiiSmOwnersForKey = {
    "name": "getNetworkPiiSmOwnersForKey",
    "description": "Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/smOwnersForKey ```",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "username": {"type": "string", "description": "The username of a Systems Manager user"},
            "email": {"type": "string", "description": "The email of a network user account or a Systems Manager device"},
            "mac": {"type": "string", "description": "The MAC of a network client device or a Systems Manager device"},
            "serial": {"type": "string", "description": "The serial of a Systems Manager device"},
            "imei": {"type": "string", "description": "The IMEI of a Systems Manager device"},
            "bluetoothMac": {"type": "string", "description": "The MAC of a Bluetooth client"},
        },
        "required": ["networkId"]
    }
}

getNetworkPoliciesByClient = {
    "name": "getNetworkPoliciesByClient",
    "description": "Get policies for all clients with policies",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
        },
        "required": ["networkId"]
    }
}

getNetworkSensorAlertsCurrentOverviewByMetric = {
    "name": "getNetworkSensorAlertsCurrentOverviewByMetric",
    "description": "Return an overview of currently alerting sensors by metric",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSensorAlertsOverviewByMetric = {
    "name": "getNetworkSensorAlertsOverviewByMetric",
    "description": "Return an overview of alert occurrences over a timespan, by metric",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 731 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 366 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 366 days. The default is 7 days. If interval is provided, the timespan will be autocalculated."},
            "interval": {"type": "integer", "description": "The time interval in seconds for returned data. The valid intervals are: 900, 3600, 86400, 604800, 2592000. The default is 604800. Interval is calculated if time params are provided."},
        },
        "required": ["networkId"]
    }
}

getNetworkSensorAlertsProfiles = {
    "name": "getNetworkSensorAlertsProfiles",
    "description": "Lists all sensor alert profiles for a network.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSensorAlertsProfile = {
    "name": "getNetworkSensorAlertsProfile",
    "description": "Show details of a sensor alert profile for a network.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "id": {"type": "string", "description": "ID"},
        },
        "required": ["networkId", "id"]
    }
}

getNetworkSensorMqttBrokers = {
    "name": "getNetworkSensorMqttBrokers",
    "description": "List the sensor settings of all MQTT brokers for this network. To get the brokers themselves, use /networks/{networkId}/mqttBrokers.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSensorMqttBroker = {
    "name": "getNetworkSensorMqttBroker",
    "description": "Return the sensor settings of an MQTT broker. To get the broker itself, use /networks/{networkId}/mqttBrokers/{mqttBrokerId}.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "mqttBrokerId": {"type": "string", "description": "Mqtt broker ID"},
        },
        "required": ["networkId", "mqttBrokerId"]
    }
}

getNetworkSensorRelationships = {
    "name": "getNetworkSensorRelationships",
    "description": "List the sensor roles for devices in a given network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSettings = {
    "name": "getNetworkSettings",
    "description": "Return the settings for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSmBypassActivationLockAttempt = {
    "name": "getNetworkSmBypassActivationLockAttempt",
    "description": "Bypass activation lock attempt status",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "attemptId": {"type": "string", "description": "Attempt ID"},
        },
        "required": ["networkId", "attemptId"]
    }
}

getNetworkSmDevices = {
    "name": "getNetworkSmDevices",
    "description": "List the devices enrolled in an SM network with various specified fields and filters",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "fields": {"type": "array", "description": "Additional fields that will be displayed for each device.     The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,     systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,     ownerEmail, ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,     simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,     isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,     hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, androidSecurityPatchVersion, cellular, and url."},
            "wifiMacs": {"type": "array", "description": "Filter devices by wifi mac(s)."},
            "serials": {"type": "array", "description": "Filter devices by serial(s)."},
            "ids": {"type": "array", "description": "Filter devices by id(s)."},
            "uuids": {"type": "array", "description": "Filter devices by uuid(s)."},
            "systemTypes": {"type": "array", "description": "Filter devices by system type(s)."},
            "scope": {"type": "array", "description": "Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId"]
    }
}

getNetworkSmDeviceCellularUsageHistory = {
    "name": "getNetworkSmDeviceCellularUsageHistory",
    "description": "Return the client's daily cellular data usage history. Usage data is in kilobytes.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmDeviceCerts = {
    "name": "getNetworkSmDeviceCerts",
    "description": "List the certs on a device",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmDeviceConnectivity = {
    "name": "getNetworkSmDeviceConnectivity",
    "description": "Returns historical connectivity data (whether a device is regularly checking in to Dashboard).",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmDeviceDesktopLogs = {
    "name": "getNetworkSmDeviceDesktopLogs",
    "description": "Return historical records of various Systems Manager network connection details for desktop devices.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmDeviceDeviceCommandLogs = {
    "name": "getNetworkSmDeviceDeviceCommandLogs",
    "description": "Return historical records of commands sent to Systems Manager devices. Note that this will include the name of the Dashboard user who initiated the command if it was generated by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out of any reports.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmDeviceDeviceProfiles = {
    "name": "getNetworkSmDeviceDeviceProfiles",
    "description": "Get the installed profiles associated with a device",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmDeviceNetworkAdapters = {
    "name": "getNetworkSmDeviceNetworkAdapters",
    "description": "List the network adapters of a device",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmDevicePerformanceHistory = {
    "name": "getNetworkSmDevicePerformanceHistory",
    "description": "Return historical records of various Systems Manager client metrics for desktop devices.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmDeviceRestrictions = {
    "name": "getNetworkSmDeviceRestrictions",
    "description": "List the restrictions on a device",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmDeviceSecurityCenters = {
    "name": "getNetworkSmDeviceSecurityCenters",
    "description": "List the security centers on a device",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmDeviceSoftwares = {
    "name": "getNetworkSmDeviceSoftwares",
    "description": "Get a list of softwares associated with a device",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmDeviceWlanLists = {
    "name": "getNetworkSmDeviceWlanLists",
    "description": "List the saved SSID names on a device",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "deviceId": {"type": "string", "description": "Device ID"},
        },
        "required": ["networkId", "deviceId"]
    }
}

getNetworkSmProfiles = {
    "name": "getNetworkSmProfiles",
    "description": "List all profiles in a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "payloadTypes": {"type": "array", "description": "Filter by payload types"},
        },
        "required": ["networkId"]
    }
}

getNetworkSmTargetGroups = {
    "name": "getNetworkSmTargetGroups",
    "description": "List the target groups in this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "withDetails": {"type": "boolean", "description": "Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response"},
        },
        "required": ["networkId"]
    }
}

getNetworkSmTargetGroup = {
    "name": "getNetworkSmTargetGroup",
    "description": "Return a target group",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "targetGroupId": {"type": "string", "description": "Target group ID"},
            "withDetails": {"type": "boolean", "description": "Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response"},
        },
        "required": ["networkId", "targetGroupId"]
    }
}

getNetworkSmTrustedAccessConfigs = {
    "name": "getNetworkSmTrustedAccessConfigs",
    "description": "List Trusted Access Configs",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId"]
    }
}

getNetworkSmUserAccessDevices = {
    "name": "getNetworkSmUserAccessDevices",
    "description": "List User Access Devices and its Trusted Access Connections",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId"]
    }
}

getNetworkSmUsers = {
    "name": "getNetworkSmUsers",
    "description": "List the owners in an SM network with various specified fields and filters",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "ids": {"type": "array", "description": "Filter users by id(s)."},
            "usernames": {"type": "array", "description": "Filter users by username(s)."},
            "emails": {"type": "array", "description": "Filter users by email(s)."},
            "scope": {"type": "array", "description": "Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags."},
        },
        "required": ["networkId"]
    }
}

getNetworkSmUserDeviceProfiles = {
    "name": "getNetworkSmUserDeviceProfiles",
    "description": "Get the profiles associated with a user",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "userId": {"type": "string", "description": "User ID"},
        },
        "required": ["networkId", "userId"]
    }
}

getNetworkSmUserSoftwares = {
    "name": "getNetworkSmUserSoftwares",
    "description": "Get a list of softwares associated with a user",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "userId": {"type": "string", "description": "User ID"},
        },
        "required": ["networkId", "userId"]
    }
}

getNetworkSnmp = {
    "name": "getNetworkSnmp",
    "description": "Return the SNMP settings for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSplashLoginAttempts = {
    "name": "getNetworkSplashLoginAttempts",
    "description": "List the splash login attempts for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "ssidNumber": {"type": "integer", "description": "Only return the login attempts for the specified SSID"},
            "loginIdentifier": {"type": "string", "description": "The username, email, or phone number used during login"},
            "timespan": {"type": "integer", "description": "The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchAccessControlLists = {
    "name": "getNetworkSwitchAccessControlLists",
    "description": "Return the access control lists for a MS network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchAccessPolicies = {
    "name": "getNetworkSwitchAccessPolicies",
    "description": "List the access policies for a switch network. Only returns access policies with 'my RADIUS server' as authentication method",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchAccessPolicy = {
    "name": "getNetworkSwitchAccessPolicy",
    "description": "Return a specific access policy for a switch network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "accessPolicyNumber": {"type": "string", "description": "Access policy number"},
        },
        "required": ["networkId", "accessPolicyNumber"]
    }
}

getNetworkSwitchAlternateManagementInterface = {
    "name": "getNetworkSwitchAlternateManagementInterface",
    "description": "Return the switch alternate management interface for the network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchDhcpV4ServersSeen = {
    "name": "getNetworkSwitchDhcpV4ServersSeen",
    "description": "Return the network's DHCPv4 servers seen within the selected timeframe (default 1 day)",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchDhcpServerPolicy = {
    "name": "getNetworkSwitchDhcpServerPolicy",
    "description": "Return the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers = {
    "name": "getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers",
    "description": "Return the list of servers trusted by Dynamic ARP Inspection on this network. These are also known as allow listed snoop entries",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice = {
    "name": "getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice",
    "description": "Return the devices that have a Dynamic ARP Inspection warning and their warnings",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchDscpToCosMappings = {
    "name": "getNetworkSwitchDscpToCosMappings",
    "description": "Return the DSCP to CoS mappings",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchLinkAggregations = {
    "name": "getNetworkSwitchLinkAggregations",
    "description": "List link aggregation groups",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchMtu = {
    "name": "getNetworkSwitchMtu",
    "description": "Return the MTU configuration",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchPortSchedules = {
    "name": "getNetworkSwitchPortSchedules",
    "description": "List switch port schedules",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchQosRules = {
    "name": "getNetworkSwitchQosRules",
    "description": "List quality of service rules",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchQosRulesOrder = {
    "name": "getNetworkSwitchQosRulesOrder",
    "description": "Return the quality of service rule IDs by order in which they will be processed by the switch",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchQosRule = {
    "name": "getNetworkSwitchQosRule",
    "description": "Return a quality of service rule",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "qosRuleId": {"type": "string", "description": "Qos rule ID"},
        },
        "required": ["networkId", "qosRuleId"]
    }
}

getNetworkSwitchRoutingMulticast = {
    "name": "getNetworkSwitchRoutingMulticast",
    "description": "Return multicast settings for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchRoutingMulticastRendezvousPoints = {
    "name": "getNetworkSwitchRoutingMulticastRendezvousPoints",
    "description": "List multicast rendezvous points",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchRoutingMulticastRendezvousPoint = {
    "name": "getNetworkSwitchRoutingMulticastRendezvousPoint",
    "description": "Return a multicast rendezvous point",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "rendezvousPointId": {"type": "string", "description": "Rendezvous point ID"},
        },
        "required": ["networkId", "rendezvousPointId"]
    }
}

getNetworkSwitchRoutingOspf = {
    "name": "getNetworkSwitchRoutingOspf",
    "description": "Return layer 3 OSPF routing configuration",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchSettings = {
    "name": "getNetworkSwitchSettings",
    "description": "Returns the switch network settings",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchStacks = {
    "name": "getNetworkSwitchStacks",
    "description": "List the switch stacks in a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchStack = {
    "name": "getNetworkSwitchStack",
    "description": "Show a switch stack",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "switchStackId": {"type": "string", "description": "Switch stack ID"},
        },
        "required": ["networkId", "switchStackId"]
    }
}

getNetworkSwitchStackRoutingInterfaces = {
    "name": "getNetworkSwitchStackRoutingInterfaces",
    "description": "List layer 3 interfaces for a switch stack",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "switchStackId": {"type": "string", "description": "Switch stack ID"},
        },
        "required": ["networkId", "switchStackId"]
    }
}

getNetworkSwitchStackRoutingInterface = {
    "name": "getNetworkSwitchStackRoutingInterface",
    "description": "Return a layer 3 interface from a switch stack",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "switchStackId": {"type": "string", "description": "Switch stack ID"},
            "interfaceId": {"type": "string", "description": "Interface ID"},
        },
        "required": ["networkId", "switchStackId", "interfaceId"]
    }
}

getNetworkSwitchStackRoutingInterfaceDhcp = {
    "name": "getNetworkSwitchStackRoutingInterfaceDhcp",
    "description": "Return a layer 3 interface DHCP configuration for a switch stack",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "switchStackId": {"type": "string", "description": "Switch stack ID"},
            "interfaceId": {"type": "string", "description": "Interface ID"},
        },
        "required": ["networkId", "switchStackId", "interfaceId"]
    }
}

getNetworkSwitchStackRoutingStaticRoutes = {
    "name": "getNetworkSwitchStackRoutingStaticRoutes",
    "description": "List layer 3 static routes for a switch stack",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "switchStackId": {"type": "string", "description": "Switch stack ID"},
        },
        "required": ["networkId", "switchStackId"]
    }
}

getNetworkSwitchStackRoutingStaticRoute = {
    "name": "getNetworkSwitchStackRoutingStaticRoute",
    "description": "Return a layer 3 static route for a switch stack",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "switchStackId": {"type": "string", "description": "Switch stack ID"},
            "staticRouteId": {"type": "string", "description": "Static route ID"},
        },
        "required": ["networkId", "switchStackId", "staticRouteId"]
    }
}

getNetworkSwitchStormControl = {
    "name": "getNetworkSwitchStormControl",
    "description": "Return the storm control configuration for a switch network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSwitchStp = {
    "name": "getNetworkSwitchStp",
    "description": "Returns STP settings",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkSyslogServers = {
    "name": "getNetworkSyslogServers",
    "description": "List the syslog servers for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkTopologyLinkLayer = {
    "name": "getNetworkTopologyLinkLayer",
    "description": "List the LLDP and CDP information for all discovered devices and connections in a network. At least one MX or MS device must be in the network in order to build the topology.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkTraffic = {
    "name": "getNetworkTraffic",
    "description": "Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 30 days from today."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days."},
            "deviceType": {"type": "string", "description": "Filter the data by device type: 'combined', 'wireless', 'switch' or 'appliance'. Defaults to 'combined'. When using 'combined', for each rule the data will come from the device type with the most usage."},
        },
        "required": ["networkId"]
    }
}

getNetworkTrafficAnalysis = {
    "name": "getNetworkTrafficAnalysis",
    "description": "Return the traffic analysis settings for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkTrafficShapingApplicationCategories = {
    "name": "getNetworkTrafficShapingApplicationCategories",
    "description": "Returns the application categories for traffic shaping rules. Only applicable on networks with a security applicance.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkTrafficShapingDscpTaggingOptions = {
    "name": "getNetworkTrafficShapingDscpTaggingOptions",
    "description": "Returns the available DSCP tagging options for your traffic shaping rules.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkVlanProfiles = {
    "name": "getNetworkVlanProfiles",
    "description": "List VLAN profiles for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkVlanProfilesAssignmentsByDevice = {
    "name": "getNetworkVlanProfilesAssignmentsByDevice",
    "description": "Get the assigned VLAN Profiles for devices in a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "serials": {"type": "array", "description": "Optional parameter to filter devices by serials. All devices returned belong to serial numbers that are an exact match."},
            "productTypes": {"type": "array", "description": "Optional parameter to filter devices by product types."},
            "stackIds": {"type": "array", "description": "Optional parameter to filter devices by Switch Stack ids."},
        },
        "required": ["networkId"]
    }
}

getNetworkVlanProfile = {
    "name": "getNetworkVlanProfile",
    "description": "Get an existing VLAN profile of a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "iname": {"type": "string", "description": "Iname"},
        },
        "required": ["networkId", "iname"]
    }
}

getNetworkWebhooksHttpServers = {
    "name": "getNetworkWebhooksHttpServers",
    "description": "List the HTTP servers for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkWebhooksHttpServer = {
    "name": "getNetworkWebhooksHttpServer",
    "description": "Return an HTTP server for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "httpServerId": {"type": "string", "description": "Http server ID"},
        },
        "required": ["networkId", "httpServerId"]
    }
}

getNetworkWebhooksPayloadTemplates = {
    "name": "getNetworkWebhooksPayloadTemplates",
    "description": "List the webhook payload templates for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkWebhooksPayloadTemplate = {
    "name": "getNetworkWebhooksPayloadTemplate",
    "description": "Get the webhook payload template for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "payloadTemplateId": {"type": "string", "description": "Payload template ID"},
        },
        "required": ["networkId", "payloadTemplateId"]
    }
}

getNetworkWebhooksWebhookTest = {
    "name": "getNetworkWebhooksWebhookTest",
    "description": "Return the status of a webhook test for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "webhookTestId": {"type": "string", "description": "Webhook test ID"},
        },
        "required": ["networkId", "webhookTestId"]
    }
}

getNetworkWirelessAirMarshal = {
    "name": "getNetworkWirelessAirMarshal",
    "description": "List Air Marshal scan results from a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days."},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessAlternateManagementInterface = {
    "name": "getNetworkWirelessAlternateManagementInterface",
    "description": "Return alternate management interface and devices with IP assigned",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessBilling = {
    "name": "getNetworkWirelessBilling",
    "description": "Return the billing settings of this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessBluetoothSettings = {
    "name": "getNetworkWirelessBluetoothSettings",
    "description": "Return the Bluetooth settings for a network. <a href=\"https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\">Bluetooth settings</a> must be enabled on the network.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessChannelUtilizationHistory = {
    "name": "getNetworkWirelessChannelUtilizationHistory",
    "description": "Return AP channel utilization over time for a device or network client",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400."},
            "autoResolution": {"type": "boolean", "description": "Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false."},
            "clientId": {"type": "string", "description": "Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client's connection history."},
            "deviceSerial": {"type": "string", "description": "Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified."},
            "apTag": {"type": "string", "description": "Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6')."},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessClientCountHistory = {
    "name": "getNetworkWirelessClientCountHistory",
    "description": "Return wireless client counts over time for a network, device, or network client",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400."},
            "autoResolution": {"type": "boolean", "description": "Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false."},
            "clientId": {"type": "string", "description": "Filter results by network client to return per-device client counts over time inner joined by the queried client's connection history."},
            "deviceSerial": {"type": "string", "description": "Filter results by device."},
            "apTag": {"type": "string", "description": "Filter results by AP tag."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6')."},
            "ssid": {"type": "integer", "description": "Filter results by SSID number."},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessClientsConnectionStats = {
    "name": "getNetworkWirelessClientsConnectionStats",
    "description": "Aggregated connectivity info for this network, grouped by clients",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 180 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information."},
            "ssid": {"type": "integer", "description": "Filter results by SSID"},
            "vlan": {"type": "integer", "description": "Filter results by VLAN"},
            "apTag": {"type": "string", "description": "Filter results by AP Tag"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessClientsLatencyStats = {
    "name": "getNetworkWirelessClientsLatencyStats",
    "description": "Aggregated latency info for this network, grouped by clients",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 180 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information."},
            "ssid": {"type": "integer", "description": "Filter results by SSID"},
            "vlan": {"type": "integer", "description": "Filter results by VLAN"},
            "apTag": {"type": "string", "description": "Filter results by AP Tag"},
            "fields": {"type": "string", "description": "Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string."},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessClientConnectionStats = {
    "name": "getNetworkWirelessClientConnectionStats",
    "description": "Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clientId": {"type": "string", "description": "Client ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 180 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information."},
            "ssid": {"type": "integer", "description": "Filter results by SSID"},
            "vlan": {"type": "integer", "description": "Filter results by VLAN"},
            "apTag": {"type": "string", "description": "Filter results by AP Tag"},
        },
        "required": ["networkId", "clientId"]
    }
}

getNetworkWirelessClientConnectivityEvents = {
    "name": "getNetworkWirelessClientConnectivityEvents",
    "description": "List the wireless connectivity events for a client within a network in the timespan.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clientId": {"type": "string", "description": "Client ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "sortOrder": {"type": "string", "description": "Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'ascending'."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
            "types": {"type": "array", "description": "A list of event types to include. If not specified, events of all types will be returned. Valid types are 'assoc', 'disassoc', 'auth', 'deauth', 'dns', 'dhcp', 'roam', 'connection' and/or 'sticky'."},
            "band": {"type": "string", "description": "Filter results by band. Valid bands are '2.4', '5' or '6'."},
            "ssidNumber": {"type": "integer", "description": "Filter results by SSID. If not specified, events for all SSIDs will be returned."},
            "includedSeverities": {"type": "array", "description": "A list of severities to include. If not specified, events of all severities will be returned. Valid severities are 'good', 'info', 'warn' and/or 'bad'."},
            "deviceSerial": {"type": "string", "description": "Filter results by an AP's serial number."},
        },
        "required": ["networkId", "clientId"]
    }
}

getNetworkWirelessClientLatencyHistory = {
    "name": "getNetworkWirelessClientLatencyHistory",
    "description": "Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clientId": {"type": "string", "description": "Client ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 791 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 791 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400."},
        },
        "required": ["networkId", "clientId"]
    }
}

getNetworkWirelessClientLatencyStats = {
    "name": "getNetworkWirelessClientLatencyStats",
    "description": "Aggregated latency info for a given client on this network. Clients are identified by their MAC.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "clientId": {"type": "string", "description": "Client ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 180 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information."},
            "ssid": {"type": "integer", "description": "Filter results by SSID"},
            "vlan": {"type": "integer", "description": "Filter results by VLAN"},
            "apTag": {"type": "string", "description": "Filter results by AP Tag"},
            "fields": {"type": "string", "description": "Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string."},
        },
        "required": ["networkId", "clientId"]
    }
}

getNetworkWirelessConnectionStats = {
    "name": "getNetworkWirelessConnectionStats",
    "description": "Aggregated connectivity info for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 180 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information."},
            "ssid": {"type": "integer", "description": "Filter results by SSID"},
            "vlan": {"type": "integer", "description": "Filter results by VLAN"},
            "apTag": {"type": "string", "description": "Filter results by AP Tag"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessDataRateHistory = {
    "name": "getNetworkWirelessDataRateHistory",
    "description": "Return PHY data rates over time for a network, device, or network client",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400."},
            "autoResolution": {"type": "boolean", "description": "Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false."},
            "clientId": {"type": "string", "description": "Filter results by network client."},
            "deviceSerial": {"type": "string", "description": "Filter results by device."},
            "apTag": {"type": "string", "description": "Filter results by AP tag."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6')."},
            "ssid": {"type": "integer", "description": "Filter results by SSID number."},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessDevicesConnectionStats = {
    "name": "getNetworkWirelessDevicesConnectionStats",
    "description": "Aggregated connectivity info for this network, grouped by node",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 180 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information."},
            "ssid": {"type": "integer", "description": "Filter results by SSID"},
            "vlan": {"type": "integer", "description": "Filter results by VLAN"},
            "apTag": {"type": "string", "description": "Filter results by AP Tag"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessDevicesLatencyStats = {
    "name": "getNetworkWirelessDevicesLatencyStats",
    "description": "Aggregated latency info for this network, grouped by node",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 180 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information."},
            "ssid": {"type": "integer", "description": "Filter results by SSID"},
            "vlan": {"type": "integer", "description": "Filter results by VLAN"},
            "apTag": {"type": "string", "description": "Filter results by AP Tag"},
            "fields": {"type": "string", "description": "Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string."},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessElectronicShelfLabel = {
    "name": "getNetworkWirelessElectronicShelfLabel",
    "description": "Return the ESL settings of a wireless network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessElectronicShelfLabelConfiguredDevices = {
    "name": "getNetworkWirelessElectronicShelfLabelConfiguredDevices",
    "description": "Get a list of all ESL eligible devices of a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessEthernetPortsProfiles = {
    "name": "getNetworkWirelessEthernetPortsProfiles",
    "description": "List the AP port profiles for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessEthernetPortsProfile = {
    "name": "getNetworkWirelessEthernetPortsProfile",
    "description": "Show the AP port profile by ID for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "profileId": {"type": "string", "description": "Profile ID"},
        },
        "required": ["networkId", "profileId"]
    }
}

getNetworkWirelessFailedConnections = {
    "name": "getNetworkWirelessFailedConnections",
    "description": "List of all failed client connection events on this network in a given time range",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 180 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information."},
            "ssid": {"type": "integer", "description": "Filter results by SSID"},
            "vlan": {"type": "integer", "description": "Filter results by VLAN"},
            "apTag": {"type": "string", "description": "Filter results by AP Tag"},
            "serial": {"type": "string", "description": "Filter by AP"},
            "clientId": {"type": "string", "description": "Filter by client MAC"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessLatencyHistory = {
    "name": "getNetworkWirelessLatencyHistory",
    "description": "Return average wireless latency over time for a network, device, or network client",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400."},
            "autoResolution": {"type": "boolean", "description": "Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false."},
            "clientId": {"type": "string", "description": "Filter results by network client."},
            "deviceSerial": {"type": "string", "description": "Filter results by device."},
            "apTag": {"type": "string", "description": "Filter results by AP tag."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6')."},
            "ssid": {"type": "integer", "description": "Filter results by SSID number."},
            "accessCategory": {"type": "string", "description": "Filter by access category."},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessLatencyStats = {
    "name": "getNetworkWirelessLatencyStats",
    "description": "Aggregated latency info for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 180 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information."},
            "ssid": {"type": "integer", "description": "Filter results by SSID"},
            "vlan": {"type": "integer", "description": "Filter results by VLAN"},
            "apTag": {"type": "string", "description": "Filter results by AP Tag"},
            "fields": {"type": "string", "description": "Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string."},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessMeshStatuses = {
    "name": "getNetworkWirelessMeshStatuses",
    "description": "List wireless mesh statuses for repeaters",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 500. Default is 50."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessRfProfiles = {
    "name": "getNetworkWirelessRfProfiles",
    "description": "List RF profiles for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "includeTemplateProfiles": {"type": "boolean", "description": "If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false."},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessRfProfile = {
    "name": "getNetworkWirelessRfProfile",
    "description": "Return a RF profile",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "rfProfileId": {"type": "string", "description": "Rf profile ID"},
        },
        "required": ["networkId", "rfProfileId"]
    }
}

getNetworkWirelessSettings = {
    "name": "getNetworkWirelessSettings",
    "description": "Return the wireless settings for a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessSignalQualityHistory = {
    "name": "getNetworkWirelessSignalQualityHistory",
    "description": "Return signal quality (SNR/RSSI) over time for a device or network client",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400."},
            "autoResolution": {"type": "boolean", "description": "Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false."},
            "clientId": {"type": "string", "description": "Filter results by network client."},
            "deviceSerial": {"type": "string", "description": "Filter results by device."},
            "apTag": {"type": "string", "description": "Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6')."},
            "ssid": {"type": "integer", "description": "Filter results by SSID number."},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessSsids = {
    "name": "getNetworkWirelessSsids",
    "description": "List the MR SSIDs in a network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
        },
        "required": ["networkId"]
    }
}

getNetworkWirelessSsid = {
    "name": "getNetworkWirelessSsid",
    "description": "Return a single MR SSID",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessSsidBonjourForwarding = {
    "name": "getNetworkWirelessSsidBonjourForwarding",
    "description": "List the Bonjour forwarding setting and rules for the SSID",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessSsidDeviceTypeGroupPolicies = {
    "name": "getNetworkWirelessSsidDeviceTypeGroupPolicies",
    "description": "List the device type group policies for the SSID",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessSsidEapOverride = {
    "name": "getNetworkWirelessSsidEapOverride",
    "description": "Return the EAP overridden parameters for an SSID",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessSsidFirewallL3FirewallRules = {
    "name": "getNetworkWirelessSsidFirewallL3FirewallRules",
    "description": "Return the L3 firewall rules for an SSID on an MR network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessSsidFirewallL7FirewallRules = {
    "name": "getNetworkWirelessSsidFirewallL7FirewallRules",
    "description": "Return the L7 firewall rules for an SSID on an MR network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessSsidHotspot20 = {
    "name": "getNetworkWirelessSsidHotspot20",
    "description": "Return the Hotspot 2.0 settings for an SSID",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessSsidIdentityPsks = {
    "name": "getNetworkWirelessSsidIdentityPsks",
    "description": "List all Identity PSKs in a wireless network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessSsidIdentityPsk = {
    "name": "getNetworkWirelessSsidIdentityPsk",
    "description": "Return an Identity PSK",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
            "identityPskId": {"type": "string", "description": "Identity psk ID"},
        },
        "required": ["networkId", "number", "identityPskId"]
    }
}

getNetworkWirelessSsidSchedules = {
    "name": "getNetworkWirelessSsidSchedules",
    "description": "List the outage schedule for the SSID",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessSsidSplashSettings = {
    "name": "getNetworkWirelessSsidSplashSettings",
    "description": "Display the splash page settings for the given SSID",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessSsidTrafficShapingRules = {
    "name": "getNetworkWirelessSsidTrafficShapingRules",
    "description": "Display the traffic shaping settings for a SSID on an MR network",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessSsidVpn = {
    "name": "getNetworkWirelessSsidVpn",
    "description": "List the VPN settings for the SSID.",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "number": {"type": "string", "description": "Number"},
        },
        "required": ["networkId", "number"]
    }
}

getNetworkWirelessUsageHistory = {
    "name": "getNetworkWirelessUsageHistory",
    "description": "Return AP usage over time for a device or network client",
    "parameters": {
        "type": "object",
        "properties": {
            "networkId": {"type": "string", "description": "Network ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days."},
            "resolution": {"type": "integer", "description": "The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400."},
            "autoResolution": {"type": "boolean", "description": "Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false."},
            "clientId": {"type": "string", "description": "Filter results by network client to return per-device AP usage over time inner joined by the queried client's connection history."},
            "deviceSerial": {"type": "string", "description": "Filter results by device. Requires :band."},
            "apTag": {"type": "string", "description": "Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified."},
            "band": {"type": "string", "description": "Filter results by band (either '2.4', '5' or '6')."},
            "ssid": {"type": "integer", "description": "Filter results by SSID number."},
        },
        "required": ["networkId"]
    }
}

getOrganizations = {
    "name": "getOrganizations",
    "description": "List the organizations that the user has privileges on",
    "parameters": {
        "type": "object",
        "properties": {
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 9000. Default is 9000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": []
    }
}

getOrganization = {
    "name": "getOrganization",
    "description": "Return an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationActionBatches = {
    "name": "getOrganizationActionBatches",
    "description": "Return the list of action batches in the organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "status": {"type": "string", "description": "Filter batches by status. Valid types are pending, completed, and failed."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationActionBatch = {
    "name": "getOrganizationActionBatch",
    "description": "Return an action batch",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "actionBatchId": {"type": "string", "description": "Action batch ID"},
        },
        "required": ["organizationId", "actionBatchId"]
    }
}

getOrganizationAdaptivePolicyAcls = {
    "name": "getOrganizationAdaptivePolicyAcls",
    "description": "List adaptive policy ACLs in a organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationAdaptivePolicyAcl = {
    "name": "getOrganizationAdaptivePolicyAcl",
    "description": "Returns the adaptive policy ACL information",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "aclId": {"type": "string", "description": "Acl ID"},
        },
        "required": ["organizationId", "aclId"]
    }
}

getOrganizationAdaptivePolicyGroups = {
    "name": "getOrganizationAdaptivePolicyGroups",
    "description": "List adaptive policy groups in a organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationAdaptivePolicyGroup = {
    "name": "getOrganizationAdaptivePolicyGroup",
    "description": "Returns an adaptive policy group",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "id": {"type": "string", "description": "ID"},
        },
        "required": ["organizationId", "id"]
    }
}

getOrganizationAdaptivePolicyOverview = {
    "name": "getOrganizationAdaptivePolicyOverview",
    "description": "Returns adaptive policy aggregate statistics for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationAdaptivePolicyPolicies = {
    "name": "getOrganizationAdaptivePolicyPolicies",
    "description": "List adaptive policies in an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationAdaptivePolicyPolicy = {
    "name": "getOrganizationAdaptivePolicyPolicy",
    "description": "Return an adaptive policy",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "id": {"type": "string", "description": "ID"},
        },
        "required": ["organizationId", "id"]
    }
}

getOrganizationAdaptivePolicySettings = {
    "name": "getOrganizationAdaptivePolicySettings",
    "description": "Returns global adaptive policy settings in an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationAdmins = {
    "name": "getOrganizationAdmins",
    "description": "List the dashboard administrators in this organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "Optional parameter to filter the result set by the included set of network IDs"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationAlertsProfiles = {
    "name": "getOrganizationAlertsProfiles",
    "description": "List all organization-wide alert configurations",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApiRequests = {
    "name": "getOrganizationApiRequests",
    "description": "List the API requests made by an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "adminId": {"type": "string", "description": "Filter the results by the ID of the admin who made the API requests"},
            "path": {"type": "string", "description": "Filter the results by the path of the API requests"},
            "method": {"type": "string", "description": "Filter the results by the method of the API requests (must be 'GET', 'PUT', 'POST' or 'DELETE')"},
            "responseCode": {"type": "integer", "description": "Filter the results by the response code of the API requests"},
            "sourceIp": {"type": "string", "description": "Filter the results by the IP address of the originating API request"},
            "userAgent": {"type": "string", "description": "Filter the results by the user agent string of the API request"},
            "version": {"type": "integer", "description": "Filter the results by the API version of the API request"},
            "operationIds": {"type": "array", "description": "Filter the results by one or more operation IDs for the API request"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApiRequestsOverview = {
    "name": "getOrganizationApiRequestsOverview",
    "description": "Return an aggregated overview of API requests data",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApiRequestsOverviewResponseCodesByInterval = {
    "name": "getOrganizationApiRequestsOverviewResponseCodesByInterval",
    "description": "Tracks organizations' API requests by response code across a given time period",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated."},
            "interval": {"type": "integer", "description": "The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided."},
            "version": {"type": "integer", "description": "Filter by API version of the endpoint. Allowable values are: [0, 1]"},
            "operationIds": {"type": "array", "description": "Filter by operation ID of the endpoint"},
            "sourceIps": {"type": "array", "description": "Filter by source IP that made the API request"},
            "adminIds": {"type": "array", "description": "Filter by admin ID of user that made the API request"},
            "userAgent": {"type": "string", "description": "Filter by user agent string for API request. This will filter by a complete or partial match."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApplianceSecurityEvents = {
    "name": "getOrganizationApplianceSecurityEvents",
    "description": "List the security events for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 365 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "sortOrder": {"type": "string", "description": "Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApplianceSecurityIntrusion = {
    "name": "getOrganizationApplianceSecurityIntrusion",
    "description": "Returns all supported intrusion settings for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork = {
    "name": "getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork",
    "description": "Display VPN exclusion rules for MX networks.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter the results by network IDs"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApplianceUplinkStatuses = {
    "name": "getOrganizationApplianceUplinkStatuses",
    "description": "List the uplink status of every Meraki MX and Z series appliances in the organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "A list of network IDs. The returned devices will be filtered to only include these networks."},
            "serials": {"type": "array", "description": "A list of serial numbers. The returned devices will be filtered to only include these serials."},
            "iccids": {"type": "array", "description": "A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApplianceUplinksStatusesOverview = {
    "name": "getOrganizationApplianceUplinksStatusesOverview",
    "description": "Returns an overview of uplink statuses",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApplianceUplinksUsageByNetwork = {
    "name": "getOrganizationApplianceUplinksUsageByNetwork",
    "description": "Get the sent and received bytes for each uplink of all MX and Z networks within an organization. If more than one device was active during the specified timespan, then the sent and received bytes will be aggregated by interface.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 365 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 14 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApplianceVpnStats = {
    "name": "getOrganizationApplianceVpnStats",
    "description": "Show VPN history stat for networks in an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 300. Default is 300."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApplianceVpnStatuses = {
    "name": "getOrganizationApplianceVpnStatuses",
    "description": "Show VPN status for networks in an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 300. Default is 300."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApplianceVpnThirdPartyVPNPeers = {
    "name": "getOrganizationApplianceVpnThirdPartyVPNPeers",
    "description": "Return the third party VPN peers for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationApplianceVpnVpnFirewallRules = {
    "name": "getOrganizationApplianceVpnVpnFirewallRules",
    "description": "Return the firewall rules for an organization's site-to-site VPN",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationAssuranceAlerts = {
    "name": "getOrganizationAssuranceAlerts",
    "description": "Return all health alerts for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 4 - 300. Default is 30."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "sortOrder": {"type": "string", "description": "Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'ascending'."},
            "networkId": {"type": "string", "description": "Optional parameter to filter alerts by network ids."},
            "severity": {"type": "string", "description": "Optional parameter to filter by severity type."},
            "types": {"type": "array", "description": "Optional parameter to filter by alert type."},
            "tsStart": {"type": "string", "description": "Optional parameter to filter by starting timestamp"},
            "tsEnd": {"type": "string", "description": "Optional parameter to filter by end timestamp"},
            "category": {"type": "string", "description": "Optional parameter to filter by category."},
            "sortBy": {"type": "string", "description": "Optional parameter to set column to sort by."},
            "serials": {"type": "array", "description": "Optional parameter to filter by primary device serial"},
            "deviceTypes": {"type": "array", "description": "Optional parameter to filter by device types"},
            "deviceTags": {"type": "array", "description": "Optional parameter to filter by device tags"},
            "active": {"type": "boolean", "description": "Optional parameter to filter by active alerts defaults to true"},
            "dismissed": {"type": "boolean", "description": "Optional parameter to filter by dismissed alerts defaults to false"},
            "resolved": {"type": "boolean", "description": "Optional parameter to filter by resolved alerts defaults to false"},
            "suppressAlertsForOfflineNodes": {"type": "boolean", "description": "When set to true the api will only return connectivity alerts for a given device if that device is in an offline state. This only applies to devices. This is ignored when resolved is true. Example:  If a Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert will be returned. Defaults to false."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationAssuranceAlertsOverview = {
    "name": "getOrganizationAssuranceAlertsOverview",
    "description": "Return overview of active health alerts for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkId": {"type": "string", "description": "Optional parameter to filter alerts overview by network ids."},
            "severity": {"type": "string", "description": "Optional parameter to filter alerts overview by severity type."},
            "types": {"type": "array", "description": "Optional parameter to filter by alert type."},
            "tsStart": {"type": "string", "description": "Optional parameter to filter by starting timestamp"},
            "tsEnd": {"type": "string", "description": "Optional parameter to filter by end timestamp"},
            "category": {"type": "string", "description": "Optional parameter to filter by category."},
            "serials": {"type": "array", "description": "Optional parameter to filter by primary device serial"},
            "deviceTypes": {"type": "array", "description": "Optional parameter to filter by device types"},
            "deviceTags": {"type": "array", "description": "Optional parameter to filter by device tags"},
            "active": {"type": "boolean", "description": "Optional parameter to filter by active alerts defaults to true"},
            "dismissed": {"type": "boolean", "description": "Optional parameter to filter by dismissed alerts defaults to false"},
            "resolved": {"type": "boolean", "description": "Optional parameter to filter by resolved alerts defaults to false"},
            "suppressAlertsForOfflineNodes": {"type": "boolean", "description": "When set to true the api will only return connectivity alerts for a given device if that device is in an offline state. This only applies to devices. This is ignored when resolved is true. Example:  If a Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert will be returned. Defaults to false."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationAssuranceAlertsOverviewByNetwork = {
    "name": "getOrganizationAssuranceAlertsOverviewByNetwork",
    "description": "Return a Summary of Alerts grouped by network and severity",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "sortOrder": {"type": "string", "description": "Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'ascending'."},
            "networkId": {"type": "string", "description": "Optional parameter to filter alerts overview by network id."},
            "severity": {"type": "string", "description": "Optional parameter to filter alerts overview by severity type."},
            "types": {"type": "array", "description": "Optional parameter to filter by alert type."},
            "tsStart": {"type": "string", "description": "Optional parameter to filter by starting timestamp"},
            "tsEnd": {"type": "string", "description": "Optional parameter to filter by end timestamp"},
            "category": {"type": "string", "description": "Optional parameter to filter by category."},
            "serials": {"type": "array", "description": "Optional parameter to filter by primary device serial"},
            "deviceTypes": {"type": "array", "description": "Optional parameter to filter by device types"},
            "deviceTags": {"type": "array", "description": "Optional parameter to filter by device tags"},
            "active": {"type": "boolean", "description": "Optional parameter to filter by active alerts defaults to true"},
            "dismissed": {"type": "boolean", "description": "Optional parameter to filter by dismissed alerts defaults to false"},
            "resolved": {"type": "boolean", "description": "Optional parameter to filter by resolved alerts defaults to false"},
            "suppressAlertsForOfflineNodes": {"type": "boolean", "description": "When set to true the api will only return connectivity alerts for a given device if that device is in an offline state. This only applies to devices. This is ignored when resolved is true. Example:  If a Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert will be returned. Defaults to false."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationAssuranceAlertsOverviewByType = {
    "name": "getOrganizationAssuranceAlertsOverviewByType",
    "description": "Return a Summary of Alerts grouped by type and severity",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "sortOrder": {"type": "string", "description": "Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'ascending'."},
            "networkId": {"type": "string", "description": "Optional parameter to filter alerts overview by network ids."},
            "severity": {"type": "string", "description": "Optional parameter to filter alerts overview by severity type."},
            "types": {"type": "array", "description": "Optional parameter to filter by alert type."},
            "tsStart": {"type": "string", "description": "Optional parameter to filter by starting timestamp"},
            "tsEnd": {"type": "string", "description": "Optional parameter to filter by end timestamp"},
            "category": {"type": "string", "description": "Optional parameter to filter by category."},
            "sortBy": {"type": "string", "description": "Optional parameter to set column to sort by."},
            "serials": {"type": "array", "description": "Optional parameter to filter by primary device serial"},
            "deviceTypes": {"type": "array", "description": "Optional parameter to filter by device types"},
            "deviceTags": {"type": "array", "description": "Optional parameter to filter by device tags"},
            "active": {"type": "boolean", "description": "Optional parameter to filter by active alerts defaults to true"},
            "dismissed": {"type": "boolean", "description": "Optional parameter to filter by dismissed alerts defaults to false"},
            "resolved": {"type": "boolean", "description": "Optional parameter to filter by resolved alerts defaults to false"},
            "suppressAlertsForOfflineNodes": {"type": "boolean", "description": "When set to true the api will only return connectivity alerts for a given device if that device is in an offline state. This only applies to devices. This is ignored when resolved is true. Example:  If a Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert will be returned. Defaults to false."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationAssuranceAlertsOverviewHistorical = {
    "name": "getOrganizationAssuranceAlertsOverviewHistorical",
    "description": "Returns historical health alert overviews",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "segmentDuration": {"type": "integer", "description": "Amount of time in seconds for each segment in the returned dataset"},
            "networkId": {"type": "string", "description": "Optional parameter to filter alerts overview by network ids."},
            "severity": {"type": "string", "description": "Optional parameter to filter alerts overview by severity type."},
            "types": {"type": "array", "description": "Optional parameter to filter by alert type."},
            "tsStart": {"type": "string", "description": "Parameter to define starting timestamp of historical totals"},
            "tsEnd": {"type": "string", "description": "Optional parameter to filter by end timestamp defaults to the current time"},
            "category": {"type": "string", "description": "Optional parameter to filter by category."},
            "serials": {"type": "array", "description": "Optional parameter to filter by primary device serial"},
            "deviceTypes": {"type": "array", "description": "Optional parameter to filter by device types"},
        },
        "required": ["organizationId", "segmentDuration", "tsStart"]
    }
}

getOrganizationAssuranceAlert = {
    "name": "getOrganizationAssuranceAlert",
    "description": "Return a singular Health Alert by its id",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "id": {"type": "string", "description": "ID"},
        },
        "required": ["organizationId", "id"]
    }
}

getOrganizationBrandingPolicies = {
    "name": "getOrganizationBrandingPolicies",
    "description": "List the branding policies of an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationBrandingPoliciesPriorities = {
    "name": "getOrganizationBrandingPoliciesPriorities",
    "description": "Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationBrandingPolicy = {
    "name": "getOrganizationBrandingPolicy",
    "description": "Return a branding policy",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "brandingPolicyId": {"type": "string", "description": "Branding policy ID"},
        },
        "required": ["organizationId", "brandingPolicyId"]
    }
}

getOrganizationCameraBoundariesAreasByDevice = {
    "name": "getOrganizationCameraBoundariesAreasByDevice",
    "description": "Returns all configured area boundaries of cameras",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "serials": {"type": "array", "description": "A list of serial numbers. The returned cameras will be filtered to only include these serials."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationCameraBoundariesLinesByDevice = {
    "name": "getOrganizationCameraBoundariesLinesByDevice",
    "description": "Returns all configured crossingline boundaries of cameras",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "serials": {"type": "array", "description": "A list of serial numbers. The returned cameras will be filtered to only include these serials."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationCameraCustomAnalyticsArtifacts = {
    "name": "getOrganizationCameraCustomAnalyticsArtifacts",
    "description": "List Custom Analytics Artifacts",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationCameraCustomAnalyticsArtifact = {
    "name": "getOrganizationCameraCustomAnalyticsArtifact",
    "description": "Get Custom Analytics Artifact",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "artifactId": {"type": "string", "description": "Artifact ID"},
        },
        "required": ["organizationId", "artifactId"]
    }
}

getOrganizationCameraDetectionsHistoryByBoundaryByInterval = {
    "name": "getOrganizationCameraDetectionsHistoryByBoundaryByInterval",
    "description": "Returns analytics data for timespans",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "boundaryIds": {"type": "array", "description": "A list of boundary ids. The returned cameras will be filtered to only include these ids."},
            "ranges": {"type": "array", "description": "A list of time ranges with intervals"},
            "duration": {"type": "integer", "description": "The minimum time, in seconds, that the person or car remains in the area to be counted. Defaults to boundary configuration or 60."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 1 - 1000. Defaults to 1000."},
            "boundaryTypes": {"type": "array", "description": "The detection types. Defaults to 'person'."},
        },
        "required": ["organizationId", "boundaryIds", "ranges"]
    }
}

getOrganizationCameraOnboardingStatuses = {
    "name": "getOrganizationCameraOnboardingStatuses",
    "description": "Fetch onboarding status of cameras",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "serials": {"type": "array", "description": "A list of serial numbers. The returned cameras will be filtered to only include these serials."},
            "networkIds": {"type": "array", "description": "A list of network IDs. The returned cameras will be filtered to only include these networks."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationCameraPermissions = {
    "name": "getOrganizationCameraPermissions",
    "description": "List the permissions scopes for this organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationCameraPermission = {
    "name": "getOrganizationCameraPermission",
    "description": "Retrieve a single permission scope",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "permissionScopeId": {"type": "string", "description": "Permission scope ID"},
        },
        "required": ["organizationId", "permissionScopeId"]
    }
}

getOrganizationCameraRoles = {
    "name": "getOrganizationCameraRoles",
    "description": "List all the roles in this organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationCameraRole = {
    "name": "getOrganizationCameraRole",
    "description": "Retrieve a single role.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "roleId": {"type": "string", "description": "Role ID"},
        },
        "required": ["organizationId", "roleId"]
    }
}

getOrganizationCellularGatewayEsimsInventory = {
    "name": "getOrganizationCellularGatewayEsimsInventory",
    "description": "The eSIM inventory of a given organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "eids": {"type": "array", "description": "Optional parameter to filter the results by EID."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationCellularGatewayEsimsServiceProviders = {
    "name": "getOrganizationCellularGatewayEsimsServiceProviders",
    "description": "Service providers customers can add accounts for.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationCellularGatewayEsimsServiceProvidersAccounts = {
    "name": "getOrganizationCellularGatewayEsimsServiceProvidersAccounts",
    "description": "Inventory of service provider accounts tied to the organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "accountIds": {"type": "array", "description": "Optional parameter to filter the results by service provider account IDs."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans = {
    "name": "getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans",
    "description": "The communication plans available for a given provider.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "accountIds": {"type": "array", "description": "Account IDs that communication plans will be fetched for"},
        },
        "required": ["organizationId", "accountIds"]
    }
}

getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans = {
    "name": "getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans",
    "description": "The rate plans available for a given provider.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "accountIds": {"type": "array", "description": "Account IDs that rate plans will be fetched for"},
        },
        "required": ["organizationId", "accountIds"]
    }
}

getOrganizationCellularGatewayUplinkStatuses = {
    "name": "getOrganizationCellularGatewayUplinkStatuses",
    "description": "List the uplink status of every Meraki MG cellular gateway in the organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "A list of network IDs. The returned devices will be filtered to only include these networks."},
            "serials": {"type": "array", "description": "A list of serial numbers. The returned devices will be filtered to only include these serials."},
            "iccids": {"type": "array", "description": "A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationClientsBandwidthUsageHistory = {
    "name": "getOrganizationClientsBandwidthUsageHistory",
    "description": "Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkTag": {"type": "string", "description": "Match result to an exact network tag"},
            "deviceTag": {"type": "string", "description": "Match result to an exact device tag"},
            "ssidName": {"type": "string", "description": "Filter results by ssid name"},
            "usageUplink": {"type": "string", "description": "Filter results by usage uplink"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationClientsOverview = {
    "name": "getOrganizationClientsOverview",
    "description": "Return summary information around client data usage (in kb) across the given organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationClientsSearch = {
    "name": "getOrganizationClientsSearch",
    "description": "Return the client details in an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 5. Default is 5."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "mac": {"type": "string", "description": "The MAC address of the client. Required."},
        },
        "required": ["organizationId", "mac"]
    }
}

getOrganizationConfigTemplates = {
    "name": "getOrganizationConfigTemplates",
    "description": "List the configuration templates for this organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationConfigTemplate = {
    "name": "getOrganizationConfigTemplate",
    "description": "Return a single configuration template",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "configTemplateId": {"type": "string", "description": "Config template ID"},
        },
        "required": ["organizationId", "configTemplateId"]
    }
}

getOrganizationConfigTemplateSwitchProfiles = {
    "name": "getOrganizationConfigTemplateSwitchProfiles",
    "description": "List the switch templates for your switch template configuration",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "configTemplateId": {"type": "string", "description": "Config template ID"},
        },
        "required": ["organizationId", "configTemplateId"]
    }
}

getOrganizationConfigTemplateSwitchProfilePorts = {
    "name": "getOrganizationConfigTemplateSwitchProfilePorts",
    "description": "Return all the ports of a switch template",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "configTemplateId": {"type": "string", "description": "Config template ID"},
            "profileId": {"type": "string", "description": "Profile ID"},
        },
        "required": ["organizationId", "configTemplateId", "profileId"]
    }
}

getOrganizationConfigTemplateSwitchProfilePort = {
    "name": "getOrganizationConfigTemplateSwitchProfilePort",
    "description": "Return a switch template port",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "configTemplateId": {"type": "string", "description": "Config template ID"},
            "profileId": {"type": "string", "description": "Profile ID"},
            "portId": {"type": "string", "description": "Port ID"},
        },
        "required": ["organizationId", "configTemplateId", "profileId", "portId"]
    }
}

getOrganizationConfigurationChanges = {
    "name": "getOrganizationConfigurationChanges",
    "description": "View the Change Log for your organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 365 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 365 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 365 days."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 5000. Default is 5000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkId": {"type": "string", "description": "Filters on the given network"},
            "adminId": {"type": "string", "description": "Filters on the given Admin"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationDevices = {
    "name": "getOrganizationDevices",
    "description": "List the devices in an organization that have been assigned to a network.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "configurationUpdatedAfter": {"type": "string", "description": "Filter results by whether or not the device's configuration has been updated after the given timestamp"},
            "networkIds": {"type": "array", "description": "Optional parameter to filter devices by network."},
            "productTypes": {"type": "array", "description": "Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor, wirelessController, and secureConnect."},
            "tags": {"type": "array", "description": "Optional parameter to filter devices by tags."},
            "tagsFilterType": {"type": "string", "description": "Optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected."},
            "name": {"type": "string", "description": "Optional parameter to filter devices by name. All returned devices will have a name that contains the search term or is an exact match."},
            "mac": {"type": "string", "description": "Optional parameter to filter devices by MAC address. All returned devices will have a MAC address that contains the search term or is an exact match."},
            "serial": {"type": "string", "description": "Optional parameter to filter devices by serial number. All returned devices will have a serial number that contains the search term or is an exact match."},
            "model": {"type": "string", "description": "Optional parameter to filter devices by model. All returned devices will have a model that contains the search term or is an exact match."},
            "macs": {"type": "array", "description": "Optional parameter to filter devices by one or more MAC addresses. All returned devices will have a MAC address that is an exact match."},
            "serials": {"type": "array", "description": "Optional parameter to filter devices by one or more serial numbers. All returned devices will have a serial number that is an exact match."},
            "sensorMetrics": {"type": "array", "description": "Optional parameter to filter devices by the metrics that they provide. Only applies to sensor devices."},
            "sensorAlertProfileIds": {"type": "array", "description": "Optional parameter to filter devices by the alert profiles that are bound to them. Only applies to sensor devices."},
            "models": {"type": "array", "description": "Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationDevicesAvailabilities = {
    "name": "getOrganizationDevicesAvailabilities",
    "description": "List the availability information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches."},
            "productTypes": {"type": "array", "description": "Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches. Valid types are wireless, appliance, switch, camera, cellularGateway, sensor, wirelessController, and campusGateway"},
            "serials": {"type": "array", "description": "Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches."},
            "tags": {"type": "array", "description": "An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches."},
            "tagsFilterType": {"type": "string", "description": "An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected."},
            "statuses": {"type": "array", "description": "Optional parameter to filter device availabilities by device status. This filter uses multiple exact matches."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationDevicesAvailabilitiesChangeHistory = {
    "name": "getOrganizationDevicesAvailabilitiesChangeHistory",
    "description": "List the availability history information for devices in an organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
            "serials": {"type": "array", "description": "Optional parameter to filter device availabilities history by device serial numbers"},
            "productTypes": {"type": "array", "description": "Optional parameter to filter device availabilities history by device product types"},
            "networkIds": {"type": "array", "description": "Optional parameter to filter device availabilities history by network IDs"},
            "statuses": {"type": "array", "description": "Optional parameter to filter device availabilities history by device statuses"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationDevicesOverviewByModel = {
    "name": "getOrganizationDevicesOverviewByModel",
    "description": "Lists the count for each device model",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "models": {"type": "array", "description": "Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter devices by networkId."},
            "productTypes": {"type": "array", "description": "Optional parameter to filter device by device product types. This filter uses multiple exact matches."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationDevicesPowerModulesStatusesByDevice = {
    "name": "getOrganizationDevicesPowerModulesStatusesByDevice",
    "description": "List the most recent status information for power modules in rackmount MX and MS devices that support them. The data returned by this endpoint is updated every 5 minutes.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches."},
            "productTypes": {"type": "array", "description": "Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches."},
            "serials": {"type": "array", "description": "Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches."},
            "tags": {"type": "array", "description": "An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches."},
            "tagsFilterType": {"type": "string", "description": "An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationDevicesProvisioningStatuses = {
    "name": "getOrganizationDevicesProvisioningStatuses",
    "description": "List the provisioning statuses information for devices in an organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter device by network ID. This filter uses multiple exact matches."},
            "productTypes": {"type": "array", "description": "Optional parameter to filter device by device product types. This filter uses multiple exact matches."},
            "serials": {"type": "array", "description": "Optional parameter to filter device by device serial numbers. This filter uses multiple exact matches."},
            "status": {"type": "string", "description": "An optional parameter to filter devices by the provisioning status. Accepted statuses: unprovisioned, incomplete, complete."},
            "tags": {"type": "array", "description": "An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches."},
            "tagsFilterType": {"type": "string", "description": "An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationDevicesStatuses = {
    "name": "getOrganizationDevicesStatuses",
    "description": "List the status of every Meraki device in the organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter devices by network ids."},
            "serials": {"type": "array", "description": "Optional parameter to filter devices by serials."},
            "statuses": {"type": "array", "description": "Optional parameter to filter devices by statuses. Valid statuses are [\"online\", \"alerting\", \"offline\", \"dormant\"]."},
            "productTypes": {"type": "array", "description": "An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor, wirelessController, and secureConnect."},
            "models": {"type": "array", "description": "Optional parameter to filter devices by models."},
            "tags": {"type": "array", "description": "An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below)."},
            "tagsFilterType": {"type": "string", "description": "An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationDevicesStatusesOverview = {
    "name": "getOrganizationDevicesStatusesOverview",
    "description": "Return an overview of current device statuses",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "productTypes": {"type": "array", "description": "An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor, wirelessController, and secureConnect."},
            "networkIds": {"type": "array", "description": "An optional parameter to filter device statuses by network."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationDevicesUplinksAddressesByDevice = {
    "name": "getOrganizationDevicesUplinksAddressesByDevice",
    "description": "List the current uplink addresses for devices in an organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches."},
            "productTypes": {"type": "array", "description": "Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches."},
            "serials": {"type": "array", "description": "Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches."},
            "tags": {"type": "array", "description": "An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches."},
            "tagsFilterType": {"type": "string", "description": "An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationDevicesUplinksLossAndLatency = {
    "name": "getOrganizationDevicesUplinksLossAndLatency",
    "description": "Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 60 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes."},
            "uplink": {"type": "string", "description": "Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, wan3, cellular. Default will return all uplinks."},
            "ip": {"type": "string", "description": "Optional filter for a specific destination IP. Default will return all destination IPs."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationEarlyAccessFeatures = {
    "name": "getOrganizationEarlyAccessFeatures",
    "description": "List the available early access features for organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationEarlyAccessFeaturesOptIns = {
    "name": "getOrganizationEarlyAccessFeaturesOptIns",
    "description": "List the early access feature opt-ins for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationEarlyAccessFeaturesOptIn = {
    "name": "getOrganizationEarlyAccessFeaturesOptIn",
    "description": "Show an early access feature opt-in for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "optInId": {"type": "string", "description": "Opt in ID"},
        },
        "required": ["organizationId", "optInId"]
    }
}

getOrganizationFirmwareUpgrades = {
    "name": "getOrganizationFirmwareUpgrades",
    "description": "Get firmware upgrade information for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "status": {"type": "array", "description": "Optional parameter to filter the upgrade by status."},
            "productTypes": {"type": "array", "description": "Optional parameter to filter the upgrade by product type."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationFirmwareUpgradesByDevice = {
    "name": "getOrganizationFirmwareUpgradesByDevice",
    "description": "Get firmware upgrade status for the filtered devices. This endpoint currently only supports Meraki switches.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter by network"},
            "serials": {"type": "array", "description": "Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match."},
            "macs": {"type": "array", "description": "Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match."},
            "firmwareUpgradeBatchIds": {"type": "array", "description": "Optional parameter to filter by firmware upgrade batch ids."},
            "upgradeStatuses": {"type": "array", "description": "Optional parameter to filter by firmware upgrade statuses."},
            "currentUpgradesOnly": {"type": "boolean", "description": "Optional parameter to filter to only current or pending upgrade statuses"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationFloorPlansAutoLocateDevices = {
    "name": "getOrganizationFloorPlansAutoLocateDevices",
    "description": "List auto locate details for each device in your organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter devices by one or more network IDs"},
            "floorPlanIds": {"type": "array", "description": "Optional parameter to filter devices by one or more floorplan IDs"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationFloorPlansAutoLocateStatuses = {
    "name": "getOrganizationFloorPlansAutoLocateStatuses",
    "description": "List the status of auto locate for each floorplan in your organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter floorplans by one or more network IDs"},
            "floorPlanIds": {"type": "array", "description": "Optional parameter to filter floorplans by one or more floorplan IDs"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationInsightApplications = {
    "name": "getOrganizationInsightApplications",
    "description": "List all Insight tracked applications",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationInsightMonitoredMediaServers = {
    "name": "getOrganizationInsightMonitoredMediaServers",
    "description": "List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationInsightMonitoredMediaServer = {
    "name": "getOrganizationInsightMonitoredMediaServer",
    "description": "Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "monitoredMediaServerId": {"type": "string", "description": "Monitored media server ID"},
        },
        "required": ["organizationId", "monitoredMediaServerId"]
    }
}

getOrganizationInventoryDevices = {
    "name": "getOrganizationInventoryDevices",
    "description": "Return the device inventory for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "usedState": {"type": "string", "description": "Filter results by used or unused inventory. Accepted values are 'used' or 'unused'."},
            "search": {"type": "string", "description": "Search for devices in inventory based on serial number, mac address, or model."},
            "macs": {"type": "array", "description": "Search for devices in inventory based on mac addresses."},
            "networkIds": {"type": "array", "description": "Search for devices in inventory based on network ids. Use explicit 'null' value to get available devices only."},
            "serials": {"type": "array", "description": "Search for devices in inventory based on serials."},
            "models": {"type": "array", "description": "Search for devices in inventory based on model."},
            "orderNumbers": {"type": "array", "description": "Search for devices in inventory based on order numbers."},
            "tags": {"type": "array", "description": "Filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below)."},
            "tagsFilterType": {"type": "string", "description": "To use with 'tags' parameter, to filter devices which contain ANY or ALL given tags. Accepted values are 'withAnyTags' or 'withAllTags', default is 'withAnyTags'."},
            "productTypes": {"type": "array", "description": "Filter devices by product type. Accepted values are appliance, camera, cellularGateway, secureConnect, sensor, switch, systemsManager, wireless, and wirelessController."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationInventoryDevicesSwapsBulk = {
    "name": "getOrganizationInventoryDevicesSwapsBulk",
    "description": "List of device swaps for a given request ID ({id}).",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "id": {"type": "string", "description": "ID"},
        },
        "required": ["organizationId", "id"]
    }
}

getOrganizationInventoryDevice = {
    "name": "getOrganizationInventoryDevice",
    "description": "Return a single device from the inventory of an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "serial": {"type": "string", "description": "Serial"},
        },
        "required": ["organizationId", "serial"]
    }
}

getOrganizationInventoryOnboardingCloudMonitoringImports = {
    "name": "getOrganizationInventoryOnboardingCloudMonitoringImports",
    "description": "Check the status of a committed Import operation",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "importIds": {"type": "array", "description": "import ids from an imports"},
        },
        "required": ["organizationId", "importIds"]
    }
}

getOrganizationInventoryOnboardingCloudMonitoringNetworks = {
    "name": "getOrganizationInventoryOnboardingCloudMonitoringNetworks",
    "description": "Returns list of networks eligible for adding cloud monitored device",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "deviceType": {"type": "string", "description": "Device Type switch or wireless controller"},
            "search": {"type": "string", "description": "Optional parameter to search on network name"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["organizationId", "deviceType"]
    }
}

getOrganizationLicenses = {
    "name": "getOrganizationLicenses",
    "description": "List the licenses for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "deviceSerial": {"type": "string", "description": "Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device."},
            "networkId": {"type": "string", "description": "Filter the licenses to those assigned in a particular network"},
            "state": {"type": "string", "description": "Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'recentlyQueued', 'unused' or 'unusedActive'"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationLicensesOverview = {
    "name": "getOrganizationLicensesOverview",
    "description": "Return an overview of the license state for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationLicense = {
    "name": "getOrganizationLicense",
    "description": "Display a license",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "licenseId": {"type": "string", "description": "License ID"},
        },
        "required": ["organizationId", "licenseId"]
    }
}

getOrganizationLicensingCotermLicenses = {
    "name": "getOrganizationLicensingCotermLicenses",
    "description": "List the licenses in a coterm organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "invalidated": {"type": "boolean", "description": "Filter for licenses that are invalidated"},
            "expired": {"type": "boolean", "description": "Filter for licenses that are expired"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationLoginSecurity = {
    "name": "getOrganizationLoginSecurity",
    "description": "Returns the login security settings for an organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationNetworks = {
    "name": "getOrganizationNetworks",
    "description": "List the networks that the user has privileges on in an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "configTemplateId": {"type": "string", "description": "An optional parameter that is the ID of a config template. Will return all networks bound to that template."},
            "isBoundToConfigTemplate": {"type": "boolean", "description": "An optional parameter to filter config template bound networks. If configTemplateId is set, this cannot be false."},
            "tags": {"type": "array", "description": "An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below)."},
            "tagsFilterType": {"type": "string", "description": "An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected."},
            "productTypes": {"type": "array", "description": "An optional parameter to filter networks by product type. Results will have at least one of the included product types."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationOpenapiSpec = {
    "name": "getOrganizationOpenapiSpec",
    "description": "Return the OpenAPI Specification of the organization's API documentation in JSON",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "version": {"type": "integer", "description": "OpenAPI Specification version to return. Default is 2"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationPolicyObjects = {
    "name": "getOrganizationPolicyObjects",
    "description": "Lists Policy Objects belonging to the organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 10 - 5000. Default is 5000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationPolicyObjectsGroups = {
    "name": "getOrganizationPolicyObjectsGroups",
    "description": "Lists Policy Object Groups belonging to the organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationPolicyObjectsGroup = {
    "name": "getOrganizationPolicyObjectsGroup",
    "description": "Shows details of a Policy Object Group.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "policyObjectGroupId": {"type": "string", "description": "Policy object group ID"},
        },
        "required": ["organizationId", "policyObjectGroupId"]
    }
}

getOrganizationPolicyObject = {
    "name": "getOrganizationPolicyObject",
    "description": "Shows details of a Policy Object.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "policyObjectId": {"type": "string", "description": "Policy object ID"},
        },
        "required": ["organizationId", "policyObjectId"]
    }
}

getOrganizationSaml = {
    "name": "getOrganizationSaml",
    "description": "Returns the SAML SSO enabled settings for an organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSamlIdps = {
    "name": "getOrganizationSamlIdps",
    "description": "List the SAML IdPs in your organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSamlIdp = {
    "name": "getOrganizationSamlIdp",
    "description": "Get a SAML IdP from your organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "idpId": {"type": "string", "description": "Idp ID"},
        },
        "required": ["organizationId", "idpId"]
    }
}

getOrganizationSamlRoles = {
    "name": "getOrganizationSamlRoles",
    "description": "List the SAML roles for this organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSamlRole = {
    "name": "getOrganizationSamlRole",
    "description": "Return a SAML role",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "samlRoleId": {"type": "string", "description": "Saml role ID"},
        },
        "required": ["organizationId", "samlRoleId"]
    }
}

getOrganizationSensorReadingsHistory = {
    "name": "getOrganizationSensorReadingsHistory",
    "description": "Return all reported readings from sensors in a given timespan, sorted by timestamp",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 7 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter readings by network."},
            "serials": {"type": "array", "description": "Optional parameter to filter readings by sensor."},
            "metrics": {"type": "array", "description": "Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are apparentPower, battery, button, co2, current, door, downstreamPower, frequency, humidity, indoorAirQuality, noise, pm25, powerFactor, realPower, remoteLockoutSwitch, temperature, tvoc, voltage, and water."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSensorReadingsLatest = {
    "name": "getOrganizationSensorReadingsLatest",
    "description": "Return the latest available reading for each metric from each sensor, sorted by sensor serial",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter readings by network."},
            "serials": {"type": "array", "description": "Optional parameter to filter readings by sensor."},
            "metrics": {"type": "array", "description": "Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are apparentPower, battery, button, co2, current, door, downstreamPower, frequency, humidity, indoorAirQuality, noise, pm25, powerFactor, realPower, remoteLockoutSwitch, temperature, tvoc, voltage, and water."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSmAdminsRoles = {
    "name": "getOrganizationSmAdminsRoles",
    "description": "List the Limited Access Roles for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSmAdminsRole = {
    "name": "getOrganizationSmAdminsRole",
    "description": "Return a Limited Access Role",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "roleId": {"type": "string", "description": "Role ID"},
        },
        "required": ["organizationId", "roleId"]
    }
}

getOrganizationSmApnsCert = {
    "name": "getOrganizationSmApnsCert",
    "description": "Get the organization's APNS certificate",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSmSentryPoliciesAssignmentsByNetwork = {
    "name": "getOrganizationSmSentryPoliciesAssignmentsByNetwork",
    "description": "List the Sentry Policies for an organization ordered in ascending order of priority",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter Sentry Policies by Network Id"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSmVppAccounts = {
    "name": "getOrganizationSmVppAccounts",
    "description": "List the VPP accounts in the organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSmVppAccount = {
    "name": "getOrganizationSmVppAccount",
    "description": "Get a hash containing the unparsed token of the VPP account with the given ID",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "vppAccountId": {"type": "string", "description": "Vpp account ID"},
        },
        "required": ["organizationId", "vppAccountId"]
    }
}

getOrganizationSnmp = {
    "name": "getOrganizationSnmp",
    "description": "Return the SNMP settings for an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSplashAsset = {
    "name": "getOrganizationSplashAsset",
    "description": "Get a Splash Theme Asset",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "id": {"type": "string", "description": "ID"},
        },
        "required": ["organizationId", "id"]
    }
}

getOrganizationSplashThemes = {
    "name": "getOrganizationSplashThemes",
    "description": "List Splash Themes",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSummarySwitchPowerHistory = {
    "name": "getOrganizationSummarySwitchPowerHistory",
    "description": "Returns the total PoE power draw for all switch ports in the organization over the requested timespan (by default the last 24 hours). The returned array is a newest-first list of intervals. The time between intervals depends on the requested timespan with 20 minute intervals used for timespans up to 1 day, 4 hour intervals used for timespans up to 2 weeks, and 1 day intervals for timespans larger than 2 weeks.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSummaryTopAppliancesByUtilization = {
    "name": "getOrganizationSummaryTopAppliancesByUtilization",
    "description": "Return the top 10 appliances sorted by utilization over given time range.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkTag": {"type": "string", "description": "Match result to an exact network tag"},
            "deviceTag": {"type": "string", "description": "Match result to an exact device tag"},
            "quantity": {"type": "integer", "description": "Set number of desired results to return. Default is 10."},
            "ssidName": {"type": "string", "description": "Filter results by ssid name"},
            "usageUplink": {"type": "string", "description": "Filter results by usage uplink"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 25 minutes and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSummaryTopApplicationsByUsage = {
    "name": "getOrganizationSummaryTopApplicationsByUsage",
    "description": "Return the top applications sorted by data usage over given time range. Default unit is megabytes.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkTag": {"type": "string", "description": "Match result to an exact network tag"},
            "device": {"type": "string", "description": "Match result to an exact device tag"},
            "networkId": {"type": "string", "description": "Match result to an exact network id"},
            "quantity": {"type": "integer", "description": "Set number of desired results to return. Default is 10."},
            "ssidName": {"type": "string", "description": "Filter results by ssid name"},
            "usageUplink": {"type": "string", "description": "Filter results by usage uplink"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 25 minutes and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSummaryTopApplicationsCategoriesByUsage = {
    "name": "getOrganizationSummaryTopApplicationsCategoriesByUsage",
    "description": "Return the top application categories sorted by data usage over given time range. Default unit is megabytes.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkTag": {"type": "string", "description": "Match result to an exact network tag"},
            "deviceTag": {"type": "string", "description": "Match result to an exact device tag"},
            "networkId": {"type": "string", "description": "Match result to an exact network id"},
            "quantity": {"type": "integer", "description": "Set number of desired results to return. Default is 10."},
            "ssidName": {"type": "string", "description": "Filter results by ssid name"},
            "usageUplink": {"type": "string", "description": "Filter results by usage uplink"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 25 minutes and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSummaryTopClientsByUsage = {
    "name": "getOrganizationSummaryTopClientsByUsage",
    "description": "Return metrics for organization's top 10 clients by data usage (in mb) over given time range.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkTag": {"type": "string", "description": "Match result to an exact network tag"},
            "deviceTag": {"type": "string", "description": "Match result to an exact device tag"},
            "quantity": {"type": "integer", "description": "Set number of desired results to return. Default is 10."},
            "ssidName": {"type": "string", "description": "Filter results by ssid name"},
            "usageUplink": {"type": "string", "description": "Filter results by usage uplink"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSummaryTopClientsManufacturersByUsage = {
    "name": "getOrganizationSummaryTopClientsManufacturersByUsage",
    "description": "Return metrics for organization's top clients by data usage (in mb) over given time range, grouped by manufacturer.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkTag": {"type": "string", "description": "Match result to an exact network tag"},
            "deviceTag": {"type": "string", "description": "Match result to an exact device tag"},
            "quantity": {"type": "integer", "description": "Set number of desired results to return. Default is 10."},
            "ssidName": {"type": "string", "description": "Filter results by ssid name"},
            "usageUplink": {"type": "string", "description": "Filter results by usage uplink"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSummaryTopDevicesByUsage = {
    "name": "getOrganizationSummaryTopDevicesByUsage",
    "description": "Return metrics for organization's top 10 devices sorted by data usage over given time range. Default unit is megabytes.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkTag": {"type": "string", "description": "Match result to an exact network tag"},
            "deviceTag": {"type": "string", "description": "Match result to an exact device tag"},
            "quantity": {"type": "integer", "description": "Set number of desired results to return. Default is 10."},
            "ssidName": {"type": "string", "description": "Filter results by ssid name"},
            "usageUplink": {"type": "string", "description": "Filter results by usage uplink"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSummaryTopDevicesModelsByUsage = {
    "name": "getOrganizationSummaryTopDevicesModelsByUsage",
    "description": "Return metrics for organization's top 10 device models sorted by data usage over given time range. Default unit is megabytes.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkTag": {"type": "string", "description": "Match result to an exact network tag"},
            "deviceTag": {"type": "string", "description": "Match result to an exact device tag"},
            "quantity": {"type": "integer", "description": "Set number of desired results to return. Default is 10."},
            "ssidName": {"type": "string", "description": "Filter results by ssid name"},
            "usageUplink": {"type": "string", "description": "Filter results by usage uplink"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSummaryTopNetworksByStatus = {
    "name": "getOrganizationSummaryTopNetworksByStatus",
    "description": "List the client and status overview information for the networks in an organization. Usage is measured in kilobytes and from the last seven days.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkTag": {"type": "string", "description": "Match result to an exact network tag"},
            "deviceTag": {"type": "string", "description": "Match result to an exact device tag"},
            "quantity": {"type": "integer", "description": "Set number of desired results to return. Default is 10."},
            "ssidName": {"type": "string", "description": "Filter results by ssid name"},
            "usageUplink": {"type": "string", "description": "Filter results by usage uplink"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 5000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSummaryTopSsidsByUsage = {
    "name": "getOrganizationSummaryTopSsidsByUsage",
    "description": "Return metrics for organization's top 10 ssids by data usage over given time range. Default unit is megabytes.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkTag": {"type": "string", "description": "Match result to an exact network tag"},
            "deviceTag": {"type": "string", "description": "Match result to an exact device tag"},
            "quantity": {"type": "integer", "description": "Set number of desired results to return. Default is 10."},
            "ssidName": {"type": "string", "description": "Filter results by ssid name"},
            "usageUplink": {"type": "string", "description": "Filter results by usage uplink"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSummaryTopSwitchesByEnergyUsage = {
    "name": "getOrganizationSummaryTopSwitchesByEnergyUsage",
    "description": "Return metrics for organization's top 10 switches by energy usage over given time range. Default unit is joules.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkTag": {"type": "string", "description": "Match result to an exact network tag"},
            "deviceTag": {"type": "string", "description": "Match result to an exact device tag"},
            "quantity": {"type": "integer", "description": "Set number of desired results to return. Default is 10."},
            "ssidName": {"type": "string", "description": "Filter results by ssid name"},
            "usageUplink": {"type": "string", "description": "Filter results by usage uplink"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 25 minutes and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSwitchPortsBySwitch = {
    "name": "getOrganizationSwitchPortsBySwitch",
    "description": "List the switchports in an organization by switch",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 50. Default is 50."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "configurationUpdatedAfter": {"type": "string", "description": "Optional parameter to filter items to switches where the configuration has been updated after the given timestamp."},
            "mac": {"type": "string", "description": "Optional parameter to filter items to switches with MAC addresses that contain the search term or are an exact match."},
            "macs": {"type": "array", "description": "Optional parameter to filter items to switches that have one of the provided MAC addresses."},
            "name": {"type": "string", "description": "Optional parameter to filter items to switches with names that contain the search term or are an exact match."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter items to switches in one of the provided networks."},
            "portProfileIds": {"type": "array", "description": "Optional parameter to filter items to switches that contain switchports belonging to one of the specified port profiles."},
            "serial": {"type": "string", "description": "Optional parameter to filter items to switches with serial number that contains the search term or are an exact match."},
            "serials": {"type": "array", "description": "Optional parameter to filter items to switches that have one of the provided serials."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSwitchPortsClientsOverviewByDevice = {
    "name": "getOrganizationSwitchPortsClientsOverviewByDevice",
    "description": "List the number of clients for all switchports with at least one online client in an organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 20. Default is 20."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "configurationUpdatedAfter": {"type": "string", "description": "Optional parameter to filter items to switches where the configuration has been updated after the given timestamp."},
            "mac": {"type": "string", "description": "Optional parameter to filter items to switches with MAC addresses that contain the search term or are an exact match."},
            "macs": {"type": "array", "description": "Optional parameter to filter items to switches that have one of the provided MAC addresses."},
            "name": {"type": "string", "description": "Optional parameter to filter items to switches with names that contain the search term or are an exact match."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter items to switches in one of the provided networks."},
            "portProfileIds": {"type": "array", "description": "Optional parameter to filter items to switches that contain switchports belonging to one of the specified port profiles."},
            "serial": {"type": "string", "description": "Optional parameter to filter items to switches with serial number that contains the search term or are an exact match."},
            "serials": {"type": "array", "description": "Optional parameter to filter items to switches that have one of the provided serials."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSwitchPortsOverview = {
    "name": "getOrganizationSwitchPortsOverview",
    "description": "Returns the counts of all active ports for the requested timespan, grouped by speed. An active port is a port that at any point during the timeframe is observed to be connected to a responsive device and isn't configured to be disabled. For a port that is observed at multiple speeds during the timeframe, it will be counted at the highest speed observed. The number of inactive ports, and the total number of ports are also provided. Only ports on switches online during the timeframe will be represented and a port is only guaranteed to be present if its switch was online for at least 6 hours of the timeframe.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 186 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 12 hours and be less than or equal to 186 days. The default is 1 day."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSwitchPortsStatusesBySwitch = {
    "name": "getOrganizationSwitchPortsStatusesBySwitch",
    "description": "List the switchports in an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 20. Default is 10."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "configurationUpdatedAfter": {"type": "string", "description": "Optional parameter to filter items to switches where the configuration has been updated after the given timestamp."},
            "mac": {"type": "string", "description": "Optional parameter to filter items to switches with MAC addresses that contain the search term or are an exact match."},
            "macs": {"type": "array", "description": "Optional parameter to filter items to switches that have one of the provided MAC addresses."},
            "name": {"type": "string", "description": "Optional parameter to filter items to switches with names that contain the search term or are an exact match."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter items to switches in one of the provided networks."},
            "portProfileIds": {"type": "array", "description": "Optional parameter to filter items to switches that contain switchports belonging to one of the specified port profiles."},
            "serial": {"type": "string", "description": "Optional parameter to filter items to switches with serial number that contains the search term or are an exact match."},
            "serials": {"type": "array", "description": "Optional parameter to filter items to switches that have one of the provided serials."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationSwitchPortsTopologyDiscoveryByDevice = {
    "name": "getOrganizationSwitchPortsTopologyDiscoveryByDevice",
    "description": "List most recently seen LLDP/CDP discovery and topology information per switch port in an organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 20. Default is 10."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "configurationUpdatedAfter": {"type": "string", "description": "Optional parameter to filter items to switches where the configuration has been updated after the given timestamp."},
            "mac": {"type": "string", "description": "Optional parameter to filter items to switches with MAC addresses that contain the search term or are an exact match."},
            "macs": {"type": "array", "description": "Optional parameter to filter items to switches that have one of the provided MAC addresses."},
            "name": {"type": "string", "description": "Optional parameter to filter items to switches with names that contain the search term or are an exact match."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter items to switches in one of the provided networks."},
            "portProfileIds": {"type": "array", "description": "Optional parameter to filter items to switches that contain switchports belonging to one of the specified port profiles."},
            "serial": {"type": "string", "description": "Optional parameter to filter items to switches with serial number that contains the search term or are an exact match."},
            "serials": {"type": "array", "description": "Optional parameter to filter items to switches that have one of the provided serials."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationUplinksStatuses = {
    "name": "getOrganizationUplinksStatuses",
    "description": "List the uplink status of every Meraki MX, MG and Z series devices in the organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "A list of network IDs. The returned devices will be filtered to only include these networks."},
            "serials": {"type": "array", "description": "A list of serial numbers. The returned devices will be filtered to only include these serials."},
            "iccids": {"type": "array", "description": "A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWebhooksAlertTypes = {
    "name": "getOrganizationWebhooksAlertTypes",
    "description": "Return a list of alert types to be used with managing webhook alerts",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "productType": {"type": "string", "description": "Filter sample alerts to a specific product type"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWebhooksCallbacksStatus = {
    "name": "getOrganizationWebhooksCallbacksStatus",
    "description": "Return the status of an API callback",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "callbackId": {"type": "string", "description": "Callback ID"},
        },
        "required": ["organizationId", "callbackId"]
    }
}

getOrganizationWebhooksLogs = {
    "name": "getOrganizationWebhooksLogs",
    "description": "Return the log of webhook POSTs sent",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 90 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "url": {"type": "string", "description": "The URL the webhook was sent to"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessAirMarshalRules = {
    "name": "getOrganizationWirelessAirMarshalRules",
    "description": "Returns the current Air Marshal rules for this organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "(optional) The set of network IDs to include."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessAirMarshalSettingsByNetwork = {
    "name": "getOrganizationWirelessAirMarshalSettingsByNetwork",
    "description": "Returns the current Air Marshal settings for this network",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "The network IDs to include in the result set."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessClientsOverviewByDevice = {
    "name": "getOrganizationWirelessClientsOverviewByDevice",
    "description": "List access point client count at the moment in an organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "Optional parameter to filter access points client counts by network ID. This filter uses multiple exact matches."},
            "serials": {"type": "array", "description": "Optional parameter to filter access points client counts by its serial numbers. This filter uses multiple exact matches."},
            "campusGatewayClusterIds": {"type": "array", "description": "Optional parameter to filter access points client counts by MCG cluster IDs. This filter uses multiple exact matches."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessDevicesChannelUtilizationByDevice = {
    "name": "getOrganizationWirelessDevicesChannelUtilizationByDevice",
    "description": "Get average channel utilization for all bands in a network, split by AP",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "Filter results by network."},
            "serials": {"type": "array", "description": "Filter results by device."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 90 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 90 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 90 days. The default is 7 days."},
            "interval": {"type": "integer", "description": "The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessDevicesChannelUtilizationByNetwork = {
    "name": "getOrganizationWirelessDevicesChannelUtilizationByNetwork",
    "description": "Get average channel utilization across all bands for all networks in the organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "Filter results by network."},
            "serials": {"type": "array", "description": "Filter results by device."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 90 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 90 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 90 days. The default is 7 days."},
            "interval": {"type": "integer", "description": "The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval = {
    "name": "getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval",
    "description": "Get a time-series of average channel utilization for all bands, segmented by device.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "Filter results by network."},
            "serials": {"type": "array", "description": "Filter results by device."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days."},
            "interval": {"type": "integer", "description": "The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval = {
    "name": "getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval",
    "description": "Get a time-series of average channel utilization for all bands",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "Filter results by network."},
            "serials": {"type": "array", "description": "Filter results by device."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 31 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 31 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days."},
            "interval": {"type": "integer", "description": "The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessDevicesEthernetStatuses = {
    "name": "getOrganizationWirelessDevicesEthernetStatuses",
    "description": "List the most recent Ethernet link speed, duplex, aggregation and power mode and status information for wireless devices.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456"},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessDevicesPacketLossByClient = {
    "name": "getOrganizationWirelessDevicesPacketLossByClient",
    "description": "Get average packet loss for the given timespan for all clients in the organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "Filter results by network."},
            "ssids": {"type": "array", "description": "Filter results by SSID number."},
            "bands": {"type": "array", "description": "Filter results by band. Valid bands are: 2.4, 5, and 6."},
            "macs": {"type": "array", "description": "Filter results by client mac address(es)."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 90 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 90 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 90 days. The default is 7 days."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessDevicesPacketLossByDevice = {
    "name": "getOrganizationWirelessDevicesPacketLossByDevice",
    "description": "Get average packet loss for the given timespan for all devices in the organization. Does not include device's own traffic.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "Filter results by network."},
            "serials": {"type": "array", "description": "Filter results by device."},
            "ssids": {"type": "array", "description": "Filter results by SSID number."},
            "bands": {"type": "array", "description": "Filter results by band. Valid bands are: 2.4, 5, and 6."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 90 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 90 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 90 days. The default is 7 days."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessDevicesPacketLossByNetwork = {
    "name": "getOrganizationWirelessDevicesPacketLossByNetwork",
    "description": "Get average packet loss for the given timespan for all networks in the organization.",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "Filter results by network."},
            "serials": {"type": "array", "description": "Filter results by device."},
            "ssids": {"type": "array", "description": "Filter results by SSID number."},
            "bands": {"type": "array", "description": "Filter results by band. Valid bands are: 2.4, 5, and 6."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "t0": {"type": "string", "description": "The beginning of the timespan for the data. The maximum lookback period is 90 days from today."},
            "t1": {"type": "string", "description": "The end of the timespan for the data. t1 can be a maximum of 90 days after t0."},
            "timespan": {"type": "number", "description": "The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 90 days. The default is 7 days."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessDevicesWirelessControllersByDevice = {
    "name": "getOrganizationWirelessDevicesWirelessControllersByDevice",
    "description": "List of Catalyst access points information",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "Optional parameter to filter access points by network ID. This filter uses multiple exact matches."},
            "serials": {"type": "array", "description": "Optional parameter to filter access points by its cloud ID. This filter uses multiple exact matches."},
            "controllerSerials": {"type": "array", "description": "Optional parameter to filter access points by its wireless LAN controller cloud ID. This filter uses multiple exact matches."},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessRfProfilesAssignmentsByDevice = {
    "name": "getOrganizationWirelessRfProfilesAssignmentsByDevice",
    "description": "List the RF profiles of an organization by device",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "networkIds": {"type": "array", "description": "Optional parameter to filter devices by network."},
            "productTypes": {"type": "array", "description": "Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor, wirelessController, and secureConnect."},
            "name": {"type": "string", "description": "Optional parameter to filter RF profiles by device name. All returned devices will have a name that contains the search term or is an exact match."},
            "mac": {"type": "string", "description": "Optional parameter to filter RF profiles by device MAC address. All returned devices will have a MAC address that contains the search term or is an exact match."},
            "serial": {"type": "string", "description": "Optional parameter to filter RF profiles by device serial number. All returned devices will have a serial number that contains the search term or is an exact match."},
            "model": {"type": "string", "description": "Optional parameter to filter RF profiles by device model. All returned devices will have a model that contains the search term or is an exact match."},
            "macs": {"type": "array", "description": "Optional parameter to filter RF profiles by one or more device MAC addresses. All returned devices will have a MAC address that is an exact match."},
            "serials": {"type": "array", "description": "Optional parameter to filter RF profiles by one or more device serial numbers. All returned devices will have a serial number that is an exact match."},
            "models": {"type": "array", "description": "Optional parameter to filter RF profiles by one or more device models. All returned devices will have a model that is an exact match."},
        },
        "required": ["organizationId"]
    }
}

getOrganizationWirelessSsidsStatusesByDevice = {
    "name": "getOrganizationWirelessSsidsStatusesByDevice",
    "description": "List status information of all BSSIDs in your organization",
    "parameters": {
        "type": "object",
        "properties": {
            "organizationId": {"type": "string", "description": "Organization ID"},
            "networkIds": {"type": "array", "description": "Optional parameter to filter the result set by the included set of network IDs"},
            "serials": {"type": "array", "description": "A list of serial numbers. The returned devices will be filtered to only include these serials."},
            "bssids": {"type": "array", "description": "A list of BSSIDs. The returned devices will be filtered to only include these BSSIDs."},
            "hideDisabled": {"type": "boolean", "description": "If true, the returned devices will not include disabled SSIDs. (default: true)"},
            "perPage": {"type": "integer", "description": "The number of entries per page returned. Acceptable range is 3 - 500. Default is 100."},
            "startingAfter": {"type": "string", "description": "A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
            "endingBefore": {"type": "string", "description": "A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it."},
        },
        "required": ["organizationId"]
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
    


    # Cisco Catalyst Center SDK
    getsAllTheVersionsOfAGivenTemplate_function,
    getMulticastVirtualNetworks_function,
    getDeviceControllabilitySettings_function,
    getChassisDetailsForDevice_function,
    getsABuilding_function,
    getCountOfAllDiscoveryJobs_function,
    getViewsForAGivenViewGroup_function,
    getDeviceById_function,
    retrieveImageDistributionServers_function,
    retrieveBannerSettingsForASite_function,
    getSiteAssignedNetworkDevices_function,
    getNetworkDevicesCredentialsSyncStatus_function,
    getSoftwareImageDetails_function,
    getAnycastGateways_function,
    getTagMembersById_function,
    getFabricSiteCount_function,
    retrievesAllTheValidationSets_function,
    retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo_function,
    getFabricDevicesLayer2HandoffsCount_function,
    countOfEventSubscriptions_function,
    getDetailsOfASingleAssuranceEvent_function,
    retrieveTelemetrySettingsForASite_function,
    getFloorSettings_function,
    getTheTotalNumberOfIssuesForGivenSetOfFilters_function,
    getTag_function,
    getLayer2VirtualNetworks_function,
    getFabricZoneCount_function,
    getWebhookDestination_function,
    retrieveTimeZoneSettingsForASite_function,
    getApplicationPolicyQueuingProfile_function,
    getSyslogDestination_function,
    getSyncResultForVirtualAccount_function,
    getApplicationPolicyDefault_function,
    getModuleInfoById_function,
    getFabricDevicesLayer3HandoffsWithSdaTransit_function,
    getFabricDevicesLayer3HandoffsWithIpTransit_function,
    countOfNotifications_function,
    getAScheduledReport_function,
    getSiteHealth_function,
    getSitesCount_function,
    retrievesTheListOfValidationWorkflows_function,
    retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned_function,
    getSiteCountV2_function,
    getExtranetPolicies_function,
    getFlexibleReportScheduleByReportId_function,
    getPortChannels_function,
    getsTheTemplatesAvailable_function,
    getSyslogSubscriptionDetails_function,
    getListOfScheduledReports_function,
    getClientDetail_function,
    countTheNumberOfEvents_function,
    getTagMemberCount_function,
    getDeviceInterfacesBySpecifiedRange_function,
    getPollingIntervalForAllDevices_function,
    getDeviceList_function,
    getQosDeviceInterfaceInfo_function,
    getDeviceFamilyIdentifiers_function,
    getTaskCount_function,
    retrievesValidationDetailsForAValidationSet_function,
    getSmartAccountList_function,
    getLayer3VirtualNetworks_function,
    getListOfAvailableNamespaces_function,
    retrieveNetworkDeviceProductName_function,
    getExecutionIdByReportId_function,
    getMobilityGroupsCount_function,
    getAdvisoriesList_function,
    getListOfFiles_function,
    retrieveSpecificImageDistributionServer_function,
    getApplicationPolicy_function,
    getWorkflowById_function,
    getAdvisoriesSummary_function,
    getTagResourceTypes_function,
    getPortAssignmentCount_function,
    getDiscoveriesByRange_function,
    getsAnArea_function,
    getExtranetPolicyCount_function,
    getResyncIntervalForTheNetworkDevice_function,
    getInterfaces_function,
    getAllViewGroups_function,
    getEvents_function,
    getEmailEventSubscriptions_function,
    getEmailSubscriptionDetails_function,
    getAllGlobalCredentialsV2_function,
    getNetworkDevicesFromDiscovery_function,
    getSites_function,
    getEventSubscriptions_function,
    getPlannedAccessPointsForFloor_function,
    getDiscoveryById_function,
    getConfigurationArchiveDetails_function,
    getAdvisoriesPerDevice_function,
    retrievesTheCountOfValidationWorkflows_function,
    getComplianceDetailCount_function,
    getOverallClientHealth_function,
    getLinecardDetails_function,
    getWirelessProfilesCount_function,
    getTagById_function,
    getAuditLogSummary_function,
    getsAListOfProjects_function,
    getAuthenticationAndPolicyServers_function,
    retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo_function,
    getProvisionedDevices_function,
    retrievesAllPreviousPathtracesSummary_function,
    getDeviceCredentialSettingsForASite_function,
    getDeviceInterfaceCount_function,
    getLayer2VirtualNetworkCount_function,
    retrievesTheCountOfNetworkProfilesForSites_function,
    getDeviceCount_function,
    getFabricDevicesLayer2Handoffs_function,
    getSyslogEventSubscriptions_function,
    getSiteV2_function,
    getFabricDevices_function,
    getTasksCount_function,
    getsAFloor_function,
    getFabricZones_function,
    getVirtualAccountList_function,
    getQosDeviceInterfaceInfoCount_function,
    countOfEvents_function,
    getNetworkDeviceImageUpdates_function,
    getTransitNetworks_function,
    getStackDetailsForDevice_function,
    getApplicationSetCount_function,
    getWorkflowCount_function,
    retrievesPreviousPathtrace_function,
    getOverallNetworkHealth_function,
    getServiceProviderDetailsV2_function,
    getWirelessProfiles_function,
    getConfigTaskDetails_function,
    getMulticastVirtualNetworkCount_function,
    getTagCount_function,
    getDeviceSummary_function,
    getAuthenticationProfiles_function,
    getAllFlexibleReportSchedules_function,
    getFunctionalCapabilityById_function,
    getFabricSites_function,
    getWorkflows_function,
    getDeviceConfigById_function,
    getOrganizationListForMeraki_function,
    getPollingIntervalById_function,
    getNotifications_function,
    getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId_function,
    getDeviceConfigCount_function,
    retrieveANetworkProfileForSitesById_function,
    getAuditLogRecords_function,
    getSupervisorCardDetail_function,
    retrieveImageDistributionSettingsForASite_function,
    getEventArtifacts_function,
    retrievesValidationWorkflowDetails_function,
    getModuleCount_function,
    getTransitNetworksCount_function,
    getAllExecutionDetailsForAGivenReport_function,
    getPortChannelCount_function,
    getAuditLogParentRecords_function,
    retrieveDNSSettingsForASite_function,
    getEmailDestination_function,
    retrieveLicenseSetting_function,
    getMulticast_function,
    getFabricDevicesCount_function,
    getLayer3VirtualNetworksCount_function,
    getDevicesDiscoveredById_function,
    getTaskById_function,
    getDiscoveredDevicesByRange_function,
    retrievesTheTotalCountOfClientsByApplyingBasicFiltering_function,
    retrievesTheListOfNetworkDeviceProductNames_function,
    getConnectedDeviceDetail_function,
    getDevicesThatAreAssignedToASite_function,
    retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned_function,
    getListOfDiscoveriesByDiscoveryId_function,
    getPhysicalTopology_function,
    getSiteTopology_function,
    retrieveNTPSettingsForASite_function,
    countOfNetworkDeviceImageUpdates_function,
    getPlannedAccessPointsForBuilding_function,
    countOfNetworkProductNames_function,
    getAccessPointConfiguration_function,
    getDeviceConfigForAllDevices_function,
    getTopologyDetails_function,
    getFabricDevicesLayer3HandoffsWithIpTransitCount_function,
    getFabricDevicesLayer3HandoffsWithSdaTransitCount_function,
    retrievesTheListOfNetworkProfilesForSites_function,
    getFunctionalCapabilityForDevices_function,
    getPortAssignments_function,
    getSiteNotAssignedNetworkDevices_function,
    getAccessPointRebootTaskResult_function,
    getDeviceDetail_function,
    getSiteNotAssignedNetworkDevicesCount_function,
    getDeviceBySerialNumber_function,
    getApplicationCount_function,
    getComplianceStatusCount_function,
    getTasks_function,
    getListOfChildEventsForTheGivenWirelessClientEvent_function,
    getProvisioningSettings_function,
    getInterfaceById_function,
    getInterfaceInfoById_function,
    getTaskByOperationId_function,
    getL3TopologyDetails_function,
    getAdvisoryDeviceDetail_function,
    getConnectorTypes_function,
    retrieveDHCPSettingsForASite_function,
    getAnycastGatewayCount_function,
    getNetworkDeviceByPaginationRange_function,
    getSiteAssignedNetworkDevice_function,
    getAllInterfaces_function,
    getWirelessLanControllerDetailsById_function,
    getDevicesPerAdvisory_function,
    getAccessPointConfigurationTaskResult_function,
    getComplianceDetail_function,
    getGlobalCredentials_function,
    getComplianceStatus_function,
    getProvisionedDevicesCount_function,
    getInterfacesCount_function,
    getModules_function,
    retrievesTheCountOfAssignedNetworkDeviceProducts_function,
    getDeviceHistory_function,
    getApplicationPolicyQueuingProfileCount_function,
    getTaskTree_function,
    getDiscoveredNetworkDevicesByDiscoveryId_function,
    getSiteAssignedNetworkDevicesCount_function,
    getNetworkV2_function,
    getDeviceValuesThatMatchFullyOrPartiallyAnAttribute_function,
    getApplications_function,
    getNetwork_function,
    getTransitPeerNetworkInfo_function,
    getApplicationSets_function,
    getApplicationsCount_function,
    getGlobalPool_function,
    getProvisionedWiredDevice_function,
    getDeviceCredentialDetails_function,
    getServiceProviderDetails_function,
    getSite_function,
    getVirtualNetworkSummary_function,
    getWirelessProfile_function,
    getIssueEnrichmentDetails_function,
    getSiteCount_function,
    getClientEnrichmentDetails_function,
    getVirtualNetworkWithScalableGroups_function,
    getDynamicInterface_function,
    getApplicationSetsCount_function,
    getUserEnrichmentDetails_function,
    getDeviceEnrichmentDetails_function,
    getMembership_function,




    # Meraki
    list_all_clients_in_org,
    list_all_clients_in_org_by_name,
    get_network_alerts_history,
    list_all_devices_in_org,
    get_all_access_points,
    list_all_switches_in_org,
    list_all_cameras_in_org,



    # Meraki SDK
        getAdministeredIdentitiesMe,
    getAdministeredIdentitiesMeApiKeys,
    getAdministeredLicensingSubscriptionEntitlements,
    getAdministeredLicensingSubscriptionSubscriptions,
    getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses,
    getDevice,
    getDeviceApplianceDhcpSubnets,
    getDeviceAppliancePerformance,
    getDeviceAppliancePrefixesDelegated,
    getDeviceAppliancePrefixesDelegatedVlanAssignments,
    getDeviceApplianceRadioSettings,
    getDeviceApplianceUplinksSettings,
    getDeviceCameraAnalyticsLive,
    getDeviceCameraAnalyticsOverview,
    getDeviceCameraAnalyticsRecent,
    getDeviceCameraAnalyticsZones,
    getDeviceCameraAnalyticsZoneHistory,
    getDeviceCameraCustomAnalytics,
    getDeviceCameraQualityAndRetention,
    getDeviceCameraSense,
    getDeviceCameraSenseObjectDetectionModels,
    getDeviceCameraVideoSettings,
    getDeviceCameraVideoLink,
    getDeviceCameraWirelessProfiles,
    getDeviceCellularSims,
    getDeviceCellularGatewayLan,
    getDeviceCellularGatewayPortForwardingRules,
    getDeviceClients,
    getDeviceLiveToolsArpTable,
    getDeviceLiveToolsCableTest,
    getDeviceLiveToolsLedsBlink,
    getDeviceLiveToolsPing,
    getDeviceLiveToolsPingDevice,
    getDeviceLiveToolsThroughputTest,
    getDeviceLiveToolsWakeOnLan,
    getDeviceLldpCdp,
    getDeviceLossAndLatencyHistory,
    getDeviceManagementInterface,
    getDeviceSensorCommands,
    getDeviceSensorCommand,
    getDeviceSensorRelationships,
    getDeviceSwitchPorts,
    getDeviceSwitchPortsStatuses,
    getDeviceSwitchPortsStatusesPackets,
    getDeviceSwitchPort,
    getDeviceSwitchRoutingInterfaces,
    getDeviceSwitchRoutingInterface,
    getDeviceSwitchRoutingInterfaceDhcp,
    getDeviceSwitchRoutingStaticRoutes,
    getDeviceSwitchRoutingStaticRoute,
    getDeviceSwitchWarmSpare,
    getDeviceWirelessBluetoothSettings,
    getDeviceWirelessConnectionStats,
    getDeviceWirelessElectronicShelfLabel,
    getDeviceWirelessLatencyStats,
    getDeviceWirelessRadioSettings,
    getDeviceWirelessStatus,
    getNetwork,
    getNetworkAlertsHistory,
    getNetworkAlertsSettings,
    getNetworkApplianceClientSecurityEvents,
    getNetworkApplianceConnectivityMonitoringDestinations,
    getNetworkApplianceContentFiltering,
    getNetworkApplianceContentFilteringCategories,
    getNetworkApplianceFirewallCellularFirewallRules,
    getNetworkApplianceFirewallFirewalledServices,
    getNetworkApplianceFirewallFirewalledService,
    getNetworkApplianceFirewallInboundCellularFirewallRules,
    getNetworkApplianceFirewallInboundFirewallRules,
    getNetworkApplianceFirewallL3FirewallRules,
    getNetworkApplianceFirewallL7FirewallRules,
    getNetworkApplianceFirewallL7FirewallRulesApplicationCategories,
    getNetworkApplianceFirewallOneToManyNatRules,
    getNetworkApplianceFirewallOneToOneNatRules,
    getNetworkApplianceFirewallPortForwardingRules,
    getNetworkApplianceFirewallSettings,
    getNetworkAppliancePorts,
    getNetworkAppliancePort,
    getNetworkAppliancePrefixesDelegatedStatics,
    getNetworkAppliancePrefixesDelegatedStatic,
    getNetworkApplianceRfProfiles,
    getNetworkApplianceRfProfile,
    getNetworkApplianceSecurityEvents,
    getNetworkApplianceSecurityIntrusion,
    getNetworkApplianceSecurityMalware,
    getNetworkApplianceSettings,
    getNetworkApplianceSingleLan,
    getNetworkApplianceSsids,
    getNetworkApplianceSsid,
    getNetworkApplianceStaticRoutes,
    getNetworkApplianceStaticRoute,
    getNetworkApplianceTrafficShaping,
    getNetworkApplianceTrafficShapingCustomPerformanceClasses,
    getNetworkApplianceTrafficShapingCustomPerformanceClass,
    getNetworkApplianceTrafficShapingRules,
    getNetworkApplianceTrafficShapingUplinkBandwidth,
    getNetworkApplianceTrafficShapingUplinkSelection,
    getNetworkApplianceUplinksUsageHistory,
    getNetworkApplianceVlans,
    getNetworkApplianceVlansSettings,
    getNetworkApplianceVlan,
    getNetworkApplianceVpnBgp,
    getNetworkApplianceVpnSiteToSiteVpn,
    getNetworkApplianceWarmSpare,
    getNetworkBluetoothClients,
    getNetworkBluetoothClient,
    getNetworkCameraQualityRetentionProfiles,
    getNetworkCameraQualityRetentionProfile,
    getNetworkCameraSchedules,
    getNetworkCameraWirelessProfiles,
    getNetworkCameraWirelessProfile,
    getNetworkCellularGatewayConnectivityMonitoringDestinations,
    getNetworkCellularGatewayDhcp,
    getNetworkCellularGatewaySubnetPool,
    getNetworkCellularGatewayUplink,
    getNetworkClients,
    getNetworkClientsApplicationUsage,
    getNetworkClientsBandwidthUsageHistory,
    getNetworkClientsOverview,
    getNetworkClientsUsageHistories,
    getNetworkClient,
    getNetworkClientPolicy,
    getNetworkClientSplashAuthorizationStatus,
    getNetworkClientTrafficHistory,
    getNetworkClientUsageHistory,
    getNetworkDevices,
    getNetworkEvents,
    getNetworkEventsEventTypes,
    getNetworkFirmwareUpgrades,
    getNetworkFirmwareUpgradesStagedEvents,
    getNetworkFirmwareUpgradesStagedGroups,
    getNetworkFirmwareUpgradesStagedGroup,
    getNetworkFirmwareUpgradesStagedStages,
    getNetworkFloorPlans,
    getNetworkFloorPlan,
    getNetworkGroupPolicies,
    getNetworkGroupPolicy,
    getNetworkHealthAlerts,
    getNetworkInsightApplicationHealthByTime,
    getNetworkMerakiAuthUsers,
    getNetworkMerakiAuthUser,
    getNetworkMqttBrokers,
    getNetworkMqttBroker,
    getNetworkNetflow,
    getNetworkNetworkHealthChannelUtilization,
    getNetworkPiiPiiKeys,
    getNetworkPiiRequests,
    getNetworkPiiRequest,
    getNetworkPiiSmDevicesForKey,
    getNetworkPiiSmOwnersForKey,
    getNetworkPoliciesByClient,
    getNetworkSensorAlertsCurrentOverviewByMetric,
    getNetworkSensorAlertsOverviewByMetric,
    getNetworkSensorAlertsProfiles,
    getNetworkSensorAlertsProfile,
    getNetworkSensorMqttBrokers,
    getNetworkSensorMqttBroker,
    getNetworkSensorRelationships,
    getNetworkSettings,
    getNetworkSmBypassActivationLockAttempt,
    getNetworkSmDevices,
    getNetworkSmDeviceCellularUsageHistory,
    getNetworkSmDeviceCerts,
    getNetworkSmDeviceConnectivity,
    getNetworkSmDeviceDesktopLogs,
    getNetworkSmDeviceDeviceCommandLogs,
    getNetworkSmDeviceDeviceProfiles,
    getNetworkSmDeviceNetworkAdapters,
    getNetworkSmDevicePerformanceHistory,
    getNetworkSmDeviceRestrictions,
    getNetworkSmDeviceSecurityCenters,
    getNetworkSmDeviceSoftwares,
    getNetworkSmDeviceWlanLists,
    getNetworkSmProfiles,
    getNetworkSmTargetGroups,
    getNetworkSmTargetGroup,
    getNetworkSmTrustedAccessConfigs,
    getNetworkSmUserAccessDevices,
    getNetworkSmUsers,
    getNetworkSmUserDeviceProfiles,
    getNetworkSmUserSoftwares,
    getNetworkSnmp,
    getNetworkSplashLoginAttempts,
    getNetworkSwitchAccessControlLists,
    getNetworkSwitchAccessPolicies,
    getNetworkSwitchAccessPolicy,
    getNetworkSwitchAlternateManagementInterface,
    getNetworkSwitchDhcpV4ServersSeen,
    getNetworkSwitchDhcpServerPolicy,
    getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers,
    getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice,
    getNetworkSwitchDscpToCosMappings,
    getNetworkSwitchLinkAggregations,
    getNetworkSwitchMtu,
    getNetworkSwitchPortSchedules,
    getNetworkSwitchQosRules,
    getNetworkSwitchQosRulesOrder,
    getNetworkSwitchQosRule,
    getNetworkSwitchRoutingMulticast,
    getNetworkSwitchRoutingMulticastRendezvousPoints,
    getNetworkSwitchRoutingMulticastRendezvousPoint,
    getNetworkSwitchRoutingOspf,
    getNetworkSwitchSettings,
    getNetworkSwitchStacks,
    getNetworkSwitchStack,
    getNetworkSwitchStackRoutingInterfaces,
    getNetworkSwitchStackRoutingInterface,
    getNetworkSwitchStackRoutingInterfaceDhcp,
    getNetworkSwitchStackRoutingStaticRoutes,
    getNetworkSwitchStackRoutingStaticRoute,
    getNetworkSwitchStormControl,
    getNetworkSwitchStp,
    getNetworkSyslogServers,
    getNetworkTopologyLinkLayer,
    getNetworkTraffic,
    getNetworkTrafficAnalysis,
    getNetworkTrafficShapingApplicationCategories,
    getNetworkTrafficShapingDscpTaggingOptions,
    getNetworkVlanProfiles,
    getNetworkVlanProfilesAssignmentsByDevice,
    getNetworkVlanProfile,
    getNetworkWebhooksHttpServers,
    getNetworkWebhooksHttpServer,
    getNetworkWebhooksPayloadTemplates,
    getNetworkWebhooksPayloadTemplate,
    getNetworkWebhooksWebhookTest,
    getNetworkWirelessAirMarshal,
    getNetworkWirelessAlternateManagementInterface,
    getNetworkWirelessBilling,
    getNetworkWirelessBluetoothSettings,
    getNetworkWirelessChannelUtilizationHistory,
    getNetworkWirelessClientCountHistory,
    getNetworkWirelessClientsConnectionStats,
    getNetworkWirelessClientsLatencyStats,
    getNetworkWirelessClientConnectionStats,
    getNetworkWirelessClientConnectivityEvents,
    getNetworkWirelessClientLatencyHistory,
    getNetworkWirelessClientLatencyStats,
    getNetworkWirelessConnectionStats,
    getNetworkWirelessDataRateHistory,
    getNetworkWirelessDevicesConnectionStats,
    getNetworkWirelessDevicesLatencyStats,
    getNetworkWirelessElectronicShelfLabel,
    getNetworkWirelessElectronicShelfLabelConfiguredDevices,
    getNetworkWirelessEthernetPortsProfiles,
    getNetworkWirelessEthernetPortsProfile,
    getNetworkWirelessFailedConnections,
    getNetworkWirelessLatencyHistory,
    getNetworkWirelessLatencyStats,
    getNetworkWirelessMeshStatuses,
    getNetworkWirelessRfProfiles,
    getNetworkWirelessRfProfile,
    getNetworkWirelessSettings,
    getNetworkWirelessSignalQualityHistory,
    getNetworkWirelessSsids,
    getNetworkWirelessSsid,
    getNetworkWirelessSsidBonjourForwarding,
    getNetworkWirelessSsidDeviceTypeGroupPolicies,
    getNetworkWirelessSsidEapOverride,
    getNetworkWirelessSsidFirewallL3FirewallRules,
    getNetworkWirelessSsidFirewallL7FirewallRules,
    getNetworkWirelessSsidHotspot20,
    getNetworkWirelessSsidIdentityPsks,
    getNetworkWirelessSsidIdentityPsk,
    getNetworkWirelessSsidSchedules,
    getNetworkWirelessSsidSplashSettings,
    getNetworkWirelessSsidTrafficShapingRules,
    getNetworkWirelessSsidVpn,
    getNetworkWirelessUsageHistory,
    getOrganizations,
    getOrganization,
    getOrganizationActionBatches,
    getOrganizationActionBatch,
    getOrganizationAdaptivePolicyAcls,
    getOrganizationAdaptivePolicyAcl,
    getOrganizationAdaptivePolicyGroups,
    getOrganizationAdaptivePolicyGroup,
    getOrganizationAdaptivePolicyOverview,
    getOrganizationAdaptivePolicyPolicies,
    getOrganizationAdaptivePolicyPolicy,
    getOrganizationAdaptivePolicySettings,
    getOrganizationAdmins,
    getOrganizationAlertsProfiles,
    getOrganizationApiRequests,
    getOrganizationApiRequestsOverview,
    getOrganizationApiRequestsOverviewResponseCodesByInterval,
    getOrganizationApplianceSecurityEvents,
    getOrganizationApplianceSecurityIntrusion,
    getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork,
    getOrganizationApplianceUplinkStatuses,
    getOrganizationApplianceUplinksStatusesOverview,
    getOrganizationApplianceUplinksUsageByNetwork,
    getOrganizationApplianceVpnStats,
    getOrganizationApplianceVpnStatuses,
    getOrganizationApplianceVpnThirdPartyVPNPeers,
    getOrganizationApplianceVpnVpnFirewallRules,
    getOrganizationAssuranceAlerts,
    getOrganizationAssuranceAlertsOverview,
    getOrganizationAssuranceAlertsOverviewByNetwork,
    getOrganizationAssuranceAlertsOverviewByType,
    getOrganizationAssuranceAlertsOverviewHistorical,
    getOrganizationAssuranceAlert,
    getOrganizationBrandingPolicies,
    getOrganizationBrandingPoliciesPriorities,
    getOrganizationBrandingPolicy,
    getOrganizationCameraBoundariesAreasByDevice,
    getOrganizationCameraBoundariesLinesByDevice,
    getOrganizationCameraCustomAnalyticsArtifacts,
    getOrganizationCameraCustomAnalyticsArtifact,
    getOrganizationCameraDetectionsHistoryByBoundaryByInterval,
    getOrganizationCameraOnboardingStatuses,
    getOrganizationCameraPermissions,
    getOrganizationCameraPermission,
    getOrganizationCameraRoles,
    getOrganizationCameraRole,
    getOrganizationCellularGatewayEsimsInventory,
    getOrganizationCellularGatewayEsimsServiceProviders,
    getOrganizationCellularGatewayEsimsServiceProvidersAccounts,
    getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans,
    getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans,
    getOrganizationCellularGatewayUplinkStatuses,
    getOrganizationClientsBandwidthUsageHistory,
    getOrganizationClientsOverview,
    getOrganizationClientsSearch,
    getOrganizationConfigTemplates,
    getOrganizationConfigTemplate,
    getOrganizationConfigTemplateSwitchProfiles,
    getOrganizationConfigTemplateSwitchProfilePorts,
    getOrganizationConfigTemplateSwitchProfilePort,
    getOrganizationConfigurationChanges,
    getOrganizationDevices,
    getOrganizationDevicesAvailabilities,
    getOrganizationDevicesAvailabilitiesChangeHistory,
    getOrganizationDevicesOverviewByModel,
    getOrganizationDevicesPowerModulesStatusesByDevice,
    getOrganizationDevicesProvisioningStatuses,
    getOrganizationDevicesStatuses,
    getOrganizationDevicesStatusesOverview,
    getOrganizationDevicesUplinksAddressesByDevice,
    getOrganizationDevicesUplinksLossAndLatency,
    getOrganizationEarlyAccessFeatures,
    getOrganizationEarlyAccessFeaturesOptIns,
    getOrganizationEarlyAccessFeaturesOptIn,
    getOrganizationFirmwareUpgrades,
    getOrganizationFirmwareUpgradesByDevice,
    getOrganizationFloorPlansAutoLocateDevices,
    getOrganizationFloorPlansAutoLocateStatuses,
    getOrganizationInsightApplications,
    getOrganizationInsightMonitoredMediaServers,
    getOrganizationInsightMonitoredMediaServer,
    getOrganizationInventoryDevices,
    getOrganizationInventoryDevicesSwapsBulk,
    getOrganizationInventoryDevice,
    getOrganizationInventoryOnboardingCloudMonitoringImports,
    getOrganizationInventoryOnboardingCloudMonitoringNetworks,
    getOrganizationLicenses,
    getOrganizationLicensesOverview,
    getOrganizationLicense,
    getOrganizationLicensingCotermLicenses,
    getOrganizationLoginSecurity,
    getOrganizationNetworks,
    getOrganizationOpenapiSpec,
    getOrganizationPolicyObjects,
    getOrganizationPolicyObjectsGroups,
    getOrganizationPolicyObjectsGroup,
    getOrganizationPolicyObject,
    getOrganizationSaml,
    getOrganizationSamlIdps,
    getOrganizationSamlIdp,
    getOrganizationSamlRoles,
    getOrganizationSamlRole,
    getOrganizationSensorReadingsHistory,
    getOrganizationSensorReadingsLatest,
    getOrganizationSmAdminsRoles,
    getOrganizationSmAdminsRole,
    getOrganizationSmApnsCert,
    getOrganizationSmSentryPoliciesAssignmentsByNetwork,
    getOrganizationSmVppAccounts,
    getOrganizationSmVppAccount,
    getOrganizationSnmp,
    getOrganizationSplashAsset,
    getOrganizationSplashThemes,
    getOrganizationSummarySwitchPowerHistory,
    getOrganizationSummaryTopAppliancesByUtilization,
    getOrganizationSummaryTopApplicationsByUsage,
    getOrganizationSummaryTopApplicationsCategoriesByUsage,
    getOrganizationSummaryTopClientsByUsage,
    getOrganizationSummaryTopClientsManufacturersByUsage,
    getOrganizationSummaryTopDevicesByUsage,
    getOrganizationSummaryTopDevicesModelsByUsage,
    getOrganizationSummaryTopNetworksByStatus,
    getOrganizationSummaryTopSsidsByUsage,
    getOrganizationSummaryTopSwitchesByEnergyUsage,
    getOrganizationSwitchPortsBySwitch,
    getOrganizationSwitchPortsClientsOverviewByDevice,
    getOrganizationSwitchPortsOverview,
    getOrganizationSwitchPortsStatusesBySwitch,
    getOrganizationSwitchPortsTopologyDiscoveryByDevice,
    getOrganizationUplinksStatuses,
    getOrganizationWebhooksAlertTypes,
    getOrganizationWebhooksCallbacksStatus,
    getOrganizationWebhooksLogs,
    getOrganizationWirelessAirMarshalRules,
    getOrganizationWirelessAirMarshalSettingsByNetwork,
    getOrganizationWirelessClientsOverviewByDevice,
    getOrganizationWirelessDevicesChannelUtilizationByDevice,
    getOrganizationWirelessDevicesChannelUtilizationByNetwork,
    getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval,
    getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval,
    getOrganizationWirelessDevicesEthernetStatuses,
    getOrganizationWirelessDevicesPacketLossByClient,
    getOrganizationWirelessDevicesPacketLossByDevice,
    getOrganizationWirelessDevicesPacketLossByNetwork,
    getOrganizationWirelessDevicesWirelessControllersByDevice,
    getOrganizationWirelessRfProfilesAssignmentsByDevice,
    getOrganizationWirelessSsidsStatusesByDevice,

       


    # Webex
    get_webex_meetings_function,
    get_webex_meeting_by_id_function,
]
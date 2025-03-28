################################################################################
# cisco-data-bridge-domain-index/cisco_integrations/cisco_catalyst_sdk_client.py
# Copyright (c) 2025 Jeff Teeter, Ph.D.
# Cisco Systems, Inc.
# Licensed under the Apache License, Version 2.0 (see LICENSE)
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import logging

from dnacentersdk import ApiError

from typing import Dict, Any


class CatalystCenterClientCustom:

    """Filtered CatalystCenter client with only matched read-only methods.

    Each method includes docstrings describing the input arguments and return type.
    """


    def __init__(self, sdk):

        """Initialize with a DNACenterSDK client instance."""

        self.sdk = sdk


    def countOfEventSubscriptions(self, event_ids, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'countOfEventSubscriptions'.
        Calls 'self.sdk.countOfEventSubscriptions' with the same parameters.
        
        :param event_ids: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.countOfEventSubscriptions(event_ids, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in countOfEventSubscriptions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in countOfEventSubscriptions: {ex}")
            return {"error": str(ex)}

    def countOfEvents(self, tags, event_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'countOfEvents'.
        Calls 'self.sdk.countOfEvents' with the same parameters.
        
        :param tags: (Inferred from the method signature)
        :param event_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.countOfEvents(tags, event_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in countOfEvents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in countOfEvents: {ex}")
            return {"error": str(ex)}

    def countOfNetworkDeviceImageUpdates(self, end_time=None, host_name=None, id=None, image_name=None, management_address=None, network_device_id=None, parent_id=None, start_time=None, status=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'countOfNetworkDeviceImageUpdates'.
        Calls 'self.sdk.countOfNetworkDeviceImageUpdates' with the same parameters.
        
        :param end_time: (Inferred from the method signature)
        :param host_name: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :param image_name: (Inferred from the method signature)
        :param management_address: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param parent_id: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param status: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.countOfNetworkDeviceImageUpdates(end_time, host_name, id, image_name, management_address, network_device_id, parent_id, start_time, status, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in countOfNetworkDeviceImageUpdates: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in countOfNetworkDeviceImageUpdates: {ex}")
            return {"error": str(ex)}

    def countOfNetworkProductNames(self, product_id=None, product_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'countOfNetworkProductNames'.
        Calls 'self.sdk.countOfNetworkProductNames' with the same parameters.
        
        :param product_id: (Inferred from the method signature)
        :param product_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.countOfNetworkProductNames(product_id, product_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in countOfNetworkProductNames: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in countOfNetworkProductNames: {ex}")
            return {"error": str(ex)}

    def countOfNotifications(self, category=None, domain=None, end_time=None, event_ids=None, severity=None, source=None, start_time=None, sub_domain=None, type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'countOfNotifications'.
        Calls 'self.sdk.countOfNotifications' with the same parameters.
        
        :param category: (Inferred from the method signature)
        :param domain: (Inferred from the method signature)
        :param end_time: (Inferred from the method signature)
        :param event_ids: (Inferred from the method signature)
        :param severity: (Inferred from the method signature)
        :param source: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param sub_domain: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.countOfNotifications(category, domain, end_time, event_ids, severity, source, start_time, sub_domain, type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in countOfNotifications: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in countOfNotifications: {ex}")
            return {"error": str(ex)}

    def countTheNumberOfEvents(self, device_family, ap_mac=None, client_mac=None, end_time=None, message_type=None, network_device_id=None, network_device_name=None, severity=None, site_hierarchy_id=None, site_id=None, start_time=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'countTheNumberOfEvents'.
        Calls 'self.sdk.countTheNumberOfEvents' with the same parameters.
        
        :param device_family: (Inferred from the method signature)
        :param ap_mac: (Inferred from the method signature)
        :param client_mac: (Inferred from the method signature)
        :param end_time: (Inferred from the method signature)
        :param message_type: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param network_device_name: (Inferred from the method signature)
        :param severity: (Inferred from the method signature)
        :param site_hierarchy_id: (Inferred from the method signature)
        :param site_id: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.countTheNumberOfEvents(device_family, ap_mac, client_mac, end_time, message_type, network_device_id, network_device_name, severity, site_hierarchy_id, site_id, start_time, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in countTheNumberOfEvents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in countTheNumberOfEvents: {ex}")
            return {"error": str(ex)}

    def getAScheduledReport(self, report_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAScheduledReport'.
        Calls 'self.sdk.getAScheduledReport' with the same parameters.
        
        :param report_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAScheduledReport(report_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAScheduledReport: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAScheduledReport: {ex}")
            return {"error": str(ex)}

    def getAccessPointConfiguration(self, ap_mode=None, ap_model=None, key=None, limit=None, mesh_role=None, offset=None, provisioned=None, wlc_ip_address=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAccessPointConfiguration'.
        Calls 'self.sdk.getAccessPointConfiguration' with the same parameters.
        
        :param ap_mode: (Inferred from the method signature)
        :param ap_model: (Inferred from the method signature)
        :param key: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param mesh_role: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param provisioned: (Inferred from the method signature)
        :param wlc_ip_address: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAccessPointConfiguration(ap_mode, ap_model, key, limit, mesh_role, offset, provisioned, wlc_ip_address, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAccessPointConfiguration: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAccessPointConfiguration: {ex}")
            return {"error": str(ex)}

    def getAccessPointConfigurationTaskResult(self, task_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAccessPointConfigurationTaskResult'.
        Calls 'self.sdk.getAccessPointConfigurationTaskResult' with the same parameters.
        
        :param task_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAccessPointConfigurationTaskResult(task_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAccessPointConfigurationTaskResult: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAccessPointConfigurationTaskResult: {ex}")
            return {"error": str(ex)}

    def getAccessPointRebootTaskResult(self, parent_task_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAccessPointRebootTaskResult'.
        Calls 'self.sdk.getAccessPointRebootTaskResult' with the same parameters.
        
        :param parent_task_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAccessPointRebootTaskResult(parent_task_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAccessPointRebootTaskResult: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAccessPointRebootTaskResult: {ex}")
            return {"error": str(ex)}

    def getAdvisoriesList(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAdvisoriesList'.
        Calls 'self.sdk.getAdvisoriesList' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAdvisoriesList(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAdvisoriesList: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAdvisoriesList: {ex}")
            return {"error": str(ex)}

    def getAdvisoriesPerDevice(self, device_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAdvisoriesPerDevice'.
        Calls 'self.sdk.getAdvisoriesPerDevice' with the same parameters.
        
        :param device_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAdvisoriesPerDevice(device_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAdvisoriesPerDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAdvisoriesPerDevice: {ex}")
            return {"error": str(ex)}

    def getAdvisoriesSummary(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAdvisoriesSummary'.
        Calls 'self.sdk.getAdvisoriesSummary' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAdvisoriesSummary(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAdvisoriesSummary: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAdvisoriesSummary: {ex}")
            return {"error": str(ex)}

    def getAdvisoryDeviceDetail(self, device_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAdvisoryDeviceDetail'.
        Calls 'self.sdk.getAdvisoryDeviceDetail' with the same parameters.
        
        :param device_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAdvisoryDeviceDetail(device_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAdvisoryDeviceDetail: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAdvisoryDeviceDetail: {ex}")
            return {"error": str(ex)}

    def getAllExecutionDetailsForAGivenReport(self, report_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAllExecutionDetailsForAGivenReport'.
        Calls 'self.sdk.getAllExecutionDetailsForAGivenReport' with the same parameters.
        
        :param report_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAllExecutionDetailsForAGivenReport(report_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAllExecutionDetailsForAGivenReport: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAllExecutionDetailsForAGivenReport: {ex}")
            return {"error": str(ex)}

    def getAllFlexibleReportSchedules(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAllFlexibleReportSchedules'.
        Calls 'self.sdk.getAllFlexibleReportSchedules' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAllFlexibleReportSchedules(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAllFlexibleReportSchedules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAllFlexibleReportSchedules: {ex}")
            return {"error": str(ex)}

    def getAllGlobalCredentialsV2(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAllGlobalCredentialsV2'.
        Calls 'self.sdk.getAllGlobalCredentialsV2' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAllGlobalCredentialsV2(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAllGlobalCredentialsV2: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAllGlobalCredentialsV2: {ex}")
            return {"error": str(ex)}

    def getAllInterfaces(self, last_input_time=None, last_output_time=None, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAllInterfaces'.
        Calls 'self.sdk.getAllInterfaces' with the same parameters.
        
        :param last_input_time: (Inferred from the method signature)
        :param last_output_time: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAllInterfaces(last_input_time, last_output_time, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAllInterfaces: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAllInterfaces: {ex}")
            return {"error": str(ex)}

    def getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId(self, id, attribute=None, view=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId'.
        Calls 'self.sdk.getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param attribute: (Inferred from the method signature)
        :param view: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId(id, attribute, view, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId: {ex}")
            return {"error": str(ex)}

    def getAllViewGroups(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAllViewGroups'.
        Calls 'self.sdk.getAllViewGroups' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAllViewGroups(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAllViewGroups: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAllViewGroups: {ex}")
            return {"error": str(ex)}

    def getAnycastGatewayCount(self, fabric_id=None, ip_pool_name=None, virtual_network_name=None, vlan_id=None, vlan_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAnycastGatewayCount'.
        Calls 'self.sdk.getAnycastGatewayCount' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param ip_pool_name: (Inferred from the method signature)
        :param virtual_network_name: (Inferred from the method signature)
        :param vlan_id: (Inferred from the method signature)
        :param vlan_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAnycastGatewayCount(fabric_id, ip_pool_name, virtual_network_name, vlan_id, vlan_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAnycastGatewayCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAnycastGatewayCount: {ex}")
            return {"error": str(ex)}

    def getAnycastGateways(self, fabric_id=None, id=None, ip_pool_name=None, limit=None, offset=None, virtual_network_name=None, vlan_id=None, vlan_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAnycastGateways'.
        Calls 'self.sdk.getAnycastGateways' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :param ip_pool_name: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param virtual_network_name: (Inferred from the method signature)
        :param vlan_id: (Inferred from the method signature)
        :param vlan_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAnycastGateways(fabric_id, id, ip_pool_name, limit, offset, virtual_network_name, vlan_id, vlan_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAnycastGateways: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAnycastGateways: {ex}")
            return {"error": str(ex)}

    def getApplicationCount(self, scalable_group_type, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getApplicationCount'.
        Calls 'self.sdk.getApplicationCount' with the same parameters.
        
        :param scalable_group_type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getApplicationCount(scalable_group_type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getApplicationCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getApplicationCount: {ex}")
            return {"error": str(ex)}

    def getApplicationPolicy(self, policy_scope=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getApplicationPolicy'.
        Calls 'self.sdk.getApplicationPolicy' with the same parameters.
        
        :param policy_scope: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getApplicationPolicy(policy_scope, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getApplicationPolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getApplicationPolicy: {ex}")
            return {"error": str(ex)}

    def getApplicationPolicyDefault(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getApplicationPolicyDefault'.
        Calls 'self.sdk.getApplicationPolicyDefault' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getApplicationPolicyDefault(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getApplicationPolicyDefault: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getApplicationPolicyDefault: {ex}")
            return {"error": str(ex)}

    def getApplicationPolicyQueuingProfile(self, name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getApplicationPolicyQueuingProfile'.
        Calls 'self.sdk.getApplicationPolicyQueuingProfile' with the same parameters.
        
        :param name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getApplicationPolicyQueuingProfile(name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getApplicationPolicyQueuingProfile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getApplicationPolicyQueuingProfile: {ex}")
            return {"error": str(ex)}

    def getApplicationPolicyQueuingProfileCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getApplicationPolicyQueuingProfileCount'.
        Calls 'self.sdk.getApplicationPolicyQueuingProfileCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getApplicationPolicyQueuingProfileCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getApplicationPolicyQueuingProfileCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getApplicationPolicyQueuingProfileCount: {ex}")
            return {"error": str(ex)}

    def getApplicationSetCount(self, scalable_group_type, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getApplicationSetCount'.
        Calls 'self.sdk.getApplicationSetCount' with the same parameters.
        
        :param scalable_group_type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getApplicationSetCount(scalable_group_type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getApplicationSetCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getApplicationSetCount: {ex}")
            return {"error": str(ex)}

    def getApplicationSets(self, limit=None, name=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getApplicationSets'.
        Calls 'self.sdk.getApplicationSets' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getApplicationSets(limit, name, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getApplicationSets: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getApplicationSets: {ex}")
            return {"error": str(ex)}

    def getApplicationSetsCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getApplicationSetsCount'.
        Calls 'self.sdk.getApplicationSetsCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getApplicationSetsCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getApplicationSetsCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getApplicationSetsCount: {ex}")
            return {"error": str(ex)}

    def getApplications(self, limit=None, name=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getApplications'.
        Calls 'self.sdk.getApplications' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getApplications(limit, name, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getApplications: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getApplications: {ex}")
            return {"error": str(ex)}

    def getApplicationsCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getApplicationsCount'.
        Calls 'self.sdk.getApplicationsCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getApplicationsCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getApplicationsCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getApplicationsCount: {ex}")
            return {"error": str(ex)}

    def getAuditLogParentRecords(self, category=None, context=None, description=None, device_id=None, domain=None, end_time=None, event_hierarchy=None, event_id=None, instance_id=None, is_system_events=None, limit=None, name=None, offset=None, order=None, severity=None, site_id=None, sort_by=None, source=None, start_time=None, sub_domain=None, user_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAuditLogParentRecords'.
        Calls 'self.sdk.getAuditLogParentRecords' with the same parameters.
        
        :param category: (Inferred from the method signature)
        :param context: (Inferred from the method signature)
        :param description: (Inferred from the method signature)
        :param device_id: (Inferred from the method signature)
        :param domain: (Inferred from the method signature)
        :param end_time: (Inferred from the method signature)
        :param event_hierarchy: (Inferred from the method signature)
        :param event_id: (Inferred from the method signature)
        :param instance_id: (Inferred from the method signature)
        :param is_system_events: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param severity: (Inferred from the method signature)
        :param site_id: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param source: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param sub_domain: (Inferred from the method signature)
        :param user_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAuditLogParentRecords(category, context, description, device_id, domain, end_time, event_hierarchy, event_id, instance_id, is_system_events, limit, name, offset, order, severity, site_id, sort_by, source, start_time, sub_domain, user_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAuditLogParentRecords: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAuditLogParentRecords: {ex}")
            return {"error": str(ex)}

    def getAuditLogRecords(self, category=None, context=None, description=None, device_id=None, domain=None, end_time=None, event_hierarchy=None, event_id=None, instance_id=None, is_system_events=None, limit=None, name=None, offset=None, order=None, parent_instance_id=None, severity=None, site_id=None, sort_by=None, source=None, start_time=None, sub_domain=None, user_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAuditLogRecords'.
        Calls 'self.sdk.getAuditLogRecords' with the same parameters.
        
        :param category: (Inferred from the method signature)
        :param context: (Inferred from the method signature)
        :param description: (Inferred from the method signature)
        :param device_id: (Inferred from the method signature)
        :param domain: (Inferred from the method signature)
        :param end_time: (Inferred from the method signature)
        :param event_hierarchy: (Inferred from the method signature)
        :param event_id: (Inferred from the method signature)
        :param instance_id: (Inferred from the method signature)
        :param is_system_events: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param parent_instance_id: (Inferred from the method signature)
        :param severity: (Inferred from the method signature)
        :param site_id: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param source: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param sub_domain: (Inferred from the method signature)
        :param user_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAuditLogRecords(category, context, description, device_id, domain, end_time, event_hierarchy, event_id, instance_id, is_system_events, limit, name, offset, order, parent_instance_id, severity, site_id, sort_by, source, start_time, sub_domain, user_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAuditLogRecords: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAuditLogRecords: {ex}")
            return {"error": str(ex)}

    def getAuditLogSummary(self, category=None, context=None, description=None, device_id=None, domain=None, end_time=None, event_hierarchy=None, event_id=None, instance_id=None, is_parent_only=None, is_system_events=None, name=None, parent_instance_id=None, severity=None, site_id=None, source=None, start_time=None, sub_domain=None, user_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAuditLogSummary'.
        Calls 'self.sdk.getAuditLogSummary' with the same parameters.
        
        :param category: (Inferred from the method signature)
        :param context: (Inferred from the method signature)
        :param description: (Inferred from the method signature)
        :param device_id: (Inferred from the method signature)
        :param domain: (Inferred from the method signature)
        :param end_time: (Inferred from the method signature)
        :param event_hierarchy: (Inferred from the method signature)
        :param event_id: (Inferred from the method signature)
        :param instance_id: (Inferred from the method signature)
        :param is_parent_only: (Inferred from the method signature)
        :param is_system_events: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param parent_instance_id: (Inferred from the method signature)
        :param severity: (Inferred from the method signature)
        :param site_id: (Inferred from the method signature)
        :param source: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param sub_domain: (Inferred from the method signature)
        :param user_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAuditLogSummary(category, context, description, device_id, domain, end_time, event_hierarchy, event_id, instance_id, is_parent_only, is_system_events, name, parent_instance_id, severity, site_id, source, start_time, sub_domain, user_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAuditLogSummary: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAuditLogSummary: {ex}")
            return {"error": str(ex)}

    def getAuthenticationAndPolicyServers(self, is_ise_enabled=None, role=None, state=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAuthenticationAndPolicyServers'.
        Calls 'self.sdk.getAuthenticationAndPolicyServers' with the same parameters.
        
        :param is_ise_enabled: (Inferred from the method signature)
        :param role: (Inferred from the method signature)
        :param state: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAuthenticationAndPolicyServers(is_ise_enabled, role, state, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAuthenticationAndPolicyServers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAuthenticationAndPolicyServers: {ex}")
            return {"error": str(ex)}

    def getAuthenticationProfiles(self, authentication_profile_name=None, fabric_id=None, is_global_authentication_profile=None, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getAuthenticationProfiles'.
        Calls 'self.sdk.getAuthenticationProfiles' with the same parameters.
        
        :param authentication_profile_name: (Inferred from the method signature)
        :param fabric_id: (Inferred from the method signature)
        :param is_global_authentication_profile: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getAuthenticationProfiles(authentication_profile_name, fabric_id, is_global_authentication_profile, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getAuthenticationProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAuthenticationProfiles: {ex}")
            return {"error": str(ex)}

    def getChassisDetailsForDevice(self, device_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getChassisDetailsForDevice'.
        Calls 'self.sdk.getChassisDetailsForDevice' with the same parameters.
        
        :param device_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getChassisDetailsForDevice(device_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getChassisDetailsForDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getChassisDetailsForDevice: {ex}")
            return {"error": str(ex)}

    def getClientDetail(self, mac_address, timestamp=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getClientDetail'.
        Calls 'self.sdk.getClientDetail' with the same parameters.
        
        :param mac_address: (Inferred from the method signature)
        :param timestamp: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getClientDetail(mac_address, timestamp, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getClientDetail: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getClientDetail: {ex}")
            return {"error": str(ex)}

    def getClientEnrichmentDetails(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getClientEnrichmentDetails'.
        Calls 'self.sdk.getClientEnrichmentDetails' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getClientEnrichmentDetails(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getClientEnrichmentDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getClientEnrichmentDetails: {ex}")
            return {"error": str(ex)}

    def getComplianceDetail(self, compliance_status=None, compliance_type=None, device_uuid=None, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getComplianceDetail'.
        Calls 'self.sdk.getComplianceDetail' with the same parameters.
        
        :param compliance_status: (Inferred from the method signature)
        :param compliance_type: (Inferred from the method signature)
        :param device_uuid: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getComplianceDetail(compliance_status, compliance_type, device_uuid, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getComplianceDetail: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getComplianceDetail: {ex}")
            return {"error": str(ex)}

    def getComplianceDetailCount(self, compliance_status=None, compliance_type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getComplianceDetailCount'.
        Calls 'self.sdk.getComplianceDetailCount' with the same parameters.
        
        :param compliance_status: (Inferred from the method signature)
        :param compliance_type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getComplianceDetailCount(compliance_status, compliance_type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getComplianceDetailCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getComplianceDetailCount: {ex}")
            return {"error": str(ex)}

    def getComplianceStatus(self, compliance_status=None, device_uuid=None, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getComplianceStatus'.
        Calls 'self.sdk.getComplianceStatus' with the same parameters.
        
        :param compliance_status: (Inferred from the method signature)
        :param device_uuid: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getComplianceStatus(compliance_status, device_uuid, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getComplianceStatus: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getComplianceStatus: {ex}")
            return {"error": str(ex)}

    def getComplianceStatusCount(self, compliance_status=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getComplianceStatusCount'.
        Calls 'self.sdk.getComplianceStatusCount' with the same parameters.
        
        :param compliance_status: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getComplianceStatusCount(compliance_status, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getComplianceStatusCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getComplianceStatusCount: {ex}")
            return {"error": str(ex)}

    def getConfigTaskDetails(self, parent_task_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getConfigTaskDetails'.
        Calls 'self.sdk.getConfigTaskDetails' with the same parameters.
        
        :param parent_task_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getConfigTaskDetails(parent_task_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getConfigTaskDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getConfigTaskDetails: {ex}")
            return {"error": str(ex)}

    def getConfigurationArchiveDetails(self, created_by=None, created_time=None, device_id=None, file_type=None, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getConfigurationArchiveDetails'.
        Calls 'self.sdk.getConfigurationArchiveDetails' with the same parameters.
        
        :param created_by: (Inferred from the method signature)
        :param created_time: (Inferred from the method signature)
        :param device_id: (Inferred from the method signature)
        :param file_type: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getConfigurationArchiveDetails(created_by, created_time, device_id, file_type, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getConfigurationArchiveDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getConfigurationArchiveDetails: {ex}")
            return {"error": str(ex)}

    def getConnectedDeviceDetail(self, device_uuid, interface_uuid, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getConnectedDeviceDetail'.
        Calls 'self.sdk.getConnectedDeviceDetail' with the same parameters.
        
        :param device_uuid: (Inferred from the method signature)
        :param interface_uuid: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getConnectedDeviceDetail(device_uuid, interface_uuid, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getConnectedDeviceDetail: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getConnectedDeviceDetail: {ex}")
            return {"error": str(ex)}

    def getConnectorTypes(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getConnectorTypes'.
        Calls 'self.sdk.getConnectorTypes' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getConnectorTypes(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getConnectorTypes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getConnectorTypes: {ex}")
            return {"error": str(ex)}

    def getCountOfAllDiscoveryJobs(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getCountOfAllDiscoveryJobs'.
        Calls 'self.sdk.getCountOfAllDiscoveryJobs' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getCountOfAllDiscoveryJobs(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getCountOfAllDiscoveryJobs: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getCountOfAllDiscoveryJobs: {ex}")
            return {"error": str(ex)}

    def getDetailsOfASingleAssuranceEvent(self, id, attribute=None, view=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDetailsOfASingleAssuranceEvent'.
        Calls 'self.sdk.getDetailsOfASingleAssuranceEvent' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param attribute: (Inferred from the method signature)
        :param view: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDetailsOfASingleAssuranceEvent(id, attribute, view, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDetailsOfASingleAssuranceEvent: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDetailsOfASingleAssuranceEvent: {ex}")
            return {"error": str(ex)}

    def getDeviceById(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceById'.
        Calls 'self.sdk.getDeviceById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceById(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceById: {ex}")
            return {"error": str(ex)}

    def getDeviceBySerialNumber(self, serial_number, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceBySerialNumber'.
        Calls 'self.sdk.getDeviceBySerialNumber' with the same parameters.
        
        :param serial_number: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceBySerialNumber(serial_number, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceBySerialNumber: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceBySerialNumber: {ex}")
            return {"error": str(ex)}

    def getDeviceConfigById(self, network_device_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceConfigById'.
        Calls 'self.sdk.getDeviceConfigById' with the same parameters.
        
        :param network_device_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceConfigById(network_device_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceConfigById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceConfigById: {ex}")
            return {"error": str(ex)}

    def getDeviceConfigCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceConfigCount'.
        Calls 'self.sdk.getDeviceConfigCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceConfigCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceConfigCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceConfigCount: {ex}")
            return {"error": str(ex)}

    def getDeviceConfigForAllDevices(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceConfigForAllDevices'.
        Calls 'self.sdk.getDeviceConfigForAllDevices' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceConfigForAllDevices(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceConfigForAllDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceConfigForAllDevices: {ex}")
            return {"error": str(ex)}

    def getDeviceControllabilitySettings(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceControllabilitySettings'.
        Calls 'self.sdk.getDeviceControllabilitySettings' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceControllabilitySettings(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceControllabilitySettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceControllabilitySettings: {ex}")
            return {"error": str(ex)}

    def getDeviceCount(self, hostname=None, location_name=None, mac_address=None, management_ip_address=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceCount'.
        Calls 'self.sdk.getDeviceCount' with the same parameters.
        
        :param hostname: (Inferred from the method signature)
        :param location_name: (Inferred from the method signature)
        :param mac_address: (Inferred from the method signature)
        :param management_ip_address: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceCount(hostname, location_name, mac_address, management_ip_address, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCount: {ex}")
            return {"error": str(ex)}

    def getDeviceCredentialDetails(self, site_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceCredentialDetails'.
        Calls 'self.sdk.getDeviceCredentialDetails' with the same parameters.
        
        :param site_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceCredentialDetails(site_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceCredentialDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCredentialDetails: {ex}")
            return {"error": str(ex)}

    def getDeviceCredentialSettingsForASite(self, id, inherited=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceCredentialSettingsForASite'.
        Calls 'self.sdk.getDeviceCredentialSettingsForASite' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param inherited: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceCredentialSettingsForASite(id, inherited, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceCredentialSettingsForASite: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCredentialSettingsForASite: {ex}")
            return {"error": str(ex)}

    def getDeviceDetail(self, identifier, search_by, timestamp=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceDetail'.
        Calls 'self.sdk.getDeviceDetail' with the same parameters.
        
        :param identifier: (Inferred from the method signature)
        :param search_by: (Inferred from the method signature)
        :param timestamp: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceDetail(identifier, search_by, timestamp, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceDetail: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceDetail: {ex}")
            return {"error": str(ex)}

    def getDeviceEnrichmentDetails(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceEnrichmentDetails'.
        Calls 'self.sdk.getDeviceEnrichmentDetails' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceEnrichmentDetails(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceEnrichmentDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceEnrichmentDetails: {ex}")
            return {"error": str(ex)}

    def getDeviceFamilyIdentifiers(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceFamilyIdentifiers'.
        Calls 'self.sdk.getDeviceFamilyIdentifiers' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceFamilyIdentifiers(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceFamilyIdentifiers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceFamilyIdentifiers: {ex}")
            return {"error": str(ex)}

    def getDeviceHistory(self, serial_number, sort=None, sort_order=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceHistory'.
        Calls 'self.sdk.getDeviceHistory' with the same parameters.
        
        :param serial_number: (Inferred from the method signature)
        :param sort: (Inferred from the method signature)
        :param sort_order: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceHistory(serial_number, sort, sort_order, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceHistory: {ex}")
            return {"error": str(ex)}

    def getDeviceInterfaceCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceInterfaceCount'.
        Calls 'self.sdk.getDeviceInterfaceCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceInterfaceCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceInterfaceCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceInterfaceCount: {ex}")
            return {"error": str(ex)}

    def getDeviceInterfacesBySpecifiedRange(self, device_id, records_to_return, start_index, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceInterfacesBySpecifiedRange'.
        Calls 'self.sdk.getDeviceInterfacesBySpecifiedRange' with the same parameters.
        
        :param device_id: (Inferred from the method signature)
        :param records_to_return: (Inferred from the method signature)
        :param start_index: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceInterfacesBySpecifiedRange(device_id, records_to_return, start_index, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceInterfacesBySpecifiedRange: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceInterfacesBySpecifiedRange: {ex}")
            return {"error": str(ex)}

    def getDeviceList(self, associated_wlc_ip=None, collection_interval=None, collection_status=None, device_support_level=None, error_code=None, error_description=None, family=None, hostname=None, id=None, license_name=None, license_status=None, license_type=None, limit=None, location=None, location_name=None, mac_address=None, management_ip_address=None, module_equpimenttype=None, module_name=None, module_operationstatecode=None, module_partnumber=None, module_servicestate=None, module_vendorequipmenttype=None, not_synced_for_minutes=None, offset=None, platform_id=None, reachability_status=None, role=None, serial_number=None, series=None, software_type=None, software_version=None, type=None, up_time=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceList'.
        Calls 'self.sdk.getDeviceList' with the same parameters.
        
        :param associated_wlc_ip: (Inferred from the method signature)
        :param collection_interval: (Inferred from the method signature)
        :param collection_status: (Inferred from the method signature)
        :param device_support_level: (Inferred from the method signature)
        :param error_code: (Inferred from the method signature)
        :param error_description: (Inferred from the method signature)
        :param family: (Inferred from the method signature)
        :param hostname: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :param license_name: (Inferred from the method signature)
        :param license_status: (Inferred from the method signature)
        :param license_type: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param location: (Inferred from the method signature)
        :param location_name: (Inferred from the method signature)
        :param mac_address: (Inferred from the method signature)
        :param management_ip_address: (Inferred from the method signature)
        :param module_equpimenttype: (Inferred from the method signature)
        :param module_name: (Inferred from the method signature)
        :param module_operationstatecode: (Inferred from the method signature)
        :param module_partnumber: (Inferred from the method signature)
        :param module_servicestate: (Inferred from the method signature)
        :param module_vendorequipmenttype: (Inferred from the method signature)
        :param not_synced_for_minutes: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param platform_id: (Inferred from the method signature)
        :param reachability_status: (Inferred from the method signature)
        :param role: (Inferred from the method signature)
        :param serial_number: (Inferred from the method signature)
        :param series: (Inferred from the method signature)
        :param software_type: (Inferred from the method signature)
        :param software_version: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param up_time: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceList(associated_wlc_ip, collection_interval, collection_status, device_support_level, error_code, error_description, family, hostname, id, license_name, license_status, license_type, limit, location, location_name, mac_address, management_ip_address, module_equpimenttype, module_name, module_operationstatecode, module_partnumber, module_servicestate, module_vendorequipmenttype, not_synced_for_minutes, offset, platform_id, reachability_status, role, serial_number, series, software_type, software_version, type, up_time, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceList: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceList: {ex}")
            return {"error": str(ex)}

    def getDeviceSummary(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceSummary'.
        Calls 'self.sdk.getDeviceSummary' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceSummary(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceSummary: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSummary: {ex}")
            return {"error": str(ex)}

    def getDeviceValuesThatMatchFullyOrPartiallyAnAttribute(self, associated_wlc_ip=None, collection_interval=None, collection_status=None, error_code=None, family=None, hostname=None, limit=None, mac_address=None, management_ip_address=None, offset=None, platform_id=None, reachability_failure_reason=None, reachability_status=None, role=None, role_source=None, serial_number=None, series=None, software_type=None, software_version=None, type=None, up_time=None, vrf_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDeviceValuesThatMatchFullyOrPartiallyAnAttribute'.
        Calls 'self.sdk.getDeviceValuesThatMatchFullyOrPartiallyAnAttribute' with the same parameters.
        
        :param associated_wlc_ip: (Inferred from the method signature)
        :param collection_interval: (Inferred from the method signature)
        :param collection_status: (Inferred from the method signature)
        :param error_code: (Inferred from the method signature)
        :param family: (Inferred from the method signature)
        :param hostname: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param mac_address: (Inferred from the method signature)
        :param management_ip_address: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param platform_id: (Inferred from the method signature)
        :param reachability_failure_reason: (Inferred from the method signature)
        :param reachability_status: (Inferred from the method signature)
        :param role: (Inferred from the method signature)
        :param role_source: (Inferred from the method signature)
        :param serial_number: (Inferred from the method signature)
        :param series: (Inferred from the method signature)
        :param software_type: (Inferred from the method signature)
        :param software_version: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param up_time: (Inferred from the method signature)
        :param vrf_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDeviceValuesThatMatchFullyOrPartiallyAnAttribute(associated_wlc_ip, collection_interval, collection_status, error_code, family, hostname, limit, mac_address, management_ip_address, offset, platform_id, reachability_failure_reason, reachability_status, role, role_source, serial_number, series, software_type, software_version, type, up_time, vrf_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDeviceValuesThatMatchFullyOrPartiallyAnAttribute: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceValuesThatMatchFullyOrPartiallyAnAttribute: {ex}")
            return {"error": str(ex)}

    def getDevicesDiscoveredById(self, id, task_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDevicesDiscoveredById'.
        Calls 'self.sdk.getDevicesDiscoveredById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param task_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDevicesDiscoveredById(id, task_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDevicesDiscoveredById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDevicesDiscoveredById: {ex}")
            return {"error": str(ex)}

    def getDevicesPerAdvisory(self, advisory_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDevicesPerAdvisory'.
        Calls 'self.sdk.getDevicesPerAdvisory' with the same parameters.
        
        :param advisory_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDevicesPerAdvisory(advisory_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDevicesPerAdvisory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDevicesPerAdvisory: {ex}")
            return {"error": str(ex)}

    def getDevicesThatAreAssignedToASite(self, id, member_type, level=None, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDevicesThatAreAssignedToASite'.
        Calls 'self.sdk.getDevicesThatAreAssignedToASite' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param member_type: (Inferred from the method signature)
        :param level: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDevicesThatAreAssignedToASite(id, member_type, level, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDevicesThatAreAssignedToASite: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDevicesThatAreAssignedToASite: {ex}")
            return {"error": str(ex)}

    def getDiscoveredDevicesByRange(self, id, records_to_return, start_index, task_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDiscoveredDevicesByRange'.
        Calls 'self.sdk.getDiscoveredDevicesByRange' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param records_to_return: (Inferred from the method signature)
        :param start_index: (Inferred from the method signature)
        :param task_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDiscoveredDevicesByRange(id, records_to_return, start_index, task_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDiscoveredDevicesByRange: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDiscoveredDevicesByRange: {ex}")
            return {"error": str(ex)}

    def getDiscoveredNetworkDevicesByDiscoveryId(self, id, task_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDiscoveredNetworkDevicesByDiscoveryId'.
        Calls 'self.sdk.getDiscoveredNetworkDevicesByDiscoveryId' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param task_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDiscoveredNetworkDevicesByDiscoveryId(id, task_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDiscoveredNetworkDevicesByDiscoveryId: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDiscoveredNetworkDevicesByDiscoveryId: {ex}")
            return {"error": str(ex)}

    def getDiscoveriesByRange(self, records_to_return, start_index, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDiscoveriesByRange'.
        Calls 'self.sdk.getDiscoveriesByRange' with the same parameters.
        
        :param records_to_return: (Inferred from the method signature)
        :param start_index: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDiscoveriesByRange(records_to_return, start_index, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDiscoveriesByRange: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDiscoveriesByRange: {ex}")
            return {"error": str(ex)}

    def getDiscoveryById(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDiscoveryById'.
        Calls 'self.sdk.getDiscoveryById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDiscoveryById(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDiscoveryById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDiscoveryById: {ex}")
            return {"error": str(ex)}

    def getDynamicInterface(self, interface_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getDynamicInterface'.
        Calls 'self.sdk.getDynamicInterface' with the same parameters.
        
        :param interface_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getDynamicInterface(interface_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getDynamicInterface: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDynamicInterface: {ex}")
            return {"error": str(ex)}

    def getEmailDestination(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getEmailDestination'.
        Calls 'self.sdk.getEmailDestination' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getEmailDestination(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getEmailDestination: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getEmailDestination: {ex}")
            return {"error": str(ex)}

    def getEmailEventSubscriptions(self, category=None, domain=None, event_ids=None, limit=None, name=None, offset=None, order=None, sort_by=None, sub_domain=None, type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getEmailEventSubscriptions'.
        Calls 'self.sdk.getEmailEventSubscriptions' with the same parameters.
        
        :param category: (Inferred from the method signature)
        :param domain: (Inferred from the method signature)
        :param event_ids: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param sub_domain: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getEmailEventSubscriptions(category, domain, event_ids, limit, name, offset, order, sort_by, sub_domain, type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getEmailEventSubscriptions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getEmailEventSubscriptions: {ex}")
            return {"error": str(ex)}

    def getEmailSubscriptionDetails(self, instance_id=None, limit=None, name=None, offset=None, order=None, sort_by=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getEmailSubscriptionDetails'.
        Calls 'self.sdk.getEmailSubscriptionDetails' with the same parameters.
        
        :param instance_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getEmailSubscriptionDetails(instance_id, limit, name, offset, order, sort_by, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getEmailSubscriptionDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getEmailSubscriptionDetails: {ex}")
            return {"error": str(ex)}

    def getEventArtifacts(self, event_ids=None, limit=None, offset=None, order=None, search=None, sort_by=None, tags=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getEventArtifacts'.
        Calls 'self.sdk.getEventArtifacts' with the same parameters.
        
        :param event_ids: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param search: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param tags: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getEventArtifacts(event_ids, limit, offset, order, search, sort_by, tags, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getEventArtifacts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getEventArtifacts: {ex}")
            return {"error": str(ex)}

    def getEventSubscriptions(self, event_ids=None, limit=None, offset=None, order=None, sort_by=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getEventSubscriptions'.
        Calls 'self.sdk.getEventSubscriptions' with the same parameters.
        
        :param event_ids: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getEventSubscriptions(event_ids, limit, offset, order, sort_by, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getEventSubscriptions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getEventSubscriptions: {ex}")
            return {"error": str(ex)}

    def getEvents(self, tags, event_id=None, limit=None, offset=None, order=None, sort_by=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getEvents'.
        Calls 'self.sdk.getEvents' with the same parameters.
        
        :param tags: (Inferred from the method signature)
        :param event_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getEvents(tags, event_id, limit, offset, order, sort_by, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getEvents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getEvents: {ex}")
            return {"error": str(ex)}

    def getExecutionIdByReportId(self, report_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getExecutionIdByReportId'.
        Calls 'self.sdk.getExecutionIdByReportId' with the same parameters.
        
        :param report_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getExecutionIdByReportId(report_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getExecutionIdByReportId: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getExecutionIdByReportId: {ex}")
            return {"error": str(ex)}

    def getExtranetPolicies(self, extranet_policy_name=None, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getExtranetPolicies'.
        Calls 'self.sdk.getExtranetPolicies' with the same parameters.
        
        :param extranet_policy_name: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getExtranetPolicies(extranet_policy_name, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getExtranetPolicies: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getExtranetPolicies: {ex}")
            return {"error": str(ex)}

    def getExtranetPolicyCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getExtranetPolicyCount'.
        Calls 'self.sdk.getExtranetPolicyCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getExtranetPolicyCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getExtranetPolicyCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getExtranetPolicyCount: {ex}")
            return {"error": str(ex)}

    def getFabricDevices(self, fabric_id, device_roles=None, limit=None, network_device_id=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricDevices'.
        Calls 'self.sdk.getFabricDevices' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param device_roles: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricDevices(fabric_id, device_roles, limit, network_device_id, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricDevices: {ex}")
            return {"error": str(ex)}

    def getFabricDevicesCount(self, fabric_id, device_roles=None, network_device_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricDevicesCount'.
        Calls 'self.sdk.getFabricDevicesCount' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param device_roles: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricDevicesCount(fabric_id, device_roles, network_device_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricDevicesCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricDevicesCount: {ex}")
            return {"error": str(ex)}

    def getFabricDevicesLayer2Handoffs(self, fabric_id, limit=None, network_device_id=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricDevicesLayer2Handoffs'.
        Calls 'self.sdk.getFabricDevicesLayer2Handoffs' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricDevicesLayer2Handoffs(fabric_id, limit, network_device_id, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricDevicesLayer2Handoffs: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricDevicesLayer2Handoffs: {ex}")
            return {"error": str(ex)}

    def getFabricDevicesLayer2HandoffsCount(self, fabric_id, network_device_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricDevicesLayer2HandoffsCount'.
        Calls 'self.sdk.getFabricDevicesLayer2HandoffsCount' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricDevicesLayer2HandoffsCount(fabric_id, network_device_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricDevicesLayer2HandoffsCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricDevicesLayer2HandoffsCount: {ex}")
            return {"error": str(ex)}

    def getFabricDevicesLayer3HandoffsWithIpTransit(self, fabric_id, limit=None, network_device_id=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricDevicesLayer3HandoffsWithIpTransit'.
        Calls 'self.sdk.getFabricDevicesLayer3HandoffsWithIpTransit' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricDevicesLayer3HandoffsWithIpTransit(fabric_id, limit, network_device_id, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricDevicesLayer3HandoffsWithIpTransit: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricDevicesLayer3HandoffsWithIpTransit: {ex}")
            return {"error": str(ex)}

    def getFabricDevicesLayer3HandoffsWithIpTransitCount(self, fabric_id, network_device_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricDevicesLayer3HandoffsWithIpTransitCount'.
        Calls 'self.sdk.getFabricDevicesLayer3HandoffsWithIpTransitCount' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricDevicesLayer3HandoffsWithIpTransitCount(fabric_id, network_device_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricDevicesLayer3HandoffsWithIpTransitCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricDevicesLayer3HandoffsWithIpTransitCount: {ex}")
            return {"error": str(ex)}

    def getFabricDevicesLayer3HandoffsWithSdaTransit(self, fabric_id, limit=None, network_device_id=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricDevicesLayer3HandoffsWithSdaTransit'.
        Calls 'self.sdk.getFabricDevicesLayer3HandoffsWithSdaTransit' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricDevicesLayer3HandoffsWithSdaTransit(fabric_id, limit, network_device_id, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricDevicesLayer3HandoffsWithSdaTransit: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricDevicesLayer3HandoffsWithSdaTransit: {ex}")
            return {"error": str(ex)}

    def getFabricDevicesLayer3HandoffsWithSdaTransitCount(self, fabric_id, network_device_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricDevicesLayer3HandoffsWithSdaTransitCount'.
        Calls 'self.sdk.getFabricDevicesLayer3HandoffsWithSdaTransitCount' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricDevicesLayer3HandoffsWithSdaTransitCount(fabric_id, network_device_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricDevicesLayer3HandoffsWithSdaTransitCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricDevicesLayer3HandoffsWithSdaTransitCount: {ex}")
            return {"error": str(ex)}

    def getFabricSiteCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricSiteCount'.
        Calls 'self.sdk.getFabricSiteCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricSiteCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricSiteCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricSiteCount: {ex}")
            return {"error": str(ex)}

    def getFabricSites(self, id=None, limit=None, offset=None, site_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricSites'.
        Calls 'self.sdk.getFabricSites' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param site_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricSites(id, limit, offset, site_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricSites: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricSites: {ex}")
            return {"error": str(ex)}

    def getFabricZoneCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricZoneCount'.
        Calls 'self.sdk.getFabricZoneCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricZoneCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricZoneCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricZoneCount: {ex}")
            return {"error": str(ex)}

    def getFabricZones(self, id=None, limit=None, offset=None, site_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFabricZones'.
        Calls 'self.sdk.getFabricZones' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param site_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFabricZones(id, limit, offset, site_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFabricZones: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFabricZones: {ex}")
            return {"error": str(ex)}

    def getFlexibleReportScheduleByReportId(self, report_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFlexibleReportScheduleByReportId'.
        Calls 'self.sdk.getFlexibleReportScheduleByReportId' with the same parameters.
        
        :param report_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFlexibleReportScheduleByReportId(report_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFlexibleReportScheduleByReportId: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFlexibleReportScheduleByReportId: {ex}")
            return {"error": str(ex)}

    def getFloorSettings(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFloorSettings'.
        Calls 'self.sdk.getFloorSettings' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFloorSettings(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFloorSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFloorSettings: {ex}")
            return {"error": str(ex)}

    def getFunctionalCapabilityById(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFunctionalCapabilityById'.
        Calls 'self.sdk.getFunctionalCapabilityById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFunctionalCapabilityById(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFunctionalCapabilityById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFunctionalCapabilityById: {ex}")
            return {"error": str(ex)}

    def getFunctionalCapabilityForDevices(self, device_id, function_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getFunctionalCapabilityForDevices'.
        Calls 'self.sdk.getFunctionalCapabilityForDevices' with the same parameters.
        
        :param device_id: (Inferred from the method signature)
        :param function_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getFunctionalCapabilityForDevices(device_id, function_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getFunctionalCapabilityForDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getFunctionalCapabilityForDevices: {ex}")
            return {"error": str(ex)}

    def getGlobalCredentials(self, credential_sub_type, order=None, sort_by=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getGlobalCredentials'.
        Calls 'self.sdk.getGlobalCredentials' with the same parameters.
        
        :param credential_sub_type: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getGlobalCredentials(credential_sub_type, order, sort_by, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getGlobalCredentials: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getGlobalCredentials: {ex}")
            return {"error": str(ex)}

    def getGlobalPool(self, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getGlobalPool'.
        Calls 'self.sdk.getGlobalPool' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getGlobalPool(limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getGlobalPool: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getGlobalPool: {ex}")
            return {"error": str(ex)}

    def getInterfaceById(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getInterfaceById'.
        Calls 'self.sdk.getInterfaceById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getInterfaceById(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getInterfaceById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getInterfaceById: {ex}")
            return {"error": str(ex)}

    def getInterfaceInfoById(self, device_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getInterfaceInfoById'.
        Calls 'self.sdk.getInterfaceInfoById' with the same parameters.
        
        :param device_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getInterfaceInfoById(device_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getInterfaceInfoById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getInterfaceInfoById: {ex}")
            return {"error": str(ex)}

    def getInterfaces(self, interface_name=None, limit=None, offset=None, vlan_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getInterfaces'.
        Calls 'self.sdk.getInterfaces' with the same parameters.
        
        :param interface_name: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param vlan_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getInterfaces(interface_name, limit, offset, vlan_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getInterfaces: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getInterfaces: {ex}")
            return {"error": str(ex)}

    def getInterfacesCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getInterfacesCount'.
        Calls 'self.sdk.getInterfacesCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getInterfacesCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getInterfacesCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getInterfacesCount: {ex}")
            return {"error": str(ex)}

    def getIssueEnrichmentDetails(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getIssueEnrichmentDetails'.
        Calls 'self.sdk.getIssueEnrichmentDetails' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getIssueEnrichmentDetails(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getIssueEnrichmentDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getIssueEnrichmentDetails: {ex}")
            return {"error": str(ex)}

    def getL3TopologyDetails(self, topology_type, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getL3TopologyDetails'.
        Calls 'self.sdk.getL3TopologyDetails' with the same parameters.
        
        :param topology_type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getL3TopologyDetails(topology_type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getL3TopologyDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getL3TopologyDetails: {ex}")
            return {"error": str(ex)}

    def getLayer2VirtualNetworkCount(self, associated_layer3_virtual_network_name=None, fabric_id=None, traffic_type=None, vlan_id=None, vlan_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getLayer2VirtualNetworkCount'.
        Calls 'self.sdk.getLayer2VirtualNetworkCount' with the same parameters.
        
        :param associated_layer3_virtual_network_name: (Inferred from the method signature)
        :param fabric_id: (Inferred from the method signature)
        :param traffic_type: (Inferred from the method signature)
        :param vlan_id: (Inferred from the method signature)
        :param vlan_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getLayer2VirtualNetworkCount(associated_layer3_virtual_network_name, fabric_id, traffic_type, vlan_id, vlan_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getLayer2VirtualNetworkCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getLayer2VirtualNetworkCount: {ex}")
            return {"error": str(ex)}

    def getLayer2VirtualNetworks(self, associated_layer3_virtual_network_name=None, fabric_id=None, id=None, limit=None, offset=None, traffic_type=None, vlan_id=None, vlan_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getLayer2VirtualNetworks'.
        Calls 'self.sdk.getLayer2VirtualNetworks' with the same parameters.
        
        :param associated_layer3_virtual_network_name: (Inferred from the method signature)
        :param fabric_id: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param traffic_type: (Inferred from the method signature)
        :param vlan_id: (Inferred from the method signature)
        :param vlan_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getLayer2VirtualNetworks(associated_layer3_virtual_network_name, fabric_id, id, limit, offset, traffic_type, vlan_id, vlan_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getLayer2VirtualNetworks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getLayer2VirtualNetworks: {ex}")
            return {"error": str(ex)}

    def getLayer3VirtualNetworks(self, anchored_site_id=None, fabric_id=None, limit=None, offset=None, virtual_network_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getLayer3VirtualNetworks'.
        Calls 'self.sdk.getLayer3VirtualNetworks' with the same parameters.
        
        :param anchored_site_id: (Inferred from the method signature)
        :param fabric_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param virtual_network_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getLayer3VirtualNetworks(anchored_site_id, fabric_id, limit, offset, virtual_network_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getLayer3VirtualNetworks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getLayer3VirtualNetworks: {ex}")
            return {"error": str(ex)}

    def getLayer3VirtualNetworksCount(self, anchored_site_id=None, fabric_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getLayer3VirtualNetworksCount'.
        Calls 'self.sdk.getLayer3VirtualNetworksCount' with the same parameters.
        
        :param anchored_site_id: (Inferred from the method signature)
        :param fabric_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getLayer3VirtualNetworksCount(anchored_site_id, fabric_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getLayer3VirtualNetworksCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getLayer3VirtualNetworksCount: {ex}")
            return {"error": str(ex)}

    def getLinecardDetails(self, device_uuid, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getLinecardDetails'.
        Calls 'self.sdk.getLinecardDetails' with the same parameters.
        
        :param device_uuid: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getLinecardDetails(device_uuid, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getLinecardDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getLinecardDetails: {ex}")
            return {"error": str(ex)}

    def getListOfAvailableNamespaces(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getListOfAvailableNamespaces'.
        Calls 'self.sdk.getListOfAvailableNamespaces' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getListOfAvailableNamespaces(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getListOfAvailableNamespaces: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getListOfAvailableNamespaces: {ex}")
            return {"error": str(ex)}

    def getListOfChildEventsForTheGivenWirelessClientEvent(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getListOfChildEventsForTheGivenWirelessClientEvent'.
        Calls 'self.sdk.getListOfChildEventsForTheGivenWirelessClientEvent' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getListOfChildEventsForTheGivenWirelessClientEvent(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getListOfChildEventsForTheGivenWirelessClientEvent: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getListOfChildEventsForTheGivenWirelessClientEvent: {ex}")
            return {"error": str(ex)}

    def getListOfDiscoveriesByDiscoveryId(self, id, ip_address=None, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getListOfDiscoveriesByDiscoveryId'.
        Calls 'self.sdk.getListOfDiscoveriesByDiscoveryId' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param ip_address: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getListOfDiscoveriesByDiscoveryId(id, ip_address, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getListOfDiscoveriesByDiscoveryId: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getListOfDiscoveriesByDiscoveryId: {ex}")
            return {"error": str(ex)}

    def getListOfFiles(self, name_space, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getListOfFiles'.
        Calls 'self.sdk.getListOfFiles' with the same parameters.
        
        :param name_space: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getListOfFiles(name_space, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getListOfFiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getListOfFiles: {ex}")
            return {"error": str(ex)}

    def getListOfScheduledReports(self, view_group_id=None, view_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getListOfScheduledReports'.
        Calls 'self.sdk.getListOfScheduledReports' with the same parameters.
        
        :param view_group_id: (Inferred from the method signature)
        :param view_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getListOfScheduledReports(view_group_id, view_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getListOfScheduledReports: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getListOfScheduledReports: {ex}")
            return {"error": str(ex)}

    def getMembership(self, site_id, device_family=None, limit=None, offset=None, serial_number=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getMembership'.
        Calls 'self.sdk.getMembership' with the same parameters.
        
        :param site_id: (Inferred from the method signature)
        :param device_family: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param serial_number: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getMembership(site_id, device_family, limit, offset, serial_number, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getMembership: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getMembership: {ex}")
            return {"error": str(ex)}

    def getMobilityGroupsCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getMobilityGroupsCount'.
        Calls 'self.sdk.getMobilityGroupsCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getMobilityGroupsCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getMobilityGroupsCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getMobilityGroupsCount: {ex}")
            return {"error": str(ex)}

    def getModuleCount(self, device_id, name_list=None, operational_state_code_list=None, part_number_list=None, vendor_equipment_type_list=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getModuleCount'.
        Calls 'self.sdk.getModuleCount' with the same parameters.
        
        :param device_id: (Inferred from the method signature)
        :param name_list: (Inferred from the method signature)
        :param operational_state_code_list: (Inferred from the method signature)
        :param part_number_list: (Inferred from the method signature)
        :param vendor_equipment_type_list: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getModuleCount(device_id, name_list, operational_state_code_list, part_number_list, vendor_equipment_type_list, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getModuleCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getModuleCount: {ex}")
            return {"error": str(ex)}

    def getModuleInfoById(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getModuleInfoById'.
        Calls 'self.sdk.getModuleInfoById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getModuleInfoById(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getModuleInfoById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getModuleInfoById: {ex}")
            return {"error": str(ex)}

    def getModules(self, device_id, limit=None, name_list=None, offset=None, operational_state_code_list=None, part_number_list=None, vendor_equipment_type_list=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getModules'.
        Calls 'self.sdk.getModules' with the same parameters.
        
        :param device_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param name_list: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param operational_state_code_list: (Inferred from the method signature)
        :param part_number_list: (Inferred from the method signature)
        :param vendor_equipment_type_list: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getModules(device_id, limit, name_list, offset, operational_state_code_list, part_number_list, vendor_equipment_type_list, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getModules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getModules: {ex}")
            return {"error": str(ex)}

    def getMulticast(self, fabric_id=None, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getMulticast'.
        Calls 'self.sdk.getMulticast' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getMulticast(fabric_id, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getMulticast: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getMulticast: {ex}")
            return {"error": str(ex)}

    def getMulticastVirtualNetworkCount(self, fabric_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getMulticastVirtualNetworkCount'.
        Calls 'self.sdk.getMulticastVirtualNetworkCount' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getMulticastVirtualNetworkCount(fabric_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getMulticastVirtualNetworkCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getMulticastVirtualNetworkCount: {ex}")
            return {"error": str(ex)}

    def getMulticastVirtualNetworks(self, fabric_id=None, limit=None, offset=None, virtual_network_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getMulticastVirtualNetworks'.
        Calls 'self.sdk.getMulticastVirtualNetworks' with the same parameters.
        
        :param fabric_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param virtual_network_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getMulticastVirtualNetworks(fabric_id, limit, offset, virtual_network_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getMulticastVirtualNetworks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getMulticastVirtualNetworks: {ex}")
            return {"error": str(ex)}

    def getNetwork(self, site_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getNetwork'.
        Calls 'self.sdk.getNetwork' with the same parameters.
        
        :param site_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getNetwork(site_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getNetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetwork: {ex}")
            return {"error": str(ex)}

    def getNetworkDeviceByPaginationRange(self, records_to_return, start_index, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getNetworkDeviceByPaginationRange'.
        Calls 'self.sdk.getNetworkDeviceByPaginationRange' with the same parameters.
        
        :param records_to_return: (Inferred from the method signature)
        :param start_index: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getNetworkDeviceByPaginationRange(records_to_return, start_index, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getNetworkDeviceByPaginationRange: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkDeviceByPaginationRange: {ex}")
            return {"error": str(ex)}

    def getNetworkDeviceImageUpdates(self, end_time=None, host_name=None, id=None, image_name=None, limit=None, management_address=None, network_device_id=None, offset=None, order=None, parent_id=None, sort_by=None, start_time=None, status=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getNetworkDeviceImageUpdates'.
        Calls 'self.sdk.getNetworkDeviceImageUpdates' with the same parameters.
        
        :param end_time: (Inferred from the method signature)
        :param host_name: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :param image_name: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param management_address: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param parent_id: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param status: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getNetworkDeviceImageUpdates(end_time, host_name, id, image_name, limit, management_address, network_device_id, offset, order, parent_id, sort_by, start_time, status, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getNetworkDeviceImageUpdates: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkDeviceImageUpdates: {ex}")
            return {"error": str(ex)}

    def getNetworkDevicesCredentialsSyncStatus(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getNetworkDevicesCredentialsSyncStatus'.
        Calls 'self.sdk.getNetworkDevicesCredentialsSyncStatus' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getNetworkDevicesCredentialsSyncStatus(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getNetworkDevicesCredentialsSyncStatus: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkDevicesCredentialsSyncStatus: {ex}")
            return {"error": str(ex)}

    def getNetworkDevicesFromDiscovery(self, id, clistatus=None, http_status=None, ip_address=None, netconf_status=None, ping_status=None, snmp_status=None, sort_by=None, sort_order=None, task_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getNetworkDevicesFromDiscovery'.
        Calls 'self.sdk.getNetworkDevicesFromDiscovery' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param clistatus: (Inferred from the method signature)
        :param http_status: (Inferred from the method signature)
        :param ip_address: (Inferred from the method signature)
        :param netconf_status: (Inferred from the method signature)
        :param ping_status: (Inferred from the method signature)
        :param snmp_status: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param sort_order: (Inferred from the method signature)
        :param task_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getNetworkDevicesFromDiscovery(id, clistatus, http_status, ip_address, netconf_status, ping_status, snmp_status, sort_by, sort_order, task_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getNetworkDevicesFromDiscovery: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkDevicesFromDiscovery: {ex}")
            return {"error": str(ex)}

    def getNetworkV2(self, site_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getNetworkV2'.
        Calls 'self.sdk.getNetworkV2' with the same parameters.
        
        :param site_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getNetworkV2(site_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getNetworkV2: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkV2: {ex}")
            return {"error": str(ex)}

    def getNotifications(self, category=None, domain=None, end_time=None, event_ids=None, limit=None, namespace=None, offset=None, order=None, severity=None, site_id=None, sort_by=None, source=None, start_time=None, sub_domain=None, tags=None, type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getNotifications'.
        Calls 'self.sdk.getNotifications' with the same parameters.
        
        :param category: (Inferred from the method signature)
        :param domain: (Inferred from the method signature)
        :param end_time: (Inferred from the method signature)
        :param event_ids: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param namespace: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param severity: (Inferred from the method signature)
        :param site_id: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param source: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param sub_domain: (Inferred from the method signature)
        :param tags: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getNotifications(category, domain, end_time, event_ids, limit, namespace, offset, order, severity, site_id, sort_by, source, start_time, sub_domain, tags, type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getNotifications: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNotifications: {ex}")
            return {"error": str(ex)}

    def getOrganizationListForMeraki(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getOrganizationListForMeraki'.
        Calls 'self.sdk.getOrganizationListForMeraki' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getOrganizationListForMeraki(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getOrganizationListForMeraki: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationListForMeraki: {ex}")
            return {"error": str(ex)}

    def getOverallClientHealth(self, timestamp=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getOverallClientHealth'.
        Calls 'self.sdk.getOverallClientHealth' with the same parameters.
        
        :param timestamp: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getOverallClientHealth(timestamp, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getOverallClientHealth: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOverallClientHealth: {ex}")
            return {"error": str(ex)}

    def getOverallNetworkHealth(self, timestamp=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getOverallNetworkHealth'.
        Calls 'self.sdk.getOverallNetworkHealth' with the same parameters.
        
        :param timestamp: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getOverallNetworkHealth(timestamp, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getOverallNetworkHealth: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOverallNetworkHealth: {ex}")
            return {"error": str(ex)}

    def getPhysicalTopology(self, node_type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getPhysicalTopology'.
        Calls 'self.sdk.getPhysicalTopology' with the same parameters.
        
        :param node_type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getPhysicalTopology(node_type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getPhysicalTopology: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getPhysicalTopology: {ex}")
            return {"error": str(ex)}

    def getPlannedAccessPointsForBuilding(self, building_id, limit=None, offset=None, radios=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getPlannedAccessPointsForBuilding'.
        Calls 'self.sdk.getPlannedAccessPointsForBuilding' with the same parameters.
        
        :param building_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param radios: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getPlannedAccessPointsForBuilding(building_id, limit, offset, radios, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getPlannedAccessPointsForBuilding: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getPlannedAccessPointsForBuilding: {ex}")
            return {"error": str(ex)}

    def getPlannedAccessPointsForFloor(self, floor_id, limit=None, offset=None, radios=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getPlannedAccessPointsForFloor'.
        Calls 'self.sdk.getPlannedAccessPointsForFloor' with the same parameters.
        
        :param floor_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param radios: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getPlannedAccessPointsForFloor(floor_id, limit, offset, radios, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getPlannedAccessPointsForFloor: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getPlannedAccessPointsForFloor: {ex}")
            return {"error": str(ex)}

    def getPollingIntervalById(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getPollingIntervalById'.
        Calls 'self.sdk.getPollingIntervalById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getPollingIntervalById(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getPollingIntervalById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getPollingIntervalById: {ex}")
            return {"error": str(ex)}

    def getPollingIntervalForAllDevices(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getPollingIntervalForAllDevices'.
        Calls 'self.sdk.getPollingIntervalForAllDevices' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getPollingIntervalForAllDevices(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getPollingIntervalForAllDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getPollingIntervalForAllDevices: {ex}")
            return {"error": str(ex)}

    def getPortAssignmentCount(self, data_vlan_name=None, fabric_id=None, interface_name=None, network_device_id=None, voice_vlan_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getPortAssignmentCount'.
        Calls 'self.sdk.getPortAssignmentCount' with the same parameters.
        
        :param data_vlan_name: (Inferred from the method signature)
        :param fabric_id: (Inferred from the method signature)
        :param interface_name: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param voice_vlan_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getPortAssignmentCount(data_vlan_name, fabric_id, interface_name, network_device_id, voice_vlan_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getPortAssignmentCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getPortAssignmentCount: {ex}")
            return {"error": str(ex)}

    def getPortAssignments(self, data_vlan_name=None, fabric_id=None, interface_name=None, limit=None, network_device_id=None, offset=None, voice_vlan_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getPortAssignments'.
        Calls 'self.sdk.getPortAssignments' with the same parameters.
        
        :param data_vlan_name: (Inferred from the method signature)
        :param fabric_id: (Inferred from the method signature)
        :param interface_name: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param voice_vlan_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getPortAssignments(data_vlan_name, fabric_id, interface_name, limit, network_device_id, offset, voice_vlan_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getPortAssignments: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getPortAssignments: {ex}")
            return {"error": str(ex)}

    def getPortChannelCount(self, connected_device_type=None, fabric_id=None, network_device_id=None, port_channel_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getPortChannelCount'.
        Calls 'self.sdk.getPortChannelCount' with the same parameters.
        
        :param connected_device_type: (Inferred from the method signature)
        :param fabric_id: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param port_channel_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getPortChannelCount(connected_device_type, fabric_id, network_device_id, port_channel_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getPortChannelCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getPortChannelCount: {ex}")
            return {"error": str(ex)}

    def getPortChannels(self, connected_device_type=None, fabric_id=None, limit=None, network_device_id=None, offset=None, port_channel_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getPortChannels'.
        Calls 'self.sdk.getPortChannels' with the same parameters.
        
        :param connected_device_type: (Inferred from the method signature)
        :param fabric_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param port_channel_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getPortChannels(connected_device_type, fabric_id, limit, network_device_id, offset, port_channel_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getPortChannels: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getPortChannels: {ex}")
            return {"error": str(ex)}

    def getProvisionedDevices(self, id=None, limit=None, network_device_id=None, offset=None, site_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getProvisionedDevices'.
        Calls 'self.sdk.getProvisionedDevices' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param network_device_id: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param site_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getProvisionedDevices(id, limit, network_device_id, offset, site_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getProvisionedDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getProvisionedDevices: {ex}")
            return {"error": str(ex)}

    def getProvisionedDevicesCount(self, site_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getProvisionedDevicesCount'.
        Calls 'self.sdk.getProvisionedDevicesCount' with the same parameters.
        
        :param site_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getProvisionedDevicesCount(site_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getProvisionedDevicesCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getProvisionedDevicesCount: {ex}")
            return {"error": str(ex)}

    def getProvisionedWiredDevice(self, device_management_ip_address, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getProvisionedWiredDevice'.
        Calls 'self.sdk.getProvisionedWiredDevice' with the same parameters.
        
        :param device_management_ip_address: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getProvisionedWiredDevice(device_management_ip_address, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getProvisionedWiredDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getProvisionedWiredDevice: {ex}")
            return {"error": str(ex)}

    def getProvisioningSettings(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getProvisioningSettings'.
        Calls 'self.sdk.getProvisioningSettings' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getProvisioningSettings(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getProvisioningSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getProvisioningSettings: {ex}")
            return {"error": str(ex)}

    def getQosDeviceInterfaceInfo(self, network_device_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getQosDeviceInterfaceInfo'.
        Calls 'self.sdk.getQosDeviceInterfaceInfo' with the same parameters.
        
        :param network_device_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getQosDeviceInterfaceInfo(network_device_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getQosDeviceInterfaceInfo: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getQosDeviceInterfaceInfo: {ex}")
            return {"error": str(ex)}

    def getQosDeviceInterfaceInfoCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getQosDeviceInterfaceInfoCount'.
        Calls 'self.sdk.getQosDeviceInterfaceInfoCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getQosDeviceInterfaceInfoCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getQosDeviceInterfaceInfoCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getQosDeviceInterfaceInfoCount: {ex}")
            return {"error": str(ex)}

    def getResyncIntervalForTheNetworkDevice(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getResyncIntervalForTheNetworkDevice'.
        Calls 'self.sdk.getResyncIntervalForTheNetworkDevice' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getResyncIntervalForTheNetworkDevice(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getResyncIntervalForTheNetworkDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getResyncIntervalForTheNetworkDevice: {ex}")
            return {"error": str(ex)}

    def getServiceProviderDetails(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getServiceProviderDetails'.
        Calls 'self.sdk.getServiceProviderDetails' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getServiceProviderDetails(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getServiceProviderDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getServiceProviderDetails: {ex}")
            return {"error": str(ex)}

    def getServiceProviderDetailsV2(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getServiceProviderDetailsV2'.
        Calls 'self.sdk.getServiceProviderDetailsV2' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getServiceProviderDetailsV2(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getServiceProviderDetailsV2: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getServiceProviderDetailsV2: {ex}")
            return {"error": str(ex)}

    def getSite(self, limit=None, name=None, offset=None, site_id=None, type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSite'.
        Calls 'self.sdk.getSite' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param site_id: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSite(limit, name, offset, site_id, type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSite: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSite: {ex}")
            return {"error": str(ex)}

    def getSiteAssignedNetworkDevice(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSiteAssignedNetworkDevice'.
        Calls 'self.sdk.getSiteAssignedNetworkDevice' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSiteAssignedNetworkDevice(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSiteAssignedNetworkDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSiteAssignedNetworkDevice: {ex}")
            return {"error": str(ex)}

    def getSiteAssignedNetworkDevices(self, site_id, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSiteAssignedNetworkDevices'.
        Calls 'self.sdk.getSiteAssignedNetworkDevices' with the same parameters.
        
        :param site_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSiteAssignedNetworkDevices(site_id, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSiteAssignedNetworkDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSiteAssignedNetworkDevices: {ex}")
            return {"error": str(ex)}

    def getSiteAssignedNetworkDevicesCount(self, site_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSiteAssignedNetworkDevicesCount'.
        Calls 'self.sdk.getSiteAssignedNetworkDevicesCount' with the same parameters.
        
        :param site_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSiteAssignedNetworkDevicesCount(site_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSiteAssignedNetworkDevicesCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSiteAssignedNetworkDevicesCount: {ex}")
            return {"error": str(ex)}

    def getSiteCount(self, site_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSiteCount'.
        Calls 'self.sdk.getSiteCount' with the same parameters.
        
        :param site_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSiteCount(site_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSiteCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSiteCount: {ex}")
            return {"error": str(ex)}

    def getSiteCountV2(self, id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSiteCountV2'.
        Calls 'self.sdk.getSiteCountV2' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSiteCountV2(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSiteCountV2: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSiteCountV2: {ex}")
            return {"error": str(ex)}

    def getSiteHealth(self, limit=None, offset=None, site_type=None, timestamp=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSiteHealth'.
        Calls 'self.sdk.getSiteHealth' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param site_type: (Inferred from the method signature)
        :param timestamp: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSiteHealth(limit, offset, site_type, timestamp, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSiteHealth: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSiteHealth: {ex}")
            return {"error": str(ex)}

    def getSiteNotAssignedNetworkDevices(self, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSiteNotAssignedNetworkDevices'.
        Calls 'self.sdk.getSiteNotAssignedNetworkDevices' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSiteNotAssignedNetworkDevices(limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSiteNotAssignedNetworkDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSiteNotAssignedNetworkDevices: {ex}")
            return {"error": str(ex)}

    def getSiteNotAssignedNetworkDevicesCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSiteNotAssignedNetworkDevicesCount'.
        Calls 'self.sdk.getSiteNotAssignedNetworkDevicesCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSiteNotAssignedNetworkDevicesCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSiteNotAssignedNetworkDevicesCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSiteNotAssignedNetworkDevicesCount: {ex}")
            return {"error": str(ex)}

    def getSiteTopology(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSiteTopology'.
        Calls 'self.sdk.getSiteTopology' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSiteTopology(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSiteTopology: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSiteTopology: {ex}")
            return {"error": str(ex)}

    def getSiteV2(self, group_name_hierarchy=None, id=None, limit=None, offset=None, type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSiteV2'.
        Calls 'self.sdk.getSiteV2' with the same parameters.
        
        :param group_name_hierarchy: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSiteV2(group_name_hierarchy, id, limit, offset, type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSiteV2: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSiteV2: {ex}")
            return {"error": str(ex)}

    def getSites(self, limit=None, name=None, name_hierarchy=None, offset=None, type=None, units_of_measure=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSites'.
        Calls 'self.sdk.getSites' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param name_hierarchy: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param units_of_measure: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSites(limit, name, name_hierarchy, offset, type, units_of_measure, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSites: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSites: {ex}")
            return {"error": str(ex)}

    def getSitesCount(self, name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSitesCount'.
        Calls 'self.sdk.getSitesCount' with the same parameters.
        
        :param name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSitesCount(name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSitesCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSitesCount: {ex}")
            return {"error": str(ex)}

    def getSmartAccountList(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSmartAccountList'.
        Calls 'self.sdk.getSmartAccountList' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSmartAccountList(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSmartAccountList: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSmartAccountList: {ex}")
            return {"error": str(ex)}

    def getSoftwareImageDetails(self, application_type=None, created_time=None, family=None, image_integrity_status=None, image_name=None, image_series=None, image_size_greater_than=None, image_size_lesser_than=None, image_uuid=None, is_cco_latest=None, is_cco_recommended=None, is_tagged_golden=None, limit=None, name=None, offset=None, sort_by=None, sort_order=None, version=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSoftwareImageDetails'.
        Calls 'self.sdk.getSoftwareImageDetails' with the same parameters.
        
        :param application_type: (Inferred from the method signature)
        :param created_time: (Inferred from the method signature)
        :param family: (Inferred from the method signature)
        :param image_integrity_status: (Inferred from the method signature)
        :param image_name: (Inferred from the method signature)
        :param image_series: (Inferred from the method signature)
        :param image_size_greater_than: (Inferred from the method signature)
        :param image_size_lesser_than: (Inferred from the method signature)
        :param image_uuid: (Inferred from the method signature)
        :param is_cco_latest: (Inferred from the method signature)
        :param is_cco_recommended: (Inferred from the method signature)
        :param is_tagged_golden: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param sort_order: (Inferred from the method signature)
        :param version: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSoftwareImageDetails(application_type, created_time, family, image_integrity_status, image_name, image_series, image_size_greater_than, image_size_lesser_than, image_uuid, is_cco_latest, is_cco_recommended, is_tagged_golden, limit, name, offset, sort_by, sort_order, version, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSoftwareImageDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSoftwareImageDetails: {ex}")
            return {"error": str(ex)}

    def getStackDetailsForDevice(self, device_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getStackDetailsForDevice'.
        Calls 'self.sdk.getStackDetailsForDevice' with the same parameters.
        
        :param device_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getStackDetailsForDevice(device_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getStackDetailsForDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getStackDetailsForDevice: {ex}")
            return {"error": str(ex)}

    def getSupervisorCardDetail(self, device_uuid, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSupervisorCardDetail'.
        Calls 'self.sdk.getSupervisorCardDetail' with the same parameters.
        
        :param device_uuid: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSupervisorCardDetail(device_uuid, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSupervisorCardDetail: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSupervisorCardDetail: {ex}")
            return {"error": str(ex)}

    def getSyncResultForVirtualAccount(self, domain, name, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSyncResultForVirtualAccount'.
        Calls 'self.sdk.getSyncResultForVirtualAccount' with the same parameters.
        
        :param domain: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSyncResultForVirtualAccount(domain, name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSyncResultForVirtualAccount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSyncResultForVirtualAccount: {ex}")
            return {"error": str(ex)}

    def getSyslogDestination(self, config_id=None, limit=None, name=None, offset=None, order=None, protocol=None, sort_by=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSyslogDestination'.
        Calls 'self.sdk.getSyslogDestination' with the same parameters.
        
        :param config_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param protocol: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSyslogDestination(config_id, limit, name, offset, order, protocol, sort_by, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSyslogDestination: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSyslogDestination: {ex}")
            return {"error": str(ex)}

    def getSyslogEventSubscriptions(self, category=None, domain=None, event_ids=None, limit=None, name=None, offset=None, order=None, sort_by=None, sub_domain=None, type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSyslogEventSubscriptions'.
        Calls 'self.sdk.getSyslogEventSubscriptions' with the same parameters.
        
        :param category: (Inferred from the method signature)
        :param domain: (Inferred from the method signature)
        :param event_ids: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param sub_domain: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSyslogEventSubscriptions(category, domain, event_ids, limit, name, offset, order, sort_by, sub_domain, type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSyslogEventSubscriptions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSyslogEventSubscriptions: {ex}")
            return {"error": str(ex)}

    def getSyslogSubscriptionDetails(self, instance_id=None, limit=None, name=None, offset=None, order=None, sort_by=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getSyslogSubscriptionDetails'.
        Calls 'self.sdk.getSyslogSubscriptionDetails' with the same parameters.
        
        :param instance_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getSyslogSubscriptionDetails(instance_id, limit, name, offset, order, sort_by, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getSyslogSubscriptionDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getSyslogSubscriptionDetails: {ex}")
            return {"error": str(ex)}

    def getTag(self, additional_info_attributes=None, additional_info_name_space=None, field=None, level=None, limit=None, name=None, offset=None, order=None, size=None, sort_by=None, system_tag=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTag'.
        Calls 'self.sdk.getTag' with the same parameters.
        
        :param additional_info_attributes: (Inferred from the method signature)
        :param additional_info_name_space: (Inferred from the method signature)
        :param field: (Inferred from the method signature)
        :param level: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param size: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param system_tag: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTag(additional_info_attributes, additional_info_name_space, field, level, limit, name, offset, order, size, sort_by, system_tag, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTag: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTag: {ex}")
            return {"error": str(ex)}

    def getTagById(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTagById'.
        Calls 'self.sdk.getTagById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTagById(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTagById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTagById: {ex}")
            return {"error": str(ex)}

    def getTagCount(self, attribute_name=None, name=None, name_space=None, size=None, system_tag=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTagCount'.
        Calls 'self.sdk.getTagCount' with the same parameters.
        
        :param attribute_name: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param name_space: (Inferred from the method signature)
        :param size: (Inferred from the method signature)
        :param system_tag: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTagCount(attribute_name, name, name_space, size, system_tag, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTagCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTagCount: {ex}")
            return {"error": str(ex)}

    def getTagMemberCount(self, id, member_type, member_association_type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTagMemberCount'.
        Calls 'self.sdk.getTagMemberCount' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param member_type: (Inferred from the method signature)
        :param member_association_type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTagMemberCount(id, member_type, member_association_type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTagMemberCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTagMemberCount: {ex}")
            return {"error": str(ex)}

    def getTagMembersById(self, id, member_type, level=None, limit=None, member_association_type=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTagMembersById'.
        Calls 'self.sdk.getTagMembersById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param member_type: (Inferred from the method signature)
        :param level: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param member_association_type: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTagMembersById(id, member_type, level, limit, member_association_type, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTagMembersById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTagMembersById: {ex}")
            return {"error": str(ex)}

    def getTagResourceTypes(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTagResourceTypes'.
        Calls 'self.sdk.getTagResourceTypes' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTagResourceTypes(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTagResourceTypes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTagResourceTypes: {ex}")
            return {"error": str(ex)}

    def getTaskById(self, task_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTaskById'.
        Calls 'self.sdk.getTaskById' with the same parameters.
        
        :param task_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTaskById(task_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTaskById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTaskById: {ex}")
            return {"error": str(ex)}

    def getTaskByOperationId(self, limit, offset, operation_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTaskByOperationId'.
        Calls 'self.sdk.getTaskByOperationId' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param operation_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTaskByOperationId(limit, offset, operation_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTaskByOperationId: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTaskByOperationId: {ex}")
            return {"error": str(ex)}

    def getTaskCount(self, data=None, end_time=None, error_code=None, failure_reason=None, is_error=None, parent_id=None, progress=None, service_type=None, start_time=None, username=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTaskCount'.
        Calls 'self.sdk.getTaskCount' with the same parameters.
        
        :param data: (Inferred from the method signature)
        :param end_time: (Inferred from the method signature)
        :param error_code: (Inferred from the method signature)
        :param failure_reason: (Inferred from the method signature)
        :param is_error: (Inferred from the method signature)
        :param parent_id: (Inferred from the method signature)
        :param progress: (Inferred from the method signature)
        :param service_type: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param username: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTaskCount(data, end_time, error_code, failure_reason, is_error, parent_id, progress, service_type, start_time, username, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTaskCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTaskCount: {ex}")
            return {"error": str(ex)}

    def getTaskTree(self, task_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTaskTree'.
        Calls 'self.sdk.getTaskTree' with the same parameters.
        
        :param task_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTaskTree(task_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTaskTree: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTaskTree: {ex}")
            return {"error": str(ex)}

    def getTasks(self, end_time=None, limit=None, offset=None, order=None, parent_id=None, root_id=None, sort_by=None, start_time=None, status=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTasks'.
        Calls 'self.sdk.getTasks' with the same parameters.
        
        :param end_time: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param parent_id: (Inferred from the method signature)
        :param root_id: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param status: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTasks(end_time, limit, offset, order, parent_id, root_id, sort_by, start_time, status, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTasks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTasks: {ex}")
            return {"error": str(ex)}

    def getTasksCount(self, end_time=None, parent_id=None, root_id=None, start_time=None, status=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTasksCount'.
        Calls 'self.sdk.getTasksCount' with the same parameters.
        
        :param end_time: (Inferred from the method signature)
        :param parent_id: (Inferred from the method signature)
        :param root_id: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param status: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTasksCount(end_time, parent_id, root_id, start_time, status, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTasksCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTasksCount: {ex}")
            return {"error": str(ex)}

    def getTheTotalNumberOfIssuesForGivenSetOfFilters(self, endTime=None, filters=None, startTime=None, headers=None, payload=None, active_validation=True, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTheTotalNumberOfIssuesForGivenSetOfFilters'.
        Calls 'self.sdk.getTheTotalNumberOfIssuesForGivenSetOfFilters' with the same parameters.
        
        :param endTime: (Inferred from the method signature)
        :param filters: (Inferred from the method signature)
        :param startTime: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param payload: (Inferred from the method signature)
        :param active_validation: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTheTotalNumberOfIssuesForGivenSetOfFilters(endTime, filters, startTime, headers, payload, active_validation, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTheTotalNumberOfIssuesForGivenSetOfFilters: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTheTotalNumberOfIssuesForGivenSetOfFilters: {ex}")
            return {"error": str(ex)}

    def getTopologyDetails(self, vlan_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTopologyDetails'.
        Calls 'self.sdk.getTopologyDetails' with the same parameters.
        
        :param vlan_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTopologyDetails(vlan_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTopologyDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTopologyDetails: {ex}")
            return {"error": str(ex)}

    def getTransitNetworks(self, id=None, limit=None, name=None, offset=None, type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTransitNetworks'.
        Calls 'self.sdk.getTransitNetworks' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTransitNetworks(id, limit, name, offset, type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTransitNetworks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTransitNetworks: {ex}")
            return {"error": str(ex)}

    def getTransitNetworksCount(self, type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTransitNetworksCount'.
        Calls 'self.sdk.getTransitNetworksCount' with the same parameters.
        
        :param type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTransitNetworksCount(type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTransitNetworksCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTransitNetworksCount: {ex}")
            return {"error": str(ex)}

    def getTransitPeerNetworkInfo(self, transit_peer_network_name, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getTransitPeerNetworkInfo'.
        Calls 'self.sdk.getTransitPeerNetworkInfo' with the same parameters.
        
        :param transit_peer_network_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getTransitPeerNetworkInfo(transit_peer_network_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getTransitPeerNetworkInfo: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getTransitPeerNetworkInfo: {ex}")
            return {"error": str(ex)}

    def getUserEnrichmentDetails(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getUserEnrichmentDetails'.
        Calls 'self.sdk.getUserEnrichmentDetails' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getUserEnrichmentDetails(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getUserEnrichmentDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getUserEnrichmentDetails: {ex}")
            return {"error": str(ex)}

    def getViewsForAGivenViewGroup(self, view_group_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getViewsForAGivenViewGroup'.
        Calls 'self.sdk.getViewsForAGivenViewGroup' with the same parameters.
        
        :param view_group_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getViewsForAGivenViewGroup(view_group_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getViewsForAGivenViewGroup: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getViewsForAGivenViewGroup: {ex}")
            return {"error": str(ex)}

    def getVirtualAccountList(self, domain, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getVirtualAccountList'.
        Calls 'self.sdk.getVirtualAccountList' with the same parameters.
        
        :param domain: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getVirtualAccountList(domain, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getVirtualAccountList: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getVirtualAccountList: {ex}")
            return {"error": str(ex)}

    def getVirtualNetworkSummary(self, site_name_hierarchy, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getVirtualNetworkSummary'.
        Calls 'self.sdk.getVirtualNetworkSummary' with the same parameters.
        
        :param site_name_hierarchy: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getVirtualNetworkSummary(site_name_hierarchy, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getVirtualNetworkSummary: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getVirtualNetworkSummary: {ex}")
            return {"error": str(ex)}

    def getVirtualNetworkWithScalableGroups(self, virtual_network_name, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getVirtualNetworkWithScalableGroups'.
        Calls 'self.sdk.getVirtualNetworkWithScalableGroups' with the same parameters.
        
        :param virtual_network_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getVirtualNetworkWithScalableGroups(virtual_network_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getVirtualNetworkWithScalableGroups: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getVirtualNetworkWithScalableGroups: {ex}")
            return {"error": str(ex)}

    def getWebhookDestination(self, limit=None, offset=None, order=None, sort_by=None, webhook_ids=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getWebhookDestination'.
        Calls 'self.sdk.getWebhookDestination' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param webhook_ids: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getWebhookDestination(limit, offset, order, sort_by, webhook_ids, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getWebhookDestination: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getWebhookDestination: {ex}")
            return {"error": str(ex)}

    def getWirelessLanControllerDetailsById(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getWirelessLanControllerDetailsById'.
        Calls 'self.sdk.getWirelessLanControllerDetailsById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getWirelessLanControllerDetailsById(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getWirelessLanControllerDetailsById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getWirelessLanControllerDetailsById: {ex}")
            return {"error": str(ex)}

    def getWirelessProfile(self, profile_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getWirelessProfile'.
        Calls 'self.sdk.getWirelessProfile' with the same parameters.
        
        :param profile_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getWirelessProfile(profile_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getWirelessProfile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getWirelessProfile: {ex}")
            return {"error": str(ex)}

    def getWirelessProfiles(self, limit=None, offset=None, wireless_profile_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getWirelessProfiles'.
        Calls 'self.sdk.getWirelessProfiles' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param wireless_profile_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getWirelessProfiles(limit, offset, wireless_profile_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getWirelessProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getWirelessProfiles: {ex}")
            return {"error": str(ex)}

    def getWirelessProfilesCount(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getWirelessProfilesCount'.
        Calls 'self.sdk.getWirelessProfilesCount' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getWirelessProfilesCount(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getWirelessProfilesCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getWirelessProfilesCount: {ex}")
            return {"error": str(ex)}

    def getWorkflowById(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getWorkflowById'.
        Calls 'self.sdk.getWorkflowById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getWorkflowById(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getWorkflowById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getWorkflowById: {ex}")
            return {"error": str(ex)}

    def getWorkflowCount(self, name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getWorkflowCount'.
        Calls 'self.sdk.getWorkflowCount' with the same parameters.
        
        :param name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getWorkflowCount(name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getWorkflowCount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getWorkflowCount: {ex}")
            return {"error": str(ex)}

    def getWorkflows(self, limit=None, name=None, offset=None, sort=None, sort_order=None, type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getWorkflows'.
        Calls 'self.sdk.getWorkflows' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param name: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param sort: (Inferred from the method signature)
        :param sort_order: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getWorkflows(limit, name, offset, sort, sort_order, type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getWorkflows: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getWorkflows: {ex}")
            return {"error": str(ex)}

    def getsABuilding(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getsABuilding'.
        Calls 'self.sdk.getsABuilding' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getsABuilding(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getsABuilding: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getsABuilding: {ex}")
            return {"error": str(ex)}

    def getsAFloor(self, id, units_of_measure=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getsAFloor'.
        Calls 'self.sdk.getsAFloor' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param units_of_measure: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getsAFloor(id, units_of_measure, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getsAFloor: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getsAFloor: {ex}")
            return {"error": str(ex)}

    def getsAListOfProjects(self, name=None, sort_order=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getsAListOfProjects'.
        Calls 'self.sdk.getsAListOfProjects' with the same parameters.
        
        :param name: (Inferred from the method signature)
        :param sort_order: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getsAListOfProjects(name, sort_order, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getsAListOfProjects: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getsAListOfProjects: {ex}")
            return {"error": str(ex)}

    def getsAllTheVersionsOfAGivenTemplate(self, template_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getsAllTheVersionsOfAGivenTemplate'.
        Calls 'self.sdk.getsAllTheVersionsOfAGivenTemplate' with the same parameters.
        
        :param template_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getsAllTheVersionsOfAGivenTemplate(template_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getsAllTheVersionsOfAGivenTemplate: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getsAllTheVersionsOfAGivenTemplate: {ex}")
            return {"error": str(ex)}

    def getsAnArea(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getsAnArea'.
        Calls 'self.sdk.getsAnArea' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getsAnArea(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getsAnArea: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getsAnArea: {ex}")
            return {"error": str(ex)}

    def getsTheTemplatesAvailable(self, filter_conflicting_templates=None, product_family=None, product_series=None, product_type=None, project_id=None, project_names=None, software_type=None, software_version=None, sort_order=None, tags=None, un_committed=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'getsTheTemplatesAvailable'.
        Calls 'self.sdk.getsTheTemplatesAvailable' with the same parameters.
        
        :param filter_conflicting_templates: (Inferred from the method signature)
        :param product_family: (Inferred from the method signature)
        :param product_series: (Inferred from the method signature)
        :param product_type: (Inferred from the method signature)
        :param project_id: (Inferred from the method signature)
        :param project_names: (Inferred from the method signature)
        :param software_type: (Inferred from the method signature)
        :param software_version: (Inferred from the method signature)
        :param sort_order: (Inferred from the method signature)
        :param tags: (Inferred from the method signature)
        :param un_committed: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.getsTheTemplatesAvailable(filter_conflicting_templates, product_family, product_series, product_type, project_id, project_names, software_type, software_version, sort_order, tags, un_committed, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in getsTheTemplatesAvailable: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getsTheTemplatesAvailable: {ex}")
            return {"error": str(ex)}

    def retrieveANetworkProfileForSitesById(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveANetworkProfileForSitesById'.
        Calls 'self.sdk.retrieveANetworkProfileForSitesById' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveANetworkProfileForSitesById(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveANetworkProfileForSitesById: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveANetworkProfileForSitesById: {ex}")
            return {"error": str(ex)}

    def retrieveBannerSettingsForASite(self, id, inherited=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveBannerSettingsForASite'.
        Calls 'self.sdk.retrieveBannerSettingsForASite' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param inherited: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveBannerSettingsForASite(id, inherited, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveBannerSettingsForASite: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveBannerSettingsForASite: {ex}")
            return {"error": str(ex)}

    def retrieveDHCPSettingsForASite(self, id, inherited=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveDHCPSettingsForASite'.
        Calls 'self.sdk.retrieveDHCPSettingsForASite' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param inherited: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveDHCPSettingsForASite(id, inherited, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveDHCPSettingsForASite: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveDHCPSettingsForASite: {ex}")
            return {"error": str(ex)}

    def retrieveDNSSettingsForASite(self, id, inherited=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveDNSSettingsForASite'.
        Calls 'self.sdk.retrieveDNSSettingsForASite' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param inherited: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveDNSSettingsForASite(id, inherited, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveDNSSettingsForASite: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveDNSSettingsForASite: {ex}")
            return {"error": str(ex)}

    def retrieveImageDistributionServers(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveImageDistributionServers'.
        Calls 'self.sdk.retrieveImageDistributionServers' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveImageDistributionServers(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveImageDistributionServers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveImageDistributionServers: {ex}")
            return {"error": str(ex)}

    def retrieveImageDistributionSettingsForASite(self, id, inherited=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveImageDistributionSettingsForASite'.
        Calls 'self.sdk.retrieveImageDistributionSettingsForASite' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param inherited: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveImageDistributionSettingsForASite(id, inherited, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveImageDistributionSettingsForASite: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveImageDistributionSettingsForASite: {ex}")
            return {"error": str(ex)}

    def retrieveLicenseSetting(self, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveLicenseSetting'.
        Calls 'self.sdk.retrieveLicenseSetting' with the same parameters.
        
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveLicenseSetting(headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveLicenseSetting: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveLicenseSetting: {ex}")
            return {"error": str(ex)}

    def retrieveNTPSettingsForASite(self, id, inherited=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveNTPSettingsForASite'.
        Calls 'self.sdk.retrieveNTPSettingsForASite' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param inherited: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveNTPSettingsForASite(id, inherited, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveNTPSettingsForASite: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveNTPSettingsForASite: {ex}")
            return {"error": str(ex)}

    def retrieveNetworkDeviceProductName(self, product_name_ordinal, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveNetworkDeviceProductName'.
        Calls 'self.sdk.retrieveNetworkDeviceProductName' with the same parameters.
        
        :param product_name_ordinal: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveNetworkDeviceProductName(product_name_ordinal, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveNetworkDeviceProductName: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveNetworkDeviceProductName: {ex}")
            return {"error": str(ex)}

    def retrieveSpecificImageDistributionServer(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveSpecificImageDistributionServer'.
        Calls 'self.sdk.retrieveSpecificImageDistributionServer' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveSpecificImageDistributionServer(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveSpecificImageDistributionServer: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveSpecificImageDistributionServer: {ex}")
            return {"error": str(ex)}

    def retrieveTelemetrySettingsForASite(self, id, inherited=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveTelemetrySettingsForASite'.
        Calls 'self.sdk.retrieveTelemetrySettingsForASite' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param inherited: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveTelemetrySettingsForASite(id, inherited, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveTelemetrySettingsForASite: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveTelemetrySettingsForASite: {ex}")
            return {"error": str(ex)}

    def retrieveTimeZoneSettingsForASite(self, id, inherited=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrieveTimeZoneSettingsForASite'.
        Calls 'self.sdk.retrieveTimeZoneSettingsForASite' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param inherited: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrieveTimeZoneSettingsForASite(id, inherited, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrieveTimeZoneSettingsForASite: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrieveTimeZoneSettingsForASite: {ex}")
            return {"error": str(ex)}

    def retrievesAllPreviousPathtracesSummary(self, dest_ip=None, dest_port=None, gt_create_time=None, last_update_time=None, limit=None, lt_create_time=None, offset=None, order=None, periodic_refresh=None, protocol=None, sort_by=None, source_ip=None, source_port=None, status=None, task_id=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesAllPreviousPathtracesSummary'.
        Calls 'self.sdk.retrievesAllPreviousPathtracesSummary' with the same parameters.
        
        :param dest_ip: (Inferred from the method signature)
        :param dest_port: (Inferred from the method signature)
        :param gt_create_time: (Inferred from the method signature)
        :param last_update_time: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param lt_create_time: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param periodic_refresh: (Inferred from the method signature)
        :param protocol: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param source_ip: (Inferred from the method signature)
        :param source_port: (Inferred from the method signature)
        :param status: (Inferred from the method signature)
        :param task_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesAllPreviousPathtracesSummary(dest_ip, dest_port, gt_create_time, last_update_time, limit, lt_create_time, offset, order, periodic_refresh, protocol, sort_by, source_ip, source_port, status, task_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesAllPreviousPathtracesSummary: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesAllPreviousPathtracesSummary: {ex}")
            return {"error": str(ex)}

    def retrievesAllTheValidationSets(self, view=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesAllTheValidationSets'.
        Calls 'self.sdk.retrievesAllTheValidationSets' with the same parameters.
        
        :param view: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesAllTheValidationSets(view, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesAllTheValidationSets: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesAllTheValidationSets: {ex}")
            return {"error": str(ex)}

    def retrievesPreviousPathtrace(self, flow_analysis_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesPreviousPathtrace'.
        Calls 'self.sdk.retrievesPreviousPathtrace' with the same parameters.
        
        :param flow_analysis_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesPreviousPathtrace(flow_analysis_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesPreviousPathtrace: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesPreviousPathtrace: {ex}")
            return {"error": str(ex)}

    def retrievesTheCountOfAssignedNetworkDeviceProducts(self, image_id, assigned=None, product_id=None, product_name=None, recommended=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesTheCountOfAssignedNetworkDeviceProducts'.
        Calls 'self.sdk.retrievesTheCountOfAssignedNetworkDeviceProducts' with the same parameters.
        
        :param image_id: (Inferred from the method signature)
        :param assigned: (Inferred from the method signature)
        :param product_id: (Inferred from the method signature)
        :param product_name: (Inferred from the method signature)
        :param recommended: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesTheCountOfAssignedNetworkDeviceProducts(image_id, assigned, product_id, product_name, recommended, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesTheCountOfAssignedNetworkDeviceProducts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesTheCountOfAssignedNetworkDeviceProducts: {ex}")
            return {"error": str(ex)}

    def retrievesTheCountOfNetworkProfilesForSites(self, type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesTheCountOfNetworkProfilesForSites'.
        Calls 'self.sdk.retrievesTheCountOfNetworkProfilesForSites' with the same parameters.
        
        :param type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesTheCountOfNetworkProfilesForSites(type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesTheCountOfNetworkProfilesForSites: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesTheCountOfNetworkProfilesForSites: {ex}")
            return {"error": str(ex)}

    def retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned(self, site_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned'.
        Calls 'self.sdk.retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned' with the same parameters.
        
        :param site_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned(site_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned: {ex}")
            return {"error": str(ex)}

    def retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(self, profile_id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo'.
        Calls 'self.sdk.retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo' with the same parameters.
        
        :param profile_id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(profile_id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo: {ex}")
            return {"error": str(ex)}

    def retrievesTheCountOfValidationWorkflows(self, end_time=None, run_status=None, start_time=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesTheCountOfValidationWorkflows'.
        Calls 'self.sdk.retrievesTheCountOfValidationWorkflows' with the same parameters.
        
        :param end_time: (Inferred from the method signature)
        :param run_status: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesTheCountOfValidationWorkflows(end_time, run_status, start_time, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesTheCountOfValidationWorkflows: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesTheCountOfValidationWorkflows: {ex}")
            return {"error": str(ex)}

    def retrievesTheListOfNetworkDeviceProductNames(self, limit=None, offset=None, product_id=None, product_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesTheListOfNetworkDeviceProductNames'.
        Calls 'self.sdk.retrievesTheListOfNetworkDeviceProductNames' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param product_id: (Inferred from the method signature)
        :param product_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesTheListOfNetworkDeviceProductNames(limit, offset, product_id, product_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesTheListOfNetworkDeviceProductNames: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesTheListOfNetworkDeviceProductNames: {ex}")
            return {"error": str(ex)}

    def retrievesTheListOfNetworkProfilesForSites(self, limit=None, offset=None, order=None, sort_by=None, type=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesTheListOfNetworkProfilesForSites'.
        Calls 'self.sdk.retrievesTheListOfNetworkProfilesForSites' with the same parameters.
        
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param order: (Inferred from the method signature)
        :param sort_by: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesTheListOfNetworkProfilesForSites(limit, offset, order, sort_by, type, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesTheListOfNetworkProfilesForSites: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesTheListOfNetworkProfilesForSites: {ex}")
            return {"error": str(ex)}

    def retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned(self, site_id, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned'.
        Calls 'self.sdk.retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned' with the same parameters.
        
        :param site_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned(site_id, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned: {ex}")
            return {"error": str(ex)}

    def retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(self, profile_id, limit=None, offset=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo'.
        Calls 'self.sdk.retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo' with the same parameters.
        
        :param profile_id: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(profile_id, limit, offset, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo: {ex}")
            return {"error": str(ex)}

    def retrievesTheListOfValidationWorkflows(self, end_time=None, limit=None, offset=None, run_status=None, start_time=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesTheListOfValidationWorkflows'.
        Calls 'self.sdk.retrievesTheListOfValidationWorkflows' with the same parameters.
        
        :param end_time: (Inferred from the method signature)
        :param limit: (Inferred from the method signature)
        :param offset: (Inferred from the method signature)
        :param run_status: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesTheListOfValidationWorkflows(end_time, limit, offset, run_status, start_time, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesTheListOfValidationWorkflows: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesTheListOfValidationWorkflows: {ex}")
            return {"error": str(ex)}

    def retrievesTheTotalCountOfClientsByApplyingBasicFiltering(self, band=None, connected_network_device_name=None, end_time=None, ipv4_address=None, ipv6_address=None, mac_address=None, os_type=None, os_version=None, site_hierarchy=None, site_hierarchy_id=None, site_id=None, ssid=None, start_time=None, type=None, wlc_name=None, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesTheTotalCountOfClientsByApplyingBasicFiltering'.
        Calls 'self.sdk.retrievesTheTotalCountOfClientsByApplyingBasicFiltering' with the same parameters.
        
        :param band: (Inferred from the method signature)
        :param connected_network_device_name: (Inferred from the method signature)
        :param end_time: (Inferred from the method signature)
        :param ipv4_address: (Inferred from the method signature)
        :param ipv6_address: (Inferred from the method signature)
        :param mac_address: (Inferred from the method signature)
        :param os_type: (Inferred from the method signature)
        :param os_version: (Inferred from the method signature)
        :param site_hierarchy: (Inferred from the method signature)
        :param site_hierarchy_id: (Inferred from the method signature)
        :param site_id: (Inferred from the method signature)
        :param ssid: (Inferred from the method signature)
        :param start_time: (Inferred from the method signature)
        :param type: (Inferred from the method signature)
        :param wlc_name: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesTheTotalCountOfClientsByApplyingBasicFiltering(band, connected_network_device_name, end_time, ipv4_address, ipv6_address, mac_address, os_type, os_version, site_hierarchy, site_hierarchy_id, site_id, ssid, start_time, type, wlc_name, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesTheTotalCountOfClientsByApplyingBasicFiltering: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesTheTotalCountOfClientsByApplyingBasicFiltering: {ex}")
            return {"error": str(ex)}

    def retrievesValidationDetailsForAValidationSet(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesValidationDetailsForAValidationSet'.
        Calls 'self.sdk.retrievesValidationDetailsForAValidationSet' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesValidationDetailsForAValidationSet(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesValidationDetailsForAValidationSet: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesValidationDetailsForAValidationSet: {ex}")
            return {"error": str(ex)}

    def retrievesValidationWorkflowDetails(self, id, headers=None, **request_parameters) -> Dict[str, Any]:
        """Auto-generated method for 'retrievesValidationWorkflowDetails'.
        Calls 'self.sdk.retrievesValidationWorkflowDetails' with the same parameters.
        
        :param id: (Inferred from the method signature)
        :param headers: (Inferred from the method signature)
        :param request_parameters: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.sdk.retrievesValidationWorkflowDetails(id, headers, **request_parameters)
        except ApiError as e:
            logging.error(f"API Error in retrievesValidationWorkflowDetails: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in retrievesValidationWorkflowDetails: {ex}")
            return {"error": str(ex)}

################################################################################
# cisco-data-bridge-domain-index/cisco_integrations/unified_service.py
# Copyright (c) 2025 Jeff Teeter, Ph.D.
# Cisco Systems, Inc.
# Licensed under the Apache License, Version 2.0 (see LICENSE)
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import logging
import os
from dotenv import load_dotenv

load_dotenv()
# Read integration flags from environment
ENABLE_CATALYST_CENTER = os.getenv("ENABLE_CATALYST_CENTER", "false").lower() == "true"
print("ENABLE_CATALYST_CENTER HERE: ", ENABLE_CATALYST_CENTER)
ENABLE_MERAKI = os.getenv("ENABLE_MERAKI", "true").lower() == "true"
print("ENABLE_MERAKI: ", ENABLE_MERAKI)
ENABLE_CISCO_SPACES = os.getenv("ENABLE_CISCO_SPACES", "true").lower() == "true"
print("ENABLE_CISCO_SPACES: ", ENABLE_CISCO_SPACES)
ENABLE_CISCO_WEBEX = os.getenv("ENABLE_CISCO_WEBEX", "false").lower() == "true"
print("ENABLE_CISCO_WEBEX: ", ENABLE_CISCO_WEBEX)

# Import platform-specific clients only if enabled
if ENABLE_CATALYST_CENTER:
    from cisco_integrations.cisco_catalyst_client import CatalystCenterClient
if ENABLE_MERAKI:
    from cisco_integrations.cisco_meraki_client import CiscoMerakiClient
if ENABLE_CISCO_SPACES:
    from cisco_integrations.cisco_spaces_client import CiscoSpacesClient
if ENABLE_CISCO_WEBEX:
    from cisco_integrations.cisco_webex_client import CiscoWebexClient

class CiscoUnifiedService:
    def __init__(
        self,
        catalyst_username=None,
        catalyst_password=None,
        catalyst_url=None,
        catalyst_version=None,
        meraki_api_key=None,
        spaces_token=None,
        webex_token=None,
    ):
        
        # -------------------------
        # Catalyst Center Integration
        # -------------------------
        if ENABLE_CATALYST_CENTER:
            self.catalyst_client = CatalystCenterClient(
                base_url=catalyst_url,
                token=None,
                dnac_username=catalyst_username,
                dnac_password=catalyst_password,
                dnac_encoded_auth=None,
                dnac_verify=False,
                dnac_version=catalyst_version
            )
        else:
            self.catalyst_client = None
            logging.info("Catalyst Center integration is disabled.")

        # -------------------------
        # Meraki Integration
        # -------------------------
        if ENABLE_MERAKI:
            # Always use the organization ID from the environment; user cannot override it.
            self.meraki_org_id = os.getenv("MERAKI_ORG_ID", "")
            logging.info(f"MERAKI_ORG_ID from environment: '{self.meraki_org_id}'")
            if not self.meraki_org_id:
                logging.warning("MERAKI_ORG_ID is not set in the environment.")
            self.meraki_client = CiscoMerakiClient(
                api_key=meraki_api_key,
                organization_id=self.meraki_org_id
            ) if meraki_api_key else None
        else:
            self.meraki_client = None
            logging.info("Meraki integration is disabled.")

        # -------------------------
        # Cisco Spaces Integration
        # -------------------------
        if ENABLE_CISCO_SPACES:
            self.spaces_client = CiscoSpacesClient(
                base_url=None,  # Will use CISCO_SPACES_BASE_URL from environment if not provided.
                api_key=spaces_token
            )
        else:
            self.spaces_client = None
            logging.info("Cisco Spaces integration is disabled.")

        # -------------------------
        # Cisco Webex Integration
        # -------------------------
        if ENABLE_CISCO_WEBEX:
            self.webex_client = CiscoWebexClient(token=webex_token)
        else:
            self.webex_client = None
            logging.info("Cisco Webex integration is disabled or token not provided.")

        logging.info("CiscoUnifiedService initialized with enabled integrations: "
                     "Catalyst: {}, Meraki: {}, Spaces: {}, Webex: {}."
                     .format(ENABLE_CATALYST_CENTER, ENABLE_MERAKI, ENABLE_CISCO_SPACES, ENABLE_CISCO_WEBEX))
        

        

    # ================================
    # Meraki Methods
    # ================================

    def list_all_clients_in_org(self, timespan=60 * 60 * 24 * 14):
        """
        Lists all Meraki clients across all networks in the organization,
        optionally limited by a timespan (default 14 days).
        """
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}

        # This calls the method you defined in cisco_meraki_client.py
        return self.meraki_client.list_all_clients_in_org(timespan=timespan)
    
    def list_all_clients_in_org_by_name(self, name_substring: str, timespan=60 * 60 * 24 * 14):
        """
        Delegate to the Meraki client. Lists all clients in the org, 
        filters them by substring match against description/hostname.
        """
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}

        # Call the function you defined in cisco_meraki_client.py
        return self.meraki_client.list_all_clients_in_org_by_name(name_substring, timespan=timespan)

    def get_network_alerts_history(self, network_id: str):
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}
        return self.meraki_client.get_network_alerts_history(network_id)

    def get_all_access_points(self):
        """
        Return all access points from the Meraki wireless controllers.
        """
        if not self.meraki_client:
            return {"error": "Meraki client not configured or Meraki is disabled."}

        return self.meraki_client.get_all_access_points()


    def list_all_switches_in_org(self):
        """
        Lists all Meraki switch devices (models starting with 'MS') in the org.
        """
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}

        # Delegate to the new method in CiscoMerakiClient
        return self.meraki_client.list_all_switches_in_org()

    def list_all_cameras_in_org(self):
        """
        Lists all Meraki cameras in the organization (onboarding statuses).
        """
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}

        return self.meraki_client.list_all_cameras_in_org()
    



    # ================================
    # Meraki SDK Methods
    # ================================


    def get_administered_identities_me(self, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getAdministeredIdentitiesMe(**kwargs)

    def get_administered_identities_me_api_keys(self, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getAdministeredIdentitiesMeApiKeys(**kwargs)

    def get_administered_licensing_subscription_entitlements(self, skus=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getAdministeredLicensingSubscriptionEntitlements(skus, **kwargs)

    def get_administered_licensing_subscription_subscriptions(self, perPage=None, startingAfter=None, endingBefore=None, subscriptionIds=None, organizationIds=None, statuses=None, productTypes=None, name=None, startDate=None, endDate=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getAdministeredLicensingSubscriptionSubscriptions(perPage, startingAfter, endingBefore, subscriptionIds, organizationIds, statuses, productTypes, name, startDate, endDate, **kwargs)

    def get_administered_licensing_subscription_subscriptions_compliance_statuses(self, organizationIds, subscriptionIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses(organizationIds, subscriptionIds, **kwargs)

    def get_device(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDevice(serial, **kwargs)

    def get_device_appliance_dhcp_subnets(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceApplianceDhcpSubnets(serial, **kwargs)

    def get_device_appliance_performance(self, serial, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceAppliancePerformance(serial, t0, t1, timespan, **kwargs)

    def get_device_appliance_prefixes_delegated(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceAppliancePrefixesDelegated(serial, **kwargs)

    def get_device_appliance_prefixes_delegated_vlan_assignments(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceAppliancePrefixesDelegatedVlanAssignments(serial, **kwargs)

    def get_device_appliance_radio_settings(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceApplianceRadioSettings(serial, **kwargs)

    def get_device_appliance_uplinks_settings(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceApplianceUplinksSettings(serial, **kwargs)

    def get_device_camera_analytics_live(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraAnalyticsLive(serial, **kwargs)

    def get_device_camera_analytics_overview(self, serial, t0=None, t1=None, timespan=None, objectType=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraAnalyticsOverview(serial, t0, t1, timespan, objectType, **kwargs)

    def get_device_camera_analytics_recent(self, serial, objectType=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraAnalyticsRecent(serial, objectType, **kwargs)

    def get_device_camera_analytics_zones(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraAnalyticsZones(serial, **kwargs)

    def get_device_camera_analytics_zone_history(self, serial, zoneId, t0=None, t1=None, timespan=None, resolution=None, objectType=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraAnalyticsZoneHistory(serial, zoneId, t0, t1, timespan, resolution, objectType, **kwargs)

    def get_device_camera_custom_analytics(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraCustomAnalytics(serial, **kwargs)

    def get_device_camera_quality_and_retention(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraQualityAndRetention(serial, **kwargs)

    def get_device_camera_sense(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraSense(serial, **kwargs)

    def get_device_camera_sense_object_detection_models(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraSenseObjectDetectionModels(serial, **kwargs)

    def get_device_camera_video_settings(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraVideoSettings(serial, **kwargs)

    def get_device_camera_video_link(self, serial, timestamp=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraVideoLink(serial, timestamp, **kwargs)

    def get_device_camera_wireless_profiles(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCameraWirelessProfiles(serial, **kwargs)

    def get_device_cellular_sims(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCellularSims(serial, **kwargs)

    def get_device_cellular_gateway_lan(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCellularGatewayLan(serial, **kwargs)

    def get_device_cellular_gateway_port_forwarding_rules(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceCellularGatewayPortForwardingRules(serial, **kwargs)

    def get_device_clients(self, serial, t0=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceClients(serial, t0, timespan, **kwargs)

    def get_device_live_tools_arp_table(self, serial, arpTableId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceLiveToolsArpTable(serial, arpTableId, **kwargs)

    def get_device_live_tools_cable_test(self, serial, id, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceLiveToolsCableTest(serial, id, **kwargs)

    def get_device_live_tools_leds_blink(self, serial, ledsBlinkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceLiveToolsLedsBlink(serial, ledsBlinkId, **kwargs)

    def get_device_live_tools_ping(self, serial, id, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceLiveToolsPing(serial, id, **kwargs)

    def get_device_live_tools_ping_device(self, serial, id, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceLiveToolsPingDevice(serial, id, **kwargs)

    def get_device_live_tools_throughput_test(self, serial, throughputTestId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceLiveToolsThroughputTest(serial, throughputTestId, **kwargs)

    def get_device_live_tools_wake_on_lan(self, serial, wakeOnLanId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceLiveToolsWakeOnLan(serial, wakeOnLanId, **kwargs)

    def get_device_lldp_cdp(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceLldpCdp(serial, **kwargs)

    def get_device_loss_and_latency_history(self, serial, ip, t0=None, t1=None, timespan=None, resolution=None, uplink=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceLossAndLatencyHistory(serial, ip, t0, t1, timespan, resolution, uplink, **kwargs)

    def get_device_management_interface(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceManagementInterface(serial, **kwargs)

    def get_device_sensor_commands(self, serial, operations=None, perPage=None, startingAfter=None, endingBefore=None, sortOrder=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSensorCommands(serial, operations, perPage, startingAfter, endingBefore, sortOrder, t0, t1, timespan, **kwargs)

    def get_device_sensor_command(self, serial, commandId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSensorCommand(serial, commandId, **kwargs)

    def get_device_sensor_relationships(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSensorRelationships(serial, **kwargs)

    def get_device_switch_ports(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSwitchPorts(serial, **kwargs)

    def get_device_switch_ports_statuses(self, serial, t0=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSwitchPortsStatuses(serial, t0, timespan, **kwargs)

    def get_device_switch_ports_statuses_packets(self, serial, t0=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSwitchPortsStatusesPackets(serial, t0, timespan, **kwargs)

    def get_device_switch_port(self, serial, portId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSwitchPort(serial, portId, **kwargs)

    def get_device_switch_routing_interfaces(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSwitchRoutingInterfaces(serial, **kwargs)

    def get_device_switch_routing_interface(self, serial, interfaceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSwitchRoutingInterface(serial, interfaceId, **kwargs)

    def get_device_switch_routing_interface_dhcp(self, serial, interfaceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSwitchRoutingInterfaceDhcp(serial, interfaceId, **kwargs)

    def get_device_switch_routing_static_routes(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSwitchRoutingStaticRoutes(serial, **kwargs)

    def get_device_switch_routing_static_route(self, serial, staticRouteId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSwitchRoutingStaticRoute(serial, staticRouteId, **kwargs)

    def get_device_switch_warm_spare(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceSwitchWarmSpare(serial, **kwargs)

    def get_device_wireless_bluetooth_settings(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceWirelessBluetoothSettings(serial, **kwargs)

    def get_device_wireless_connection_stats(self, serial, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, apTag=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceWirelessConnectionStats(serial, t0, t1, timespan, band, ssid, vlan, apTag, **kwargs)

    def get_device_wireless_electronic_shelf_label(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceWirelessElectronicShelfLabel(serial, **kwargs)

    def get_device_wireless_latency_stats(self, serial, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, apTag=None, fields=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceWirelessLatencyStats(serial, t0, t1, timespan, band, ssid, vlan, apTag, fields, **kwargs)

    def get_device_wireless_radio_settings(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceWirelessRadioSettings(serial, **kwargs)

    def get_device_wireless_status(self, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getDeviceWirelessStatus(serial, **kwargs)

    def get_network(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetwork(networkId, **kwargs)

    def get_network_alerts_history(self, networkId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkAlertsHistory(networkId, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_alerts_settings(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkAlertsSettings(networkId, **kwargs)

    def get_network_appliance_client_security_events(self, networkId, clientId, t0=None, t1=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, sortOrder=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceClientSecurityEvents(networkId, clientId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder, **kwargs)

    def get_network_appliance_connectivity_monitoring_destinations(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceConnectivityMonitoringDestinations(networkId, **kwargs)

    def get_network_appliance_content_filtering(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceContentFiltering(networkId, **kwargs)

    def get_network_appliance_content_filtering_categories(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceContentFilteringCategories(networkId, **kwargs)

    def get_network_appliance_firewall_cellular_firewall_rules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallCellularFirewallRules(networkId, **kwargs)

    def get_network_appliance_firewall_firewalled_services(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallFirewalledServices(networkId, **kwargs)

    def get_network_appliance_firewall_firewalled_service(self, networkId, service, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallFirewalledService(networkId, service, **kwargs)

    def get_network_appliance_firewall_inbound_cellular_firewall_rules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallInboundCellularFirewallRules(networkId, **kwargs)

    def get_network_appliance_firewall_inbound_firewall_rules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallInboundFirewallRules(networkId, **kwargs)

    def get_network_appliance_firewall_l3_firewall_rules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallL3FirewallRules(networkId, **kwargs)

    def get_network_appliance_firewall_l7_firewall_rules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallL7FirewallRules(networkId, **kwargs)

    def get_network_appliance_firewall_l7_firewall_rules_application_categories(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(networkId, **kwargs)

    def get_network_appliance_firewall_one_to_many_nat_rules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallOneToManyNatRules(networkId, **kwargs)

    def get_network_appliance_firewall_one_to_one_nat_rules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallOneToOneNatRules(networkId, **kwargs)

    def get_network_appliance_firewall_port_forwarding_rules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallPortForwardingRules(networkId, **kwargs)

    def get_network_appliance_firewall_settings(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceFirewallSettings(networkId, **kwargs)

    def get_network_appliance_ports(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkAppliancePorts(networkId, **kwargs)

    def get_network_appliance_port(self, networkId, portId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkAppliancePort(networkId, portId, **kwargs)

    def get_network_appliance_prefixes_delegated_statics(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkAppliancePrefixesDelegatedStatics(networkId, **kwargs)

    def get_network_appliance_prefixes_delegated_static(self, networkId, staticDelegatedPrefixId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkAppliancePrefixesDelegatedStatic(networkId, staticDelegatedPrefixId, **kwargs)

    def get_network_appliance_rf_profiles(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceRfProfiles(networkId, **kwargs)

    def get_network_appliance_rf_profile(self, networkId, rfProfileId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceRfProfile(networkId, rfProfileId, **kwargs)

    def get_network_appliance_security_events(self, networkId, t0=None, t1=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, sortOrder=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceSecurityEvents(networkId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder, **kwargs)

    def get_network_appliance_security_intrusion(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceSecurityIntrusion(networkId, **kwargs)

    def get_network_appliance_security_malware(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceSecurityMalware(networkId, **kwargs)

    def get_network_appliance_settings(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceSettings(networkId, **kwargs)

    def get_network_appliance_single_lan(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceSingleLan(networkId, **kwargs)

    def get_network_appliance_ssids(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceSsids(networkId, **kwargs)

    def get_network_appliance_ssid(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceSsid(networkId, number, **kwargs)

    def get_network_appliance_static_routes(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceStaticRoutes(networkId, **kwargs)

    def get_network_appliance_static_route(self, networkId, staticRouteId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceStaticRoute(networkId, staticRouteId, **kwargs)

    def get_network_appliance_traffic_shaping(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceTrafficShaping(networkId, **kwargs)

    def get_network_appliance_traffic_shaping_custom_performance_classes(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceTrafficShapingCustomPerformanceClasses(networkId, **kwargs)

    def get_network_appliance_traffic_shaping_custom_performance_class(self, networkId, customPerformanceClassId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceTrafficShapingCustomPerformanceClass(networkId, customPerformanceClassId, **kwargs)

    def get_network_appliance_traffic_shaping_rules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceTrafficShapingRules(networkId, **kwargs)

    def get_network_appliance_traffic_shaping_uplink_bandwidth(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceTrafficShapingUplinkBandwidth(networkId, **kwargs)

    def get_network_appliance_traffic_shaping_uplink_selection(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceTrafficShapingUplinkSelection(networkId, **kwargs)

    def get_network_appliance_uplinks_usage_history(self, networkId, t0=None, t1=None, timespan=None, resolution=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceUplinksUsageHistory(networkId, t0, t1, timespan, resolution, **kwargs)

    def get_network_appliance_vlans(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceVlans(networkId, **kwargs)

    def get_network_appliance_vlans_settings(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceVlansSettings(networkId, **kwargs)

    def get_network_appliance_vlan(self, networkId, vlanId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceVlan(networkId, vlanId, **kwargs)

    def get_network_appliance_vpn_bgp(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceVpnBgp(networkId, **kwargs)

    def get_network_appliance_vpn_site_to_site_vpn(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceVpnSiteToSiteVpn(networkId, **kwargs)

    def get_network_appliance_warm_spare(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkApplianceWarmSpare(networkId, **kwargs)

    def get_network_bluetooth_clients(self, networkId, t0=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, includeConnectivityHistory=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkBluetoothClients(networkId, t0, timespan, perPage, startingAfter, endingBefore, includeConnectivityHistory, **kwargs)

    def get_network_bluetooth_client(self, networkId, bluetoothClientId, includeConnectivityHistory=None, connectivityHistoryTimespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkBluetoothClient(networkId, bluetoothClientId, includeConnectivityHistory, connectivityHistoryTimespan, **kwargs)

    def get_network_camera_quality_retention_profiles(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkCameraQualityRetentionProfiles(networkId, **kwargs)

    def get_network_camera_quality_retention_profile(self, networkId, qualityRetentionProfileId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkCameraQualityRetentionProfile(networkId, qualityRetentionProfileId, **kwargs)

    def get_network_camera_schedules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkCameraSchedules(networkId, **kwargs)

    def get_network_camera_wireless_profiles(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkCameraWirelessProfiles(networkId, **kwargs)

    def get_network_camera_wireless_profile(self, networkId, wirelessProfileId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkCameraWirelessProfile(networkId, wirelessProfileId, **kwargs)

    def get_network_cellular_gateway_connectivity_monitoring_destinations(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkCellularGatewayConnectivityMonitoringDestinations(networkId, **kwargs)

    def get_network_cellular_gateway_dhcp(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkCellularGatewayDhcp(networkId, **kwargs)

    def get_network_cellular_gateway_subnet_pool(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkCellularGatewaySubnetPool(networkId, **kwargs)

    def get_network_cellular_gateway_uplink(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkCellularGatewayUplink(networkId, **kwargs)

    def get_network_clients(self, networkId, t0=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, statuses=None, ip=None, ip6=None, ip6Local=None, mac=None, os=None, pskGroup=None, description=None, vlan=None, namedVlan=None, recentDeviceConnections=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkClients(networkId, t0, timespan, perPage, startingAfter, endingBefore, statuses, ip, ip6, ip6Local, mac, os, pskGroup, description, vlan, namedVlan, recentDeviceConnections, **kwargs)

    def get_network_clients_application_usage(self, networkId, clients, ssidNumber=None, perPage=None, startingAfter=None, endingBefore=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkClientsApplicationUsage(networkId, clients, ssidNumber, perPage, startingAfter, endingBefore, t0, t1, timespan, **kwargs)

    def get_network_clients_bandwidth_usage_history(self, networkId, t0=None, t1=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkClientsBandwidthUsageHistory(networkId, t0, t1, timespan, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_clients_overview(self, networkId, t0=None, t1=None, timespan=None, resolution=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkClientsOverview(networkId, t0, t1, timespan, resolution, **kwargs)

    def get_network_clients_usage_histories(self, networkId, clients, ssidNumber=None, perPage=None, startingAfter=None, endingBefore=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkClientsUsageHistories(networkId, clients, ssidNumber, perPage, startingAfter, endingBefore, t0, t1, timespan, **kwargs)

    def get_network_client(self, networkId, clientId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkClient(networkId, clientId, **kwargs)

    def get_network_client_policy(self, networkId, clientId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkClientPolicy(networkId, clientId, **kwargs)

    def get_network_client_splash_authorization_status(self, networkId, clientId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkClientSplashAuthorizationStatus(networkId, clientId, **kwargs)

    def get_network_client_traffic_history(self, networkId, clientId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkClientTrafficHistory(networkId, clientId, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_client_usage_history(self, networkId, clientId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkClientUsageHistory(networkId, clientId, **kwargs)

    def get_network_devices(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkDevices(networkId, **kwargs)

    def get_network_events(self, networkId, productType=None, includedEventTypes=None, excludedEventTypes=None, deviceMac=None, deviceSerial=None, deviceName=None, clientIp=None, clientMac=None, clientName=None, smDeviceMac=None, smDeviceName=None, eventDetails=None, eventSeverity=None, isCatalyst=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkEvents(networkId, productType, includedEventTypes, excludedEventTypes, deviceMac, deviceSerial, deviceName, clientIp, clientMac, clientName, smDeviceMac, smDeviceName, eventDetails, eventSeverity, isCatalyst, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_events_event_types(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkEventsEventTypes(networkId, **kwargs)

    def get_network_firmware_upgrades(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkFirmwareUpgrades(networkId, **kwargs)

    def get_network_firmware_upgrades_staged_events(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkFirmwareUpgradesStagedEvents(networkId, **kwargs)

    def get_network_firmware_upgrades_staged_groups(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkFirmwareUpgradesStagedGroups(networkId, **kwargs)

    def get_network_firmware_upgrades_staged_group(self, networkId, groupId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkFirmwareUpgradesStagedGroup(networkId, groupId, **kwargs)

    def get_network_firmware_upgrades_staged_stages(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkFirmwareUpgradesStagedStages(networkId, **kwargs)

    def get_network_floor_plans(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkFloorPlans(networkId, **kwargs)

    def get_network_floor_plan(self, networkId, floorPlanId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkFloorPlan(networkId, floorPlanId, **kwargs)

    def get_network_group_policies(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkGroupPolicies(networkId, **kwargs)

    def get_network_group_policy(self, networkId, groupPolicyId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkGroupPolicy(networkId, groupPolicyId, **kwargs)

    def get_network_health_alerts(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkHealthAlerts(networkId, **kwargs)

    def get_network_insight_application_health_by_time(self, networkId, applicationId, t0=None, t1=None, timespan=None, resolution=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkInsightApplicationHealthByTime(networkId, applicationId, t0, t1, timespan, resolution, **kwargs)

    def get_network_meraki_auth_users(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkMerakiAuthUsers(networkId, **kwargs)

    def get_network_meraki_auth_user(self, networkId, merakiAuthUserId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkMerakiAuthUser(networkId, merakiAuthUserId, **kwargs)

    def get_network_mqtt_brokers(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkMqttBrokers(networkId, **kwargs)

    def get_network_mqtt_broker(self, networkId, mqttBrokerId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkMqttBroker(networkId, mqttBrokerId, **kwargs)

    def get_network_netflow(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkNetflow(networkId, **kwargs)

    def get_network_network_health_channel_utilization(self, networkId, t0=None, t1=None, timespan=None, resolution=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkNetworkHealthChannelUtilization(networkId, t0, t1, timespan, resolution, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_pii_pii_keys(self, networkId, username=None, email=None, mac=None, serial=None, imei=None, bluetoothMac=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkPiiPiiKeys(networkId, username, email, mac, serial, imei, bluetoothMac, **kwargs)

    def get_network_pii_requests(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkPiiRequests(networkId, **kwargs)

    def get_network_pii_request(self, networkId, requestId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkPiiRequest(networkId, requestId, **kwargs)

    def get_network_pii_sm_devices_for_key(self, networkId, username=None, email=None, mac=None, serial=None, imei=None, bluetoothMac=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkPiiSmDevicesForKey(networkId, username, email, mac, serial, imei, bluetoothMac, **kwargs)

    def get_network_pii_sm_owners_for_key(self, networkId, username=None, email=None, mac=None, serial=None, imei=None, bluetoothMac=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkPiiSmOwnersForKey(networkId, username, email, mac, serial, imei, bluetoothMac, **kwargs)

    def get_network_policies_by_client(self, networkId, perPage=None, startingAfter=None, endingBefore=None, t0=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkPoliciesByClient(networkId, perPage, startingAfter, endingBefore, t0, timespan, **kwargs)

    def get_network_sensor_alerts_current_overview_by_metric(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSensorAlertsCurrentOverviewByMetric(networkId, **kwargs)

    def get_network_sensor_alerts_overview_by_metric(self, networkId, t0=None, t1=None, timespan=None, interval=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSensorAlertsOverviewByMetric(networkId, t0, t1, timespan, interval, **kwargs)

    def get_network_sensor_alerts_profiles(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSensorAlertsProfiles(networkId, **kwargs)

    def get_network_sensor_alerts_profile(self, networkId, id, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSensorAlertsProfile(networkId, id, **kwargs)

    def get_network_sensor_mqtt_brokers(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSensorMqttBrokers(networkId, **kwargs)

    def get_network_sensor_mqtt_broker(self, networkId, mqttBrokerId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSensorMqttBroker(networkId, mqttBrokerId, **kwargs)

    def get_network_sensor_relationships(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSensorRelationships(networkId, **kwargs)

    def get_network_settings(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSettings(networkId, **kwargs)

    def get_network_sm_bypass_activation_lock_attempt(self, networkId, attemptId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmBypassActivationLockAttempt(networkId, attemptId, **kwargs)

    def get_network_sm_devices(self, networkId, fields=None, wifiMacs=None, serials=None, ids=None, uuids=None, systemTypes=None, scope=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDevices(networkId, fields, wifiMacs, serials, ids, uuids, systemTypes, scope, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_sm_device_cellular_usage_history(self, networkId, deviceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDeviceCellularUsageHistory(networkId, deviceId, **kwargs)

    def get_network_sm_device_certs(self, networkId, deviceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDeviceCerts(networkId, deviceId, **kwargs)

    def get_network_sm_device_connectivity(self, networkId, deviceId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDeviceConnectivity(networkId, deviceId, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_sm_device_desktop_logs(self, networkId, deviceId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDeviceDesktopLogs(networkId, deviceId, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_sm_device_device_command_logs(self, networkId, deviceId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDeviceDeviceCommandLogs(networkId, deviceId, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_sm_device_device_profiles(self, networkId, deviceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDeviceDeviceProfiles(networkId, deviceId, **kwargs)

    def get_network_sm_device_network_adapters(self, networkId, deviceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDeviceNetworkAdapters(networkId, deviceId, **kwargs)

    def get_network_sm_device_performance_history(self, networkId, deviceId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDevicePerformanceHistory(networkId, deviceId, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_sm_device_restrictions(self, networkId, deviceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDeviceRestrictions(networkId, deviceId, **kwargs)

    def get_network_sm_device_security_centers(self, networkId, deviceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDeviceSecurityCenters(networkId, deviceId, **kwargs)

    def get_network_sm_device_softwares(self, networkId, deviceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDeviceSoftwares(networkId, deviceId, **kwargs)

    def get_network_sm_device_wlan_lists(self, networkId, deviceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmDeviceWlanLists(networkId, deviceId, **kwargs)

    def get_network_sm_profiles(self, networkId, payloadTypes=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmProfiles(networkId, payloadTypes, **kwargs)

    def get_network_sm_target_groups(self, networkId, withDetails=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmTargetGroups(networkId, withDetails, **kwargs)

    def get_network_sm_target_group(self, networkId, targetGroupId, withDetails=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmTargetGroup(networkId, targetGroupId, withDetails, **kwargs)

    def get_network_sm_trusted_access_configs(self, networkId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmTrustedAccessConfigs(networkId, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_sm_user_access_devices(self, networkId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmUserAccessDevices(networkId, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_sm_users(self, networkId, ids=None, usernames=None, emails=None, scope=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmUsers(networkId, ids, usernames, emails, scope, **kwargs)

    def get_network_sm_user_device_profiles(self, networkId, userId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmUserDeviceProfiles(networkId, userId, **kwargs)

    def get_network_sm_user_softwares(self, networkId, userId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSmUserSoftwares(networkId, userId, **kwargs)

    def get_network_snmp(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSnmp(networkId, **kwargs)

    def get_network_splash_login_attempts(self, networkId, ssidNumber=None, loginIdentifier=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSplashLoginAttempts(networkId, ssidNumber, loginIdentifier, timespan, **kwargs)

    def get_network_switch_access_control_lists(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchAccessControlLists(networkId, **kwargs)

    def get_network_switch_access_policies(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchAccessPolicies(networkId, **kwargs)

    def get_network_switch_access_policy(self, networkId, accessPolicyNumber, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchAccessPolicy(networkId, accessPolicyNumber, **kwargs)

    def get_network_switch_alternate_management_interface(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchAlternateManagementInterface(networkId, **kwargs)

    def get_network_switch_dhcp_v4_servers_seen(self, networkId, t0=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchDhcpV4ServersSeen(networkId, t0, timespan, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_switch_dhcp_server_policy(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchDhcpServerPolicy(networkId, **kwargs)

    def get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers(self, networkId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(networkId, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device(self, networkId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(networkId, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_switch_dscp_to_cos_mappings(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchDscpToCosMappings(networkId, **kwargs)

    def get_network_switch_link_aggregations(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchLinkAggregations(networkId, **kwargs)

    def get_network_switch_mtu(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchMtu(networkId, **kwargs)

    def get_network_switch_port_schedules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchPortSchedules(networkId, **kwargs)

    def get_network_switch_qos_rules(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchQosRules(networkId, **kwargs)

    def get_network_switch_qos_rules_order(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchQosRulesOrder(networkId, **kwargs)

    def get_network_switch_qos_rule(self, networkId, qosRuleId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchQosRule(networkId, qosRuleId, **kwargs)

    def get_network_switch_routing_multicast(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchRoutingMulticast(networkId, **kwargs)

    def get_network_switch_routing_multicast_rendezvous_points(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchRoutingMulticastRendezvousPoints(networkId, **kwargs)

    def get_network_switch_routing_multicast_rendezvous_point(self, networkId, rendezvousPointId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchRoutingMulticastRendezvousPoint(networkId, rendezvousPointId, **kwargs)

    def get_network_switch_routing_ospf(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchRoutingOspf(networkId, **kwargs)

    def get_network_switch_settings(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchSettings(networkId, **kwargs)

    def get_network_switch_stacks(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchStacks(networkId, **kwargs)

    def get_network_switch_stack(self, networkId, switchStackId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchStack(networkId, switchStackId, **kwargs)

    def get_network_switch_stack_routing_interfaces(self, networkId, switchStackId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchStackRoutingInterfaces(networkId, switchStackId, **kwargs)

    def get_network_switch_stack_routing_interface(self, networkId, switchStackId, interfaceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchStackRoutingInterface(networkId, switchStackId, interfaceId, **kwargs)

    def get_network_switch_stack_routing_interface_dhcp(self, networkId, switchStackId, interfaceId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchStackRoutingInterfaceDhcp(networkId, switchStackId, interfaceId, **kwargs)

    def get_network_switch_stack_routing_static_routes(self, networkId, switchStackId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchStackRoutingStaticRoutes(networkId, switchStackId, **kwargs)

    def get_network_switch_stack_routing_static_route(self, networkId, switchStackId, staticRouteId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchStackRoutingStaticRoute(networkId, switchStackId, staticRouteId, **kwargs)

    def get_network_switch_storm_control(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchStormControl(networkId, **kwargs)

    def get_network_switch_stp(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSwitchStp(networkId, **kwargs)

    def get_network_syslog_servers(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkSyslogServers(networkId, **kwargs)

    def get_network_topology_link_layer(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkTopologyLinkLayer(networkId, **kwargs)

    def get_network_traffic(self, networkId, t0=None, timespan=None, deviceType=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkTraffic(networkId, t0, timespan, deviceType, **kwargs)

    def get_network_traffic_analysis(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkTrafficAnalysis(networkId, **kwargs)

    def get_network_traffic_shaping_application_categories(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkTrafficShapingApplicationCategories(networkId, **kwargs)

    def get_network_traffic_shaping_dscp_tagging_options(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkTrafficShapingDscpTaggingOptions(networkId, **kwargs)

    def get_network_vlan_profiles(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkVlanProfiles(networkId, **kwargs)

    def get_network_vlan_profiles_assignments_by_device(self, networkId, perPage=None, startingAfter=None, endingBefore=None, serials=None, productTypes=None, stackIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkVlanProfilesAssignmentsByDevice(networkId, perPage, startingAfter, endingBefore, serials, productTypes, stackIds, **kwargs)

    def get_network_vlan_profile(self, networkId, iname, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkVlanProfile(networkId, iname, **kwargs)

    def get_network_webhooks_http_servers(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWebhooksHttpServers(networkId, **kwargs)

    def get_network_webhooks_http_server(self, networkId, httpServerId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWebhooksHttpServer(networkId, httpServerId, **kwargs)

    def get_network_webhooks_payload_templates(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWebhooksPayloadTemplates(networkId, **kwargs)

    def get_network_webhooks_payload_template(self, networkId, payloadTemplateId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWebhooksPayloadTemplate(networkId, payloadTemplateId, **kwargs)

    def get_network_webhooks_webhook_test(self, networkId, webhookTestId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWebhooksWebhookTest(networkId, webhookTestId, **kwargs)

    def get_network_wireless_air_marshal(self, networkId, t0=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessAirMarshal(networkId, t0, timespan, **kwargs)

    def get_network_wireless_alternate_management_interface(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessAlternateManagementInterface(networkId, **kwargs)

    def get_network_wireless_billing(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessBilling(networkId, **kwargs)

    def get_network_wireless_bluetooth_settings(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessBluetoothSettings(networkId, **kwargs)

    def get_network_wireless_channel_utilization_history(self, networkId, t0=None, t1=None, timespan=None, resolution=None, autoResolution=None, clientId=None, deviceSerial=None, apTag=None, band=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessChannelUtilizationHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, **kwargs)

    def get_network_wireless_client_count_history(self, networkId, t0=None, t1=None, timespan=None, resolution=None, autoResolution=None, clientId=None, deviceSerial=None, apTag=None, band=None, ssid=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessClientCountHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid, **kwargs)

    def get_network_wireless_clients_connection_stats(self, networkId, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, apTag=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessClientsConnectionStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, **kwargs)

    def get_network_wireless_clients_latency_stats(self, networkId, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, apTag=None, fields=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessClientsLatencyStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields, **kwargs)

    def get_network_wireless_client_connection_stats(self, networkId, clientId, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, apTag=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessClientConnectionStats(networkId, clientId, t0, t1, timespan, band, ssid, vlan, apTag, **kwargs)

    def get_network_wireless_client_connectivity_events(self, networkId, clientId, perPage=None, startingAfter=None, endingBefore=None, sortOrder=None, t0=None, t1=None, timespan=None, types=None, band=None, ssidNumber=None, includedSeverities=None, deviceSerial=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessClientConnectivityEvents(networkId, clientId, perPage, startingAfter, endingBefore, sortOrder, t0, t1, timespan, types, band, ssidNumber, includedSeverities, deviceSerial, **kwargs)

    def get_network_wireless_client_latency_history(self, networkId, clientId, t0=None, t1=None, timespan=None, resolution=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessClientLatencyHistory(networkId, clientId, t0, t1, timespan, resolution, **kwargs)

    def get_network_wireless_client_latency_stats(self, networkId, clientId, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, apTag=None, fields=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessClientLatencyStats(networkId, clientId, t0, t1, timespan, band, ssid, vlan, apTag, fields, **kwargs)

    def get_network_wireless_connection_stats(self, networkId, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, apTag=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessConnectionStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, **kwargs)

    def get_network_wireless_data_rate_history(self, networkId, t0=None, t1=None, timespan=None, resolution=None, autoResolution=None, clientId=None, deviceSerial=None, apTag=None, band=None, ssid=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessDataRateHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid, **kwargs)

    def get_network_wireless_devices_connection_stats(self, networkId, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, apTag=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessDevicesConnectionStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, **kwargs)

    def get_network_wireless_devices_latency_stats(self, networkId, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, apTag=None, fields=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessDevicesLatencyStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields, **kwargs)

    def get_network_wireless_electronic_shelf_label(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessElectronicShelfLabel(networkId, **kwargs)

    def get_network_wireless_electronic_shelf_label_configured_devices(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessElectronicShelfLabelConfiguredDevices(networkId, **kwargs)

    def get_network_wireless_ethernet_ports_profiles(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessEthernetPortsProfiles(networkId, **kwargs)

    def get_network_wireless_ethernet_ports_profile(self, networkId, profileId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessEthernetPortsProfile(networkId, profileId, **kwargs)

    def get_network_wireless_failed_connections(self, networkId, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, apTag=None, serial=None, clientId=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessFailedConnections(networkId, t0, t1, timespan, band, ssid, vlan, apTag, serial, clientId, **kwargs)

    def get_network_wireless_latency_history(self, networkId, t0=None, t1=None, timespan=None, resolution=None, autoResolution=None, clientId=None, deviceSerial=None, apTag=None, band=None, ssid=None, accessCategory=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessLatencyHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid, accessCategory, **kwargs)

    def get_network_wireless_latency_stats(self, networkId, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, apTag=None, fields=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessLatencyStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields, **kwargs)

    def get_network_wireless_mesh_statuses(self, networkId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessMeshStatuses(networkId, perPage, startingAfter, endingBefore, **kwargs)

    def get_network_wireless_rf_profiles(self, networkId, includeTemplateProfiles=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessRfProfiles(networkId, includeTemplateProfiles, **kwargs)

    def get_network_wireless_rf_profile(self, networkId, rfProfileId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessRfProfile(networkId, rfProfileId, **kwargs)

    def get_network_wireless_settings(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSettings(networkId, **kwargs)

    def get_network_wireless_signal_quality_history(self, networkId, t0=None, t1=None, timespan=None, resolution=None, autoResolution=None, clientId=None, deviceSerial=None, apTag=None, band=None, ssid=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSignalQualityHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid, **kwargs)

    def get_network_wireless_ssids(self, networkId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsids(networkId, **kwargs)

    def get_network_wireless_ssid(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsid(networkId, number, **kwargs)

    def get_network_wireless_ssid_bonjour_forwarding(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidBonjourForwarding(networkId, number, **kwargs)

    def get_network_wireless_ssid_device_type_group_policies(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidDeviceTypeGroupPolicies(networkId, number, **kwargs)

    def get_network_wireless_ssid_eap_override(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidEapOverride(networkId, number, **kwargs)

    def get_network_wireless_ssid_firewall_l3_firewall_rules(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidFirewallL3FirewallRules(networkId, number, **kwargs)

    def get_network_wireless_ssid_firewall_l7_firewall_rules(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidFirewallL7FirewallRules(networkId, number, **kwargs)

    def get_network_wireless_ssid_hotspot20(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidHotspot20(networkId, number, **kwargs)

    def get_network_wireless_ssid_identity_psks(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidIdentityPsks(networkId, number, **kwargs)

    def get_network_wireless_ssid_identity_psk(self, networkId, number, identityPskId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId, **kwargs)

    def get_network_wireless_ssid_schedules(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidSchedules(networkId, number, **kwargs)

    def get_network_wireless_ssid_splash_settings(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidSplashSettings(networkId, number, **kwargs)

    def get_network_wireless_ssid_traffic_shaping_rules(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidTrafficShapingRules(networkId, number, **kwargs)

    def get_network_wireless_ssid_vpn(self, networkId, number, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessSsidVpn(networkId, number, **kwargs)

    def get_network_wireless_usage_history(self, networkId, t0=None, t1=None, timespan=None, resolution=None, autoResolution=None, clientId=None, deviceSerial=None, apTag=None, band=None, ssid=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getNetworkWirelessUsageHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid, **kwargs)

    def get_organizations(self, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizations(perPage, startingAfter, endingBefore, **kwargs)

    def get_organization(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganization(organizationId, **kwargs)

    def get_organization_action_batches(self, organizationId, status=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationActionBatches(organizationId, status, **kwargs)

    def get_organization_action_batch(self, organizationId, actionBatchId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationActionBatch(organizationId, actionBatchId, **kwargs)

    def get_organization_adaptive_policy_acls(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAdaptivePolicyAcls(organizationId, **kwargs)

    def get_organization_adaptive_policy_acl(self, organizationId, aclId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAdaptivePolicyAcl(organizationId, aclId, **kwargs)

    def get_organization_adaptive_policy_groups(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAdaptivePolicyGroups(organizationId, **kwargs)

    def get_organization_adaptive_policy_group(self, organizationId, id, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAdaptivePolicyGroup(organizationId, id, **kwargs)

    def get_organization_adaptive_policy_overview(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAdaptivePolicyOverview(organizationId, **kwargs)

    def get_organization_adaptive_policy_policies(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAdaptivePolicyPolicies(organizationId, **kwargs)

    def get_organization_adaptive_policy_policy(self, organizationId, id, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAdaptivePolicyPolicy(organizationId, id, **kwargs)

    def get_organization_adaptive_policy_settings(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAdaptivePolicySettings(organizationId, **kwargs)

    def get_organization_admins(self, organizationId, networkIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAdmins(organizationId, networkIds, **kwargs)

    def get_organization_alerts_profiles(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAlertsProfiles(organizationId, **kwargs)

    def get_organization_api_requests(self, organizationId, t0=None, t1=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, adminId=None, path=None, method=None, responseCode=None, sourceIp=None, userAgent=None, version=None, operationIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApiRequests(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, adminId, path, method, responseCode, sourceIp, userAgent, version, operationIds, **kwargs)

    def get_organization_api_requests_overview(self, organizationId, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApiRequestsOverview(organizationId, t0, t1, timespan, **kwargs)

    def get_organization_api_requests_overview_response_codes_by_interval(self, organizationId, t0=None, t1=None, timespan=None, interval=None, version=None, operationIds=None, sourceIps=None, adminIds=None, userAgent=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApiRequestsOverviewResponseCodesByInterval(organizationId, t0, t1, timespan, interval, version, operationIds, sourceIps, adminIds, userAgent, **kwargs)

    def get_organization_appliance_security_events(self, organizationId, t0=None, t1=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, sortOrder=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApplianceSecurityEvents(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, sortOrder, **kwargs)

    def get_organization_appliance_security_intrusion(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApplianceSecurityIntrusion(organizationId, **kwargs)

    def get_organization_appliance_traffic_shaping_vpn_exclusions_by_network(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(organizationId, perPage, startingAfter, endingBefore, networkIds, **kwargs)

    def get_organization_appliance_uplink_statuses(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, serials=None, iccids=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApplianceUplinkStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids, **kwargs)

    def get_organization_appliance_uplinks_statuses_overview(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApplianceUplinksStatusesOverview(organizationId, **kwargs)

    def get_organization_appliance_uplinks_usage_by_network(self, organizationId, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApplianceUplinksUsageByNetwork(organizationId, t0, t1, timespan, **kwargs)

    def get_organization_appliance_vpn_stats(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApplianceVpnStats(organizationId, perPage, startingAfter, endingBefore, networkIds, t0, t1, timespan, **kwargs)

    def get_organization_appliance_vpn_statuses(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApplianceVpnStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds, **kwargs)

    def get_organization_appliance_vpn_third_party_v_p_n_peers(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApplianceVpnThirdPartyVPNPeers(organizationId, **kwargs)

    def get_organization_appliance_vpn_vpn_firewall_rules(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationApplianceVpnVpnFirewallRules(organizationId, **kwargs)

    def get_organization_assurance_alerts(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, sortOrder=None, networkId=None, severity=None, types=None, tsStart=None, tsEnd=None, category=None, sortBy=None, serials=None, deviceTypes=None, deviceTags=None, active=None, dismissed=None, resolved=None, suppressAlertsForOfflineNodes=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAssuranceAlerts(organizationId, perPage, startingAfter, endingBefore, sortOrder, networkId, severity, types, tsStart, tsEnd, category, sortBy, serials, deviceTypes, deviceTags, active, dismissed, resolved, suppressAlertsForOfflineNodes, **kwargs)

    def get_organization_assurance_alerts_overview(self, organizationId, networkId=None, severity=None, types=None, tsStart=None, tsEnd=None, category=None, serials=None, deviceTypes=None, deviceTags=None, active=None, dismissed=None, resolved=None, suppressAlertsForOfflineNodes=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAssuranceAlertsOverview(organizationId, networkId, severity, types, tsStart, tsEnd, category, serials, deviceTypes, deviceTags, active, dismissed, resolved, suppressAlertsForOfflineNodes, **kwargs)

    def get_organization_assurance_alerts_overview_by_network(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, sortOrder=None, networkId=None, severity=None, types=None, tsStart=None, tsEnd=None, category=None, serials=None, deviceTypes=None, deviceTags=None, active=None, dismissed=None, resolved=None, suppressAlertsForOfflineNodes=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAssuranceAlertsOverviewByNetwork(organizationId, perPage, startingAfter, endingBefore, sortOrder, networkId, severity, types, tsStart, tsEnd, category, serials, deviceTypes, deviceTags, active, dismissed, resolved, suppressAlertsForOfflineNodes, **kwargs)

    def get_organization_assurance_alerts_overview_by_type(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, sortOrder=None, networkId=None, severity=None, types=None, tsStart=None, tsEnd=None, category=None, sortBy=None, serials=None, deviceTypes=None, deviceTags=None, active=None, dismissed=None, resolved=None, suppressAlertsForOfflineNodes=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAssuranceAlertsOverviewByType(organizationId, perPage, startingAfter, endingBefore, sortOrder, networkId, severity, types, tsStart, tsEnd, category, sortBy, serials, deviceTypes, deviceTags, active, dismissed, resolved, suppressAlertsForOfflineNodes, **kwargs)

    def get_organization_assurance_alerts_overview_historical(self, organizationId, segmentDuration, tsStart, networkId=None, severity=None, types=None, tsEnd=None, category=None, serials=None, deviceTypes=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAssuranceAlertsOverviewHistorical(organizationId, segmentDuration, tsStart, networkId, severity, types, tsEnd, category, serials, deviceTypes, **kwargs)

    def get_organization_assurance_alert(self, organizationId, id, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationAssuranceAlert(organizationId, id, **kwargs)

    def get_organization_branding_policies(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationBrandingPolicies(organizationId, **kwargs)

    def get_organization_branding_policies_priorities(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationBrandingPoliciesPriorities(organizationId, **kwargs)

    def get_organization_branding_policy(self, organizationId, brandingPolicyId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationBrandingPolicy(organizationId, brandingPolicyId, **kwargs)

    def get_organization_camera_boundaries_areas_by_device(self, organizationId, serials=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCameraBoundariesAreasByDevice(organizationId, serials, **kwargs)

    def get_organization_camera_boundaries_lines_by_device(self, organizationId, serials=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCameraBoundariesLinesByDevice(organizationId, serials, **kwargs)

    def get_organization_camera_custom_analytics_artifacts(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCameraCustomAnalyticsArtifacts(organizationId, **kwargs)

    def get_organization_camera_custom_analytics_artifact(self, organizationId, artifactId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCameraCustomAnalyticsArtifact(organizationId, artifactId, **kwargs)

    def get_organization_camera_detections_history_by_boundary_by_interval(self, organizationId, boundaryIds, ranges, duration=None, perPage=None, boundaryTypes=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCameraDetectionsHistoryByBoundaryByInterval(organizationId, boundaryIds, ranges, duration, perPage, boundaryTypes, **kwargs)

    def get_organization_camera_onboarding_statuses(self, organizationId, serials=None, networkIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCameraOnboardingStatuses(organizationId, serials, networkIds, **kwargs)

    def get_organization_camera_permissions(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCameraPermissions(organizationId, **kwargs)

    def get_organization_camera_permission(self, organizationId, permissionScopeId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCameraPermission(organizationId, permissionScopeId, **kwargs)

    def get_organization_camera_roles(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCameraRoles(organizationId, **kwargs)

    def get_organization_camera_role(self, organizationId, roleId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCameraRole(organizationId, roleId, **kwargs)

    def get_organization_cellular_gateway_esims_inventory(self, organizationId, eids=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCellularGatewayEsimsInventory(organizationId, eids, **kwargs)

    def get_organization_cellular_gateway_esims_service_providers(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCellularGatewayEsimsServiceProviders(organizationId, **kwargs)

    def get_organization_cellular_gateway_esims_service_providers_accounts(self, organizationId, accountIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCellularGatewayEsimsServiceProvidersAccounts(organizationId, accountIds, **kwargs)

    def get_organization_cellular_gateway_esims_service_providers_accounts_communication_plans(self, organizationId, accountIds, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans(organizationId, accountIds, **kwargs)

    def get_organization_cellular_gateway_esims_service_providers_accounts_rate_plans(self, organizationId, accountIds, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans(organizationId, accountIds, **kwargs)

    def get_organization_cellular_gateway_uplink_statuses(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, serials=None, iccids=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationCellularGatewayUplinkStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids, **kwargs)

    def get_organization_clients_bandwidth_usage_history(self, organizationId, networkTag=None, deviceTag=None, ssidName=None, usageUplink=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationClientsBandwidthUsageHistory(organizationId, networkTag, deviceTag, ssidName, usageUplink, t0, t1, timespan, **kwargs)

    def get_organization_clients_overview(self, organizationId, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationClientsOverview(organizationId, t0, t1, timespan, **kwargs)

    def get_organization_clients_search(self, organizationId, mac, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationClientsSearch(organizationId, mac, perPage, startingAfter, endingBefore, **kwargs)

    def get_organization_config_templates(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationConfigTemplates(organizationId, **kwargs)

    def get_organization_config_template(self, organizationId, configTemplateId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationConfigTemplate(organizationId, configTemplateId, **kwargs)

    def get_organization_config_template_switch_profiles(self, organizationId, configTemplateId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationConfigTemplateSwitchProfiles(organizationId, configTemplateId, **kwargs)

    def get_organization_config_template_switch_profile_ports(self, organizationId, configTemplateId, profileId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationConfigTemplateSwitchProfilePorts(organizationId, configTemplateId, profileId, **kwargs)

    def get_organization_config_template_switch_profile_port(self, organizationId, configTemplateId, profileId, portId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationConfigTemplateSwitchProfilePort(organizationId, configTemplateId, profileId, portId, **kwargs)

    def get_organization_configuration_changes(self, organizationId, t0=None, t1=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, networkId=None, adminId=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationConfigurationChanges(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, networkId, adminId, **kwargs)

    def get_organization_devices(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, configurationUpdatedAfter=None, networkIds=None, productTypes=None, tags=None, tagsFilterType=None, name=None, mac=None, serial=None, model=None, macs=None, serials=None, sensorMetrics=None, sensorAlertProfileIds=None, models=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationDevices(organizationId, perPage, startingAfter, endingBefore, configurationUpdatedAfter, networkIds, productTypes, tags, tagsFilterType, name, mac, serial, model, macs, serials, sensorMetrics, sensorAlertProfileIds, models, **kwargs)

    def get_organization_devices_availabilities(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, productTypes=None, serials=None, tags=None, tagsFilterType=None, statuses=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationDevicesAvailabilities(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType, statuses, **kwargs)

    def get_organization_devices_availabilities_change_history(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, t0=None, t1=None, timespan=None, serials=None, productTypes=None, networkIds=None, statuses=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationDevicesAvailabilitiesChangeHistory(organizationId, perPage, startingAfter, endingBefore, t0, t1, timespan, serials, productTypes, networkIds, statuses, **kwargs)

    def get_organization_devices_overview_by_model(self, organizationId, models=None, networkIds=None, productTypes=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationDevicesOverviewByModel(organizationId, models, networkIds, productTypes, **kwargs)

    def get_organization_devices_power_modules_statuses_by_device(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, productTypes=None, serials=None, tags=None, tagsFilterType=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationDevicesPowerModulesStatusesByDevice(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType, **kwargs)

    def get_organization_devices_provisioning_statuses(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, productTypes=None, serials=None, status=None, tags=None, tagsFilterType=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationDevicesProvisioningStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, status, tags, tagsFilterType, **kwargs)

    def get_organization_devices_statuses(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, serials=None, statuses=None, productTypes=None, models=None, tags=None, tagsFilterType=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationDevicesStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, statuses, productTypes, models, tags, tagsFilterType, **kwargs)

    def get_organization_devices_statuses_overview(self, organizationId, productTypes=None, networkIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationDevicesStatusesOverview(organizationId, productTypes, networkIds, **kwargs)

    def get_organization_devices_uplinks_addresses_by_device(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, productTypes=None, serials=None, tags=None, tagsFilterType=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationDevicesUplinksAddressesByDevice(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType, **kwargs)

    def get_organization_devices_uplinks_loss_and_latency(self, organizationId, t0=None, t1=None, timespan=None, uplink=None, ip=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationDevicesUplinksLossAndLatency(organizationId, t0, t1, timespan, uplink, ip, **kwargs)

    def get_organization_early_access_features(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationEarlyAccessFeatures(organizationId, **kwargs)

    def get_organization_early_access_features_opt_ins(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationEarlyAccessFeaturesOptIns(organizationId, **kwargs)

    def get_organization_early_access_features_opt_in(self, organizationId, optInId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationEarlyAccessFeaturesOptIn(organizationId, optInId, **kwargs)

    def get_organization_firmware_upgrades(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, status=None, productTypes=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationFirmwareUpgrades(organizationId, perPage, startingAfter, endingBefore, status, productTypes, **kwargs)

    def get_organization_firmware_upgrades_by_device(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, serials=None, macs=None, firmwareUpgradeBatchIds=None, upgradeStatuses=None, currentUpgradesOnly=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationFirmwareUpgradesByDevice(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, macs, firmwareUpgradeBatchIds, upgradeStatuses, currentUpgradesOnly, **kwargs)

    def get_organization_floor_plans_auto_locate_devices(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, floorPlanIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationFloorPlansAutoLocateDevices(organizationId, perPage, startingAfter, endingBefore, networkIds, floorPlanIds, **kwargs)

    def get_organization_floor_plans_auto_locate_statuses(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, floorPlanIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationFloorPlansAutoLocateStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds, floorPlanIds, **kwargs)

    def get_organization_insight_applications(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationInsightApplications(organizationId, **kwargs)

    def get_organization_insight_monitored_media_servers(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationInsightMonitoredMediaServers(organizationId, **kwargs)

    def get_organization_insight_monitored_media_server(self, organizationId, monitoredMediaServerId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationInsightMonitoredMediaServer(organizationId, monitoredMediaServerId, **kwargs)

    def get_organization_inventory_devices(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, usedState=None, search=None, macs=None, networkIds=None, serials=None, models=None, orderNumbers=None, tags=None, tagsFilterType=None, productTypes=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationInventoryDevices(organizationId, perPage, startingAfter, endingBefore, usedState, search, macs, networkIds, serials, models, orderNumbers, tags, tagsFilterType, productTypes, **kwargs)

    def get_organization_inventory_devices_swaps_bulk(self, organizationId, id, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationInventoryDevicesSwapsBulk(organizationId, id, **kwargs)

    def get_organization_inventory_device(self, organizationId, serial, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationInventoryDevice(organizationId, serial, **kwargs)

    def get_organization_inventory_onboarding_cloud_monitoring_imports(self, organizationId, importIds, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationInventoryOnboardingCloudMonitoringImports(organizationId, importIds, **kwargs)

    def get_organization_inventory_onboarding_cloud_monitoring_networks(self, organizationId, deviceType, search=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationInventoryOnboardingCloudMonitoringNetworks(organizationId, deviceType, search, perPage, startingAfter, endingBefore, **kwargs)

    def get_organization_licenses(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, deviceSerial=None, networkId=None, state=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationLicenses(organizationId, perPage, startingAfter, endingBefore, deviceSerial, networkId, state, **kwargs)

    def get_organization_licenses_overview(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationLicensesOverview(organizationId, **kwargs)

    def get_organization_license(self, organizationId, licenseId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationLicense(organizationId, licenseId, **kwargs)

    def get_organization_licensing_coterm_licenses(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, invalidated=None, expired=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationLicensingCotermLicenses(organizationId, perPage, startingAfter, endingBefore, invalidated, expired, **kwargs)

    def get_organization_login_security(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationLoginSecurity(organizationId, **kwargs)

    def get_organization_networks(self, organizationId, configTemplateId=None, isBoundToConfigTemplate=None, tags=None, tagsFilterType=None, productTypes=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationNetworks(organizationId, configTemplateId, isBoundToConfigTemplate, tags, tagsFilterType, productTypes, perPage, startingAfter, endingBefore, **kwargs)

    def get_organization_openapi_spec(self, organizationId, version=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationOpenapiSpec(organizationId, version, **kwargs)

    def get_organization_policy_objects(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationPolicyObjects(organizationId, perPage, startingAfter, endingBefore, **kwargs)

    def get_organization_policy_objects_groups(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationPolicyObjectsGroups(organizationId, perPage, startingAfter, endingBefore, **kwargs)

    def get_organization_policy_objects_group(self, organizationId, policyObjectGroupId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationPolicyObjectsGroup(organizationId, policyObjectGroupId, **kwargs)

    def get_organization_policy_object(self, organizationId, policyObjectId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationPolicyObject(organizationId, policyObjectId, **kwargs)

    def get_organization_saml(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSaml(organizationId, **kwargs)

    def get_organization_saml_idps(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSamlIdps(organizationId, **kwargs)

    def get_organization_saml_idp(self, organizationId, idpId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSamlIdp(organizationId, idpId, **kwargs)

    def get_organization_saml_roles(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSamlRoles(organizationId, **kwargs)

    def get_organization_saml_role(self, organizationId, samlRoleId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSamlRole(organizationId, samlRoleId, **kwargs)

    def get_organization_sensor_readings_history(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, t0=None, t1=None, timespan=None, networkIds=None, serials=None, metrics=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSensorReadingsHistory(organizationId, perPage, startingAfter, endingBefore, t0, t1, timespan, networkIds, serials, metrics, **kwargs)

    def get_organization_sensor_readings_latest(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, serials=None, metrics=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSensorReadingsLatest(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, metrics, **kwargs)

    def get_organization_sm_admins_roles(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSmAdminsRoles(organizationId, perPage, startingAfter, endingBefore, **kwargs)

    def get_organization_sm_admins_role(self, organizationId, roleId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSmAdminsRole(organizationId, roleId, **kwargs)

    def get_organization_sm_apns_cert(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSmApnsCert(organizationId, **kwargs)

    def get_organization_sm_sentry_policies_assignments_by_network(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSmSentryPoliciesAssignmentsByNetwork(organizationId, perPage, startingAfter, endingBefore, networkIds, **kwargs)

    def get_organization_sm_vpp_accounts(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSmVppAccounts(organizationId, **kwargs)

    def get_organization_sm_vpp_account(self, organizationId, vppAccountId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSmVppAccount(organizationId, vppAccountId, **kwargs)

    def get_organization_snmp(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSnmp(organizationId, **kwargs)

    def get_organization_splash_asset(self, organizationId, id, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSplashAsset(organizationId, id, **kwargs)

    def get_organization_splash_themes(self, organizationId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSplashThemes(organizationId, **kwargs)

    def get_organization_summary_switch_power_history(self, organizationId, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSummarySwitchPowerHistory(organizationId, t0, t1, timespan, **kwargs)

    def get_organization_summary_top_appliances_by_utilization(self, organizationId, networkTag=None, deviceTag=None, quantity=None, ssidName=None, usageUplink=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSummaryTopAppliancesByUtilization(organizationId, networkTag, deviceTag, quantity, ssidName, usageUplink, t0, t1, timespan, **kwargs)

    def get_organization_summary_top_applications_by_usage(self, organizationId, networkTag=None, device=None, networkId=None, quantity=None, ssidName=None, usageUplink=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSummaryTopApplicationsByUsage(organizationId, networkTag, device, networkId, quantity, ssidName, usageUplink, t0, t1, timespan, **kwargs)

    def get_organization_summary_top_applications_categories_by_usage(self, organizationId, networkTag=None, deviceTag=None, networkId=None, quantity=None, ssidName=None, usageUplink=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSummaryTopApplicationsCategoriesByUsage(organizationId, networkTag, deviceTag, networkId, quantity, ssidName, usageUplink, t0, t1, timespan, **kwargs)

    def get_organization_summary_top_clients_by_usage(self, organizationId, networkTag=None, deviceTag=None, quantity=None, ssidName=None, usageUplink=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSummaryTopClientsByUsage(organizationId, networkTag, deviceTag, quantity, ssidName, usageUplink, t0, t1, timespan, **kwargs)

    def get_organization_summary_top_clients_manufacturers_by_usage(self, organizationId, networkTag=None, deviceTag=None, quantity=None, ssidName=None, usageUplink=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSummaryTopClientsManufacturersByUsage(organizationId, networkTag, deviceTag, quantity, ssidName, usageUplink, t0, t1, timespan, **kwargs)

    def get_organization_summary_top_devices_by_usage(self, organizationId, networkTag=None, deviceTag=None, quantity=None, ssidName=None, usageUplink=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSummaryTopDevicesByUsage(organizationId, networkTag, deviceTag, quantity, ssidName, usageUplink, t0, t1, timespan, **kwargs)

    def get_organization_summary_top_devices_models_by_usage(self, organizationId, networkTag=None, deviceTag=None, quantity=None, ssidName=None, usageUplink=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSummaryTopDevicesModelsByUsage(organizationId, networkTag, deviceTag, quantity, ssidName, usageUplink, t0, t1, timespan, **kwargs)

    def get_organization_summary_top_networks_by_status(self, organizationId, networkTag=None, deviceTag=None, quantity=None, ssidName=None, usageUplink=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSummaryTopNetworksByStatus(organizationId, networkTag, deviceTag, quantity, ssidName, usageUplink, perPage, startingAfter, endingBefore, **kwargs)

    def get_organization_summary_top_ssids_by_usage(self, organizationId, networkTag=None, deviceTag=None, quantity=None, ssidName=None, usageUplink=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSummaryTopSsidsByUsage(organizationId, networkTag, deviceTag, quantity, ssidName, usageUplink, t0, t1, timespan, **kwargs)

    def get_organization_summary_top_switches_by_energy_usage(self, organizationId, networkTag=None, deviceTag=None, quantity=None, ssidName=None, usageUplink=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSummaryTopSwitchesByEnergyUsage(organizationId, networkTag, deviceTag, quantity, ssidName, usageUplink, t0, t1, timespan, **kwargs)

    def get_organization_switch_ports_by_switch(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, configurationUpdatedAfter=None, mac=None, macs=None, name=None, networkIds=None, portProfileIds=None, serial=None, serials=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSwitchPortsBySwitch(organizationId, perPage, startingAfter, endingBefore, configurationUpdatedAfter, mac, macs, name, networkIds, portProfileIds, serial, serials, **kwargs)

    def get_organization_switch_ports_clients_overview_by_device(self, organizationId, t0=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, configurationUpdatedAfter=None, mac=None, macs=None, name=None, networkIds=None, portProfileIds=None, serial=None, serials=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSwitchPortsClientsOverviewByDevice(organizationId, t0, timespan, perPage, startingAfter, endingBefore, configurationUpdatedAfter, mac, macs, name, networkIds, portProfileIds, serial, serials, **kwargs)

    def get_organization_switch_ports_overview(self, organizationId, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSwitchPortsOverview(organizationId, t0, t1, timespan, **kwargs)

    def get_organization_switch_ports_statuses_by_switch(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, configurationUpdatedAfter=None, mac=None, macs=None, name=None, networkIds=None, portProfileIds=None, serial=None, serials=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSwitchPortsStatusesBySwitch(organizationId, perPage, startingAfter, endingBefore, configurationUpdatedAfter, mac, macs, name, networkIds, portProfileIds, serial, serials, **kwargs)

    def get_organization_switch_ports_topology_discovery_by_device(self, organizationId, t0=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, configurationUpdatedAfter=None, mac=None, macs=None, name=None, networkIds=None, portProfileIds=None, serial=None, serials=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationSwitchPortsTopologyDiscoveryByDevice(organizationId, t0, timespan, perPage, startingAfter, endingBefore, configurationUpdatedAfter, mac, macs, name, networkIds, portProfileIds, serial, serials, **kwargs)

    def get_organization_uplinks_statuses(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, serials=None, iccids=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationUplinksStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids, **kwargs)

    def get_organization_webhooks_alert_types(self, organizationId, productType=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWebhooksAlertTypes(organizationId, productType, **kwargs)

    def get_organization_webhooks_callbacks_status(self, organizationId, callbackId, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWebhooksCallbacksStatus(organizationId, callbackId, **kwargs)

    def get_organization_webhooks_logs(self, organizationId, t0=None, t1=None, timespan=None, perPage=None, startingAfter=None, endingBefore=None, url=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWebhooksLogs(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, url, **kwargs)

    def get_organization_wireless_air_marshal_rules(self, organizationId, networkIds=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessAirMarshalRules(organizationId, networkIds, perPage, startingAfter, endingBefore, **kwargs)

    def get_organization_wireless_air_marshal_settings_by_network(self, organizationId, networkIds=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessAirMarshalSettingsByNetwork(organizationId, networkIds, perPage, startingAfter, endingBefore, **kwargs)

    def get_organization_wireless_clients_overview_by_device(self, organizationId, networkIds=None, serials=None, campusGatewayClusterIds=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessClientsOverviewByDevice(organizationId, networkIds, serials, campusGatewayClusterIds, perPage, startingAfter, endingBefore, **kwargs)

    def get_organization_wireless_devices_channel_utilization_by_device(self, organizationId, networkIds=None, serials=None, perPage=None, startingAfter=None, endingBefore=None, t0=None, t1=None, timespan=None, interval=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessDevicesChannelUtilizationByDevice(organizationId, networkIds, serials, perPage, startingAfter, endingBefore, t0, t1, timespan, interval, **kwargs)

    def get_organization_wireless_devices_channel_utilization_by_network(self, organizationId, networkIds=None, serials=None, perPage=None, startingAfter=None, endingBefore=None, t0=None, t1=None, timespan=None, interval=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessDevicesChannelUtilizationByNetwork(organizationId, networkIds, serials, perPage, startingAfter, endingBefore, t0, t1, timespan, interval, **kwargs)

    def get_organization_wireless_devices_channel_utilization_history_by_device_by_interval(self, organizationId, networkIds=None, serials=None, perPage=None, startingAfter=None, endingBefore=None, t0=None, t1=None, timespan=None, interval=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval(organizationId, networkIds, serials, perPage, startingAfter, endingBefore, t0, t1, timespan, interval, **kwargs)

    def get_organization_wireless_devices_channel_utilization_history_by_network_by_interval(self, organizationId, networkIds=None, serials=None, perPage=None, startingAfter=None, endingBefore=None, t0=None, t1=None, timespan=None, interval=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval(organizationId, networkIds, serials, perPage, startingAfter, endingBefore, t0, t1, timespan, interval, **kwargs)

    def get_organization_wireless_devices_ethernet_statuses(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessDevicesEthernetStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds, **kwargs)

    def get_organization_wireless_devices_packet_loss_by_client(self, organizationId, networkIds=None, ssids=None, bands=None, macs=None, perPage=None, startingAfter=None, endingBefore=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessDevicesPacketLossByClient(organizationId, networkIds, ssids, bands, macs, perPage, startingAfter, endingBefore, t0, t1, timespan, **kwargs)

    def get_organization_wireless_devices_packet_loss_by_device(self, organizationId, networkIds=None, serials=None, ssids=None, bands=None, perPage=None, startingAfter=None, endingBefore=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessDevicesPacketLossByDevice(organizationId, networkIds, serials, ssids, bands, perPage, startingAfter, endingBefore, t0, t1, timespan, **kwargs)

    def get_organization_wireless_devices_packet_loss_by_network(self, organizationId, networkIds=None, serials=None, ssids=None, bands=None, perPage=None, startingAfter=None, endingBefore=None, t0=None, t1=None, timespan=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessDevicesPacketLossByNetwork(organizationId, networkIds, serials, ssids, bands, perPage, startingAfter, endingBefore, t0, t1, timespan, **kwargs)

    def get_organization_wireless_devices_wireless_controllers_by_device(self, organizationId, networkIds=None, serials=None, controllerSerials=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessDevicesWirelessControllersByDevice(organizationId, networkIds, serials, controllerSerials, perPage, startingAfter, endingBefore, **kwargs)

    def get_organization_wireless_rf_profiles_assignments_by_device(self, organizationId, perPage=None, startingAfter=None, endingBefore=None, networkIds=None, productTypes=None, name=None, mac=None, serial=None, model=None, macs=None, serials=None, models=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessRfProfilesAssignmentsByDevice(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, name, mac, serial, model, macs, serials, models, **kwargs)

    def get_organization_wireless_ssids_statuses_by_device(self, organizationId, networkIds=None, serials=None, bssids=None, hideDisabled=None, perPage=None, startingAfter=None, endingBefore=None, **kwargs):
        if not self.meraki_client:
            return {"error": "Meraki integration is disabled."}
        return self.meraki_client.getOrganizationWirelessSsidsStatusesByDevice(organizationId, networkIds, serials, bssids, hideDisabled, perPage, startingAfter, endingBefore, **kwargs)









    # ================================
    # Catalyst Methods
    # ================================
    def get_all_catalyst_devices(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_all_devices()

    def get_catalyst_device_by_id(self, device_id):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_device_by_id(device_id)

    def run_cli_command_on_catalyst_device(self, device_id: str, command: str):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.run_cli_command(device_id, command)

    def get_catalyst_task_status_by_id(self, task_id: str):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_task_status_by_id(task_id)

    def get_command_output(self, file_id):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.fetch_command_output_by_file_id(file_id)

    def get_all_sites(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_all_sites()

    def get_all_ssids(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_all_ssids()

    def get_catalyst_system_info(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_catalyst_system_info()

    def get_dnac_packages_summary(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_dnac_packages_summary()

    def get_all_interfaces(self):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_all_interfaces()

    def get_device_interfaces(self, device_id):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_device_interfaces(device_id)

    def get_interfaces_by_ip(self, ip_address):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_interfaces_by_ip(ip_address)

    def initiate_path_trace(self, source_ip, destination_ip):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.initiate_path_trace(source_ip, destination_ip)

    def get_path_trace_result(self, flow_analysis_id):
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_path_trace_result(flow_analysis_id)
 
    def get_catalyst_device_list_direct(self):
        if self.catalyst_client:
            return self.catalyst_client.get_device_list_direct()
        return {"error": "Catalyst client not available"}

    def get_catalyst_device_detail_by_name(self, device_name: str):
        """ Retrieve device detail by hostname. """
        if not self.catalyst_client:
            return {"error": "Catalyst client not initialized."}
        return self.catalyst_client.get_device_detail_by_name(device_name)

    def get_catalyst_device_detail_by_mac_address(self, mac_address: str):
        """ Retrieve device detail by MAC address. """
        if not self.catalyst_client:
            return {"error": "Catalyst client not initialized."}
        return self.catalyst_client.get_device_detail_by_mac(mac_address)
    

    def get_site_by_name(self, site_name: str):
        """
        Wraps the CatalystCenterClient's get_site_by_name_v2 method.
        """
        if not self.catalyst_client:
            return {"error": "Catalyst client not initialized."}
        return self.catalyst_client.get_site_by_name_v2(site_name)

    def get_all_devices_by_site(self, site_id: str):
        """
        Calls CatalystCenterClient.get_all_devices_by_site
        to retrieve all devices for a given site ID.
        """
        if not self.catalyst_client:
            return {"message": "Catalyst Center integration is disabled."}
        return self.catalyst_client.get_all_devices_by_site(site_id)





    # ================================
    # Catalyst Methods SDK  
    # ================================
    def gets_all_the_versions_of_a_given_template(self, templateId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getsAllTheVersionsOfAGivenTemplate(templateId, **kwargs)

    def get_multicast_virtual_networks(self, fabricId=None, virtualNetworkName=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getMulticastVirtualNetworks(fabricId, virtualNetworkName, offset, limit, **kwargs)

    def get_device_controllability_settings(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceControllabilitySettings(**kwargs)

    def get_chassis_details_for_device(self, deviceId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getChassisDetailsForDevice(deviceId, **kwargs)

    def gets_a_building(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getsABuilding(id, **kwargs)

    def get_count_of_all_discovery_jobs(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getCountOfAllDiscoveryJobs(**kwargs)

    def get_views_for_a_given_view_group(self, viewGroupId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getViewsForAGivenViewGroup(viewGroupId, **kwargs)

    def get_device_by_id(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceById(id, **kwargs)

    def retrieve_image_distribution_servers(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveImageDistributionServers(**kwargs)

    def retrieve_banner_settings_for_a_site(self, id, _inherited=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveBannerSettingsForASite(id, _inherited, **kwargs)

    def get_site_assigned_network_devices(self, siteId, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSiteAssignedNetworkDevices(siteId, offset, limit, **kwargs)

    def get_network_devices_credentials_sync_status(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getNetworkDevicesCredentialsSyncStatus(id, **kwargs)

    def get_software_image_details(self, imageUuid=None, name=None, family=None, applicationType=None, imageIntegrityStatus=None, version=None, imageSeries=None, imageName=None, isTaggedGolden=None, isCCORecommended=None, isCCOLatest=None, createdTime=None, imageSizeGreaterThan=None, imageSizeLesserThan=None, sortBy=None, sortOrder=None, limit=None, offset=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSoftwareImageDetails(imageUuid, name, family, applicationType, imageIntegrityStatus, version, imageSeries, imageName, isTaggedGolden, isCCORecommended, isCCOLatest, createdTime, imageSizeGreaterThan, imageSizeLesserThan, sortBy, sortOrder, limit, offset, **kwargs)

    def get_anycast_gateways(self, id=None, fabricId=None, virtualNetworkName=None, ipPoolName=None, vlanName=None, vlanId=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAnycastGateways(id, fabricId, virtualNetworkName, ipPoolName, vlanName, vlanId, offset, limit, **kwargs)

    def get_tag_members_by_id(self, id, memberType, offset=None, limit=None, memberAssociationType=None, level=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTagMembersById(id, memberType, offset, limit, memberAssociationType, level, **kwargs)

    def get_fabric_site_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricSiteCount(**kwargs)

    def retrieves_all_the_validation_sets(self, view=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesAllTheValidationSets(view, **kwargs)

    def retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to(self, profileId, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(profileId, offset, limit, **kwargs)

    def get_fabric_devices_layer2_handoffs_count(self, fabricId, networkDeviceId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricDevicesLayer2HandoffsCount(fabricId, networkDeviceId, **kwargs)

    def count_of_event_subscriptions(self, eventIds, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.countOfEventSubscriptions(eventIds, **kwargs)

    def get_details_of_a_single_assurance_event(self, id, X_CALLER_ID=None, attribute=None, view=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDetailsOfASingleAssuranceEvent(id, X_CALLER_ID, attribute, view, **kwargs)

    def retrieve_telemetry_settings_for_a_site(self, id, _inherited=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveTelemetrySettingsForASite(id, _inherited, **kwargs)

    def get_floor_settings(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFloorSettings(**kwargs)

    def get_the_total_number_of_issues_for_given_set_of_filters(self, X_CALLER_ID=None, startTime=None, endTime=None, isGlobal=None, priority=None, severity=None, status=None, entityType=None, category=None, deviceType=None, name=None, issueId=None, entityId=None, updatedBy=None, siteHierarchy=None, siteHierarchyId=None, siteName=None, siteId=None, fabricSiteId=None, fabricVnName=None, fabricTransitSiteId=None, networkDeviceId=None, networkDeviceIpAddress=None, macAddress=None, aiDriven=None, fabricDriven=None, fabricSiteDriven=None, fabricVnDriven=None, fabricTransitDriven=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTheTotalNumberOfIssuesForGivenSetOfFilters(X_CALLER_ID, startTime, endTime, isGlobal, priority, severity, status, entityType, category, deviceType, name, issueId, entityId, updatedBy, siteHierarchy, siteHierarchyId, siteName, siteId, fabricSiteId, fabricVnName, fabricTransitSiteId, networkDeviceId, networkDeviceIpAddress, macAddress, aiDriven, fabricDriven, fabricSiteDriven, fabricVnDriven, fabricTransitDriven, **kwargs)

    def get_tag(self, name=None, additionalInfo_nameSpace=None, additionalInfo_attributes=None, level=None, offset=None, limit=None, size=None, field=None, sortBy=None, order=None, systemTag=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTag(name, additionalInfo_nameSpace, additionalInfo_attributes, level, offset, limit, size, field, sortBy, order, systemTag, **kwargs)

    def get_layer2_virtual_networks(self, id=None, fabricId=None, vlanName=None, vlanId=None, trafficType=None, associatedLayer3VirtualNetworkName=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getLayer2VirtualNetworks(id, fabricId, vlanName, vlanId, trafficType, associatedLayer3VirtualNetworkName, offset, limit, **kwargs)

    def get_fabric_zone_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricZoneCount(**kwargs)

    def get_webhook_destination(self, webhookIds=None, offset=None, limit=None, sortBy=None, order=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getWebhookDestination(webhookIds, offset, limit, sortBy, order, **kwargs)

    def retrieve_time_zone_settings_for_a_site(self, id, _inherited=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveTimeZoneSettingsForASite(id, _inherited, **kwargs)

    def get_application_policy_queuing_profile(self, name=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getApplicationPolicyQueuingProfile(name, **kwargs)

    def get_syslog_destination(self, configId=None, name=None, protocol=None, offset=None, limit=None, sortBy=None, order=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSyslogDestination(configId, name, protocol, offset, limit, sortBy, order, **kwargs)

    def get_sync_result_for_virtual_account(self, domain, name, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSyncResultForVirtualAccount(domain, name, **kwargs)

    def get_application_policy_default(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getApplicationPolicyDefault(**kwargs)

    def get_module_info_by_id(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getModuleInfoById(id, **kwargs)

    def get_fabric_devices_layer3_handoffs_with_sda_transit(self, fabricId, networkDeviceId=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricDevicesLayer3HandoffsWithSdaTransit(fabricId, networkDeviceId, offset, limit, **kwargs)

    def get_fabric_devices_layer3_handoffs_with_ip_transit(self, fabricId, networkDeviceId=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricDevicesLayer3HandoffsWithIpTransit(fabricId, networkDeviceId, offset, limit, **kwargs)

    def count_of_notifications(self, eventIds=None, startTime=None, endTime=None, category=None, type=None, severity=None, domain=None, subDomain=None, source=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.countOfNotifications(eventIds, startTime, endTime, category, type, severity, domain, subDomain, source, **kwargs)

    def get_a_scheduled_report(self, reportId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAScheduledReport(reportId, **kwargs)

    def get_site_health(self, siteType=None, offset=None, limit=None, timestamp=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSiteHealth(siteType, offset, limit, timestamp, **kwargs)

    def get_sites_count(self, name=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSitesCount(name, **kwargs)

    def retrieves_the_list_of_validation_workflows(self, startTime=None, endTime=None, runStatus=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesTheListOfValidationWorkflows(startTime, endTime, runStatus, offset, limit, **kwargs)

    def retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned(self, siteId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned(siteId, **kwargs)

    def get_site_count_v2(self, id=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSiteCountV2(id, **kwargs)

    def get_extranet_policies(self, extranetPolicyName=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getExtranetPolicies(extranetPolicyName, offset, limit, **kwargs)

    def get_flexible_report_schedule_by_report_id(self, Content_Type, reportId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFlexibleReportScheduleByReportId(Content_Type, reportId, **kwargs)

    def get_port_channels(self, fabricId=None, networkDeviceId=None, portChannelName=None, connectedDeviceType=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getPortChannels(fabricId, networkDeviceId, portChannelName, connectedDeviceType, offset, limit, **kwargs)

    def gets_the_templates_available(self, projectId=None, softwareType=None, softwareVersion=None, productFamily=None, productSeries=None, productType=None, filterConflictingTemplates=None, tags=None, projectNames=None, unCommitted=None, sortOrder=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getsTheTemplatesAvailable(projectId, softwareType, softwareVersion, productFamily, productSeries, productType, filterConflictingTemplates, tags, projectNames, unCommitted, sortOrder, **kwargs)

    def get_syslog_subscription_details(self, name=None, instanceId=None, offset=None, limit=None, sortBy=None, order=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSyslogSubscriptionDetails(name, instanceId, offset, limit, sortBy, order, **kwargs)

    def get_list_of_scheduled_reports(self, viewGroupId=None, viewId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getListOfScheduledReports(viewGroupId, viewId, **kwargs)

    def get_client_detail(self, macAddress, timestamp=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getClientDetail(macAddress, timestamp, **kwargs)

    def count_the_number_of_events(self, deviceFamily, X_CALLER_ID=None, startTime=None, endTime=None, messageType=None, severity=None, siteId=None, siteHierarchyId=None, networkDeviceName=None, networkDeviceId=None, apMac=None, clientMac=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.countTheNumberOfEvents(deviceFamily, X_CALLER_ID, startTime, endTime, messageType, severity, siteId, siteHierarchyId, networkDeviceName, networkDeviceId, apMac, clientMac, **kwargs)

    def get_tag_member_count(self, id, memberType, memberAssociationType=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTagMemberCount(id, memberType, memberAssociationType, **kwargs)

    def get_device_interfaces_by_specified_range(self, deviceId, startIndex, recordsToReturn, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceInterfacesBySpecifiedRange(deviceId, startIndex, recordsToReturn, **kwargs)

    def get_polling_interval_for_all_devices(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getPollingIntervalForAllDevices(**kwargs)

    def get_device_list(self, hostname=None, managementIpAddress=None, macAddress=None, locationName=None, serialNumber=None, location=None, family=None, type=None, series=None, collectionStatus=None, collectionInterval=None, notSyncedForMinutes=None, errorCode=None, errorDescription=None, softwareVersion=None, softwareType=None, platformId=None, role=None, reachabilityStatus=None, upTime=None, associatedWlcIp=None, license_name=None, license_type=None, license_status=None, module_name=None, module_equpimenttype=None, module_servicestate=None, module_vendorequipmenttype=None, module_partnumber=None, module_operationstatecode=None, id=None, deviceSupportLevel=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceList(hostname, managementIpAddress, macAddress, locationName, serialNumber, location, family, type, series, collectionStatus, collectionInterval, notSyncedForMinutes, errorCode, errorDescription, softwareVersion, softwareType, platformId, role, reachabilityStatus, upTime, associatedWlcIp, license_name, license_type, license_status, module_name, module_equpimenttype, module_servicestate, module_vendorequipmenttype, module_partnumber, module_operationstatecode, id, deviceSupportLevel, offset, limit, **kwargs)

    def get_qos_device_interface_info(self, networkDeviceId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getQosDeviceInterfaceInfo(networkDeviceId, **kwargs)

    def get_device_family_identifiers(self, Accept=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceFamilyIdentifiers(Accept, **kwargs)

    def get_task_count(self, startTime=None, endTime=None, data=None, errorCode=None, serviceType=None, username=None, progress=None, isError=None, failureReason=None, parentId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTaskCount(startTime, endTime, data, errorCode, serviceType, username, progress, isError, failureReason, parentId, **kwargs)

    def retrieves_validation_details_for_a_validation_set(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesValidationDetailsForAValidationSet(id, **kwargs)

    def get_smart_account_list(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSmartAccountList(**kwargs)

    def get_layer3_virtual_networks(self, virtualNetworkName=None, fabricId=None, anchoredSiteId=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getLayer3VirtualNetworks(virtualNetworkName, fabricId, anchoredSiteId, offset, limit, **kwargs)

    def get_list_of_available_namespaces(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getListOfAvailableNamespaces(**kwargs)

    def retrieve_network_device_product_name(self, productNameOrdinal, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveNetworkDeviceProductName(productNameOrdinal, **kwargs)

    def get_execution_id_by_report_id(self, Content_Type, reportId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getExecutionIdByReportId(Content_Type, reportId, **kwargs)

    def get_mobility_groups_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getMobilityGroupsCount(**kwargs)

    def get_advisories_list(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAdvisoriesList(**kwargs)

    def get_list_of_files(self, nameSpace, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getListOfFiles(nameSpace, **kwargs)

    def retrieve_specific_image_distribution_server(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveSpecificImageDistributionServer(id, **kwargs)

    def get_application_policy(self, policyScope=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getApplicationPolicy(policyScope, **kwargs)

    def get_workflow_by_id(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getWorkflowById(id, **kwargs)

    def get_advisories_summary(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAdvisoriesSummary(**kwargs)

    def get_tag_resource_types(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTagResourceTypes(**kwargs)

    def get_port_assignment_count(self, fabricId=None, networkDeviceId=None, interfaceName=None, dataVlanName=None, voiceVlanName=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getPortAssignmentCount(fabricId, networkDeviceId, interfaceName, dataVlanName, voiceVlanName, **kwargs)

    def get_discoveries_by_range(self, startIndex, recordsToReturn, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDiscoveriesByRange(startIndex, recordsToReturn, **kwargs)

    def gets_an_area(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getsAnArea(id, **kwargs)

    def get_extranet_policy_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getExtranetPolicyCount(**kwargs)

    def get_resync_interval_for_the_network_device(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getResyncIntervalForTheNetworkDevice(id, **kwargs)

    def get_interfaces(self, limit=None, offset=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getInterfaces(limit, offset, **kwargs)

    def get_all_view_groups(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAllViewGroups(**kwargs)

    def get_events(self, tags, eventId=None, offset=None, limit=None, sortBy=None, order=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getEvents(tags, eventId, offset, limit, sortBy, order, **kwargs)

    def get_email_event_subscriptions(self, eventIds=None, offset=None, limit=None, sortBy=None, order=None, domain=None, subDomain=None, category=None, type=None, name=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getEmailEventSubscriptions(eventIds, offset, limit, sortBy, order, domain, subDomain, category, type, name, **kwargs)

    def get_email_subscription_details(self, name=None, instanceId=None, offset=None, limit=None, sortBy=None, order=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getEmailSubscriptionDetails(name, instanceId, offset, limit, sortBy, order, **kwargs)

    def get_all_global_credentials_v2(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAllGlobalCredentialsV2(**kwargs)

    def get_network_devices_from_discovery(self, id, taskId=None, sortBy=None, sortOrder=None, ipAddress=None, pingStatus=None, snmpStatus=None, cliStatus=None, netconfStatus=None, httpStatus=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getNetworkDevicesFromDiscovery(id, taskId, sortBy, sortOrder, ipAddress, pingStatus, snmpStatus, cliStatus, netconfStatus, httpStatus, **kwargs)

    def get_sites(self, name=None, nameHierarchy=None, type=None, _unitsOfMeasure=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSites(name, nameHierarchy, type, _unitsOfMeasure, offset, limit, **kwargs)

    def get_event_subscriptions(self, eventIds=None, offset=None, limit=None, sortBy=None, order=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getEventSubscriptions(eventIds, offset, limit, sortBy, order, **kwargs)

    def get_planned_access_points_for_floor(self, floorId, limit=None, offset=None, radios=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getPlannedAccessPointsForFloor(floorId, limit, offset, radios, **kwargs)

    def get_discovery_by_id(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDiscoveryById(id, **kwargs)

    def get_configuration_archive_details(self, deviceId=None, fileType=None, createdTime=None, createdBy=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getConfigurationArchiveDetails(deviceId, fileType, createdTime, createdBy, offset, limit, **kwargs)

    def get_advisories_per_device(self, deviceId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAdvisoriesPerDevice(deviceId, **kwargs)

    def retrieves_the_count_of_validation_workflows(self, startTime=None, endTime=None, runStatus=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesTheCountOfValidationWorkflows(startTime, endTime, runStatus, **kwargs)

    def get_compliance_detail_count(self, complianceType=None, complianceStatus=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getComplianceDetailCount(complianceType, complianceStatus, **kwargs)

    def get_overall_client_health(self, timestamp=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getOverallClientHealth(timestamp, **kwargs)

    def get_linecard_details(self, deviceUuid, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getLinecardDetails(deviceUuid, **kwargs)

    def get_wireless_profiles_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getWirelessProfilesCount(**kwargs)

    def get_tag_by_id(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTagById(id, **kwargs)

    def get_audit_log_summary(self, parentInstanceId=None, isParentOnly=None, instanceId=None, name=None, eventId=None, category=None, severity=None, domain=None, subDomain=None, source=None, userId=None, context=None, eventHierarchy=None, siteId=None, deviceId=None, isSystemEvents=None, description=None, startTime=None, endTime=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAuditLogSummary(parentInstanceId, isParentOnly, instanceId, name, eventId, category, severity, domain, subDomain, source, userId, context, eventHierarchy, siteId, deviceId, isSystemEvents, description, startTime, endTime, **kwargs)

    def gets_a_list_of_projects(self, name=None, sortOrder=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getsAListOfProjects(name, sortOrder, **kwargs)

    def get_authentication_and_policy_servers(self, isIseEnabled=None, state=None, role=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAuthenticationAndPolicyServers(isIseEnabled, state, role, **kwargs)

    def retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to(self, profileId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(profileId, **kwargs)

    def get_provisioned_devices(self, id=None, networkDeviceId=None, siteId=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getProvisionedDevices(id, networkDeviceId, siteId, offset, limit, **kwargs)

    def retrieves_all_previous_pathtraces_summary(self, periodicRefresh=None, sourceIP=None, destIP=None, sourcePort=None, destPort=None, gtCreateTime=None, ltCreateTime=None, protocol=None, status=None, taskId=None, lastUpdateTime=None, limit=None, offset=None, order=None, sortBy=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesAllPreviousPathtracesSummary(periodicRefresh, sourceIP, destIP, sourcePort, destPort, gtCreateTime, ltCreateTime, protocol, status, taskId, lastUpdateTime, limit, offset, order, sortBy, **kwargs)

    def get_device_credential_settings_for_a_site(self, id, _inherited=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceCredentialSettingsForASite(id, _inherited, **kwargs)

    def get_device_interface_count(self, deviceId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceInterfaceCount(deviceId, **kwargs)

    def get_layer2_virtual_network_count(self, fabricId=None, vlanName=None, vlanId=None, trafficType=None, associatedLayer3VirtualNetworkName=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getLayer2VirtualNetworkCount(fabricId, vlanName, vlanId, trafficType, associatedLayer3VirtualNetworkName, **kwargs)

    def retrieves_the_count_of_network_profiles_for_sites(self, type=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesTheCountOfNetworkProfilesForSites(type, **kwargs)

    def get_device_count(self, hostname=None, managementIpAddress=None, macAddress=None, locationName=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceCount(hostname, managementIpAddress, macAddress, locationName, **kwargs)

    def get_fabric_devices_layer2_handoffs(self, fabricId, networkDeviceId=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricDevicesLayer2Handoffs(fabricId, networkDeviceId, offset, limit, **kwargs)

    def get_syslog_event_subscriptions(self, eventIds=None, offset=None, limit=None, sortBy=None, order=None, domain=None, subDomain=None, category=None, type=None, name=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSyslogEventSubscriptions(eventIds, offset, limit, sortBy, order, domain, subDomain, category, type, name, **kwargs)

    def get_site_v2(self, groupNameHierarchy=None, id=None, type=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSiteV2(groupNameHierarchy, id, type, offset, limit, **kwargs)

    def get_fabric_devices(self, fabricId, networkDeviceId=None, deviceRoles=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricDevices(fabricId, networkDeviceId, deviceRoles, offset, limit, **kwargs)

    def get_tasks_count(self, startTime=None, endTime=None, parentId=None, rootId=None, status=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTasksCount(startTime, endTime, parentId, rootId, status, **kwargs)

    def gets_a_floor(self, id, _unitsOfMeasure=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getsAFloor(id, _unitsOfMeasure, **kwargs)

    def get_fabric_zones(self, id=None, siteId=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricZones(id, siteId, offset, limit, **kwargs)

    def get_virtual_account_list(self, domain, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getVirtualAccountList(domain, **kwargs)

    def get_qos_device_interface_info_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getQosDeviceInterfaceInfoCount(**kwargs)

    def count_of_events(self, tags, eventId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.countOfEvents(tags, eventId, **kwargs)

    def get_network_device_image_updates(self, id=None, parentId=None, networkDeviceId=None, status=None, imageName=None, hostName=None, managementAddress=None, startTime=None, endTime=None, sortBy=None, order=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getNetworkDeviceImageUpdates(id, parentId, networkDeviceId, status, imageName, hostName, managementAddress, startTime, endTime, sortBy, order, offset, limit, **kwargs)

    def get_transit_networks(self, id=None, name=None, type=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTransitNetworks(id, name, type, offset, limit, **kwargs)

    def get_stack_details_for_device(self, deviceId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getStackDetailsForDevice(deviceId, **kwargs)

    def get_application_set_count(self, scalableGroupType, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getApplicationSetCount(scalableGroupType, **kwargs)

    def get_workflow_count(self, name=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getWorkflowCount(name, **kwargs)

    def retrieves_previous_pathtrace(self, flowAnalysisId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesPreviousPathtrace(flowAnalysisId, **kwargs)

    def get_overall_network_health(self, timestamp=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getOverallNetworkHealth(timestamp, **kwargs)

    def get_service_provider_details_v2(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getServiceProviderDetailsV2(**kwargs)

    def get_wireless_profiles(self, limit=None, offset=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getWirelessProfiles(limit, offset, **kwargs)

    def get_config_task_details(self, parentTaskId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getConfigTaskDetails(parentTaskId, **kwargs)

    def get_multicast_virtual_network_count(self, fabricId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getMulticastVirtualNetworkCount(fabricId, **kwargs)

    def get_tag_count(self, name=None, nameSpace=None, attributeName=None, size=None, systemTag=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTagCount(name, nameSpace, attributeName, size, systemTag, **kwargs)

    def get_device_summary(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceSummary(id, **kwargs)

    def get_authentication_profiles(self, fabricId=None, authenticationProfileName=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAuthenticationProfiles(fabricId, authenticationProfileName, offset, limit, **kwargs)

    def get_all_flexible_report_schedules(self, Content_Type, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAllFlexibleReportSchedules(Content_Type, **kwargs)

    def get_functional_capability_by_id(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFunctionalCapabilityById(id, **kwargs)

    def get_fabric_sites(self, id=None, siteId=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricSites(id, siteId, offset, limit, **kwargs)

    def get_workflows(self, limit=None, offset=None, sort=None, sortOrder=None, type=None, name=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getWorkflows(limit, offset, sort, sortOrder, type, name, **kwargs)

    def get_device_config_by_id(self, networkDeviceId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceConfigById(networkDeviceId, **kwargs)

    def get_organization_list_for_meraki(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getOrganizationListForMeraki(id, **kwargs)

    def get_polling_interval_by_id(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getPollingIntervalById(id, **kwargs)

    def get_notifications(self, eventIds=None, startTime=None, endTime=None, category=None, type=None, severity=None, domain=None, subDomain=None, source=None, offset=None, limit=None, sortBy=None, order=None, tags=None, namespace=None, siteId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getNotifications(eventIds, startTime, endTime, category, type, severity, domain, subDomain, source, offset, limit, sortBy, order, tags, namespace, siteId, **kwargs)

    def get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id(self, id, Accept_Language=None, X_CALLER_ID=None, view=None, attribute=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId(id, Accept_Language, X_CALLER_ID, view, attribute, **kwargs)

    def get_device_config_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceConfigCount(**kwargs)

    def retrieve_a_network_profile_for_sites_by_id(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveANetworkProfileForSitesById(id, **kwargs)

    def get_audit_log_records(self, parentInstanceId=None, instanceId=None, name=None, eventId=None, category=None, severity=None, domain=None, subDomain=None, source=None, userId=None, context=None, eventHierarchy=None, siteId=None, deviceId=None, isSystemEvents=None, description=None, offset=None, limit=None, startTime=None, endTime=None, sortBy=None, order=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAuditLogRecords(parentInstanceId, instanceId, name, eventId, category, severity, domain, subDomain, source, userId, context, eventHierarchy, siteId, deviceId, isSystemEvents, description, offset, limit, startTime, endTime, sortBy, order, **kwargs)

    def get_supervisor_card_detail(self, deviceUuid, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSupervisorCardDetail(deviceUuid, **kwargs)

    def retrieve_image_distribution_settings_for_a_site(self, id, _inherited=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveImageDistributionSettingsForASite(id, _inherited, **kwargs)

    def get_event_artifacts(self, eventIds=None, tags=None, offset=None, limit=None, sortBy=None, order=None, search=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getEventArtifacts(eventIds, tags, offset, limit, sortBy, order, search, **kwargs)

    def retrieves_validation_workflow_details(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesValidationWorkflowDetails(id, **kwargs)

    def get_module_count(self, deviceId, nameList=None, vendorEquipmentTypeList=None, partNumberList=None, operationalStateCodeList=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getModuleCount(deviceId, nameList, vendorEquipmentTypeList, partNumberList, operationalStateCodeList, **kwargs)

    def get_transit_networks_count(self, type=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTransitNetworksCount(type, **kwargs)

    def get_all_execution_details_for_a_given_report(self, reportId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAllExecutionDetailsForAGivenReport(reportId, **kwargs)

    def get_port_channel_count(self, fabricId=None, networkDeviceId=None, portChannelName=None, connectedDeviceType=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getPortChannelCount(fabricId, networkDeviceId, portChannelName, connectedDeviceType, **kwargs)

    def get_audit_log_parent_records(self, instanceId=None, name=None, eventId=None, category=None, severity=None, domain=None, subDomain=None, source=None, userId=None, context=None, eventHierarchy=None, siteId=None, deviceId=None, isSystemEvents=None, description=None, offset=None, limit=None, startTime=None, endTime=None, sortBy=None, order=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAuditLogParentRecords(instanceId, name, eventId, category, severity, domain, subDomain, source, userId, context, eventHierarchy, siteId, deviceId, isSystemEvents, description, offset, limit, startTime, endTime, sortBy, order, **kwargs)

    def retrieve_d_n_s_settings_for_a_site(self, id, _inherited=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveDNSSettingsForASite(id, _inherited, **kwargs)

    def get_email_destination(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getEmailDestination(**kwargs)

    def retrieve_license_setting(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveLicenseSetting(**kwargs)

    def get_multicast(self, fabricId=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getMulticast(fabricId, offset, limit, **kwargs)

    def get_fabric_devices_count(self, fabricId, networkDeviceId=None, deviceRoles=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricDevicesCount(fabricId, networkDeviceId, deviceRoles, **kwargs)

    def get_layer3_virtual_networks_count(self, fabricId=None, anchoredSiteId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getLayer3VirtualNetworksCount(fabricId, anchoredSiteId, **kwargs)

    def get_devices_discovered_by_id(self, id, taskId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDevicesDiscoveredById(id, taskId, **kwargs)

    def get_task_by_id(self, taskId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTaskById(taskId, **kwargs)

    def get_discovered_devices_by_range(self, id, startIndex, recordsToReturn, taskId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDiscoveredDevicesByRange(id, startIndex, recordsToReturn, taskId, **kwargs)

    def retrieves_the_total_count_of_clients_by_applying_basic_filtering(self, X_CALLER_ID=None, startTime=None, endTime=None, type=None, osType=None, osVersion=None, siteHierarchy=None, siteHierarchyId=None, siteId=None, ipv4Address=None, ipv6Address=None, macAddress=None, wlcName=None, connectedNetworkDeviceName=None, ssid=None, band=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesTheTotalCountOfClientsByApplyingBasicFiltering(X_CALLER_ID, startTime, endTime, type, osType, osVersion, siteHierarchy, siteHierarchyId, siteId, ipv4Address, ipv6Address, macAddress, wlcName, connectedNetworkDeviceName, ssid, band, **kwargs)

    def retrieves_the_list_of_network_device_product_names(self, productName=None, productId=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesTheListOfNetworkDeviceProductNames(productName, productId, offset, limit, **kwargs)

    def get_connected_device_detail(self, deviceUuid, interfaceUuid, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getConnectedDeviceDetail(deviceUuid, interfaceUuid, **kwargs)

    def get_devices_that_are_assigned_to_a_site(self, id, memberType, offset=None, limit=None, level=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDevicesThatAreAssignedToASite(id, memberType, offset, limit, level, **kwargs)

    def retrieves_the_list_of_network_profiles_that_the_given_site_has_been_assigned(self, siteId, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned(siteId, offset, limit, **kwargs)

    def get_list_of_discoveries_by_discovery_id(self, id, offset=None, limit=None, ipAddress=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getListOfDiscoveriesByDiscoveryId(id, offset, limit, ipAddress, **kwargs)

    def get_physical_topology(self, nodeType=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getPhysicalTopology(nodeType, **kwargs)

    def get_site_topology(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSiteTopology(**kwargs)

    def retrieve_n_t_p_settings_for_a_site(self, id, _inherited=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveNTPSettingsForASite(id, _inherited, **kwargs)

    def count_of_network_device_image_updates(self, id=None, parentId=None, networkDeviceId=None, status=None, imageName=None, hostName=None, managementAddress=None, startTime=None, endTime=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.countOfNetworkDeviceImageUpdates(id, parentId, networkDeviceId, status, imageName, hostName, managementAddress, startTime, endTime, **kwargs)

    def get_planned_access_points_for_building(self, buildingId, limit=None, offset=None, radios=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getPlannedAccessPointsForBuilding(buildingId, limit, offset, radios, **kwargs)

    def count_of_network_product_names(self, productName=None, productId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.countOfNetworkProductNames(productName, productId, **kwargs)

    def get_access_point_configuration(self, key, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAccessPointConfiguration(key, **kwargs)

    def get_device_config_for_all_devices(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceConfigForAllDevices(**kwargs)

    def get_topology_details(self, vlanID, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTopologyDetails(vlanID, **kwargs)

    def get_fabric_devices_layer3_handoffs_with_ip_transit_count(self, fabricId, networkDeviceId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricDevicesLayer3HandoffsWithIpTransitCount(fabricId, networkDeviceId, **kwargs)

    def get_fabric_devices_layer3_handoffs_with_sda_transit_count(self, fabricId, networkDeviceId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFabricDevicesLayer3HandoffsWithSdaTransitCount(fabricId, networkDeviceId, **kwargs)

    def retrieves_the_list_of_network_profiles_for_sites(self, offset=None, limit=None, sortBy=None, order=None, type=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesTheListOfNetworkProfilesForSites(offset, limit, sortBy, order, type, **kwargs)

    def get_functional_capability_for_devices(self, deviceId, functionName=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getFunctionalCapabilityForDevices(deviceId, functionName, **kwargs)

    def get_port_assignments(self, fabricId=None, networkDeviceId=None, interfaceName=None, dataVlanName=None, voiceVlanName=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getPortAssignments(fabricId, networkDeviceId, interfaceName, dataVlanName, voiceVlanName, offset, limit, **kwargs)

    def get_site_not_assigned_network_devices(self, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSiteNotAssignedNetworkDevices(offset, limit, **kwargs)

    def get_access_point_reboot_task_result(self, parentTaskId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAccessPointRebootTaskResult(parentTaskId, **kwargs)

    def get_device_detail(self, identifier, searchBy, timestamp=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceDetail(identifier, searchBy, timestamp, **kwargs)

    def get_site_not_assigned_network_devices_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSiteNotAssignedNetworkDevicesCount(**kwargs)

    def get_device_by_serial_number(self, serialNumber, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceBySerialNumber(serialNumber, **kwargs)

    def get_application_count(self, scalableGroupType, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getApplicationCount(scalableGroupType, **kwargs)

    def get_compliance_status_count(self, complianceStatus=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getComplianceStatusCount(complianceStatus, **kwargs)

    def get_tasks(self, offset=None, limit=None, sortBy=None, order=None, startTime=None, endTime=None, parentId=None, rootId=None, status=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTasks(offset, limit, sortBy, order, startTime, endTime, parentId, rootId, status, **kwargs)

    def get_list_of_child_events_for_the_given_wireless_client_event(self, id, X_CALLER_ID=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getListOfChildEventsForTheGivenWirelessClientEvent(id, X_CALLER_ID, **kwargs)

    def get_provisioning_settings(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getProvisioningSettings(**kwargs)

    def get_interface_by_id(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getInterfaceById(id, **kwargs)

    def get_interface_info_by_id(self, deviceId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getInterfaceInfoById(deviceId, **kwargs)

    def get_task_by_operation_id(self, operationId, offset, limit, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTaskByOperationId(operationId, offset, limit, **kwargs)

    def get_l3_topology_details(self, topologyType, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getL3TopologyDetails(topologyType, **kwargs)

    def get_advisory_device_detail(self, deviceId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAdvisoryDeviceDetail(deviceId, **kwargs)

    def get_connector_types(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getConnectorTypes(**kwargs)

    def retrieve_d_h_c_p_settings_for_a_site(self, id, _inherited=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrieveDHCPSettingsForASite(id, _inherited, **kwargs)

    def get_anycast_gateway_count(self, fabricId=None, virtualNetworkName=None, ipPoolName=None, vlanName=None, vlanId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAnycastGatewayCount(fabricId, virtualNetworkName, ipPoolName, vlanName, vlanId, **kwargs)

    def get_network_device_by_pagination_range(self, startIndex, recordsToReturn, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getNetworkDeviceByPaginationRange(startIndex, recordsToReturn, **kwargs)

    def get_site_assigned_network_device(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSiteAssignedNetworkDevice(id, **kwargs)

    def get_all_interfaces(self, offset=None, limit=None, lastInputTime=None, lastOutputTime=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAllInterfaces(offset, limit, lastInputTime, lastOutputTime, **kwargs)

    def get_wireless_lan_controller_details_by_id(self, id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getWirelessLanControllerDetailsById(id, **kwargs)

    def get_devices_per_advisory(self, advisoryId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDevicesPerAdvisory(advisoryId, **kwargs)

    def get_access_point_configuration_task_result(self, task_id, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getAccessPointConfigurationTaskResult(task_id, **kwargs)

    def get_compliance_detail(self, complianceType=None, complianceStatus=None, deviceUuid=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getComplianceDetail(complianceType, complianceStatus, deviceUuid, offset, limit, **kwargs)

    def get_global_credentials(self, credentialSubType, sortBy=None, order=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getGlobalCredentials(credentialSubType, sortBy, order, **kwargs)

    def get_compliance_status(self, complianceStatus=None, deviceUuid=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getComplianceStatus(complianceStatus, deviceUuid, **kwargs)

    def get_provisioned_devices_count(self, siteId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getProvisionedDevicesCount(siteId, **kwargs)

    def get_interfaces_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getInterfacesCount(**kwargs)

    def get_modules(self, deviceId, limit=None, offset=None, nameList=None, vendorEquipmentTypeList=None, partNumberList=None, operationalStateCodeList=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getModules(deviceId, limit, offset, nameList, vendorEquipmentTypeList, partNumberList, operationalStateCodeList, **kwargs)

    def retrieves_the_count_of_assigned_network_device_products(self, imageId, productName=None, productId=None, recommended=None, assigned=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.retrievesTheCountOfAssignedNetworkDeviceProducts(imageId, productName, productId, recommended, assigned, **kwargs)

    def get_device_history(self, serialNumber, sort=None, sortOrder=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceHistory(serialNumber, sort, sortOrder, **kwargs)

    def get_application_policy_queuing_profile_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getApplicationPolicyQueuingProfileCount(**kwargs)

    def get_task_tree(self, taskId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTaskTree(taskId, **kwargs)

    def get_discovered_network_devices_by_discovery_id(self, id, taskId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDiscoveredNetworkDevicesByDiscoveryId(id, taskId, **kwargs)

    def get_site_assigned_network_devices_count(self, siteId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSiteAssignedNetworkDevicesCount(siteId, **kwargs)

    def get_network_v2(self, siteId, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getNetworkV2(siteId, **kwargs)

    def get_device_values_that_match_fully_or_partially_an_attribute(self, vrfName=None, managementIpAddress=None, hostname=None, macAddress=None, family=None, collectionStatus=None, collectionInterval=None, softwareVersion=None, softwareType=None, reachabilityStatus=None, reachabilityFailureReason=None, errorCode=None, platformId=None, series=None, type=None, serialNumber=None, upTime=None, role=None, roleSource=None, associatedWlcIp=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceValuesThatMatchFullyOrPartiallyAnAttribute(vrfName, managementIpAddress, hostname, macAddress, family, collectionStatus, collectionInterval, softwareVersion, softwareType, reachabilityStatus, reachabilityFailureReason, errorCode, platformId, series, type, serialNumber, upTime, role, roleSource, associatedWlcIp, offset, limit, **kwargs)

    def get_applications(self, offset=None, limit=None, name=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getApplications(offset, limit, name, **kwargs)

    def get_network(self, siteId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getNetwork(siteId, **kwargs)

    def get_transit_peer_network_info(self, transitPeerNetworkName, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getTransitPeerNetworkInfo(transitPeerNetworkName, **kwargs)

    def get_application_sets(self, offset=None, limit=None, name=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getApplicationSets(offset, limit, name, **kwargs)

    def get_applications_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getApplicationsCount(**kwargs)

    def get_global_pool(self, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getGlobalPool(offset, limit, **kwargs)

    def get_provisioned_wired_device(self, deviceManagementIpAddress, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getProvisionedWiredDevice(deviceManagementIpAddress, **kwargs)

    def get_device_credential_details(self, siteId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceCredentialDetails(siteId, **kwargs)

    def get_service_provider_details(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getServiceProviderDetails(**kwargs)

    def get_site(self, name=None, siteId=None, type=None, offset=None, limit=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSite(name, siteId, type, offset, limit, **kwargs)

    def get_virtual_network_summary(self, siteNameHierarchy, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getVirtualNetworkSummary(siteNameHierarchy, **kwargs)

    def get_wireless_profile(self, profileName=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getWirelessProfile(profileName, **kwargs)

    def get_issue_enrichment_details(self, entity_type, entity_value, __persistbapioutput=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getIssueEnrichmentDetails(entity_type, entity_value, __persistbapioutput, **kwargs)

    def get_site_count(self, siteId=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getSiteCount(siteId, **kwargs)

    def get_client_enrichment_details(self, entity_type, entity_value, issueCategory=None, __persistbapioutput=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getClientEnrichmentDetails(entity_type, entity_value, issueCategory, __persistbapioutput, **kwargs)

    def get_virtual_network_with_scalable_groups(self, virtualNetworkName, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getVirtualNetworkWithScalableGroups(virtualNetworkName, **kwargs)

    def get_dynamic_interface(self, __runsync=None, __timeout=None, interface_name=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDynamicInterface(__runsync, __timeout, interface_name, **kwargs)

    def get_application_sets_count(self, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getApplicationSetsCount(**kwargs)

    def get_user_enrichment_details(self, entity_type, entity_value, __persistbapioutput=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getUserEnrichmentDetails(entity_type, entity_value, __persistbapioutput, **kwargs)

    def get_device_enrichment_details(self, entity_type, entity_value, __persistbapioutput=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getDeviceEnrichmentDetails(entity_type, entity_value, __persistbapioutput, **kwargs)

    def get_membership(self, siteId, offset=None, limit=None, deviceFamily=None, serialNumber=None, **kwargs):
        if not self.catalyst_client:
            return {"error": "Catalyst Center integration is disabled."}
        return self.catalyst_client.getMembership(siteId, offset, limit, deviceFamily, serialNumber, **kwargs)




    # ================================
    # Cisco Spaces Methods
    # ================================
    
    def get_spaces_location_hierarchy(self, tenant_id=None):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_location_hierarchy(tenant_id)

    def get_organization_inventory_devices(self):
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}

        return self.meraki_client.get_organization_inventory_devices()

    def get_organization_networks(self):
        if not self.meraki_client:
            return {"message": "Meraki client not configured."}
        return self.meraki_client.get_organization_networks()
    
    def get_spaces_floor_details(self, floor_id: str):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_floor_details(floor_id)

    def get_spaces_floor_image(self, tenant_id: str, image_path: str, image_type: str):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_floor_image(tenant_id, image_path, image_type)

    def get_spaces_devices(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices(**kwargs)

    def get_spaces_devices_count(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices_count(**kwargs)

    def get_spaces_devices_floors(self):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices_floors()

    def export_history_csv(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.export_history_csv(**kwargs)

    def export_history_gz(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.export_history_gz(**kwargs)

    def get_history_record_count(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices_count(**kwargs)

    def get_history_devices(self, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices(**kwargs)

    def get_history_for_device(self, device_id: str, **kwargs):
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_devices(**kwargs)
    
    def get_spaces_location_subtree(self, location_id: str) -> dict:
        if not self.spaces_client:
            return {"message": "Cisco Spaces integration is disabled."}
        return self.spaces_client.get_location_subtree(location_id)


    # ================================
    # Cisco Webex Methods (Stubs)
    # ================================
    def get_webex_meetings(self):
        if not self.webex_client:
            return {"message": "Webex integration is disabled or not configured."}
        return self.webex_client.get_meetings()

    def get_webex_meeting_by_id(self, meeting_id):
        if not self.webex_client:
            return {"message": "Webex integration is disabled or not configured."}
        return self.webex_client.get_meeting_by_id(meeting_id)
################################################################################
# cisco-data-bridge-domain-index/cisco_integrations/meraki_sdk_client.py
# Copyright (c) 2025 Jeff Teeter, Ph.D.
# Cisco Systems, Inc.
# Licensed under the Apache License, Version 2.0 (see LICENSE)
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import meraki
import logging

class MerakiSDKClient:
    """
    A thin wrapper around the official Meraki Dashboard API, customized for
    a chat-driven AI agent. It centralizes calls to Meraki’s many endpoints
    and organizes them by functional domain for clarity. Each method simply
    delegates to self.dashboard.<section>.<method>.

    Usage Example:
        client = MerakiSDKClient(api_key='YOUR_API_KEY')
        networks = client.get_organization_networks('12345')
        ...
    """

    def __init__(self, api_key: str, base_url: str = None):
        if not meraki:
            raise ImportError(
                "The 'meraki' Python package is not installed. "
                "Please install via 'pip install meraki'."
            )
        self.api_key = api_key
        self.dashboard = meraki.DashboardAPI(
            api_key=api_key,
            base_url=base_url or "https://api.meraki.com/api/v1",
            print_console=False,
        )
        logging.info("MerakiSDKClient initialized.")

    # =========================================================================
    # ORGANIZATIONS
    # =========================================================================

    def get_organization(self, organization_id: str):
        """Retrieve details for a specific organization."""
        return self.dashboard.organizations.getOrganization(organization_id)

    def get_organization_networks(self, organization_id: str):
        """Retrieve all networks in an organization."""
        return self.dashboard.organizations.getOrganizationNetworks(organization_id)

    def get_organization_inventory_devices(self, organization_id: str):
        """Retrieve all devices in an organization's inventory."""
        return self.dashboard.organizations.getOrganizationInventoryDevices(organization_id)

    def get_organization_licenses(self, organization_id: str, **kwargs):
        """Retrieve licenses in the organization."""
        return self.dashboard.organizations.getOrganizationLicenses(organization_id, **kwargs)

    def get_organization_licenses_overview(self, organization_id: str):
        """Retrieve high-level license overview (co-termination info, etc.)."""
        return self.dashboard.organizations.getOrganizationLicensesOverview(organization_id)

    def get_organization_appliance_security_intrusion(self, organization_id: str):
        return self.dashboard.organizations.getOrganizationApplianceSecurityIntrusion(organization_id)

    def get_organization_appliance_security_events(self, organization_id: str, **kwargs):
        return self.dashboard.organizations.getOrganizationApplianceSecurityEvents(
            organization_id, **kwargs
        )

    def get_organization_appliance_uplink_statuses(self, organization_id: str):
        return self.dashboard.organizations.getOrganizationApplianceUplinkStatuses(organization_id)

    def get_organization_appliance_vpn_third_party_vpn_peers(self, organization_id: str):
        return self.dashboard.organizations.getOrganizationApplianceVpnThirdPartyVPNPeers(
            organization_id
        )

    def get_organization_appliance_traffic_shaping_vpn_exclusions_by_network(
        self, organization_id: str, **kwargs
    ):
        return self.dashboard.organizations.getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(
            organization_id, **kwargs
        )

    def get_organization_appliance_uplinks_usage_by_network(self, organization_id: str, **kwargs):
        return self.dashboard.organizations.getOrganizationApplianceUplinksUsageByNetwork(
            organization_id, **kwargs
        )

    def get_organization_appliance_uplinks_statuses_overview(self, organization_id: str):
        return self.dashboard.organizations.getOrganizationApplianceUplinksStatusesOverview(
            organization_id
        )

    def get_organization_appliance_vpn_stats(self, organization_id: str):
        return self.dashboard.organizations.getOrganizationApplianceVpnStats(organization_id)

    def get_organization_appliance_vpn_statuses(self, organization_id: str):
        return self.dashboard.organizations.getOrganizationApplianceVpnStatuses(organization_id)

    def get_organization_appliance_vpn_vpn_firewall_rules(self, organization_id: str):
        return self.dashboard.organizations.getOrganizationApplianceVpnVpnFirewallRules(
            organization_id
        )

    def update_organization_appliance_security_intrusion(self, organization_id: str, **kwargs):
        return self.dashboard.organizations.updateOrganizationApplianceSecurityIntrusion(
            organization_id, **kwargs
        )

    def update_organization_appliance_vpn_third_party_vpn_peers(
        self, organization_id: str, payload: dict
    ):
        return self.dashboard.organizations.updateOrganizationApplianceVpnThirdPartyVPNPeers(
            organization_id, **payload
        )

    def update_organization_appliance_vpn_vpn_firewall_rules(
        self, organization_id: str, **kwargs
    ):
        return self.dashboard.organizations.updateOrganizationApplianceVpnVpnFirewallRules(
            organization_id, **kwargs
        )

    def get_organization_login_security(self, organization_id: str):
        """Retrieve login security settings for the organization."""
        return self.dashboard.organizations.getOrganizationLoginSecurity(organization_id)

    # =========================================================================
    # NETWORKS
    # =========================================================================

    def get_networks(self, organization_id: str):
        """Same as get_organization_networks but included for legacy usage."""
        return self.dashboard.organizations.getOrganizationNetworks(organization_id)

    def get_network_by_id(self, organization_id: str, network_id: str):
        """Retrieve details about a single network."""
        return self.dashboard.networks.getNetwork(network_id)

    def get_network(self, network_id: str):
        """Another form of retrieving one network by ID (without org param)."""
        return self.dashboard.networks.getNetwork(network_id)

    def update_network(self, network_id: str, **kwargs):
        return self.dashboard.networks.updateNetwork(network_id, **kwargs)

    def get_network_alerts_history(self, network_id: str, **kwargs):
        """Retrieve historical alerts for a given network."""
        return self.dashboard.networks.getNetworkAlertsHistory(network_id, **kwargs)

    def get_network_clients(self, network_id: str, **kwargs):
        """List the clients of a given network."""
        return self.dashboard.networks.getNetworkClients(network_id, **kwargs)

    def create_network_appliance_traffic_shaping_custom_performance_class(
        self, network_id: str, payload: dict
    ):
        return self.dashboard.networks.createNetworkApplianceTrafficShapingCustomPerformanceClass(
            network_id, **payload
        )

    def delete_network_appliance_traffic_shaping_custom_performance_class(
        self, network_id: str, class_id: str
    ):
        return self.dashboard.networks.deleteNetworkApplianceTrafficShapingCustomPerformanceClass(
            network_id, class_id
        )

    def swap_network_appliance_warm_spare(self, network_id: str):
        return self.dashboard.networks.swapNetworkApplianceWarmSpare(network_id)

    # =========================================================================
    # APPLIANCE (Routing, Security, Firewall, VLAN, etc.)
    # =========================================================================

    def get_network_appliance_firewall_port_forwarding_rules(self, network_id: str):
        return self.dashboard.networks.getNetworkApplianceFirewallPortForwardingRules(network_id)

    def get_network_appliance_security_intrusion(self, network_id: str):
        return self.dashboard.networks.getNetworkApplianceSecurityIntrusion(network_id)

    def get_network_appliance_security_malware(self, network_id: str):
        return self.dashboard.networks.getNetworkApplianceSecurityMalware(network_id)

    def update_network_appliance_firewall_port_forwarding_rules(
        self, network_id: str, payload: dict
    ):
        return self.dashboard.networks.updateNetworkApplianceFirewallPortForwardingRules(
            network_id, **payload
        )

    def update_network_appliance_security_intrusion(self, network_id: str, payload: dict):
        return self.dashboard.networks.updateNetworkApplianceSecurityIntrusion(
            network_id, **payload
        )

    def update_network_appliance_security_malware(self, network_id: str, payload: dict):
        return self.dashboard.networks.updateNetworkApplianceSecurityMalware(
            network_id, **payload
        )

    # --- Additional APPLIANCE device-level or network-level calls ---

    def create_device_appliance_vmx_authentication_token(self, serial: str, **kwargs):
        return self.dashboard.appliance.createDeviceApplianceVmxAuthenticationToken(serial, **kwargs)

    def get_device_appliance_radio_settings(self, serial: str):
        return self.dashboard.devices.getDeviceApplianceRadioSettings(serial)

    def get_device_appliance_uplinks_settings(self, serial: str):
        return self.dashboard.devices.getDeviceApplianceUplinksSettings(serial)

    def update_device_appliance_radio_settings(self, serial: str, **kwargs):
        return self.dashboard.appliance.updateDeviceApplianceRadioSettings(serial, **kwargs)

    def update_device_appliance_uplinks_settings(self, serial: str, **kwargs):
        return self.dashboard.appliance.updateDeviceApplianceUplinksSettings(serial, **kwargs)

    def get_device_appliance_dhcp_subnets(self, serial: str):
        return self.dashboard.appliance.getDeviceApplianceDhcpSubnets(serial)

    def get_device_appliance_performance(self, serial: str):
        return self.dashboard.appliance.getDeviceAppliancePerformance(serial)

    def get_device_appliance_prefixes_delegated(self, serial: str):
        return self.dashboard.appliance.getDeviceAppliancePrefixesDelegated(serial)

    def get_device_appliance_prefixes_delegated_vlan_assignments(self, serial: str):
        return self.dashboard.appliance.getDeviceAppliancePrefixesDelegatedVlanAssignments(serial)

    def create_network_appliance_prefixes_delegated_static(self, network_id: str, **kwargs):
        return self.dashboard.appliance.createNetworkAppliancePrefixesDelegatedStatic(
            network_id, **kwargs
        )

    def delete_network_appliance_prefixes_delegated_static(
        self, network_id: str, delegated_prefix_id: str
    ):
        return self.dashboard.appliance.deleteNetworkAppliancePrefixesDelegatedStatic(
            network_id, delegated_prefix_id
        )

    def create_network_appliance_rf_profile(self, network_id: str, **kwargs):
        return self.dashboard.appliance.createNetworkApplianceRfProfile(network_id, **kwargs)

    def delete_network_appliance_rf_profile(self, network_id: str, rf_profile_id: str):
        return self.dashboard.appliance.deleteNetworkApplianceRfProfile(network_id, rf_profile_id)

    def get_network_appliance_rf_profile(self, network_id: str, rf_profile_id: str):
        return self.dashboard.appliance.getNetworkApplianceRfProfile(network_id, rf_profile_id)

    def get_network_appliance_rf_profiles(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceRfProfiles(network_id)

    def update_network_appliance_rf_profile(self, network_id: str, rf_profile_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceRfProfile(
            network_id, rf_profile_id, **kwargs
        )

    def create_network_appliance_static_route(self, network_id: str, **kwargs):
        return self.dashboard.appliance.createNetworkApplianceStaticRoute(network_id, **kwargs)

    def delete_network_appliance_static_route(self, network_id: str, static_route_id: str):
        return self.dashboard.appliance.deleteNetworkApplianceStaticRoute(
            network_id, static_route_id
        )

    def get_network_appliance_static_route(self, network_id: str, static_route_id: str):
        return self.dashboard.appliance.getNetworkApplianceStaticRoute(network_id, static_route_id)

    def get_network_appliance_static_routes(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceStaticRoutes(network_id)

    def update_network_appliance_static_route(
        self, network_id: str, static_route_id: str, **kwargs
    ):
        return self.dashboard.appliance.updateNetworkApplianceStaticRoute(
            network_id, static_route_id, **kwargs
        )

    def create_network_appliance_vmx_authentication_token(self, network_id: str, **kwargs):
        return self.dashboard.appliance.createDeviceApplianceVmxAuthenticationToken(
            network_id, **kwargs
        )

    def get_network_appliance_vpn_bgp(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceVpnBgp(network_id)

    def update_network_appliance_vpn_bgp(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceVpnBgp(network_id, **kwargs)

    def get_network_appliance_vpn_site_to_site_vpn(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceVpnSiteToSiteVpn(network_id)

    def update_network_appliance_vpn_site_to_site_vpn(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceVpnSiteToSiteVpn(
            network_id, **kwargs
        )

    def get_network_appliance_firewall_cellular_firewall_rules(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceFirewallCellularFirewallRules(network_id)

    def update_network_appliance_firewall_cellular_firewall_rules(
        self, network_id: str, **kwargs
    ):
        return self.dashboard.appliance.updateNetworkApplianceFirewallCellularFirewallRules(
            network_id, **kwargs
        )

    def get_network_appliance_firewall_firewalled_services(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceFirewallFirewalledServices(network_id)

    def get_network_appliance_firewall_firewalled_service(
        self, network_id: str, service_name: str
    ):
        return self.dashboard.appliance.getNetworkApplianceFirewallFirewalledService(
            network_id, service_name
        )

    def update_network_appliance_firewall_firewalled_service(
        self, network_id: str, service_name: str, **kwargs
    ):
        return self.dashboard.appliance.updateNetworkApplianceFirewallFirewalledService(
            network_id, service_name, **kwargs
        )

    def get_network_appliance_firewall_inbound_cellular_firewall_rules(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceFirewallInboundCellularFirewallRules(
            network_id
        )

    def update_network_appliance_firewall_inbound_cellular_firewall_rules(
        self, network_id: str, **kwargs
    ):
        return self.dashboard.appliance.updateNetworkApplianceFirewallInboundCellularFirewallRules(
            network_id, **kwargs
        )

    def get_network_appliance_firewall_inbound_firewall_rules(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceFirewallInboundFirewallRules(network_id)

    def update_network_appliance_firewall_inbound_firewall_rules(
        self, network_id: str, **kwargs
    ):
        return self.dashboard.appliance.updateNetworkApplianceFirewallInboundFirewallRules(
            network_id, **kwargs
        )

    def get_network_appliance_firewall_l3_firewall_rules(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(network_id)

    def update_network_appliance_firewall_l3_firewall_rules(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(
            network_id, **kwargs
        )

    def get_network_appliance_firewall_l7_firewall_rules(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceFirewallL7FirewallRules(network_id)

    def update_network_appliance_firewall_l7_firewall_rules(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceFirewallL7FirewallRules(
            network_id, **kwargs
        )

    def get_network_appliance_firewall_l7_firewall_rules_application_categories(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(
            network_id
        )

    def get_network_appliance_firewall_one_to_many_nat_rules(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceFirewallOneToManyNatRules(network_id)

    def update_network_appliance_firewall_one_to_many_nat_rules(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceFirewallOneToManyNatRules(
            network_id, **kwargs
        )

    def get_network_appliance_firewall_one_to_one_nat_rules(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceFirewallOneToOneNatRules(network_id)

    def update_network_appliance_firewall_one_to_one_nat_rules(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceFirewallOneToOneNatRules(
            network_id, **kwargs
        )

    def get_network_appliance_firewall_settings(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceFirewallSettings(network_id)

    def update_network_appliance_firewall_settings(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceFirewallSettings(
            network_id, **kwargs
        )

    def get_network_appliance_traffic_shaping(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceTrafficShaping(network_id)

    def update_network_appliance_traffic_shaping(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceTrafficShaping(network_id, **kwargs)

    def get_network_appliance_traffic_shaping_custom_performance_class(
        self, network_id: str, custom_performance_class_id: str
    ):
        return self.dashboard.appliance.getNetworkApplianceTrafficShapingCustomPerformanceClass(
            network_id, custom_performance_class_id
        )

    def get_network_appliance_traffic_shaping_custom_performance_classes(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceTrafficShapingCustomPerformanceClasses(
            network_id
        )

    def update_network_appliance_traffic_shaping_custom_performance_class(
        self, network_id: str, custom_performance_class_id: str, **kwargs
    ):
        return self.dashboard.appliance.updateNetworkApplianceTrafficShapingCustomPerformanceClass(
            network_id, custom_performance_class_id, **kwargs
        )

    def get_network_appliance_uplinks_usage_history(self, network_id: str, **kwargs):
        return self.dashboard.appliance.getNetworkApplianceUplinksUsageHistory(
            network_id, **kwargs
        )

    def update_network_appliance_traffic_shaping_vpn_exclusions(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceTrafficShapingVpnExclusions(
            network_id, **kwargs
        )

    def create_network_appliance_vlan(self, network_id: str, **kwargs):
        return self.dashboard.appliance.createNetworkApplianceVlan(network_id, **kwargs)

    def delete_network_appliance_vlan(self, network_id: str, vlan_id: str):
        return self.dashboard.appliance.deleteNetworkApplianceVlan(network_id, vlan_id)

    def get_network_appliance_vlan(self, network_id: str, vlan_id: str):
        return self.dashboard.appliance.getNetworkApplianceVlan(network_id, vlan_id)

    def get_network_appliance_vlans(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceVlans(network_id)

    def update_network_appliance_vlan(self, network_id: str, vlan_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceVlan(network_id, vlan_id, **kwargs)

    def get_network_appliance_vlans_settings(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceVlansSettings(network_id)

    def update_network_appliance_vlans_settings(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceVlansSettings(network_id, **kwargs)

    def get_network_appliance_single_lan(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceSingleLan(network_id)

    def update_network_appliance_single_lan(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceSingleLan(network_id, **kwargs)

    def get_network_appliance_ssid(self, network_id: str, number: str):
        return self.dashboard.appliance.getNetworkApplianceSsid(network_id, number)

    def get_network_appliance_ssids(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceSsids(network_id)

    def update_network_appliance_ssid(self, network_id: str, number: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceSsid(network_id, number, **kwargs)

    def get_network_appliance_port(self, network_id: str, port_id: str):
        return self.dashboard.appliance.getNetworkAppliancePort(network_id, port_id)

    def get_network_appliance_ports(self, network_id: str):
        return self.dashboard.appliance.getNetworkAppliancePorts(network_id)

    def update_network_appliance_port(self, network_id: str, port_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkAppliancePort(network_id, port_id, **kwargs)

    def update_network_appliance_sdwan_internet_policies(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceSdwanInternetPolicies(
            network_id, **kwargs
        )

    def get_network_appliance_settings(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceSettings(network_id)

    def update_network_appliance_settings(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceSettings(network_id, **kwargs)

    def get_network_appliance_warm_spare(self, network_id: str):
        return self.dashboard.appliance.getNetworkApplianceWarmSpare(network_id)

    def update_network_appliance_warm_spare(self, network_id: str, **kwargs):
        return self.dashboard.appliance.updateNetworkApplianceWarmSpare(network_id, **kwargs)

    # =========================================================================
    # CELLULAR GATEWAY
    # =========================================================================

    def get_device_cellular_gateway_lan(self, serial: str):
        return self.dashboard.cellularGateway.getDeviceCellularGatewayLan(serial)

    def get_network_cellular_gateway_connectivity_monitoring_destinations(self, network_id: str):
        return self.dashboard.cellularGateway.getNetworkCellularGatewayConnectivityMonitoringDestinations(
            network_id
        )

    # ...other cellular gateway calls if needed...

    # =========================================================================
    # CAMERA
    # =========================================================================

    def create_network_camera_quality_retention_profile(self, network_id: str, **kwargs):
        return self.dashboard.camera.createNetworkCameraQualityRetentionProfile(
            network_id, **kwargs
        )

    def delete_network_camera_quality_retention_profile(self, network_id: str, profile_id: str):
        return self.dashboard.camera.deleteNetworkCameraQualityRetentionProfile(
            network_id, profile_id
        )

    def generate_device_camera_snapshot(self, serial: str, **kwargs):
        return self.dashboard.camera.generateDeviceCameraSnapshot(serial, **kwargs)

    def get_device_camera_analytics_live(self, serial: str, **kwargs):
        return self.dashboard.camera.getDeviceCameraAnalyticsLive(serial, **kwargs)

    def get_network_camera_quality_retention_profile(self, network_id: str, profile_id: str):
        return self.dashboard.camera.getNetworkCameraQualityRetentionProfile(network_id, profile_id)

    # ...additional camera.* methods...

    # =========================================================================
    # DEVICES
    # =========================================================================

    def get_device(self, serial: str):
        return self.dashboard.devices.getDevice(serial)

    def update_device(self, serial: str, **kwargs):
        return self.dashboard.devices.updateDevice(serial, **kwargs)

    # ...other devices.* methods if desired...

    # =========================================================================
    # INSIGHT
    # =========================================================================

    def get_organization_insight_applications(self, organization_id: str):
        return self.dashboard.insight.getOrganizationInsightApplications(organization_id)

    # ...other insight.* calls...

    # =========================================================================
    # LICENSING
    # =========================================================================

    # (We placed some licensing calls under 'ORGANIZATIONS' above.
    #  Additional licensing calls can go here if needed.)

    # =========================================================================
    # SENSOR
    # =========================================================================

    def create_device_sensor_command(self, serial: str, **kwargs):
        return self.dashboard.sensor.createDeviceSensorCommand(serial, **kwargs)

    def get_network_sensor_alerts_current_overview_by_metric(self, network_id: str, metric: str, **kwargs):
        return self.dashboard.sensor.getNetworkSensorAlertsCurrentOverviewByMetric(
            network_id, metric, **kwargs
        )

    # ...other sensor.* calls...

    # =========================================================================
    # SM (Systems Manager)
    # =========================================================================

    def get_network_sm_devices(self, network_id: str, **kwargs):
        return self.dashboard.sm.getNetworkSmDevices(network_id, **kwargs)

    def wipe_network_sm_devices(self, network_id: str, **kwargs):
        return self.dashboard.sm.wipeNetworkSmDevices(network_id, **kwargs)

    # ...other sm.* calls...

    # =========================================================================
    # SWITCH
    # =========================================================================

    def add_network_switch_stack(self, network_id: str, **kwargs):
        return self.dashboard.switch.addNetworkSwitchStack(network_id, **kwargs)

    def get_device_switch_port(self, serial: str, port_id: str):
        return self.dashboard.switch.getDeviceSwitchPort(serial, port_id)

    def update_device_switch_port(self, serial: str, port_id: str, **kwargs):
        return self.dashboard.switch.updateDeviceSwitchPort(serial, port_id, **kwargs)

    # ...additional switch.* calls...

    # =========================================================================
    # WIRELESS
    # =========================================================================

    def get_device_wireless_bluetooth_settings(self, serial: str):
        return self.dashboard.wireless.getDeviceWirelessBluetoothSettings(serial)

    def update_device_wireless_bluetooth_settings(self, serial: str, **kwargs):
        return self.dashboard.wireless.updateDeviceWirelessBluetoothSettings(serial, **kwargs)

    def get_network_wireless_air_marshal(self, network_id: str, **kwargs):
        return self.dashboard.wireless.getNetworkWirelessAirMarshal(network_id, **kwargs)

    def get_network_wireless_ssids(self, network_id: str):
        return self.dashboard.wireless.getNetworkWirelessSsids(network_id)

    def update_network_wireless_ssid(self, network_id: str, number: str, **kwargs):
        return self.dashboard.wireless.updateNetworkWirelessSsid(network_id, number, **kwargs)

    # ...additional wireless.* calls...

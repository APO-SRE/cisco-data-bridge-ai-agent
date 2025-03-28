################################################################################
# cisco-data-bridge-ai-agent\teeter_tools\Output\Meraki\meraki_sdk_client.py
# Copyright (c) 2025 Jeff Teeter, Ph.D.
# Cisco Systems, Inc.
# Licensed under the Apache License, Version 2.0 (see LICENSE)
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
#!/usr/bin/env python3


# This file was auto-generated to include only matched read-only methods.

import logging

from meraki.exceptions import APIError

from typing import Dict, Any


class MerakiSDKClientCustom:

    """Filtered Meraki client with only matched read-only methods."""

    def __init__(self, dashboard):

        self.dashboard = dashboard


    def getAdministeredIdentitiesMe(self, ) -> Dict[str, Any]:
        try:
            return self.dashboard.getAdministeredIdentitiesMe()
        except APIError as e:
            logging.error(f"API Error in getAdministeredIdentitiesMe: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAdministeredIdentitiesMe: {ex}")
            return {"error": str(ex)}

    def getAdministeredIdentitiesMeApiKeys(self, ) -> Dict[str, Any]:
        try:
            return self.dashboard.getAdministeredIdentitiesMeApiKeys()
        except APIError as e:
            logging.error(f"API Error in getAdministeredIdentitiesMeApiKeys: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAdministeredIdentitiesMeApiKeys: {ex}")
            return {"error": str(ex)}

    def getAdministeredLicensingSubscriptionEntitlements(self, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getAdministeredLicensingSubscriptionEntitlements(**kwargs)
        except APIError as e:
            logging.error(f"API Error in getAdministeredLicensingSubscriptionEntitlements: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAdministeredLicensingSubscriptionEntitlements: {ex}")
            return {"error": str(ex)}

    def getAdministeredLicensingSubscriptionSubscriptions(self, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getAdministeredLicensingSubscriptionSubscriptions(total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getAdministeredLicensingSubscriptionSubscriptions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAdministeredLicensingSubscriptionSubscriptions: {ex}")
            return {"error": str(ex)}

    def getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses(self, organizationIds, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses(organizationIds, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses: {ex}")
            return {"error": str(ex)}

    def getDevice(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDevice(serial)
        except APIError as e:
            logging.error(f"API Error in getDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDevice: {ex}")
            return {"error": str(ex)}

    def getDeviceApplianceDhcpSubnets(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceApplianceDhcpSubnets(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceApplianceDhcpSubnets: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceApplianceDhcpSubnets: {ex}")
            return {"error": str(ex)}

    def getDeviceAppliancePerformance(self, serial, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceAppliancePerformance(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceAppliancePerformance: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceAppliancePerformance: {ex}")
            return {"error": str(ex)}

    def getDeviceAppliancePrefixesDelegated(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceAppliancePrefixesDelegated(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceAppliancePrefixesDelegated: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceAppliancePrefixesDelegated: {ex}")
            return {"error": str(ex)}

    def getDeviceAppliancePrefixesDelegatedVlanAssignments(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceAppliancePrefixesDelegatedVlanAssignments(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceAppliancePrefixesDelegatedVlanAssignments: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceAppliancePrefixesDelegatedVlanAssignments: {ex}")
            return {"error": str(ex)}

    def getDeviceApplianceRadioSettings(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceApplianceRadioSettings(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceApplianceRadioSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceApplianceRadioSettings: {ex}")
            return {"error": str(ex)}

    def getDeviceApplianceUplinksSettings(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceApplianceUplinksSettings(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceApplianceUplinksSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceApplianceUplinksSettings: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraAnalyticsLive(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraAnalyticsLive(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraAnalyticsLive: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraAnalyticsLive: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraAnalyticsOverview(self, serial, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraAnalyticsOverview(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraAnalyticsOverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraAnalyticsOverview: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraAnalyticsRecent(self, serial, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraAnalyticsRecent(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraAnalyticsRecent: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraAnalyticsRecent: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraAnalyticsZoneHistory(self, serial, zoneId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraAnalyticsZoneHistory(serial, zoneId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraAnalyticsZoneHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraAnalyticsZoneHistory: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraAnalyticsZones(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraAnalyticsZones(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraAnalyticsZones: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraAnalyticsZones: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraCustomAnalytics(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraCustomAnalytics(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraCustomAnalytics: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraCustomAnalytics: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraQualityAndRetention(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraQualityAndRetention(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraQualityAndRetention: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraQualityAndRetention: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraSense(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraSense(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraSense: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraSense: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraSenseObjectDetectionModels(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraSenseObjectDetectionModels(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraSenseObjectDetectionModels: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraSenseObjectDetectionModels: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraVideoLink(self, serial, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraVideoLink(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraVideoLink: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraVideoLink: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraVideoSettings(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraVideoSettings(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraVideoSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraVideoSettings: {ex}")
            return {"error": str(ex)}

    def getDeviceCameraWirelessProfiles(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCameraWirelessProfiles(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceCameraWirelessProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCameraWirelessProfiles: {ex}")
            return {"error": str(ex)}

    def getDeviceCellularGatewayLan(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCellularGatewayLan(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceCellularGatewayLan: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCellularGatewayLan: {ex}")
            return {"error": str(ex)}

    def getDeviceCellularGatewayPortForwardingRules(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCellularGatewayPortForwardingRules(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceCellularGatewayPortForwardingRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCellularGatewayPortForwardingRules: {ex}")
            return {"error": str(ex)}

    def getDeviceCellularSims(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceCellularSims(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceCellularSims: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceCellularSims: {ex}")
            return {"error": str(ex)}

    def getDeviceClients(self, serial, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceClients(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceClients: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceClients: {ex}")
            return {"error": str(ex)}

    def getDeviceLiveToolsArpTable(self, serial, arpTableId) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceLiveToolsArpTable(serial, arpTableId)
        except APIError as e:
            logging.error(f"API Error in getDeviceLiveToolsArpTable: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceLiveToolsArpTable: {ex}")
            return {"error": str(ex)}

    def getDeviceLiveToolsCableTest(self, serial, id) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceLiveToolsCableTest(serial, id)
        except APIError as e:
            logging.error(f"API Error in getDeviceLiveToolsCableTest: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceLiveToolsCableTest: {ex}")
            return {"error": str(ex)}

    def getDeviceLiveToolsLedsBlink(self, serial, ledsBlinkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceLiveToolsLedsBlink(serial, ledsBlinkId)
        except APIError as e:
            logging.error(f"API Error in getDeviceLiveToolsLedsBlink: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceLiveToolsLedsBlink: {ex}")
            return {"error": str(ex)}

    def getDeviceLiveToolsPing(self, serial, id) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceLiveToolsPing(serial, id)
        except APIError as e:
            logging.error(f"API Error in getDeviceLiveToolsPing: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceLiveToolsPing: {ex}")
            return {"error": str(ex)}

    def getDeviceLiveToolsPingDevice(self, serial, id) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceLiveToolsPingDevice(serial, id)
        except APIError as e:
            logging.error(f"API Error in getDeviceLiveToolsPingDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceLiveToolsPingDevice: {ex}")
            return {"error": str(ex)}

    def getDeviceLiveToolsThroughputTest(self, serial, throughputTestId) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceLiveToolsThroughputTest(serial, throughputTestId)
        except APIError as e:
            logging.error(f"API Error in getDeviceLiveToolsThroughputTest: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceLiveToolsThroughputTest: {ex}")
            return {"error": str(ex)}

    def getDeviceLiveToolsWakeOnLan(self, serial, wakeOnLanId) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceLiveToolsWakeOnLan(serial, wakeOnLanId)
        except APIError as e:
            logging.error(f"API Error in getDeviceLiveToolsWakeOnLan: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceLiveToolsWakeOnLan: {ex}")
            return {"error": str(ex)}

    def getDeviceLldpCdp(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceLldpCdp(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceLldpCdp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceLldpCdp: {ex}")
            return {"error": str(ex)}

    def getDeviceLossAndLatencyHistory(self, serial, ip, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceLossAndLatencyHistory(serial, ip, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceLossAndLatencyHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceLossAndLatencyHistory: {ex}")
            return {"error": str(ex)}

    def getDeviceManagementInterface(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceManagementInterface(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceManagementInterface: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceManagementInterface: {ex}")
            return {"error": str(ex)}

    def getDeviceSensorCommand(self, serial, commandId) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSensorCommand(serial, commandId)
        except APIError as e:
            logging.error(f"API Error in getDeviceSensorCommand: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSensorCommand: {ex}")
            return {"error": str(ex)}

    def getDeviceSensorCommands(self, serial, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSensorCommands(serial, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceSensorCommands: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSensorCommands: {ex}")
            return {"error": str(ex)}

    def getDeviceSensorRelationships(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSensorRelationships(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceSensorRelationships: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSensorRelationships: {ex}")
            return {"error": str(ex)}

    def getDeviceSwitchPort(self, serial, portId) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSwitchPort(serial, portId)
        except APIError as e:
            logging.error(f"API Error in getDeviceSwitchPort: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSwitchPort: {ex}")
            return {"error": str(ex)}

    def getDeviceSwitchPorts(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSwitchPorts(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceSwitchPorts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSwitchPorts: {ex}")
            return {"error": str(ex)}

    def getDeviceSwitchPortsStatuses(self, serial, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSwitchPortsStatuses(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceSwitchPortsStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSwitchPortsStatuses: {ex}")
            return {"error": str(ex)}

    def getDeviceSwitchPortsStatusesPackets(self, serial, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSwitchPortsStatusesPackets(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceSwitchPortsStatusesPackets: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSwitchPortsStatusesPackets: {ex}")
            return {"error": str(ex)}

    def getDeviceSwitchRoutingInterface(self, serial, interfaceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSwitchRoutingInterface(serial, interfaceId)
        except APIError as e:
            logging.error(f"API Error in getDeviceSwitchRoutingInterface: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSwitchRoutingInterface: {ex}")
            return {"error": str(ex)}

    def getDeviceSwitchRoutingInterfaceDhcp(self, serial, interfaceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSwitchRoutingInterfaceDhcp(serial, interfaceId)
        except APIError as e:
            logging.error(f"API Error in getDeviceSwitchRoutingInterfaceDhcp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSwitchRoutingInterfaceDhcp: {ex}")
            return {"error": str(ex)}

    def getDeviceSwitchRoutingInterfaces(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSwitchRoutingInterfaces(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceSwitchRoutingInterfaces: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSwitchRoutingInterfaces: {ex}")
            return {"error": str(ex)}

    def getDeviceSwitchRoutingStaticRoute(self, serial, staticRouteId) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSwitchRoutingStaticRoute(serial, staticRouteId)
        except APIError as e:
            logging.error(f"API Error in getDeviceSwitchRoutingStaticRoute: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSwitchRoutingStaticRoute: {ex}")
            return {"error": str(ex)}

    def getDeviceSwitchRoutingStaticRoutes(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSwitchRoutingStaticRoutes(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceSwitchRoutingStaticRoutes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSwitchRoutingStaticRoutes: {ex}")
            return {"error": str(ex)}

    def getDeviceSwitchWarmSpare(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceSwitchWarmSpare(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceSwitchWarmSpare: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceSwitchWarmSpare: {ex}")
            return {"error": str(ex)}

    def getDeviceWirelessBluetoothSettings(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceWirelessBluetoothSettings(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceWirelessBluetoothSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceWirelessBluetoothSettings: {ex}")
            return {"error": str(ex)}

    def getDeviceWirelessConnectionStats(self, serial, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceWirelessConnectionStats(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceWirelessConnectionStats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceWirelessConnectionStats: {ex}")
            return {"error": str(ex)}

    def getDeviceWirelessElectronicShelfLabel(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceWirelessElectronicShelfLabel(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceWirelessElectronicShelfLabel: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceWirelessElectronicShelfLabel: {ex}")
            return {"error": str(ex)}

    def getDeviceWirelessLatencyStats(self, serial, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceWirelessLatencyStats(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getDeviceWirelessLatencyStats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceWirelessLatencyStats: {ex}")
            return {"error": str(ex)}

    def getDeviceWirelessRadioSettings(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceWirelessRadioSettings(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceWirelessRadioSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceWirelessRadioSettings: {ex}")
            return {"error": str(ex)}

    def getDeviceWirelessStatus(self, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getDeviceWirelessStatus(serial)
        except APIError as e:
            logging.error(f"API Error in getDeviceWirelessStatus: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getDeviceWirelessStatus: {ex}")
            return {"error": str(ex)}

    def getNetwork(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetwork(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetwork: {ex}")
            return {"error": str(ex)}

    def getNetworkAlertsHistory(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkAlertsHistory(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkAlertsHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkAlertsHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkAlertsSettings(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkAlertsSettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkAlertsSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkAlertsSettings: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceClientSecurityEvents(self, networkId, clientId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceClientSecurityEvents(networkId, clientId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceClientSecurityEvents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceClientSecurityEvents: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceConnectivityMonitoringDestinations(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceConnectivityMonitoringDestinations(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceConnectivityMonitoringDestinations: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceConnectivityMonitoringDestinations: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceContentFiltering(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceContentFiltering(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceContentFiltering: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceContentFiltering: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceContentFilteringCategories(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceContentFilteringCategories(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceContentFilteringCategories: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceContentFilteringCategories: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallCellularFirewallRules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallCellularFirewallRules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallCellularFirewallRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallCellularFirewallRules: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallFirewalledService(self, networkId, service) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallFirewalledService(networkId, service)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallFirewalledService: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallFirewalledService: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallFirewalledServices(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallFirewalledServices(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallFirewalledServices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallFirewalledServices: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallInboundCellularFirewallRules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallInboundCellularFirewallRules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallInboundCellularFirewallRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallInboundCellularFirewallRules: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallInboundFirewallRules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallInboundFirewallRules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallInboundFirewallRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallInboundFirewallRules: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallL3FirewallRules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallL3FirewallRules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallL3FirewallRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallL3FirewallRules: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallL7FirewallRules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallL7FirewallRules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallL7FirewallRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallL7FirewallRules: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallL7FirewallRulesApplicationCategories: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallL7FirewallRulesApplicationCategories: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallOneToManyNatRules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallOneToManyNatRules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallOneToManyNatRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallOneToManyNatRules: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallOneToOneNatRules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallOneToOneNatRules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallOneToOneNatRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallOneToOneNatRules: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallPortForwardingRules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallPortForwardingRules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallPortForwardingRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallPortForwardingRules: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceFirewallSettings(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceFirewallSettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceFirewallSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceFirewallSettings: {ex}")
            return {"error": str(ex)}

    def getNetworkAppliancePort(self, networkId, portId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkAppliancePort(networkId, portId)
        except APIError as e:
            logging.error(f"API Error in getNetworkAppliancePort: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkAppliancePort: {ex}")
            return {"error": str(ex)}

    def getNetworkAppliancePorts(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkAppliancePorts(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkAppliancePorts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkAppliancePorts: {ex}")
            return {"error": str(ex)}

    def getNetworkAppliancePrefixesDelegatedStatic(self, networkId, staticDelegatedPrefixId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkAppliancePrefixesDelegatedStatic(networkId, staticDelegatedPrefixId)
        except APIError as e:
            logging.error(f"API Error in getNetworkAppliancePrefixesDelegatedStatic: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkAppliancePrefixesDelegatedStatic: {ex}")
            return {"error": str(ex)}

    def getNetworkAppliancePrefixesDelegatedStatics(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkAppliancePrefixesDelegatedStatics(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkAppliancePrefixesDelegatedStatics: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkAppliancePrefixesDelegatedStatics: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceRfProfile(self, networkId, rfProfileId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceRfProfile(networkId, rfProfileId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceRfProfile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceRfProfile: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceRfProfiles(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceRfProfiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceRfProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceRfProfiles: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceSecurityEvents(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceSecurityEvents(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceSecurityEvents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceSecurityEvents: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceSecurityIntrusion(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceSecurityIntrusion(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceSecurityIntrusion: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceSecurityIntrusion: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceSecurityMalware(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceSecurityMalware(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceSecurityMalware: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceSecurityMalware: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceSettings(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceSettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceSettings: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceSingleLan(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceSingleLan(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceSingleLan: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceSingleLan: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceSsid(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceSsid(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceSsid: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceSsid: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceSsids(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceSsids(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceSsids: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceSsids: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceStaticRoute(self, networkId, staticRouteId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceStaticRoute(networkId, staticRouteId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceStaticRoute: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceStaticRoute: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceStaticRoutes(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceStaticRoutes(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceStaticRoutes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceStaticRoutes: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceTrafficShaping(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceTrafficShaping(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceTrafficShaping: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceTrafficShaping: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId, customPerformanceClassId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceTrafficShapingCustomPerformanceClass(networkId, customPerformanceClassId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceTrafficShapingCustomPerformanceClass: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceTrafficShapingCustomPerformanceClass: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceTrafficShapingCustomPerformanceClasses(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceTrafficShapingCustomPerformanceClasses(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceTrafficShapingCustomPerformanceClasses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceTrafficShapingCustomPerformanceClasses: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceTrafficShapingRules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceTrafficShapingRules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceTrafficShapingRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceTrafficShapingRules: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceTrafficShapingUplinkBandwidth(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceTrafficShapingUplinkBandwidth(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceTrafficShapingUplinkBandwidth: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceTrafficShapingUplinkBandwidth: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceTrafficShapingUplinkSelection(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceTrafficShapingUplinkSelection(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceTrafficShapingUplinkSelection: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceTrafficShapingUplinkSelection: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceUplinksUsageHistory(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceUplinksUsageHistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceUplinksUsageHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceUplinksUsageHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceVlan(self, networkId, vlanId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceVlan(networkId, vlanId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceVlan: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceVlan: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceVlans(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceVlans(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceVlans: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceVlans: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceVlansSettings(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceVlansSettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceVlansSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceVlansSettings: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceVpnBgp(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceVpnBgp(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceVpnBgp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceVpnBgp: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceVpnSiteToSiteVpn(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceVpnSiteToSiteVpn(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceVpnSiteToSiteVpn: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceVpnSiteToSiteVpn: {ex}")
            return {"error": str(ex)}

    def getNetworkApplianceWarmSpare(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkApplianceWarmSpare(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkApplianceWarmSpare: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkApplianceWarmSpare: {ex}")
            return {"error": str(ex)}

    def getNetworkBluetoothClient(self, networkId, bluetoothClientId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkBluetoothClient(networkId, bluetoothClientId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkBluetoothClient: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkBluetoothClient: {ex}")
            return {"error": str(ex)}

    def getNetworkBluetoothClients(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkBluetoothClients(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkBluetoothClients: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkBluetoothClients: {ex}")
            return {"error": str(ex)}

    def getNetworkCameraQualityRetentionProfile(self, networkId, qualityRetentionProfileId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkCameraQualityRetentionProfile(networkId, qualityRetentionProfileId)
        except APIError as e:
            logging.error(f"API Error in getNetworkCameraQualityRetentionProfile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkCameraQualityRetentionProfile: {ex}")
            return {"error": str(ex)}

    def getNetworkCameraQualityRetentionProfiles(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkCameraQualityRetentionProfiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkCameraQualityRetentionProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkCameraQualityRetentionProfiles: {ex}")
            return {"error": str(ex)}

    def getNetworkCameraSchedules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkCameraSchedules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkCameraSchedules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkCameraSchedules: {ex}")
            return {"error": str(ex)}

    def getNetworkCameraWirelessProfile(self, networkId, wirelessProfileId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkCameraWirelessProfile(networkId, wirelessProfileId)
        except APIError as e:
            logging.error(f"API Error in getNetworkCameraWirelessProfile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkCameraWirelessProfile: {ex}")
            return {"error": str(ex)}

    def getNetworkCameraWirelessProfiles(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkCameraWirelessProfiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkCameraWirelessProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkCameraWirelessProfiles: {ex}")
            return {"error": str(ex)}

    def getNetworkCellularGatewayConnectivityMonitoringDestinations(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkCellularGatewayConnectivityMonitoringDestinations(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkCellularGatewayConnectivityMonitoringDestinations: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkCellularGatewayConnectivityMonitoringDestinations: {ex}")
            return {"error": str(ex)}

    def getNetworkCellularGatewayDhcp(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkCellularGatewayDhcp(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkCellularGatewayDhcp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkCellularGatewayDhcp: {ex}")
            return {"error": str(ex)}

    def getNetworkCellularGatewaySubnetPool(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkCellularGatewaySubnetPool(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkCellularGatewaySubnetPool: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkCellularGatewaySubnetPool: {ex}")
            return {"error": str(ex)}

    def getNetworkCellularGatewayUplink(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkCellularGatewayUplink(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkCellularGatewayUplink: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkCellularGatewayUplink: {ex}")
            return {"error": str(ex)}

    def getNetworkClient(self, networkId, clientId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkClient(networkId, clientId)
        except APIError as e:
            logging.error(f"API Error in getNetworkClient: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkClient: {ex}")
            return {"error": str(ex)}

    def getNetworkClientPolicy(self, networkId, clientId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkClientPolicy(networkId, clientId)
        except APIError as e:
            logging.error(f"API Error in getNetworkClientPolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkClientPolicy: {ex}")
            return {"error": str(ex)}

    def getNetworkClientSplashAuthorizationStatus(self, networkId, clientId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkClientSplashAuthorizationStatus(networkId, clientId)
        except APIError as e:
            logging.error(f"API Error in getNetworkClientSplashAuthorizationStatus: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkClientSplashAuthorizationStatus: {ex}")
            return {"error": str(ex)}

    def getNetworkClientTrafficHistory(self, networkId, clientId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkClientTrafficHistory(networkId, clientId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkClientTrafficHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkClientTrafficHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkClientUsageHistory(self, networkId, clientId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkClientUsageHistory(networkId, clientId)
        except APIError as e:
            logging.error(f"API Error in getNetworkClientUsageHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkClientUsageHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkClients(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkClients(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkClients: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkClients: {ex}")
            return {"error": str(ex)}

    def getNetworkClientsApplicationUsage(self, networkId, clients, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkClientsApplicationUsage(networkId, clients, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkClientsApplicationUsage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkClientsApplicationUsage: {ex}")
            return {"error": str(ex)}

    def getNetworkClientsBandwidthUsageHistory(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkClientsBandwidthUsageHistory(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkClientsBandwidthUsageHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkClientsBandwidthUsageHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkClientsOverview(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkClientsOverview(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkClientsOverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkClientsOverview: {ex}")
            return {"error": str(ex)}

    def getNetworkClientsUsageHistories(self, networkId, clients, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkClientsUsageHistories(networkId, clients, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkClientsUsageHistories: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkClientsUsageHistories: {ex}")
            return {"error": str(ex)}

    def getNetworkDevices(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkDevices(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkDevices: {ex}")
            return {"error": str(ex)}

    def getNetworkEvents(self, networkId, total_pages=1, direction='prev', event_log_end_time=None, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkEvents(networkId, total_pages, direction, event_log_end_time, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkEvents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkEvents: {ex}")
            return {"error": str(ex)}

    def getNetworkEventsEventTypes(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkEventsEventTypes(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkEventsEventTypes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkEventsEventTypes: {ex}")
            return {"error": str(ex)}

    def getNetworkFirmwareUpgrades(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkFirmwareUpgrades(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkFirmwareUpgrades: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkFirmwareUpgrades: {ex}")
            return {"error": str(ex)}

    def getNetworkFirmwareUpgradesStagedEvents(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkFirmwareUpgradesStagedEvents(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkFirmwareUpgradesStagedEvents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkFirmwareUpgradesStagedEvents: {ex}")
            return {"error": str(ex)}

    def getNetworkFirmwareUpgradesStagedGroup(self, networkId, groupId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkFirmwareUpgradesStagedGroup(networkId, groupId)
        except APIError as e:
            logging.error(f"API Error in getNetworkFirmwareUpgradesStagedGroup: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkFirmwareUpgradesStagedGroup: {ex}")
            return {"error": str(ex)}

    def getNetworkFirmwareUpgradesStagedGroups(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkFirmwareUpgradesStagedGroups(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkFirmwareUpgradesStagedGroups: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkFirmwareUpgradesStagedGroups: {ex}")
            return {"error": str(ex)}

    def getNetworkFirmwareUpgradesStagedStages(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkFirmwareUpgradesStagedStages(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkFirmwareUpgradesStagedStages: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkFirmwareUpgradesStagedStages: {ex}")
            return {"error": str(ex)}

    def getNetworkFloorPlan(self, networkId, floorPlanId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkFloorPlan(networkId, floorPlanId)
        except APIError as e:
            logging.error(f"API Error in getNetworkFloorPlan: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkFloorPlan: {ex}")
            return {"error": str(ex)}

    def getNetworkFloorPlans(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkFloorPlans(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkFloorPlans: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkFloorPlans: {ex}")
            return {"error": str(ex)}

    def getNetworkGroupPolicies(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkGroupPolicies(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkGroupPolicies: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkGroupPolicies: {ex}")
            return {"error": str(ex)}

    def getNetworkGroupPolicy(self, networkId, groupPolicyId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkGroupPolicy(networkId, groupPolicyId)
        except APIError as e:
            logging.error(f"API Error in getNetworkGroupPolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkGroupPolicy: {ex}")
            return {"error": str(ex)}

    def getNetworkHealthAlerts(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkHealthAlerts(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkHealthAlerts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkHealthAlerts: {ex}")
            return {"error": str(ex)}

    def getNetworkInsightApplicationHealthByTime(self, networkId, applicationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkInsightApplicationHealthByTime(networkId, applicationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkInsightApplicationHealthByTime: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkInsightApplicationHealthByTime: {ex}")
            return {"error": str(ex)}

    def getNetworkMerakiAuthUser(self, networkId, merakiAuthUserId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkMerakiAuthUser(networkId, merakiAuthUserId)
        except APIError as e:
            logging.error(f"API Error in getNetworkMerakiAuthUser: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkMerakiAuthUser: {ex}")
            return {"error": str(ex)}

    def getNetworkMerakiAuthUsers(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkMerakiAuthUsers(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkMerakiAuthUsers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkMerakiAuthUsers: {ex}")
            return {"error": str(ex)}

    def getNetworkMqttBroker(self, networkId, mqttBrokerId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkMqttBroker(networkId, mqttBrokerId)
        except APIError as e:
            logging.error(f"API Error in getNetworkMqttBroker: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkMqttBroker: {ex}")
            return {"error": str(ex)}

    def getNetworkMqttBrokers(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkMqttBrokers(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkMqttBrokers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkMqttBrokers: {ex}")
            return {"error": str(ex)}

    def getNetworkNetflow(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkNetflow(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkNetflow: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkNetflow: {ex}")
            return {"error": str(ex)}

    def getNetworkNetworkHealthChannelUtilization(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkNetworkHealthChannelUtilization(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkNetworkHealthChannelUtilization: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkNetworkHealthChannelUtilization: {ex}")
            return {"error": str(ex)}

    def getNetworkPiiPiiKeys(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkPiiPiiKeys(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkPiiPiiKeys: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkPiiPiiKeys: {ex}")
            return {"error": str(ex)}

    def getNetworkPiiRequest(self, networkId, requestId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkPiiRequest(networkId, requestId)
        except APIError as e:
            logging.error(f"API Error in getNetworkPiiRequest: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkPiiRequest: {ex}")
            return {"error": str(ex)}

    def getNetworkPiiRequests(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkPiiRequests(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkPiiRequests: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkPiiRequests: {ex}")
            return {"error": str(ex)}

    def getNetworkPiiSmDevicesForKey(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkPiiSmDevicesForKey(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkPiiSmDevicesForKey: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkPiiSmDevicesForKey: {ex}")
            return {"error": str(ex)}

    def getNetworkPiiSmOwnersForKey(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkPiiSmOwnersForKey(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkPiiSmOwnersForKey: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkPiiSmOwnersForKey: {ex}")
            return {"error": str(ex)}

    def getNetworkPoliciesByClient(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkPoliciesByClient(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkPoliciesByClient: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkPoliciesByClient: {ex}")
            return {"error": str(ex)}

    def getNetworkSensorAlertsCurrentOverviewByMetric(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSensorAlertsCurrentOverviewByMetric(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSensorAlertsCurrentOverviewByMetric: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSensorAlertsCurrentOverviewByMetric: {ex}")
            return {"error": str(ex)}

    def getNetworkSensorAlertsOverviewByMetric(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSensorAlertsOverviewByMetric(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSensorAlertsOverviewByMetric: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSensorAlertsOverviewByMetric: {ex}")
            return {"error": str(ex)}

    def getNetworkSensorAlertsProfile(self, networkId, id) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSensorAlertsProfile(networkId, id)
        except APIError as e:
            logging.error(f"API Error in getNetworkSensorAlertsProfile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSensorAlertsProfile: {ex}")
            return {"error": str(ex)}

    def getNetworkSensorAlertsProfiles(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSensorAlertsProfiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSensorAlertsProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSensorAlertsProfiles: {ex}")
            return {"error": str(ex)}

    def getNetworkSensorMqttBroker(self, networkId, mqttBrokerId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSensorMqttBroker(networkId, mqttBrokerId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSensorMqttBroker: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSensorMqttBroker: {ex}")
            return {"error": str(ex)}

    def getNetworkSensorMqttBrokers(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSensorMqttBrokers(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSensorMqttBrokers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSensorMqttBrokers: {ex}")
            return {"error": str(ex)}

    def getNetworkSensorRelationships(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSensorRelationships(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSensorRelationships: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSensorRelationships: {ex}")
            return {"error": str(ex)}

    def getNetworkSettings(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSettings: {ex}")
            return {"error": str(ex)}

    def getNetworkSmBypassActivationLockAttempt(self, networkId, attemptId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmBypassActivationLockAttempt(networkId, attemptId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmBypassActivationLockAttempt: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmBypassActivationLockAttempt: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDeviceCellularUsageHistory(self, networkId, deviceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDeviceCellularUsageHistory(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDeviceCellularUsageHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDeviceCellularUsageHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDeviceCerts(self, networkId, deviceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDeviceCerts(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDeviceCerts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDeviceCerts: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDeviceConnectivity(self, networkId, deviceId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDeviceConnectivity(networkId, deviceId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDeviceConnectivity: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDeviceConnectivity: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDeviceDesktopLogs(self, networkId, deviceId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDeviceDesktopLogs(networkId, deviceId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDeviceDesktopLogs: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDeviceDesktopLogs: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDeviceDeviceCommandLogs(self, networkId, deviceId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDeviceDeviceCommandLogs(networkId, deviceId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDeviceDeviceCommandLogs: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDeviceDeviceCommandLogs: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDeviceDeviceProfiles(self, networkId, deviceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDeviceDeviceProfiles(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDeviceDeviceProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDeviceDeviceProfiles: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDeviceNetworkAdapters(self, networkId, deviceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDeviceNetworkAdapters(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDeviceNetworkAdapters: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDeviceNetworkAdapters: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDevicePerformanceHistory(self, networkId, deviceId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDevicePerformanceHistory(networkId, deviceId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDevicePerformanceHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDevicePerformanceHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDeviceRestrictions(self, networkId, deviceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDeviceRestrictions(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDeviceRestrictions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDeviceRestrictions: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDeviceSecurityCenters(self, networkId, deviceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDeviceSecurityCenters(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDeviceSecurityCenters: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDeviceSecurityCenters: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDeviceSoftwares(self, networkId, deviceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDeviceSoftwares(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDeviceSoftwares: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDeviceSoftwares: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDeviceWlanLists(self, networkId, deviceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDeviceWlanLists(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDeviceWlanLists: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDeviceWlanLists: {ex}")
            return {"error": str(ex)}

    def getNetworkSmDevices(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmDevices(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmDevices: {ex}")
            return {"error": str(ex)}

    def getNetworkSmProfiles(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmProfiles(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmProfiles: {ex}")
            return {"error": str(ex)}

    def getNetworkSmTargetGroup(self, networkId, targetGroupId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmTargetGroup(networkId, targetGroupId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmTargetGroup: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmTargetGroup: {ex}")
            return {"error": str(ex)}

    def getNetworkSmTargetGroups(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmTargetGroups(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmTargetGroups: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmTargetGroups: {ex}")
            return {"error": str(ex)}

    def getNetworkSmTrustedAccessConfigs(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmTrustedAccessConfigs(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmTrustedAccessConfigs: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmTrustedAccessConfigs: {ex}")
            return {"error": str(ex)}

    def getNetworkSmUserAccessDevices(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmUserAccessDevices(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmUserAccessDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmUserAccessDevices: {ex}")
            return {"error": str(ex)}

    def getNetworkSmUserDeviceProfiles(self, networkId, userId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmUserDeviceProfiles(networkId, userId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmUserDeviceProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmUserDeviceProfiles: {ex}")
            return {"error": str(ex)}

    def getNetworkSmUserSoftwares(self, networkId, userId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmUserSoftwares(networkId, userId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmUserSoftwares: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmUserSoftwares: {ex}")
            return {"error": str(ex)}

    def getNetworkSmUsers(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSmUsers(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSmUsers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSmUsers: {ex}")
            return {"error": str(ex)}

    def getNetworkSnmp(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSnmp(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSnmp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSnmp: {ex}")
            return {"error": str(ex)}

    def getNetworkSplashLoginAttempts(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSplashLoginAttempts(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSplashLoginAttempts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSplashLoginAttempts: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchAccessControlLists(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchAccessControlLists(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchAccessControlLists: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchAccessControlLists: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchAccessPolicies(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchAccessPolicies(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchAccessPolicies: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchAccessPolicies: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchAccessPolicy(self, networkId, accessPolicyNumber) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchAccessPolicy(networkId, accessPolicyNumber)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchAccessPolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchAccessPolicy: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchAlternateManagementInterface(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchAlternateManagementInterface(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchAlternateManagementInterface: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchAlternateManagementInterface: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchDhcpServerPolicy(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchDhcpServerPolicy(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchDhcpServerPolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchDhcpServerPolicy: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchDhcpV4ServersSeen(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchDhcpV4ServersSeen(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchDhcpV4ServersSeen: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchDhcpV4ServersSeen: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchDscpToCosMappings(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchDscpToCosMappings(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchDscpToCosMappings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchDscpToCosMappings: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchLinkAggregations(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchLinkAggregations(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchLinkAggregations: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchLinkAggregations: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchMtu(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchMtu(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchMtu: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchMtu: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchPortSchedules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchPortSchedules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchPortSchedules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchPortSchedules: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchQosRule(self, networkId, qosRuleId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchQosRule(networkId, qosRuleId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchQosRule: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchQosRule: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchQosRules(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchQosRules(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchQosRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchQosRules: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchQosRulesOrder(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchQosRulesOrder(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchQosRulesOrder: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchQosRulesOrder: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchRoutingMulticast(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchRoutingMulticast(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchRoutingMulticast: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchRoutingMulticast: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchRoutingMulticastRendezvousPoint(self, networkId, rendezvousPointId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchRoutingMulticastRendezvousPoint(networkId, rendezvousPointId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchRoutingMulticastRendezvousPoint: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchRoutingMulticastRendezvousPoint: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchRoutingMulticastRendezvousPoints(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchRoutingMulticastRendezvousPoints(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchRoutingMulticastRendezvousPoints: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchRoutingMulticastRendezvousPoints: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchRoutingOspf(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchRoutingOspf(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchRoutingOspf: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchRoutingOspf: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchSettings(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchSettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchSettings: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchStack(self, networkId, switchStackId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchStack(networkId, switchStackId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchStack: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchStack: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchStackRoutingInterface(self, networkId, switchStackId, interfaceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchStackRoutingInterface(networkId, switchStackId, interfaceId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchStackRoutingInterface: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchStackRoutingInterface: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchStackRoutingInterfaceDhcp(self, networkId, switchStackId, interfaceId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchStackRoutingInterfaceDhcp(networkId, switchStackId, interfaceId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchStackRoutingInterfaceDhcp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchStackRoutingInterfaceDhcp: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchStackRoutingInterfaces(self, networkId, switchStackId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchStackRoutingInterfaces(networkId, switchStackId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchStackRoutingInterfaces: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchStackRoutingInterfaces: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchStackRoutingStaticRoute(self, networkId, switchStackId, staticRouteId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchStackRoutingStaticRoute(networkId, switchStackId, staticRouteId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchStackRoutingStaticRoute: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchStackRoutingStaticRoute: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchStackRoutingStaticRoutes(self, networkId, switchStackId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchStackRoutingStaticRoutes(networkId, switchStackId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchStackRoutingStaticRoutes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchStackRoutingStaticRoutes: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchStacks(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchStacks(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchStacks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchStacks: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchStormControl(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchStormControl(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchStormControl: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchStormControl: {ex}")
            return {"error": str(ex)}

    def getNetworkSwitchStp(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSwitchStp(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSwitchStp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSwitchStp: {ex}")
            return {"error": str(ex)}

    def getNetworkSyslogServers(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkSyslogServers(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkSyslogServers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkSyslogServers: {ex}")
            return {"error": str(ex)}

    def getNetworkTopologyLinkLayer(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkTopologyLinkLayer(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkTopologyLinkLayer: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkTopologyLinkLayer: {ex}")
            return {"error": str(ex)}

    def getNetworkTraffic(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkTraffic(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkTraffic: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkTraffic: {ex}")
            return {"error": str(ex)}

    def getNetworkTrafficAnalysis(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkTrafficAnalysis(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkTrafficAnalysis: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkTrafficAnalysis: {ex}")
            return {"error": str(ex)}

    def getNetworkTrafficShapingApplicationCategories(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkTrafficShapingApplicationCategories(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkTrafficShapingApplicationCategories: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkTrafficShapingApplicationCategories: {ex}")
            return {"error": str(ex)}

    def getNetworkTrafficShapingDscpTaggingOptions(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkTrafficShapingDscpTaggingOptions(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkTrafficShapingDscpTaggingOptions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkTrafficShapingDscpTaggingOptions: {ex}")
            return {"error": str(ex)}

    def getNetworkVlanProfile(self, networkId, iname) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkVlanProfile(networkId, iname)
        except APIError as e:
            logging.error(f"API Error in getNetworkVlanProfile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkVlanProfile: {ex}")
            return {"error": str(ex)}

    def getNetworkVlanProfiles(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkVlanProfiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkVlanProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkVlanProfiles: {ex}")
            return {"error": str(ex)}

    def getNetworkVlanProfilesAssignmentsByDevice(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkVlanProfilesAssignmentsByDevice(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkVlanProfilesAssignmentsByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkVlanProfilesAssignmentsByDevice: {ex}")
            return {"error": str(ex)}

    def getNetworkWebhooksHttpServer(self, networkId, httpServerId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWebhooksHttpServer(networkId, httpServerId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWebhooksHttpServer: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWebhooksHttpServer: {ex}")
            return {"error": str(ex)}

    def getNetworkWebhooksHttpServers(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWebhooksHttpServers(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWebhooksHttpServers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWebhooksHttpServers: {ex}")
            return {"error": str(ex)}

    def getNetworkWebhooksPayloadTemplate(self, networkId, payloadTemplateId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWebhooksPayloadTemplate(networkId, payloadTemplateId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWebhooksPayloadTemplate: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWebhooksPayloadTemplate: {ex}")
            return {"error": str(ex)}

    def getNetworkWebhooksPayloadTemplates(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWebhooksPayloadTemplates(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWebhooksPayloadTemplates: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWebhooksPayloadTemplates: {ex}")
            return {"error": str(ex)}

    def getNetworkWebhooksWebhookTest(self, networkId, webhookTestId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWebhooksWebhookTest(networkId, webhookTestId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWebhooksWebhookTest: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWebhooksWebhookTest: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessAirMarshal(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessAirMarshal(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessAirMarshal: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessAirMarshal: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessAlternateManagementInterface(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessAlternateManagementInterface(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessAlternateManagementInterface: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessAlternateManagementInterface: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessBilling(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessBilling(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessBilling: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessBilling: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessBluetoothSettings(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessBluetoothSettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessBluetoothSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessBluetoothSettings: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessChannelUtilizationHistory(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessChannelUtilizationHistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessChannelUtilizationHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessChannelUtilizationHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessClientConnectionStats(self, networkId, clientId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessClientConnectionStats(networkId, clientId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessClientConnectionStats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessClientConnectionStats: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessClientConnectivityEvents(self, networkId, clientId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessClientConnectivityEvents(networkId, clientId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessClientConnectivityEvents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessClientConnectivityEvents: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessClientCountHistory(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessClientCountHistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessClientCountHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessClientCountHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessClientLatencyHistory(self, networkId, clientId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessClientLatencyHistory(networkId, clientId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessClientLatencyHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessClientLatencyHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessClientLatencyStats(self, networkId, clientId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessClientLatencyStats(networkId, clientId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessClientLatencyStats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessClientLatencyStats: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessClientsConnectionStats(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessClientsConnectionStats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessClientsConnectionStats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessClientsConnectionStats: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessClientsLatencyStats(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessClientsLatencyStats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessClientsLatencyStats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessClientsLatencyStats: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessConnectionStats(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessConnectionStats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessConnectionStats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessConnectionStats: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessDataRateHistory(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessDataRateHistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessDataRateHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessDataRateHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessDevicesConnectionStats(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessDevicesConnectionStats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessDevicesConnectionStats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessDevicesConnectionStats: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessDevicesLatencyStats(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessDevicesLatencyStats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessDevicesLatencyStats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessDevicesLatencyStats: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessElectronicShelfLabel(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessElectronicShelfLabel(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessElectronicShelfLabel: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessElectronicShelfLabel: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessElectronicShelfLabelConfiguredDevices(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessElectronicShelfLabelConfiguredDevices(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessElectronicShelfLabelConfiguredDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessElectronicShelfLabelConfiguredDevices: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessEthernetPortsProfile(self, networkId, profileId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessEthernetPortsProfile(networkId, profileId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessEthernetPortsProfile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessEthernetPortsProfile: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessEthernetPortsProfiles(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessEthernetPortsProfiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessEthernetPortsProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessEthernetPortsProfiles: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessFailedConnections(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessFailedConnections(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessFailedConnections: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessFailedConnections: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessLatencyHistory(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessLatencyHistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessLatencyHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessLatencyHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessLatencyStats(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessLatencyStats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessLatencyStats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessLatencyStats: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessMeshStatuses(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessMeshStatuses(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessMeshStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessMeshStatuses: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessRfProfile(self, networkId, rfProfileId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessRfProfile(networkId, rfProfileId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessRfProfile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessRfProfile: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessRfProfiles(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessRfProfiles(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessRfProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessRfProfiles: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSettings(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSettings: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSignalQualityHistory(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSignalQualityHistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSignalQualityHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSignalQualityHistory: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsid(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsid(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsid: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsid: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidBonjourForwarding(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidBonjourForwarding(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidBonjourForwarding: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidBonjourForwarding: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidDeviceTypeGroupPolicies(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidDeviceTypeGroupPolicies(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidDeviceTypeGroupPolicies: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidDeviceTypeGroupPolicies: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidEapOverride(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidEapOverride(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidEapOverride: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidEapOverride: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidFirewallL3FirewallRules(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidFirewallL3FirewallRules(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidFirewallL3FirewallRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidFirewallL3FirewallRules: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidFirewallL7FirewallRules(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidFirewallL7FirewallRules(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidFirewallL7FirewallRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidFirewallL7FirewallRules: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidHotspot20(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidHotspot20(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidHotspot20: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidHotspot20: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidIdentityPsk(self, networkId, number, identityPskId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidIdentityPsk: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidIdentityPsk: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidIdentityPsks(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidIdentityPsks(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidIdentityPsks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidIdentityPsks: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidSchedules(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidSchedules(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidSchedules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidSchedules: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidSplashSettings(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidSplashSettings(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidSplashSettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidSplashSettings: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidTrafficShapingRules(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidTrafficShapingRules(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidTrafficShapingRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidTrafficShapingRules: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsidVpn(self, networkId, number) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsidVpn(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsidVpn: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsidVpn: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessSsids(self, networkId) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessSsids(networkId)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessSsids: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessSsids: {ex}")
            return {"error": str(ex)}

    def getNetworkWirelessUsageHistory(self, networkId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getNetworkWirelessUsageHistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getNetworkWirelessUsageHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getNetworkWirelessUsageHistory: {ex}")
            return {"error": str(ex)}

    def getOrganization(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganization(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganization: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganization: {ex}")
            return {"error": str(ex)}

    def getOrganizationActionBatch(self, organizationId, actionBatchId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationActionBatch(organizationId, actionBatchId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationActionBatch: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationActionBatch: {ex}")
            return {"error": str(ex)}

    def getOrganizationActionBatches(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationActionBatches(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationActionBatches: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationActionBatches: {ex}")
            return {"error": str(ex)}

    def getOrganizationAdaptivePolicyAcl(self, organizationId, aclId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAdaptivePolicyAcl(organizationId, aclId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAdaptivePolicyAcl: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAdaptivePolicyAcl: {ex}")
            return {"error": str(ex)}

    def getOrganizationAdaptivePolicyAcls(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAdaptivePolicyAcls(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAdaptivePolicyAcls: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAdaptivePolicyAcls: {ex}")
            return {"error": str(ex)}

    def getOrganizationAdaptivePolicyGroup(self, organizationId, id) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAdaptivePolicyGroup(organizationId, id)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAdaptivePolicyGroup: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAdaptivePolicyGroup: {ex}")
            return {"error": str(ex)}

    def getOrganizationAdaptivePolicyGroups(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAdaptivePolicyGroups(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAdaptivePolicyGroups: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAdaptivePolicyGroups: {ex}")
            return {"error": str(ex)}

    def getOrganizationAdaptivePolicyOverview(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAdaptivePolicyOverview(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAdaptivePolicyOverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAdaptivePolicyOverview: {ex}")
            return {"error": str(ex)}

    def getOrganizationAdaptivePolicyPolicies(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAdaptivePolicyPolicies(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAdaptivePolicyPolicies: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAdaptivePolicyPolicies: {ex}")
            return {"error": str(ex)}

    def getOrganizationAdaptivePolicyPolicy(self, organizationId, id) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAdaptivePolicyPolicy(organizationId, id)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAdaptivePolicyPolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAdaptivePolicyPolicy: {ex}")
            return {"error": str(ex)}

    def getOrganizationAdaptivePolicySettings(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAdaptivePolicySettings(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAdaptivePolicySettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAdaptivePolicySettings: {ex}")
            return {"error": str(ex)}

    def getOrganizationAdmins(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAdmins(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAdmins: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAdmins: {ex}")
            return {"error": str(ex)}

    def getOrganizationAlertsProfiles(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAlertsProfiles(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAlertsProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAlertsProfiles: {ex}")
            return {"error": str(ex)}

    def getOrganizationApiRequests(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApiRequests(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApiRequests: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApiRequests: {ex}")
            return {"error": str(ex)}

    def getOrganizationApiRequestsOverview(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApiRequestsOverview(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApiRequestsOverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApiRequestsOverview: {ex}")
            return {"error": str(ex)}

    def getOrganizationApiRequestsOverviewResponseCodesByInterval(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApiRequestsOverviewResponseCodesByInterval(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApiRequestsOverviewResponseCodesByInterval: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApiRequestsOverviewResponseCodesByInterval: {ex}")
            return {"error": str(ex)}

    def getOrganizationApplianceSecurityEvents(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApplianceSecurityEvents(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApplianceSecurityEvents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApplianceSecurityEvents: {ex}")
            return {"error": str(ex)}

    def getOrganizationApplianceSecurityIntrusion(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApplianceSecurityIntrusion(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApplianceSecurityIntrusion: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApplianceSecurityIntrusion: {ex}")
            return {"error": str(ex)}

    def getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork: {ex}")
            return {"error": str(ex)}

    def getOrganizationApplianceUplinkStatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApplianceUplinkStatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApplianceUplinkStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApplianceUplinkStatuses: {ex}")
            return {"error": str(ex)}

    def getOrganizationApplianceUplinksStatusesOverview(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApplianceUplinksStatusesOverview(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApplianceUplinksStatusesOverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApplianceUplinksStatusesOverview: {ex}")
            return {"error": str(ex)}

    def getOrganizationApplianceUplinksUsageByNetwork(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApplianceUplinksUsageByNetwork(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApplianceUplinksUsageByNetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApplianceUplinksUsageByNetwork: {ex}")
            return {"error": str(ex)}

    def getOrganizationApplianceVpnStats(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApplianceVpnStats(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApplianceVpnStats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApplianceVpnStats: {ex}")
            return {"error": str(ex)}

    def getOrganizationApplianceVpnStatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApplianceVpnStatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApplianceVpnStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApplianceVpnStatuses: {ex}")
            return {"error": str(ex)}

    def getOrganizationApplianceVpnThirdPartyVPNPeers(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApplianceVpnThirdPartyVPNPeers(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApplianceVpnThirdPartyVPNPeers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApplianceVpnThirdPartyVPNPeers: {ex}")
            return {"error": str(ex)}

    def getOrganizationApplianceVpnVpnFirewallRules(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationApplianceVpnVpnFirewallRules(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationApplianceVpnVpnFirewallRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationApplianceVpnVpnFirewallRules: {ex}")
            return {"error": str(ex)}

    def getOrganizationAssuranceAlert(self, organizationId, id) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAssuranceAlert(organizationId, id)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAssuranceAlert: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAssuranceAlert: {ex}")
            return {"error": str(ex)}

    def getOrganizationAssuranceAlerts(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAssuranceAlerts(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAssuranceAlerts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAssuranceAlerts: {ex}")
            return {"error": str(ex)}

    def getOrganizationAssuranceAlertsOverview(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAssuranceAlertsOverview(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAssuranceAlertsOverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAssuranceAlertsOverview: {ex}")
            return {"error": str(ex)}

    def getOrganizationAssuranceAlertsOverviewByNetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAssuranceAlertsOverviewByNetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAssuranceAlertsOverviewByNetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAssuranceAlertsOverviewByNetwork: {ex}")
            return {"error": str(ex)}

    def getOrganizationAssuranceAlertsOverviewByType(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAssuranceAlertsOverviewByType(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAssuranceAlertsOverviewByType: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAssuranceAlertsOverviewByType: {ex}")
            return {"error": str(ex)}

    def getOrganizationAssuranceAlertsOverviewHistorical(self, organizationId, segmentDuration, tsStart, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationAssuranceAlertsOverviewHistorical(organizationId, segmentDuration, tsStart, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationAssuranceAlertsOverviewHistorical: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationAssuranceAlertsOverviewHistorical: {ex}")
            return {"error": str(ex)}

    def getOrganizationBrandingPolicies(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationBrandingPolicies(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationBrandingPolicies: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationBrandingPolicies: {ex}")
            return {"error": str(ex)}

    def getOrganizationBrandingPoliciesPriorities(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationBrandingPoliciesPriorities(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationBrandingPoliciesPriorities: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationBrandingPoliciesPriorities: {ex}")
            return {"error": str(ex)}

    def getOrganizationBrandingPolicy(self, organizationId, brandingPolicyId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationBrandingPolicy(organizationId, brandingPolicyId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationBrandingPolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationBrandingPolicy: {ex}")
            return {"error": str(ex)}

    def getOrganizationCameraBoundariesAreasByDevice(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCameraBoundariesAreasByDevice(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCameraBoundariesAreasByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCameraBoundariesAreasByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationCameraBoundariesLinesByDevice(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCameraBoundariesLinesByDevice(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCameraBoundariesLinesByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCameraBoundariesLinesByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationCameraCustomAnalyticsArtifact(self, organizationId, artifactId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCameraCustomAnalyticsArtifact(organizationId, artifactId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCameraCustomAnalyticsArtifact: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCameraCustomAnalyticsArtifact: {ex}")
            return {"error": str(ex)}

    def getOrganizationCameraCustomAnalyticsArtifacts(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCameraCustomAnalyticsArtifacts(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCameraCustomAnalyticsArtifacts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCameraCustomAnalyticsArtifacts: {ex}")
            return {"error": str(ex)}

    def getOrganizationCameraDetectionsHistoryByBoundaryByInterval(self, organizationId, boundaryIds, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCameraDetectionsHistoryByBoundaryByInterval(organizationId, boundaryIds, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCameraDetectionsHistoryByBoundaryByInterval: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCameraDetectionsHistoryByBoundaryByInterval: {ex}")
            return {"error": str(ex)}

    def getOrganizationCameraOnboardingStatuses(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCameraOnboardingStatuses(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCameraOnboardingStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCameraOnboardingStatuses: {ex}")
            return {"error": str(ex)}

    def getOrganizationCameraPermission(self, organizationId, permissionScopeId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCameraPermission(organizationId, permissionScopeId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCameraPermission: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCameraPermission: {ex}")
            return {"error": str(ex)}

    def getOrganizationCameraPermissions(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCameraPermissions(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCameraPermissions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCameraPermissions: {ex}")
            return {"error": str(ex)}

    def getOrganizationCameraRole(self, organizationId, roleId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCameraRole(organizationId, roleId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCameraRole: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCameraRole: {ex}")
            return {"error": str(ex)}

    def getOrganizationCameraRoles(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCameraRoles(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCameraRoles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCameraRoles: {ex}")
            return {"error": str(ex)}

    def getOrganizationCellularGatewayEsimsInventory(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCellularGatewayEsimsInventory(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCellularGatewayEsimsInventory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCellularGatewayEsimsInventory: {ex}")
            return {"error": str(ex)}

    def getOrganizationCellularGatewayEsimsServiceProviders(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCellularGatewayEsimsServiceProviders(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCellularGatewayEsimsServiceProviders: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCellularGatewayEsimsServiceProviders: {ex}")
            return {"error": str(ex)}

    def getOrganizationCellularGatewayEsimsServiceProvidersAccounts(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCellularGatewayEsimsServiceProvidersAccounts(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCellularGatewayEsimsServiceProvidersAccounts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCellularGatewayEsimsServiceProvidersAccounts: {ex}")
            return {"error": str(ex)}

    def getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans(self, organizationId, accountIds) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans(organizationId, accountIds)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans: {ex}")
            return {"error": str(ex)}

    def getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans(self, organizationId, accountIds) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans(organizationId, accountIds)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans: {ex}")
            return {"error": str(ex)}

    def getOrganizationCellularGatewayUplinkStatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationCellularGatewayUplinkStatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationCellularGatewayUplinkStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationCellularGatewayUplinkStatuses: {ex}")
            return {"error": str(ex)}

    def getOrganizationClientsBandwidthUsageHistory(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationClientsBandwidthUsageHistory(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationClientsBandwidthUsageHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationClientsBandwidthUsageHistory: {ex}")
            return {"error": str(ex)}

    def getOrganizationClientsOverview(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationClientsOverview(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationClientsOverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationClientsOverview: {ex}")
            return {"error": str(ex)}

    def getOrganizationClientsSearch(self, organizationId, mac, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationClientsSearch(organizationId, mac, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationClientsSearch: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationClientsSearch: {ex}")
            return {"error": str(ex)}

    def getOrganizationConfigTemplate(self, organizationId, configTemplateId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationConfigTemplate(organizationId, configTemplateId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationConfigTemplate: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationConfigTemplate: {ex}")
            return {"error": str(ex)}

    def getOrganizationConfigTemplateSwitchProfilePort(self, organizationId, configTemplateId, profileId, portId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationConfigTemplateSwitchProfilePort(organizationId, configTemplateId, profileId, portId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationConfigTemplateSwitchProfilePort: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationConfigTemplateSwitchProfilePort: {ex}")
            return {"error": str(ex)}

    def getOrganizationConfigTemplateSwitchProfilePorts(self, organizationId, configTemplateId, profileId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationConfigTemplateSwitchProfilePorts(organizationId, configTemplateId, profileId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationConfigTemplateSwitchProfilePorts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationConfigTemplateSwitchProfilePorts: {ex}")
            return {"error": str(ex)}

    def getOrganizationConfigTemplateSwitchProfiles(self, organizationId, configTemplateId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationConfigTemplateSwitchProfiles(organizationId, configTemplateId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationConfigTemplateSwitchProfiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationConfigTemplateSwitchProfiles: {ex}")
            return {"error": str(ex)}

    def getOrganizationConfigTemplates(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationConfigTemplates(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationConfigTemplates: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationConfigTemplates: {ex}")
            return {"error": str(ex)}

    def getOrganizationConfigurationChanges(self, organizationId, total_pages=1, direction='prev', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationConfigurationChanges(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationConfigurationChanges: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationConfigurationChanges: {ex}")
            return {"error": str(ex)}

    def getOrganizationDevices(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationDevices(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationDevices: {ex}")
            return {"error": str(ex)}

    def getOrganizationDevicesAvailabilities(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationDevicesAvailabilities(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationDevicesAvailabilities: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationDevicesAvailabilities: {ex}")
            return {"error": str(ex)}

    def getOrganizationDevicesAvailabilitiesChangeHistory(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationDevicesAvailabilitiesChangeHistory(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationDevicesAvailabilitiesChangeHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationDevicesAvailabilitiesChangeHistory: {ex}")
            return {"error": str(ex)}

    def getOrganizationDevicesOverviewByModel(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationDevicesOverviewByModel(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationDevicesOverviewByModel: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationDevicesOverviewByModel: {ex}")
            return {"error": str(ex)}

    def getOrganizationDevicesPowerModulesStatusesByDevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationDevicesPowerModulesStatusesByDevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationDevicesPowerModulesStatusesByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationDevicesPowerModulesStatusesByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationDevicesProvisioningStatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationDevicesProvisioningStatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationDevicesProvisioningStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationDevicesProvisioningStatuses: {ex}")
            return {"error": str(ex)}

    def getOrganizationDevicesStatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationDevicesStatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationDevicesStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationDevicesStatuses: {ex}")
            return {"error": str(ex)}

    def getOrganizationDevicesStatusesOverview(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationDevicesStatusesOverview(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationDevicesStatusesOverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationDevicesStatusesOverview: {ex}")
            return {"error": str(ex)}

    def getOrganizationDevicesUplinksAddressesByDevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationDevicesUplinksAddressesByDevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationDevicesUplinksAddressesByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationDevicesUplinksAddressesByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationDevicesUplinksLossAndLatency(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationDevicesUplinksLossAndLatency(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationDevicesUplinksLossAndLatency: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationDevicesUplinksLossAndLatency: {ex}")
            return {"error": str(ex)}

    def getOrganizationEarlyAccessFeatures(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationEarlyAccessFeatures(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationEarlyAccessFeatures: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationEarlyAccessFeatures: {ex}")
            return {"error": str(ex)}

    def getOrganizationEarlyAccessFeaturesOptIn(self, organizationId, optInId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationEarlyAccessFeaturesOptIn(organizationId, optInId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationEarlyAccessFeaturesOptIn: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationEarlyAccessFeaturesOptIn: {ex}")
            return {"error": str(ex)}

    def getOrganizationEarlyAccessFeaturesOptIns(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationEarlyAccessFeaturesOptIns(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationEarlyAccessFeaturesOptIns: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationEarlyAccessFeaturesOptIns: {ex}")
            return {"error": str(ex)}

    def getOrganizationFirmwareUpgrades(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationFirmwareUpgrades(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationFirmwareUpgrades: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationFirmwareUpgrades: {ex}")
            return {"error": str(ex)}

    def getOrganizationFirmwareUpgradesByDevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationFirmwareUpgradesByDevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationFirmwareUpgradesByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationFirmwareUpgradesByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationFloorPlansAutoLocateDevices(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationFloorPlansAutoLocateDevices(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationFloorPlansAutoLocateDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationFloorPlansAutoLocateDevices: {ex}")
            return {"error": str(ex)}

    def getOrganizationFloorPlansAutoLocateStatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationFloorPlansAutoLocateStatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationFloorPlansAutoLocateStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationFloorPlansAutoLocateStatuses: {ex}")
            return {"error": str(ex)}

    def getOrganizationInsightApplications(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationInsightApplications(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationInsightApplications: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationInsightApplications: {ex}")
            return {"error": str(ex)}

    def getOrganizationInsightMonitoredMediaServer(self, organizationId, monitoredMediaServerId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationInsightMonitoredMediaServer(organizationId, monitoredMediaServerId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationInsightMonitoredMediaServer: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationInsightMonitoredMediaServer: {ex}")
            return {"error": str(ex)}

    def getOrganizationInsightMonitoredMediaServers(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationInsightMonitoredMediaServers(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationInsightMonitoredMediaServers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationInsightMonitoredMediaServers: {ex}")
            return {"error": str(ex)}

    def getOrganizationInventoryDevice(self, organizationId, serial) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationInventoryDevice(organizationId, serial)
        except APIError as e:
            logging.error(f"API Error in getOrganizationInventoryDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationInventoryDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationInventoryDevices(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationInventoryDevices(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationInventoryDevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationInventoryDevices: {ex}")
            return {"error": str(ex)}

    def getOrganizationInventoryDevicesSwapsBulk(self, organizationId, id) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationInventoryDevicesSwapsBulk(organizationId, id)
        except APIError as e:
            logging.error(f"API Error in getOrganizationInventoryDevicesSwapsBulk: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationInventoryDevicesSwapsBulk: {ex}")
            return {"error": str(ex)}

    def getOrganizationInventoryOnboardingCloudMonitoringImports(self, organizationId, importIds) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationInventoryOnboardingCloudMonitoringImports(organizationId, importIds)
        except APIError as e:
            logging.error(f"API Error in getOrganizationInventoryOnboardingCloudMonitoringImports: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationInventoryOnboardingCloudMonitoringImports: {ex}")
            return {"error": str(ex)}

    def getOrganizationInventoryOnboardingCloudMonitoringNetworks(self, organizationId, deviceType, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationInventoryOnboardingCloudMonitoringNetworks(organizationId, deviceType, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationInventoryOnboardingCloudMonitoringNetworks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationInventoryOnboardingCloudMonitoringNetworks: {ex}")
            return {"error": str(ex)}

    def getOrganizationLicense(self, organizationId, licenseId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationLicense(organizationId, licenseId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationLicense: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationLicense: {ex}")
            return {"error": str(ex)}

    def getOrganizationLicenses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationLicenses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationLicenses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationLicenses: {ex}")
            return {"error": str(ex)}

    def getOrganizationLicensesOverview(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationLicensesOverview(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationLicensesOverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationLicensesOverview: {ex}")
            return {"error": str(ex)}

    def getOrganizationLicensingCotermLicenses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationLicensingCotermLicenses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationLicensingCotermLicenses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationLicensingCotermLicenses: {ex}")
            return {"error": str(ex)}

    def getOrganizationLoginSecurity(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationLoginSecurity(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationLoginSecurity: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationLoginSecurity: {ex}")
            return {"error": str(ex)}

    def getOrganizationNetworks(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationNetworks(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationNetworks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationNetworks: {ex}")
            return {"error": str(ex)}

    def getOrganizationOpenapiSpec(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationOpenapiSpec(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationOpenapiSpec: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationOpenapiSpec: {ex}")
            return {"error": str(ex)}

    def getOrganizationPolicyObject(self, organizationId, policyObjectId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationPolicyObject(organizationId, policyObjectId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationPolicyObject: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationPolicyObject: {ex}")
            return {"error": str(ex)}

    def getOrganizationPolicyObjects(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationPolicyObjects(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationPolicyObjects: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationPolicyObjects: {ex}")
            return {"error": str(ex)}

    def getOrganizationPolicyObjectsGroup(self, organizationId, policyObjectGroupId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationPolicyObjectsGroup(organizationId, policyObjectGroupId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationPolicyObjectsGroup: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationPolicyObjectsGroup: {ex}")
            return {"error": str(ex)}

    def getOrganizationPolicyObjectsGroups(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationPolicyObjectsGroups(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationPolicyObjectsGroups: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationPolicyObjectsGroups: {ex}")
            return {"error": str(ex)}

    def getOrganizationSaml(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSaml(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSaml: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSaml: {ex}")
            return {"error": str(ex)}

    def getOrganizationSamlIdp(self, organizationId, idpId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSamlIdp(organizationId, idpId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSamlIdp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSamlIdp: {ex}")
            return {"error": str(ex)}

    def getOrganizationSamlIdps(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSamlIdps(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSamlIdps: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSamlIdps: {ex}")
            return {"error": str(ex)}

    def getOrganizationSamlRole(self, organizationId, samlRoleId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSamlRole(organizationId, samlRoleId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSamlRole: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSamlRole: {ex}")
            return {"error": str(ex)}

    def getOrganizationSamlRoles(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSamlRoles(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSamlRoles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSamlRoles: {ex}")
            return {"error": str(ex)}

    def getOrganizationSensorReadingsHistory(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSensorReadingsHistory(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSensorReadingsHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSensorReadingsHistory: {ex}")
            return {"error": str(ex)}

    def getOrganizationSensorReadingsLatest(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSensorReadingsLatest(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSensorReadingsLatest: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSensorReadingsLatest: {ex}")
            return {"error": str(ex)}

    def getOrganizationSmAdminsRole(self, organizationId, roleId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSmAdminsRole(organizationId, roleId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSmAdminsRole: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSmAdminsRole: {ex}")
            return {"error": str(ex)}

    def getOrganizationSmAdminsRoles(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSmAdminsRoles(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSmAdminsRoles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSmAdminsRoles: {ex}")
            return {"error": str(ex)}

    def getOrganizationSmApnsCert(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSmApnsCert(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSmApnsCert: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSmApnsCert: {ex}")
            return {"error": str(ex)}

    def getOrganizationSmSentryPoliciesAssignmentsByNetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSmSentryPoliciesAssignmentsByNetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSmSentryPoliciesAssignmentsByNetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSmSentryPoliciesAssignmentsByNetwork: {ex}")
            return {"error": str(ex)}

    def getOrganizationSmVppAccount(self, organizationId, vppAccountId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSmVppAccount(organizationId, vppAccountId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSmVppAccount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSmVppAccount: {ex}")
            return {"error": str(ex)}

    def getOrganizationSmVppAccounts(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSmVppAccounts(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSmVppAccounts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSmVppAccounts: {ex}")
            return {"error": str(ex)}

    def getOrganizationSnmp(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSnmp(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSnmp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSnmp: {ex}")
            return {"error": str(ex)}

    def getOrganizationSplashAsset(self, organizationId, id) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSplashAsset(organizationId, id)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSplashAsset: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSplashAsset: {ex}")
            return {"error": str(ex)}

    def getOrganizationSplashThemes(self, organizationId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSplashThemes(organizationId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSplashThemes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSplashThemes: {ex}")
            return {"error": str(ex)}

    def getOrganizationSummarySwitchPowerHistory(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSummarySwitchPowerHistory(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSummarySwitchPowerHistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSummarySwitchPowerHistory: {ex}")
            return {"error": str(ex)}

    def getOrganizationSummaryTopAppliancesByUtilization(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSummaryTopAppliancesByUtilization(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSummaryTopAppliancesByUtilization: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSummaryTopAppliancesByUtilization: {ex}")
            return {"error": str(ex)}

    def getOrganizationSummaryTopApplicationsByUsage(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSummaryTopApplicationsByUsage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSummaryTopApplicationsByUsage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSummaryTopApplicationsByUsage: {ex}")
            return {"error": str(ex)}

    def getOrganizationSummaryTopApplicationsCategoriesByUsage(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSummaryTopApplicationsCategoriesByUsage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSummaryTopApplicationsCategoriesByUsage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSummaryTopApplicationsCategoriesByUsage: {ex}")
            return {"error": str(ex)}

    def getOrganizationSummaryTopClientsByUsage(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSummaryTopClientsByUsage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSummaryTopClientsByUsage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSummaryTopClientsByUsage: {ex}")
            return {"error": str(ex)}

    def getOrganizationSummaryTopClientsManufacturersByUsage(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSummaryTopClientsManufacturersByUsage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSummaryTopClientsManufacturersByUsage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSummaryTopClientsManufacturersByUsage: {ex}")
            return {"error": str(ex)}

    def getOrganizationSummaryTopDevicesByUsage(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSummaryTopDevicesByUsage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSummaryTopDevicesByUsage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSummaryTopDevicesByUsage: {ex}")
            return {"error": str(ex)}

    def getOrganizationSummaryTopDevicesModelsByUsage(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSummaryTopDevicesModelsByUsage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSummaryTopDevicesModelsByUsage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSummaryTopDevicesModelsByUsage: {ex}")
            return {"error": str(ex)}

    def getOrganizationSummaryTopNetworksByStatus(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSummaryTopNetworksByStatus(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSummaryTopNetworksByStatus: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSummaryTopNetworksByStatus: {ex}")
            return {"error": str(ex)}

    def getOrganizationSummaryTopSsidsByUsage(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSummaryTopSsidsByUsage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSummaryTopSsidsByUsage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSummaryTopSsidsByUsage: {ex}")
            return {"error": str(ex)}

    def getOrganizationSummaryTopSwitchesByEnergyUsage(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSummaryTopSwitchesByEnergyUsage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSummaryTopSwitchesByEnergyUsage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSummaryTopSwitchesByEnergyUsage: {ex}")
            return {"error": str(ex)}

    def getOrganizationSwitchPortsBySwitch(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSwitchPortsBySwitch(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSwitchPortsBySwitch: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSwitchPortsBySwitch: {ex}")
            return {"error": str(ex)}

    def getOrganizationSwitchPortsClientsOverviewByDevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSwitchPortsClientsOverviewByDevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSwitchPortsClientsOverviewByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSwitchPortsClientsOverviewByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationSwitchPortsOverview(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSwitchPortsOverview(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSwitchPortsOverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSwitchPortsOverview: {ex}")
            return {"error": str(ex)}

    def getOrganizationSwitchPortsStatusesBySwitch(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSwitchPortsStatusesBySwitch(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSwitchPortsStatusesBySwitch: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSwitchPortsStatusesBySwitch: {ex}")
            return {"error": str(ex)}

    def getOrganizationSwitchPortsTopologyDiscoveryByDevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationSwitchPortsTopologyDiscoveryByDevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationSwitchPortsTopologyDiscoveryByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationSwitchPortsTopologyDiscoveryByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationUplinksStatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationUplinksStatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationUplinksStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationUplinksStatuses: {ex}")
            return {"error": str(ex)}

    def getOrganizationWebhooksAlertTypes(self, organizationId, **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWebhooksAlertTypes(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWebhooksAlertTypes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWebhooksAlertTypes: {ex}")
            return {"error": str(ex)}

    def getOrganizationWebhooksCallbacksStatus(self, organizationId, callbackId) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWebhooksCallbacksStatus(organizationId, callbackId)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWebhooksCallbacksStatus: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWebhooksCallbacksStatus: {ex}")
            return {"error": str(ex)}

    def getOrganizationWebhooksLogs(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWebhooksLogs(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWebhooksLogs: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWebhooksLogs: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessAirMarshalRules(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessAirMarshalRules(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessAirMarshalRules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessAirMarshalRules: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessAirMarshalSettingsByNetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessAirMarshalSettingsByNetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessAirMarshalSettingsByNetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessAirMarshalSettingsByNetwork: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessClientsOverviewByDevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessClientsOverviewByDevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessClientsOverviewByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessClientsOverviewByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessDevicesChannelUtilizationByDevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessDevicesChannelUtilizationByDevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessDevicesChannelUtilizationByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessDevicesChannelUtilizationByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessDevicesChannelUtilizationByNetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessDevicesChannelUtilizationByNetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessDevicesChannelUtilizationByNetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessDevicesChannelUtilizationByNetwork: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessDevicesEthernetStatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessDevicesEthernetStatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessDevicesEthernetStatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessDevicesEthernetStatuses: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessDevicesPacketLossByClient(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessDevicesPacketLossByClient(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessDevicesPacketLossByClient: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessDevicesPacketLossByClient: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessDevicesPacketLossByDevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessDevicesPacketLossByDevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessDevicesPacketLossByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessDevicesPacketLossByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessDevicesPacketLossByNetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessDevicesPacketLossByNetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessDevicesPacketLossByNetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessDevicesPacketLossByNetwork: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessDevicesWirelessControllersByDevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessDevicesWirelessControllersByDevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessDevicesWirelessControllersByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessDevicesWirelessControllersByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessRfProfilesAssignmentsByDevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessRfProfilesAssignmentsByDevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessRfProfilesAssignmentsByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessRfProfilesAssignmentsByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizationWirelessSsidsStatusesByDevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizationWirelessSsidsStatusesByDevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizationWirelessSsidsStatusesByDevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizationWirelessSsidsStatusesByDevice: {ex}")
            return {"error": str(ex)}

    def getOrganizations(self, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        try:
            return self.dashboard.getOrganizations(total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getOrganizations: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getOrganizations: {ex}")
            return {"error": str(ex)}

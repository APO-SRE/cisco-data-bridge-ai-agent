################################################################################
## cisco_integrations/cisco_meraki_sdk_client.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

import logging

from meraki.exceptions import APIError

from typing import Dict, Any


class MerakiSDKClientCustom:


    def __init__(self, dashboard):

        """Initialize with a meraki.DashboardAPI client instance."""

        self.dashboard = dashboard


    def getadministeredidentitiesme(self, ) -> Dict[str, Any]:
        """Auto-generated method for 'getadministeredidentitiesme'.
        Calls 'self.dashboard.getadministeredidentitiesme' with the same parameters.
        
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getadministeredidentitiesme()
        except APIError as e:
            logging.error(f"API Error in getadministeredidentitiesme: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getadministeredidentitiesme: {ex}")
            return {"error": str(ex)}

    def getadministeredidentitiesmeapikeys(self, ) -> Dict[str, Any]:
        """Auto-generated method for 'getadministeredidentitiesmeapikeys'.
        Calls 'self.dashboard.getadministeredidentitiesmeapikeys' with the same parameters.
        
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getadministeredidentitiesmeapikeys()
        except APIError as e:
            logging.error(f"API Error in getadministeredidentitiesmeapikeys: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getadministeredidentitiesmeapikeys: {ex}")
            return {"error": str(ex)}

    def getadministeredlicensingsubscriptionentitlements(self, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getadministeredlicensingsubscriptionentitlements'.
        Calls 'self.dashboard.getadministeredlicensingsubscriptionentitlements' with the same parameters.
        
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getadministeredlicensingsubscriptionentitlements(**kwargs)
        except APIError as e:
            logging.error(f"API Error in getadministeredlicensingsubscriptionentitlements: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getadministeredlicensingsubscriptionentitlements: {ex}")
            return {"error": str(ex)}

    def getadministeredlicensingsubscriptionsubscriptions(self, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getadministeredlicensingsubscriptionsubscriptions'.
        Calls 'self.dashboard.getadministeredlicensingsubscriptionsubscriptions' with the same parameters.
        
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getadministeredlicensingsubscriptionsubscriptions(total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getadministeredlicensingsubscriptionsubscriptions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getadministeredlicensingsubscriptionsubscriptions: {ex}")
            return {"error": str(ex)}

    def getadministeredlicensingsubscriptionsubscriptionscompliancestatuses(self, organizationIds, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getadministeredlicensingsubscriptionsubscriptionscompliancestatuses'.
        Calls 'self.dashboard.getadministeredlicensingsubscriptionsubscriptionscompliancestatuses' with the same parameters.
        
        :param organizationIds: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getadministeredlicensingsubscriptionsubscriptionscompliancestatuses(organizationIds, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getadministeredlicensingsubscriptionsubscriptionscompliancestatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getadministeredlicensingsubscriptionsubscriptionscompliancestatuses: {ex}")
            return {"error": str(ex)}

    def getdevice(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevice'.
        Calls 'self.dashboard.getdevice' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevice(serial)
        except APIError as e:
            logging.error(f"API Error in getdevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevice: {ex}")
            return {"error": str(ex)}

    def getdeviceappliancedhcpsubnets(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceappliancedhcpsubnets'.
        Calls 'self.dashboard.getdeviceappliancedhcpsubnets' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceappliancedhcpsubnets(serial)
        except APIError as e:
            logging.error(f"API Error in getdeviceappliancedhcpsubnets: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceappliancedhcpsubnets: {ex}")
            return {"error": str(ex)}

    def getdeviceapplianceperformance(self, serial, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceapplianceperformance'.
        Calls 'self.dashboard.getdeviceapplianceperformance' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceapplianceperformance(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdeviceapplianceperformance: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceapplianceperformance: {ex}")
            return {"error": str(ex)}

    def getdeviceapplianceprefixesdelegated(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceapplianceprefixesdelegated'.
        Calls 'self.dashboard.getdeviceapplianceprefixesdelegated' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceapplianceprefixesdelegated(serial)
        except APIError as e:
            logging.error(f"API Error in getdeviceapplianceprefixesdelegated: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceapplianceprefixesdelegated: {ex}")
            return {"error": str(ex)}

    def getdeviceapplianceprefixesdelegatedvlanassignments(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceapplianceprefixesdelegatedvlanassignments'.
        Calls 'self.dashboard.getdeviceapplianceprefixesdelegatedvlanassignments' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceapplianceprefixesdelegatedvlanassignments(serial)
        except APIError as e:
            logging.error(f"API Error in getdeviceapplianceprefixesdelegatedvlanassignments: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceapplianceprefixesdelegatedvlanassignments: {ex}")
            return {"error": str(ex)}

    def getdeviceapplianceradiosettings(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceapplianceradiosettings'.
        Calls 'self.dashboard.getdeviceapplianceradiosettings' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceapplianceradiosettings(serial)
        except APIError as e:
            logging.error(f"API Error in getdeviceapplianceradiosettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceapplianceradiosettings: {ex}")
            return {"error": str(ex)}

    def getdeviceapplianceuplinkssettings(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceapplianceuplinkssettings'.
        Calls 'self.dashboard.getdeviceapplianceuplinkssettings' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceapplianceuplinkssettings(serial)
        except APIError as e:
            logging.error(f"API Error in getdeviceapplianceuplinkssettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceapplianceuplinkssettings: {ex}")
            return {"error": str(ex)}

    def getdevicecameraanalyticslive(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecameraanalyticslive'.
        Calls 'self.dashboard.getdevicecameraanalyticslive' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecameraanalyticslive(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicecameraanalyticslive: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecameraanalyticslive: {ex}")
            return {"error": str(ex)}

    def getdevicecameraanalyticsoverview(self, serial, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecameraanalyticsoverview'.
        Calls 'self.dashboard.getdevicecameraanalyticsoverview' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecameraanalyticsoverview(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdevicecameraanalyticsoverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecameraanalyticsoverview: {ex}")
            return {"error": str(ex)}

    def getdevicecameraanalyticsrecent(self, serial, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecameraanalyticsrecent'.
        Calls 'self.dashboard.getdevicecameraanalyticsrecent' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecameraanalyticsrecent(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdevicecameraanalyticsrecent: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecameraanalyticsrecent: {ex}")
            return {"error": str(ex)}

    def getdevicecameraanalyticszonehistory(self, serial, zoneId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecameraanalyticszonehistory'.
        Calls 'self.dashboard.getdevicecameraanalyticszonehistory' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param zoneId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecameraanalyticszonehistory(serial, zoneId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdevicecameraanalyticszonehistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecameraanalyticszonehistory: {ex}")
            return {"error": str(ex)}

    def getdevicecameraanalyticszones(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecameraanalyticszones'.
        Calls 'self.dashboard.getdevicecameraanalyticszones' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecameraanalyticszones(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicecameraanalyticszones: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecameraanalyticszones: {ex}")
            return {"error": str(ex)}

    def getdevicecameracustomanalytics(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecameracustomanalytics'.
        Calls 'self.dashboard.getdevicecameracustomanalytics' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecameracustomanalytics(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicecameracustomanalytics: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecameracustomanalytics: {ex}")
            return {"error": str(ex)}

    def getdevicecameraqualityandretention(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecameraqualityandretention'.
        Calls 'self.dashboard.getdevicecameraqualityandretention' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecameraqualityandretention(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicecameraqualityandretention: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecameraqualityandretention: {ex}")
            return {"error": str(ex)}

    def getdevicecamerasense(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecamerasense'.
        Calls 'self.dashboard.getdevicecamerasense' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecamerasense(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicecamerasense: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecamerasense: {ex}")
            return {"error": str(ex)}

    def getdevicecamerasenseobjectdetectionmodels(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecamerasenseobjectdetectionmodels'.
        Calls 'self.dashboard.getdevicecamerasenseobjectdetectionmodels' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecamerasenseobjectdetectionmodels(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicecamerasenseobjectdetectionmodels: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecamerasenseobjectdetectionmodels: {ex}")
            return {"error": str(ex)}

    def getdevicecameravideolink(self, serial, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecameravideolink'.
        Calls 'self.dashboard.getdevicecameravideolink' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecameravideolink(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdevicecameravideolink: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecameravideolink: {ex}")
            return {"error": str(ex)}

    def getdevicecameravideosettings(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecameravideosettings'.
        Calls 'self.dashboard.getdevicecameravideosettings' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecameravideosettings(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicecameravideosettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecameravideosettings: {ex}")
            return {"error": str(ex)}

    def getdevicecamerawirelessprofiles(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecamerawirelessprofiles'.
        Calls 'self.dashboard.getdevicecamerawirelessprofiles' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecamerawirelessprofiles(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicecamerawirelessprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecamerawirelessprofiles: {ex}")
            return {"error": str(ex)}

    def getdevicecellulargatewaylan(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecellulargatewaylan'.
        Calls 'self.dashboard.getdevicecellulargatewaylan' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecellulargatewaylan(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicecellulargatewaylan: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecellulargatewaylan: {ex}")
            return {"error": str(ex)}

    def getdevicecellulargatewayportforwardingrules(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecellulargatewayportforwardingrules'.
        Calls 'self.dashboard.getdevicecellulargatewayportforwardingrules' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecellulargatewayportforwardingrules(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicecellulargatewayportforwardingrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecellulargatewayportforwardingrules: {ex}")
            return {"error": str(ex)}

    def getdevicecellularsims(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicecellularsims'.
        Calls 'self.dashboard.getdevicecellularsims' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicecellularsims(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicecellularsims: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicecellularsims: {ex}")
            return {"error": str(ex)}

    def getdeviceclients(self, serial, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceclients'.
        Calls 'self.dashboard.getdeviceclients' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceclients(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdeviceclients: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceclients: {ex}")
            return {"error": str(ex)}

    def getdevicelivetoolsarptable(self, serial, arpTableId) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicelivetoolsarptable'.
        Calls 'self.dashboard.getdevicelivetoolsarptable' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param arpTableId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicelivetoolsarptable(serial, arpTableId)
        except APIError as e:
            logging.error(f"API Error in getdevicelivetoolsarptable: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicelivetoolsarptable: {ex}")
            return {"error": str(ex)}

    def getdevicelivetoolscabletest(self, serial, id) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicelivetoolscabletest'.
        Calls 'self.dashboard.getdevicelivetoolscabletest' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicelivetoolscabletest(serial, id)
        except APIError as e:
            logging.error(f"API Error in getdevicelivetoolscabletest: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicelivetoolscabletest: {ex}")
            return {"error": str(ex)}

    def getdevicelivetoolsledsblink(self, serial, ledsBlinkId) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicelivetoolsledsblink'.
        Calls 'self.dashboard.getdevicelivetoolsledsblink' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param ledsBlinkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicelivetoolsledsblink(serial, ledsBlinkId)
        except APIError as e:
            logging.error(f"API Error in getdevicelivetoolsledsblink: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicelivetoolsledsblink: {ex}")
            return {"error": str(ex)}

    def getdevicelivetoolsping(self, serial, id) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicelivetoolsping'.
        Calls 'self.dashboard.getdevicelivetoolsping' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicelivetoolsping(serial, id)
        except APIError as e:
            logging.error(f"API Error in getdevicelivetoolsping: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicelivetoolsping: {ex}")
            return {"error": str(ex)}

    def getdevicelivetoolspingdevice(self, serial, id) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicelivetoolspingdevice'.
        Calls 'self.dashboard.getdevicelivetoolspingdevice' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicelivetoolspingdevice(serial, id)
        except APIError as e:
            logging.error(f"API Error in getdevicelivetoolspingdevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicelivetoolspingdevice: {ex}")
            return {"error": str(ex)}

    def getdevicelivetoolsthroughputtest(self, serial, throughputTestId) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicelivetoolsthroughputtest'.
        Calls 'self.dashboard.getdevicelivetoolsthroughputtest' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param throughputTestId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicelivetoolsthroughputtest(serial, throughputTestId)
        except APIError as e:
            logging.error(f"API Error in getdevicelivetoolsthroughputtest: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicelivetoolsthroughputtest: {ex}")
            return {"error": str(ex)}

    def getdevicelivetoolswakeonlan(self, serial, wakeOnLanId) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicelivetoolswakeonlan'.
        Calls 'self.dashboard.getdevicelivetoolswakeonlan' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param wakeOnLanId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicelivetoolswakeonlan(serial, wakeOnLanId)
        except APIError as e:
            logging.error(f"API Error in getdevicelivetoolswakeonlan: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicelivetoolswakeonlan: {ex}")
            return {"error": str(ex)}

    def getdevicelldpcdp(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicelldpcdp'.
        Calls 'self.dashboard.getdevicelldpcdp' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicelldpcdp(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicelldpcdp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicelldpcdp: {ex}")
            return {"error": str(ex)}

    def getdevicelossandlatencyhistory(self, serial, ip, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicelossandlatencyhistory'.
        Calls 'self.dashboard.getdevicelossandlatencyhistory' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param ip: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicelossandlatencyhistory(serial, ip, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdevicelossandlatencyhistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicelossandlatencyhistory: {ex}")
            return {"error": str(ex)}

    def getdevicemanagementinterface(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicemanagementinterface'.
        Calls 'self.dashboard.getdevicemanagementinterface' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicemanagementinterface(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicemanagementinterface: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicemanagementinterface: {ex}")
            return {"error": str(ex)}

    def getdevicesensorcommand(self, serial, commandId) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicesensorcommand'.
        Calls 'self.dashboard.getdevicesensorcommand' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param commandId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicesensorcommand(serial, commandId)
        except APIError as e:
            logging.error(f"API Error in getdevicesensorcommand: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicesensorcommand: {ex}")
            return {"error": str(ex)}

    def getdevicesensorcommands(self, serial, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicesensorcommands'.
        Calls 'self.dashboard.getdevicesensorcommands' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicesensorcommands(serial, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdevicesensorcommands: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicesensorcommands: {ex}")
            return {"error": str(ex)}

    def getdevicesensorrelationships(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicesensorrelationships'.
        Calls 'self.dashboard.getdevicesensorrelationships' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicesensorrelationships(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicesensorrelationships: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicesensorrelationships: {ex}")
            return {"error": str(ex)}

    def getdeviceswitchport(self, serial, portId) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceswitchport'.
        Calls 'self.dashboard.getdeviceswitchport' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param portId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceswitchport(serial, portId)
        except APIError as e:
            logging.error(f"API Error in getdeviceswitchport: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceswitchport: {ex}")
            return {"error": str(ex)}

    def getdeviceswitchports(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceswitchports'.
        Calls 'self.dashboard.getdeviceswitchports' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceswitchports(serial)
        except APIError as e:
            logging.error(f"API Error in getdeviceswitchports: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceswitchports: {ex}")
            return {"error": str(ex)}

    def getdeviceswitchportsstatuses(self, serial, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceswitchportsstatuses'.
        Calls 'self.dashboard.getdeviceswitchportsstatuses' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceswitchportsstatuses(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdeviceswitchportsstatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceswitchportsstatuses: {ex}")
            return {"error": str(ex)}

    def getdeviceswitchportsstatusespackets(self, serial, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceswitchportsstatusespackets'.
        Calls 'self.dashboard.getdeviceswitchportsstatusespackets' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceswitchportsstatusespackets(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdeviceswitchportsstatusespackets: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceswitchportsstatusespackets: {ex}")
            return {"error": str(ex)}

    def getdeviceswitchroutinginterface(self, serial, interfaceId) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceswitchroutinginterface'.
        Calls 'self.dashboard.getdeviceswitchroutinginterface' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param interfaceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceswitchroutinginterface(serial, interfaceId)
        except APIError as e:
            logging.error(f"API Error in getdeviceswitchroutinginterface: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceswitchroutinginterface: {ex}")
            return {"error": str(ex)}

    def getdeviceswitchroutinginterfacedhcp(self, serial, interfaceId) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceswitchroutinginterfacedhcp'.
        Calls 'self.dashboard.getdeviceswitchroutinginterfacedhcp' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param interfaceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceswitchroutinginterfacedhcp(serial, interfaceId)
        except APIError as e:
            logging.error(f"API Error in getdeviceswitchroutinginterfacedhcp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceswitchroutinginterfacedhcp: {ex}")
            return {"error": str(ex)}

    def getdeviceswitchroutinginterfaces(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceswitchroutinginterfaces'.
        Calls 'self.dashboard.getdeviceswitchroutinginterfaces' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceswitchroutinginterfaces(serial)
        except APIError as e:
            logging.error(f"API Error in getdeviceswitchroutinginterfaces: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceswitchroutinginterfaces: {ex}")
            return {"error": str(ex)}

    def getdeviceswitchroutingstaticroute(self, serial, staticRouteId) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceswitchroutingstaticroute'.
        Calls 'self.dashboard.getdeviceswitchroutingstaticroute' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param staticRouteId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceswitchroutingstaticroute(serial, staticRouteId)
        except APIError as e:
            logging.error(f"API Error in getdeviceswitchroutingstaticroute: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceswitchroutingstaticroute: {ex}")
            return {"error": str(ex)}

    def getdeviceswitchroutingstaticroutes(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceswitchroutingstaticroutes'.
        Calls 'self.dashboard.getdeviceswitchroutingstaticroutes' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceswitchroutingstaticroutes(serial)
        except APIError as e:
            logging.error(f"API Error in getdeviceswitchroutingstaticroutes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceswitchroutingstaticroutes: {ex}")
            return {"error": str(ex)}

    def getdeviceswitchwarmspare(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdeviceswitchwarmspare'.
        Calls 'self.dashboard.getdeviceswitchwarmspare' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdeviceswitchwarmspare(serial)
        except APIError as e:
            logging.error(f"API Error in getdeviceswitchwarmspare: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdeviceswitchwarmspare: {ex}")
            return {"error": str(ex)}

    def getdevicewirelessbluetoothsettings(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicewirelessbluetoothsettings'.
        Calls 'self.dashboard.getdevicewirelessbluetoothsettings' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicewirelessbluetoothsettings(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicewirelessbluetoothsettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicewirelessbluetoothsettings: {ex}")
            return {"error": str(ex)}

    def getdevicewirelessconnectionstats(self, serial, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicewirelessconnectionstats'.
        Calls 'self.dashboard.getdevicewirelessconnectionstats' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicewirelessconnectionstats(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdevicewirelessconnectionstats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicewirelessconnectionstats: {ex}")
            return {"error": str(ex)}

    def getdevicewirelesselectronicshelflabel(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicewirelesselectronicshelflabel'.
        Calls 'self.dashboard.getdevicewirelesselectronicshelflabel' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicewirelesselectronicshelflabel(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicewirelesselectronicshelflabel: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicewirelesselectronicshelflabel: {ex}")
            return {"error": str(ex)}

    def getdevicewirelesslatencystats(self, serial, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicewirelesslatencystats'.
        Calls 'self.dashboard.getdevicewirelesslatencystats' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicewirelesslatencystats(serial, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getdevicewirelesslatencystats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicewirelesslatencystats: {ex}")
            return {"error": str(ex)}

    def getdevicewirelessradiosettings(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicewirelessradiosettings'.
        Calls 'self.dashboard.getdevicewirelessradiosettings' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicewirelessradiosettings(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicewirelessradiosettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicewirelessradiosettings: {ex}")
            return {"error": str(ex)}

    def getdevicewirelessstatus(self, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getdevicewirelessstatus'.
        Calls 'self.dashboard.getdevicewirelessstatus' with the same parameters.
        
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getdevicewirelessstatus(serial)
        except APIError as e:
            logging.error(f"API Error in getdevicewirelessstatus: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getdevicewirelessstatus: {ex}")
            return {"error": str(ex)}

    def getnetwork(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetwork'.
        Calls 'self.dashboard.getnetwork' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetwork(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetwork: {ex}")
            return {"error": str(ex)}

    def getnetworkalertshistory(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkalertshistory'.
        Calls 'self.dashboard.getnetworkalertshistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkalertshistory(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkalertshistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkalertshistory: {ex}")
            return {"error": str(ex)}

    def getnetworkalertssettings(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkalertssettings'.
        Calls 'self.dashboard.getnetworkalertssettings' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkalertssettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkalertssettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkalertssettings: {ex}")
            return {"error": str(ex)}

    def getnetworkapplianceclientsecurityevents(self, networkId, clientId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkapplianceclientsecurityevents'.
        Calls 'self.dashboard.getnetworkapplianceclientsecurityevents' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clientId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkapplianceclientsecurityevents(networkId, clientId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkapplianceclientsecurityevents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkapplianceclientsecurityevents: {ex}")
            return {"error": str(ex)}

    def getnetworkapplianceconnectivitymonitoringdestinations(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkapplianceconnectivitymonitoringdestinations'.
        Calls 'self.dashboard.getnetworkapplianceconnectivitymonitoringdestinations' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkapplianceconnectivitymonitoringdestinations(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkapplianceconnectivitymonitoringdestinations: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkapplianceconnectivitymonitoringdestinations: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancecontentfiltering(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancecontentfiltering'.
        Calls 'self.dashboard.getnetworkappliancecontentfiltering' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancecontentfiltering(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancecontentfiltering: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancecontentfiltering: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancecontentfilteringcategories(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancecontentfilteringcategories'.
        Calls 'self.dashboard.getnetworkappliancecontentfilteringcategories' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancecontentfilteringcategories(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancecontentfilteringcategories: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancecontentfilteringcategories: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewallcellularfirewallrules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewallcellularfirewallrules'.
        Calls 'self.dashboard.getnetworkappliancefirewallcellularfirewallrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewallcellularfirewallrules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewallcellularfirewallrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewallcellularfirewallrules: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewallfirewalledservice(self, networkId, service) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewallfirewalledservice'.
        Calls 'self.dashboard.getnetworkappliancefirewallfirewalledservice' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param service: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewallfirewalledservice(networkId, service)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewallfirewalledservice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewallfirewalledservice: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewallfirewalledservices(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewallfirewalledservices'.
        Calls 'self.dashboard.getnetworkappliancefirewallfirewalledservices' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewallfirewalledservices(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewallfirewalledservices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewallfirewalledservices: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewallinboundcellularfirewallrules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewallinboundcellularfirewallrules'.
        Calls 'self.dashboard.getnetworkappliancefirewallinboundcellularfirewallrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewallinboundcellularfirewallrules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewallinboundcellularfirewallrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewallinboundcellularfirewallrules: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewallinboundfirewallrules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewallinboundfirewallrules'.
        Calls 'self.dashboard.getnetworkappliancefirewallinboundfirewallrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewallinboundfirewallrules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewallinboundfirewallrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewallinboundfirewallrules: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewalll3firewallrules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewalll3firewallrules'.
        Calls 'self.dashboard.getnetworkappliancefirewalll3firewallrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewalll3firewallrules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewalll3firewallrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewalll3firewallrules: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewalll7firewallrules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewalll7firewallrules'.
        Calls 'self.dashboard.getnetworkappliancefirewalll7firewallrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewalll7firewallrules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewalll7firewallrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewalll7firewallrules: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewalll7firewallrulesapplicationcategories(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewalll7firewallrulesapplicationcategories'.
        Calls 'self.dashboard.getnetworkappliancefirewalll7firewallrulesapplicationcategories' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewalll7firewallrulesapplicationcategories(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewalll7firewallrulesapplicationcategories: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewalll7firewallrulesapplicationcategories: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewallonetomanynatrules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewallonetomanynatrules'.
        Calls 'self.dashboard.getnetworkappliancefirewallonetomanynatrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewallonetomanynatrules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewallonetomanynatrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewallonetomanynatrules: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewallonetoonenatrules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewallonetoonenatrules'.
        Calls 'self.dashboard.getnetworkappliancefirewallonetoonenatrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewallonetoonenatrules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewallonetoonenatrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewallonetoonenatrules: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewallportforwardingrules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewallportforwardingrules'.
        Calls 'self.dashboard.getnetworkappliancefirewallportforwardingrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewallportforwardingrules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewallportforwardingrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewallportforwardingrules: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancefirewallsettings(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancefirewallsettings'.
        Calls 'self.dashboard.getnetworkappliancefirewallsettings' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancefirewallsettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancefirewallsettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancefirewallsettings: {ex}")
            return {"error": str(ex)}

    def getnetworkapplianceport(self, networkId, portId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkapplianceport'.
        Calls 'self.dashboard.getnetworkapplianceport' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param portId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkapplianceport(networkId, portId)
        except APIError as e:
            logging.error(f"API Error in getnetworkapplianceport: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkapplianceport: {ex}")
            return {"error": str(ex)}

    def getnetworkapplianceports(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkapplianceports'.
        Calls 'self.dashboard.getnetworkapplianceports' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkapplianceports(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkapplianceports: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkapplianceports: {ex}")
            return {"error": str(ex)}

    def getnetworkapplianceprefixesdelegatedstatic(self, networkId, staticDelegatedPrefixId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkapplianceprefixesdelegatedstatic'.
        Calls 'self.dashboard.getnetworkapplianceprefixesdelegatedstatic' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param staticDelegatedPrefixId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkapplianceprefixesdelegatedstatic(networkId, staticDelegatedPrefixId)
        except APIError as e:
            logging.error(f"API Error in getnetworkapplianceprefixesdelegatedstatic: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkapplianceprefixesdelegatedstatic: {ex}")
            return {"error": str(ex)}

    def getnetworkapplianceprefixesdelegatedstatics(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkapplianceprefixesdelegatedstatics'.
        Calls 'self.dashboard.getnetworkapplianceprefixesdelegatedstatics' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkapplianceprefixesdelegatedstatics(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkapplianceprefixesdelegatedstatics: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkapplianceprefixesdelegatedstatics: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancerfprofile(self, networkId, rfProfileId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancerfprofile'.
        Calls 'self.dashboard.getnetworkappliancerfprofile' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param rfProfileId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancerfprofile(networkId, rfProfileId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancerfprofile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancerfprofile: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancerfprofiles(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancerfprofiles'.
        Calls 'self.dashboard.getnetworkappliancerfprofiles' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancerfprofiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancerfprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancerfprofiles: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancesecurityevents(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancesecurityevents'.
        Calls 'self.dashboard.getnetworkappliancesecurityevents' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancesecurityevents(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancesecurityevents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancesecurityevents: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancesecurityintrusion(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancesecurityintrusion'.
        Calls 'self.dashboard.getnetworkappliancesecurityintrusion' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancesecurityintrusion(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancesecurityintrusion: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancesecurityintrusion: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancesecuritymalware(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancesecuritymalware'.
        Calls 'self.dashboard.getnetworkappliancesecuritymalware' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancesecuritymalware(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancesecuritymalware: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancesecuritymalware: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancesettings(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancesettings'.
        Calls 'self.dashboard.getnetworkappliancesettings' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancesettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancesettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancesettings: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancesinglelan(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancesinglelan'.
        Calls 'self.dashboard.getnetworkappliancesinglelan' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancesinglelan(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancesinglelan: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancesinglelan: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancessid(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancessid'.
        Calls 'self.dashboard.getnetworkappliancessid' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancessid(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancessid: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancessid: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancessids(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancessids'.
        Calls 'self.dashboard.getnetworkappliancessids' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancessids(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancessids: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancessids: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancestaticroute(self, networkId, staticRouteId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancestaticroute'.
        Calls 'self.dashboard.getnetworkappliancestaticroute' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param staticRouteId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancestaticroute(networkId, staticRouteId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancestaticroute: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancestaticroute: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancestaticroutes(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancestaticroutes'.
        Calls 'self.dashboard.getnetworkappliancestaticroutes' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancestaticroutes(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancestaticroutes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancestaticroutes: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancetrafficshaping(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancetrafficshaping'.
        Calls 'self.dashboard.getnetworkappliancetrafficshaping' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancetrafficshaping(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancetrafficshaping: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancetrafficshaping: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancetrafficshapingcustomperformanceclass(self, networkId, customPerformanceClassId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancetrafficshapingcustomperformanceclass'.
        Calls 'self.dashboard.getnetworkappliancetrafficshapingcustomperformanceclass' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param customPerformanceClassId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancetrafficshapingcustomperformanceclass(networkId, customPerformanceClassId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancetrafficshapingcustomperformanceclass: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancetrafficshapingcustomperformanceclass: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancetrafficshapingcustomperformanceclasses(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancetrafficshapingcustomperformanceclasses'.
        Calls 'self.dashboard.getnetworkappliancetrafficshapingcustomperformanceclasses' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancetrafficshapingcustomperformanceclasses(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancetrafficshapingcustomperformanceclasses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancetrafficshapingcustomperformanceclasses: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancetrafficshapingrules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancetrafficshapingrules'.
        Calls 'self.dashboard.getnetworkappliancetrafficshapingrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancetrafficshapingrules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancetrafficshapingrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancetrafficshapingrules: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancetrafficshapinguplinkbandwidth(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancetrafficshapinguplinkbandwidth'.
        Calls 'self.dashboard.getnetworkappliancetrafficshapinguplinkbandwidth' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancetrafficshapinguplinkbandwidth(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancetrafficshapinguplinkbandwidth: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancetrafficshapinguplinkbandwidth: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancetrafficshapinguplinkselection(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancetrafficshapinguplinkselection'.
        Calls 'self.dashboard.getnetworkappliancetrafficshapinguplinkselection' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancetrafficshapinguplinkselection(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancetrafficshapinguplinkselection: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancetrafficshapinguplinkselection: {ex}")
            return {"error": str(ex)}

    def getnetworkapplianceuplinksusagehistory(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkapplianceuplinksusagehistory'.
        Calls 'self.dashboard.getnetworkapplianceuplinksusagehistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkapplianceuplinksusagehistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkapplianceuplinksusagehistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkapplianceuplinksusagehistory: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancevlan(self, networkId, vlanId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancevlan'.
        Calls 'self.dashboard.getnetworkappliancevlan' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param vlanId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancevlan(networkId, vlanId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancevlan: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancevlan: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancevlans(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancevlans'.
        Calls 'self.dashboard.getnetworkappliancevlans' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancevlans(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancevlans: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancevlans: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancevlanssettings(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancevlanssettings'.
        Calls 'self.dashboard.getnetworkappliancevlanssettings' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancevlanssettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancevlanssettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancevlanssettings: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancevpnbgp(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancevpnbgp'.
        Calls 'self.dashboard.getnetworkappliancevpnbgp' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancevpnbgp(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancevpnbgp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancevpnbgp: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancevpnsitetositevpn(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancevpnsitetositevpn'.
        Calls 'self.dashboard.getnetworkappliancevpnsitetositevpn' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancevpnsitetositevpn(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancevpnsitetositevpn: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancevpnsitetositevpn: {ex}")
            return {"error": str(ex)}

    def getnetworkappliancewarmspare(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkappliancewarmspare'.
        Calls 'self.dashboard.getnetworkappliancewarmspare' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkappliancewarmspare(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkappliancewarmspare: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkappliancewarmspare: {ex}")
            return {"error": str(ex)}

    def getnetworkbluetoothclient(self, networkId, bluetoothClientId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkbluetoothclient'.
        Calls 'self.dashboard.getnetworkbluetoothclient' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param bluetoothClientId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkbluetoothclient(networkId, bluetoothClientId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkbluetoothclient: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkbluetoothclient: {ex}")
            return {"error": str(ex)}

    def getnetworkbluetoothclients(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkbluetoothclients'.
        Calls 'self.dashboard.getnetworkbluetoothclients' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkbluetoothclients(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkbluetoothclients: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkbluetoothclients: {ex}")
            return {"error": str(ex)}

    def getnetworkcameraqualityretentionprofile(self, networkId, qualityRetentionProfileId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkcameraqualityretentionprofile'.
        Calls 'self.dashboard.getnetworkcameraqualityretentionprofile' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param qualityRetentionProfileId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkcameraqualityretentionprofile(networkId, qualityRetentionProfileId)
        except APIError as e:
            logging.error(f"API Error in getnetworkcameraqualityretentionprofile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkcameraqualityretentionprofile: {ex}")
            return {"error": str(ex)}

    def getnetworkcameraqualityretentionprofiles(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkcameraqualityretentionprofiles'.
        Calls 'self.dashboard.getnetworkcameraqualityretentionprofiles' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkcameraqualityretentionprofiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkcameraqualityretentionprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkcameraqualityretentionprofiles: {ex}")
            return {"error": str(ex)}

    def getnetworkcameraschedules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkcameraschedules'.
        Calls 'self.dashboard.getnetworkcameraschedules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkcameraschedules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkcameraschedules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkcameraschedules: {ex}")
            return {"error": str(ex)}

    def getnetworkcamerawirelessprofile(self, networkId, wirelessProfileId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkcamerawirelessprofile'.
        Calls 'self.dashboard.getnetworkcamerawirelessprofile' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param wirelessProfileId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkcamerawirelessprofile(networkId, wirelessProfileId)
        except APIError as e:
            logging.error(f"API Error in getnetworkcamerawirelessprofile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkcamerawirelessprofile: {ex}")
            return {"error": str(ex)}

    def getnetworkcamerawirelessprofiles(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkcamerawirelessprofiles'.
        Calls 'self.dashboard.getnetworkcamerawirelessprofiles' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkcamerawirelessprofiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkcamerawirelessprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkcamerawirelessprofiles: {ex}")
            return {"error": str(ex)}

    def getnetworkcellulargatewayconnectivitymonitoringdestinations(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkcellulargatewayconnectivitymonitoringdestinations'.
        Calls 'self.dashboard.getnetworkcellulargatewayconnectivitymonitoringdestinations' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkcellulargatewayconnectivitymonitoringdestinations(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkcellulargatewayconnectivitymonitoringdestinations: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkcellulargatewayconnectivitymonitoringdestinations: {ex}")
            return {"error": str(ex)}

    def getnetworkcellulargatewaydhcp(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkcellulargatewaydhcp'.
        Calls 'self.dashboard.getnetworkcellulargatewaydhcp' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkcellulargatewaydhcp(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkcellulargatewaydhcp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkcellulargatewaydhcp: {ex}")
            return {"error": str(ex)}

    def getnetworkcellulargatewaysubnetpool(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkcellulargatewaysubnetpool'.
        Calls 'self.dashboard.getnetworkcellulargatewaysubnetpool' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkcellulargatewaysubnetpool(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkcellulargatewaysubnetpool: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkcellulargatewaysubnetpool: {ex}")
            return {"error": str(ex)}

    def getnetworkcellulargatewayuplink(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkcellulargatewayuplink'.
        Calls 'self.dashboard.getnetworkcellulargatewayuplink' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkcellulargatewayuplink(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkcellulargatewayuplink: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkcellulargatewayuplink: {ex}")
            return {"error": str(ex)}

    def getnetworkclient(self, networkId, clientId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkclient'.
        Calls 'self.dashboard.getnetworkclient' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clientId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkclient(networkId, clientId)
        except APIError as e:
            logging.error(f"API Error in getnetworkclient: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkclient: {ex}")
            return {"error": str(ex)}

    def getnetworkclientpolicy(self, networkId, clientId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkclientpolicy'.
        Calls 'self.dashboard.getnetworkclientpolicy' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clientId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkclientpolicy(networkId, clientId)
        except APIError as e:
            logging.error(f"API Error in getnetworkclientpolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkclientpolicy: {ex}")
            return {"error": str(ex)}

    def getnetworkclients(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkclients'.
        Calls 'self.dashboard.getnetworkclients' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkclients(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkclients: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkclients: {ex}")
            return {"error": str(ex)}

    def getnetworkclientsapplicationusage(self, networkId, clients, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkclientsapplicationusage'.
        Calls 'self.dashboard.getnetworkclientsapplicationusage' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clients: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkclientsapplicationusage(networkId, clients, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkclientsapplicationusage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkclientsapplicationusage: {ex}")
            return {"error": str(ex)}

    def getnetworkclientsbandwidthusagehistory(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkclientsbandwidthusagehistory'.
        Calls 'self.dashboard.getnetworkclientsbandwidthusagehistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkclientsbandwidthusagehistory(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkclientsbandwidthusagehistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkclientsbandwidthusagehistory: {ex}")
            return {"error": str(ex)}

    def getnetworkclientsoverview(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkclientsoverview'.
        Calls 'self.dashboard.getnetworkclientsoverview' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkclientsoverview(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkclientsoverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkclientsoverview: {ex}")
            return {"error": str(ex)}

    def getnetworkclientsplashauthorizationstatus(self, networkId, clientId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkclientsplashauthorizationstatus'.
        Calls 'self.dashboard.getnetworkclientsplashauthorizationstatus' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clientId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkclientsplashauthorizationstatus(networkId, clientId)
        except APIError as e:
            logging.error(f"API Error in getnetworkclientsplashauthorizationstatus: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkclientsplashauthorizationstatus: {ex}")
            return {"error": str(ex)}

    def getnetworkclientsusagehistories(self, networkId, clients, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkclientsusagehistories'.
        Calls 'self.dashboard.getnetworkclientsusagehistories' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clients: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkclientsusagehistories(networkId, clients, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkclientsusagehistories: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkclientsusagehistories: {ex}")
            return {"error": str(ex)}

    def getnetworkclienttraffichistory(self, networkId, clientId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkclienttraffichistory'.
        Calls 'self.dashboard.getnetworkclienttraffichistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clientId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkclienttraffichistory(networkId, clientId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkclienttraffichistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkclienttraffichistory: {ex}")
            return {"error": str(ex)}

    def getnetworkclientusagehistory(self, networkId, clientId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkclientusagehistory'.
        Calls 'self.dashboard.getnetworkclientusagehistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clientId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkclientusagehistory(networkId, clientId)
        except APIError as e:
            logging.error(f"API Error in getnetworkclientusagehistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkclientusagehistory: {ex}")
            return {"error": str(ex)}

    def getnetworkdevices(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkdevices'.
        Calls 'self.dashboard.getnetworkdevices' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkdevices(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkdevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkdevices: {ex}")
            return {"error": str(ex)}

    def getnetworkevents(self, networkId, total_pages=1, direction='prev', event_log_end_time=None, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkevents'.
        Calls 'self.dashboard.getnetworkevents' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param event_log_end_time: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkevents(networkId, total_pages, direction, event_log_end_time, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkevents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkevents: {ex}")
            return {"error": str(ex)}

    def getnetworkeventseventtypes(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkeventseventtypes'.
        Calls 'self.dashboard.getnetworkeventseventtypes' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkeventseventtypes(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkeventseventtypes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkeventseventtypes: {ex}")
            return {"error": str(ex)}

    def getnetworkfirmwareupgrades(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkfirmwareupgrades'.
        Calls 'self.dashboard.getnetworkfirmwareupgrades' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkfirmwareupgrades(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkfirmwareupgrades: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkfirmwareupgrades: {ex}")
            return {"error": str(ex)}

    def getnetworkfirmwareupgradesstagedevents(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkfirmwareupgradesstagedevents'.
        Calls 'self.dashboard.getnetworkfirmwareupgradesstagedevents' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkfirmwareupgradesstagedevents(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkfirmwareupgradesstagedevents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkfirmwareupgradesstagedevents: {ex}")
            return {"error": str(ex)}

    def getnetworkfirmwareupgradesstagedgroup(self, networkId, groupId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkfirmwareupgradesstagedgroup'.
        Calls 'self.dashboard.getnetworkfirmwareupgradesstagedgroup' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param groupId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkfirmwareupgradesstagedgroup(networkId, groupId)
        except APIError as e:
            logging.error(f"API Error in getnetworkfirmwareupgradesstagedgroup: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkfirmwareupgradesstagedgroup: {ex}")
            return {"error": str(ex)}

    def getnetworkfirmwareupgradesstagedgroups(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkfirmwareupgradesstagedgroups'.
        Calls 'self.dashboard.getnetworkfirmwareupgradesstagedgroups' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkfirmwareupgradesstagedgroups(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkfirmwareupgradesstagedgroups: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkfirmwareupgradesstagedgroups: {ex}")
            return {"error": str(ex)}

    def getnetworkfirmwareupgradesstagedstages(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkfirmwareupgradesstagedstages'.
        Calls 'self.dashboard.getnetworkfirmwareupgradesstagedstages' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkfirmwareupgradesstagedstages(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkfirmwareupgradesstagedstages: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkfirmwareupgradesstagedstages: {ex}")
            return {"error": str(ex)}

    def getnetworkfloorplan(self, networkId, floorPlanId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkfloorplan'.
        Calls 'self.dashboard.getnetworkfloorplan' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param floorPlanId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkfloorplan(networkId, floorPlanId)
        except APIError as e:
            logging.error(f"API Error in getnetworkfloorplan: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkfloorplan: {ex}")
            return {"error": str(ex)}

    def getnetworkfloorplans(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkfloorplans'.
        Calls 'self.dashboard.getnetworkfloorplans' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkfloorplans(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkfloorplans: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkfloorplans: {ex}")
            return {"error": str(ex)}

    def getnetworkgrouppolicies(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkgrouppolicies'.
        Calls 'self.dashboard.getnetworkgrouppolicies' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkgrouppolicies(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkgrouppolicies: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkgrouppolicies: {ex}")
            return {"error": str(ex)}

    def getnetworkgrouppolicy(self, networkId, groupPolicyId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkgrouppolicy'.
        Calls 'self.dashboard.getnetworkgrouppolicy' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param groupPolicyId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkgrouppolicy(networkId, groupPolicyId)
        except APIError as e:
            logging.error(f"API Error in getnetworkgrouppolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkgrouppolicy: {ex}")
            return {"error": str(ex)}

    def getnetworkhealthalerts(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkhealthalerts'.
        Calls 'self.dashboard.getnetworkhealthalerts' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkhealthalerts(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkhealthalerts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkhealthalerts: {ex}")
            return {"error": str(ex)}

    def getnetworkinsightapplicationhealthbytime(self, networkId, applicationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkinsightapplicationhealthbytime'.
        Calls 'self.dashboard.getnetworkinsightapplicationhealthbytime' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param applicationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkinsightapplicationhealthbytime(networkId, applicationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkinsightapplicationhealthbytime: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkinsightapplicationhealthbytime: {ex}")
            return {"error": str(ex)}

    def getnetworkmerakiauthuser(self, networkId, merakiAuthUserId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkmerakiauthuser'.
        Calls 'self.dashboard.getnetworkmerakiauthuser' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param merakiAuthUserId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkmerakiauthuser(networkId, merakiAuthUserId)
        except APIError as e:
            logging.error(f"API Error in getnetworkmerakiauthuser: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkmerakiauthuser: {ex}")
            return {"error": str(ex)}

    def getnetworkmerakiauthusers(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkmerakiauthusers'.
        Calls 'self.dashboard.getnetworkmerakiauthusers' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkmerakiauthusers(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkmerakiauthusers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkmerakiauthusers: {ex}")
            return {"error": str(ex)}

    def getnetworkmqttbroker(self, networkId, mqttBrokerId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkmqttbroker'.
        Calls 'self.dashboard.getnetworkmqttbroker' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param mqttBrokerId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkmqttbroker(networkId, mqttBrokerId)
        except APIError as e:
            logging.error(f"API Error in getnetworkmqttbroker: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkmqttbroker: {ex}")
            return {"error": str(ex)}

    def getnetworkmqttbrokers(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkmqttbrokers'.
        Calls 'self.dashboard.getnetworkmqttbrokers' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkmqttbrokers(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkmqttbrokers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkmqttbrokers: {ex}")
            return {"error": str(ex)}

    def getnetworknetflow(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworknetflow'.
        Calls 'self.dashboard.getnetworknetflow' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworknetflow(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworknetflow: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworknetflow: {ex}")
            return {"error": str(ex)}

    def getnetworknetworkhealthchannelutilization(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworknetworkhealthchannelutilization'.
        Calls 'self.dashboard.getnetworknetworkhealthchannelutilization' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworknetworkhealthchannelutilization(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworknetworkhealthchannelutilization: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworknetworkhealthchannelutilization: {ex}")
            return {"error": str(ex)}

    def getnetworkpiipiikeys(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkpiipiikeys'.
        Calls 'self.dashboard.getnetworkpiipiikeys' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkpiipiikeys(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkpiipiikeys: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkpiipiikeys: {ex}")
            return {"error": str(ex)}

    def getnetworkpiirequest(self, networkId, requestId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkpiirequest'.
        Calls 'self.dashboard.getnetworkpiirequest' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param requestId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkpiirequest(networkId, requestId)
        except APIError as e:
            logging.error(f"API Error in getnetworkpiirequest: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkpiirequest: {ex}")
            return {"error": str(ex)}

    def getnetworkpiirequests(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkpiirequests'.
        Calls 'self.dashboard.getnetworkpiirequests' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkpiirequests(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkpiirequests: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkpiirequests: {ex}")
            return {"error": str(ex)}

    def getnetworkpiismdevicesforkey(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkpiismdevicesforkey'.
        Calls 'self.dashboard.getnetworkpiismdevicesforkey' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkpiismdevicesforkey(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkpiismdevicesforkey: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkpiismdevicesforkey: {ex}")
            return {"error": str(ex)}

    def getnetworkpiismownersforkey(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkpiismownersforkey'.
        Calls 'self.dashboard.getnetworkpiismownersforkey' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkpiismownersforkey(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkpiismownersforkey: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkpiismownersforkey: {ex}")
            return {"error": str(ex)}

    def getnetworkpoliciesbyclient(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkpoliciesbyclient'.
        Calls 'self.dashboard.getnetworkpoliciesbyclient' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkpoliciesbyclient(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkpoliciesbyclient: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkpoliciesbyclient: {ex}")
            return {"error": str(ex)}

    def getnetworksensoralertscurrentoverviewbymetric(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksensoralertscurrentoverviewbymetric'.
        Calls 'self.dashboard.getnetworksensoralertscurrentoverviewbymetric' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksensoralertscurrentoverviewbymetric(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworksensoralertscurrentoverviewbymetric: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksensoralertscurrentoverviewbymetric: {ex}")
            return {"error": str(ex)}

    def getnetworksensoralertsoverviewbymetric(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksensoralertsoverviewbymetric'.
        Calls 'self.dashboard.getnetworksensoralertsoverviewbymetric' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksensoralertsoverviewbymetric(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksensoralertsoverviewbymetric: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksensoralertsoverviewbymetric: {ex}")
            return {"error": str(ex)}

    def getnetworksensoralertsprofile(self, networkId, id) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksensoralertsprofile'.
        Calls 'self.dashboard.getnetworksensoralertsprofile' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksensoralertsprofile(networkId, id)
        except APIError as e:
            logging.error(f"API Error in getnetworksensoralertsprofile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksensoralertsprofile: {ex}")
            return {"error": str(ex)}

    def getnetworksensoralertsprofiles(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksensoralertsprofiles'.
        Calls 'self.dashboard.getnetworksensoralertsprofiles' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksensoralertsprofiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworksensoralertsprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksensoralertsprofiles: {ex}")
            return {"error": str(ex)}

    def getnetworksensormqttbroker(self, networkId, mqttBrokerId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksensormqttbroker'.
        Calls 'self.dashboard.getnetworksensormqttbroker' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param mqttBrokerId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksensormqttbroker(networkId, mqttBrokerId)
        except APIError as e:
            logging.error(f"API Error in getnetworksensormqttbroker: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksensormqttbroker: {ex}")
            return {"error": str(ex)}

    def getnetworksensormqttbrokers(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksensormqttbrokers'.
        Calls 'self.dashboard.getnetworksensormqttbrokers' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksensormqttbrokers(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworksensormqttbrokers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksensormqttbrokers: {ex}")
            return {"error": str(ex)}

    def getnetworksensorrelationships(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksensorrelationships'.
        Calls 'self.dashboard.getnetworksensorrelationships' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksensorrelationships(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworksensorrelationships: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksensorrelationships: {ex}")
            return {"error": str(ex)}

    def getnetworksettings(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksettings'.
        Calls 'self.dashboard.getnetworksettings' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworksettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksettings: {ex}")
            return {"error": str(ex)}

    def getnetworksmbypassactivationlockattempt(self, networkId, attemptId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmbypassactivationlockattempt'.
        Calls 'self.dashboard.getnetworksmbypassactivationlockattempt' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param attemptId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmbypassactivationlockattempt(networkId, attemptId)
        except APIError as e:
            logging.error(f"API Error in getnetworksmbypassactivationlockattempt: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmbypassactivationlockattempt: {ex}")
            return {"error": str(ex)}

    def getnetworksmdevicecellularusagehistory(self, networkId, deviceId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdevicecellularusagehistory'.
        Calls 'self.dashboard.getnetworksmdevicecellularusagehistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdevicecellularusagehistory(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdevicecellularusagehistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdevicecellularusagehistory: {ex}")
            return {"error": str(ex)}

    def getnetworksmdevicecerts(self, networkId, deviceId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdevicecerts'.
        Calls 'self.dashboard.getnetworksmdevicecerts' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdevicecerts(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdevicecerts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdevicecerts: {ex}")
            return {"error": str(ex)}

    def getnetworksmdeviceconnectivity(self, networkId, deviceId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdeviceconnectivity'.
        Calls 'self.dashboard.getnetworksmdeviceconnectivity' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdeviceconnectivity(networkId, deviceId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdeviceconnectivity: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdeviceconnectivity: {ex}")
            return {"error": str(ex)}

    def getnetworksmdevicedesktoplogs(self, networkId, deviceId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdevicedesktoplogs'.
        Calls 'self.dashboard.getnetworksmdevicedesktoplogs' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdevicedesktoplogs(networkId, deviceId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdevicedesktoplogs: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdevicedesktoplogs: {ex}")
            return {"error": str(ex)}

    def getnetworksmdevicedevicecommandlogs(self, networkId, deviceId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdevicedevicecommandlogs'.
        Calls 'self.dashboard.getnetworksmdevicedevicecommandlogs' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdevicedevicecommandlogs(networkId, deviceId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdevicedevicecommandlogs: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdevicedevicecommandlogs: {ex}")
            return {"error": str(ex)}

    def getnetworksmdevicedeviceprofiles(self, networkId, deviceId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdevicedeviceprofiles'.
        Calls 'self.dashboard.getnetworksmdevicedeviceprofiles' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdevicedeviceprofiles(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdevicedeviceprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdevicedeviceprofiles: {ex}")
            return {"error": str(ex)}

    def getnetworksmdevicenetworkadapters(self, networkId, deviceId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdevicenetworkadapters'.
        Calls 'self.dashboard.getnetworksmdevicenetworkadapters' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdevicenetworkadapters(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdevicenetworkadapters: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdevicenetworkadapters: {ex}")
            return {"error": str(ex)}

    def getnetworksmdeviceperformancehistory(self, networkId, deviceId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdeviceperformancehistory'.
        Calls 'self.dashboard.getnetworksmdeviceperformancehistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdeviceperformancehistory(networkId, deviceId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdeviceperformancehistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdeviceperformancehistory: {ex}")
            return {"error": str(ex)}

    def getnetworksmdevicerestrictions(self, networkId, deviceId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdevicerestrictions'.
        Calls 'self.dashboard.getnetworksmdevicerestrictions' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdevicerestrictions(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdevicerestrictions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdevicerestrictions: {ex}")
            return {"error": str(ex)}

    def getnetworksmdevices(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdevices'.
        Calls 'self.dashboard.getnetworksmdevices' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdevices(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdevices: {ex}")
            return {"error": str(ex)}

    def getnetworksmdevicesecuritycenters(self, networkId, deviceId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdevicesecuritycenters'.
        Calls 'self.dashboard.getnetworksmdevicesecuritycenters' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdevicesecuritycenters(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdevicesecuritycenters: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdevicesecuritycenters: {ex}")
            return {"error": str(ex)}

    def getnetworksmdevicesoftwares(self, networkId, deviceId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdevicesoftwares'.
        Calls 'self.dashboard.getnetworksmdevicesoftwares' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdevicesoftwares(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdevicesoftwares: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdevicesoftwares: {ex}")
            return {"error": str(ex)}

    def getnetworksmdevicewlanlists(self, networkId, deviceId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmdevicewlanlists'.
        Calls 'self.dashboard.getnetworksmdevicewlanlists' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param deviceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmdevicewlanlists(networkId, deviceId)
        except APIError as e:
            logging.error(f"API Error in getnetworksmdevicewlanlists: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmdevicewlanlists: {ex}")
            return {"error": str(ex)}

    def getnetworksmprofiles(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmprofiles'.
        Calls 'self.dashboard.getnetworksmprofiles' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmprofiles(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksmprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmprofiles: {ex}")
            return {"error": str(ex)}

    def getnetworksmtargetgroup(self, networkId, targetGroupId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmtargetgroup'.
        Calls 'self.dashboard.getnetworksmtargetgroup' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param targetGroupId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmtargetgroup(networkId, targetGroupId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksmtargetgroup: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmtargetgroup: {ex}")
            return {"error": str(ex)}

    def getnetworksmtargetgroups(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmtargetgroups'.
        Calls 'self.dashboard.getnetworksmtargetgroups' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmtargetgroups(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksmtargetgroups: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmtargetgroups: {ex}")
            return {"error": str(ex)}

    def getnetworksmtrustedaccessconfigs(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmtrustedaccessconfigs'.
        Calls 'self.dashboard.getnetworksmtrustedaccessconfigs' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmtrustedaccessconfigs(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksmtrustedaccessconfigs: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmtrustedaccessconfigs: {ex}")
            return {"error": str(ex)}

    def getnetworksmuseraccessdevices(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmuseraccessdevices'.
        Calls 'self.dashboard.getnetworksmuseraccessdevices' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmuseraccessdevices(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksmuseraccessdevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmuseraccessdevices: {ex}")
            return {"error": str(ex)}

    def getnetworksmuserdeviceprofiles(self, networkId, userId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmuserdeviceprofiles'.
        Calls 'self.dashboard.getnetworksmuserdeviceprofiles' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param userId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmuserdeviceprofiles(networkId, userId)
        except APIError as e:
            logging.error(f"API Error in getnetworksmuserdeviceprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmuserdeviceprofiles: {ex}")
            return {"error": str(ex)}

    def getnetworksmusers(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmusers'.
        Calls 'self.dashboard.getnetworksmusers' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmusers(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksmusers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmusers: {ex}")
            return {"error": str(ex)}

    def getnetworksmusersoftwares(self, networkId, userId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksmusersoftwares'.
        Calls 'self.dashboard.getnetworksmusersoftwares' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param userId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksmusersoftwares(networkId, userId)
        except APIError as e:
            logging.error(f"API Error in getnetworksmusersoftwares: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksmusersoftwares: {ex}")
            return {"error": str(ex)}

    def getnetworksnmp(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksnmp'.
        Calls 'self.dashboard.getnetworksnmp' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksnmp(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworksnmp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksnmp: {ex}")
            return {"error": str(ex)}

    def getnetworksplashloginattempts(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksplashloginattempts'.
        Calls 'self.dashboard.getnetworksplashloginattempts' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksplashloginattempts(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworksplashloginattempts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksplashloginattempts: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchaccesscontrollists(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchaccesscontrollists'.
        Calls 'self.dashboard.getnetworkswitchaccesscontrollists' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchaccesscontrollists(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchaccesscontrollists: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchaccesscontrollists: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchaccesspolicies(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchaccesspolicies'.
        Calls 'self.dashboard.getnetworkswitchaccesspolicies' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchaccesspolicies(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchaccesspolicies: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchaccesspolicies: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchaccesspolicy(self, networkId, accessPolicyNumber) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchaccesspolicy'.
        Calls 'self.dashboard.getnetworkswitchaccesspolicy' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param accessPolicyNumber: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchaccesspolicy(networkId, accessPolicyNumber)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchaccesspolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchaccesspolicy: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchalternatemanagementinterface(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchalternatemanagementinterface'.
        Calls 'self.dashboard.getnetworkswitchalternatemanagementinterface' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchalternatemanagementinterface(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchalternatemanagementinterface: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchalternatemanagementinterface: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchdhcpserverpolicy(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchdhcpserverpolicy'.
        Calls 'self.dashboard.getnetworkswitchdhcpserverpolicy' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchdhcpserverpolicy(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchdhcpserverpolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchdhcpserverpolicy: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchdhcpserverpolicyarpinspectiontrustedservers(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchdhcpserverpolicyarpinspectiontrustedservers'.
        Calls 'self.dashboard.getnetworkswitchdhcpserverpolicyarpinspectiontrustedservers' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchdhcpserverpolicyarpinspectiontrustedservers(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchdhcpserverpolicyarpinspectiontrustedservers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchdhcpserverpolicyarpinspectiontrustedservers: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchdhcpserverpolicyarpinspectionwarningsbydevice(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchdhcpserverpolicyarpinspectionwarningsbydevice'.
        Calls 'self.dashboard.getnetworkswitchdhcpserverpolicyarpinspectionwarningsbydevice' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchdhcpserverpolicyarpinspectionwarningsbydevice(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchdhcpserverpolicyarpinspectionwarningsbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchdhcpserverpolicyarpinspectionwarningsbydevice: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchdhcpv4serversseen(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchdhcpv4serversseen'.
        Calls 'self.dashboard.getnetworkswitchdhcpv4serversseen' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchdhcpv4serversseen(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchdhcpv4serversseen: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchdhcpv4serversseen: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchdscptocosmappings(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchdscptocosmappings'.
        Calls 'self.dashboard.getnetworkswitchdscptocosmappings' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchdscptocosmappings(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchdscptocosmappings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchdscptocosmappings: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchlinkaggregations(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchlinkaggregations'.
        Calls 'self.dashboard.getnetworkswitchlinkaggregations' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchlinkaggregations(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchlinkaggregations: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchlinkaggregations: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchmtu(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchmtu'.
        Calls 'self.dashboard.getnetworkswitchmtu' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchmtu(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchmtu: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchmtu: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchportschedules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchportschedules'.
        Calls 'self.dashboard.getnetworkswitchportschedules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchportschedules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchportschedules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchportschedules: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchqosrule(self, networkId, qosRuleId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchqosrule'.
        Calls 'self.dashboard.getnetworkswitchqosrule' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param qosRuleId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchqosrule(networkId, qosRuleId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchqosrule: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchqosrule: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchqosrules(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchqosrules'.
        Calls 'self.dashboard.getnetworkswitchqosrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchqosrules(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchqosrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchqosrules: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchqosrulesorder(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchqosrulesorder'.
        Calls 'self.dashboard.getnetworkswitchqosrulesorder' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchqosrulesorder(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchqosrulesorder: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchqosrulesorder: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchroutingmulticast(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchroutingmulticast'.
        Calls 'self.dashboard.getnetworkswitchroutingmulticast' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchroutingmulticast(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchroutingmulticast: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchroutingmulticast: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchroutingmulticastrendezvouspoint(self, networkId, rendezvousPointId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchroutingmulticastrendezvouspoint'.
        Calls 'self.dashboard.getnetworkswitchroutingmulticastrendezvouspoint' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param rendezvousPointId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchroutingmulticastrendezvouspoint(networkId, rendezvousPointId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchroutingmulticastrendezvouspoint: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchroutingmulticastrendezvouspoint: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchroutingmulticastrendezvouspoints(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchroutingmulticastrendezvouspoints'.
        Calls 'self.dashboard.getnetworkswitchroutingmulticastrendezvouspoints' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchroutingmulticastrendezvouspoints(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchroutingmulticastrendezvouspoints: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchroutingmulticastrendezvouspoints: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchroutingospf(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchroutingospf'.
        Calls 'self.dashboard.getnetworkswitchroutingospf' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchroutingospf(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchroutingospf: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchroutingospf: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchsettings(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchsettings'.
        Calls 'self.dashboard.getnetworkswitchsettings' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchsettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchsettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchsettings: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchstack(self, networkId, switchStackId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchstack'.
        Calls 'self.dashboard.getnetworkswitchstack' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param switchStackId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchstack(networkId, switchStackId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchstack: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchstack: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchstackroutinginterface(self, networkId, switchStackId, interfaceId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchstackroutinginterface'.
        Calls 'self.dashboard.getnetworkswitchstackroutinginterface' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param switchStackId: (Inferred from the method signature)
        :param interfaceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchstackroutinginterface(networkId, switchStackId, interfaceId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchstackroutinginterface: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchstackroutinginterface: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchstackroutinginterfacedhcp(self, networkId, switchStackId, interfaceId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchstackroutinginterfacedhcp'.
        Calls 'self.dashboard.getnetworkswitchstackroutinginterfacedhcp' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param switchStackId: (Inferred from the method signature)
        :param interfaceId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchstackroutinginterfacedhcp(networkId, switchStackId, interfaceId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchstackroutinginterfacedhcp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchstackroutinginterfacedhcp: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchstackroutinginterfaces(self, networkId, switchStackId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchstackroutinginterfaces'.
        Calls 'self.dashboard.getnetworkswitchstackroutinginterfaces' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param switchStackId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchstackroutinginterfaces(networkId, switchStackId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchstackroutinginterfaces: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchstackroutinginterfaces: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchstackroutingstaticroute(self, networkId, switchStackId, staticRouteId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchstackroutingstaticroute'.
        Calls 'self.dashboard.getnetworkswitchstackroutingstaticroute' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param switchStackId: (Inferred from the method signature)
        :param staticRouteId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchstackroutingstaticroute(networkId, switchStackId, staticRouteId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchstackroutingstaticroute: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchstackroutingstaticroute: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchstackroutingstaticroutes(self, networkId, switchStackId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchstackroutingstaticroutes'.
        Calls 'self.dashboard.getnetworkswitchstackroutingstaticroutes' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param switchStackId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchstackroutingstaticroutes(networkId, switchStackId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchstackroutingstaticroutes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchstackroutingstaticroutes: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchstacks(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchstacks'.
        Calls 'self.dashboard.getnetworkswitchstacks' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchstacks(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchstacks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchstacks: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchstormcontrol(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchstormcontrol'.
        Calls 'self.dashboard.getnetworkswitchstormcontrol' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchstormcontrol(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchstormcontrol: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchstormcontrol: {ex}")
            return {"error": str(ex)}

    def getnetworkswitchstp(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkswitchstp'.
        Calls 'self.dashboard.getnetworkswitchstp' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkswitchstp(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkswitchstp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkswitchstp: {ex}")
            return {"error": str(ex)}

    def getnetworksyslogservers(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworksyslogservers'.
        Calls 'self.dashboard.getnetworksyslogservers' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworksyslogservers(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworksyslogservers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworksyslogservers: {ex}")
            return {"error": str(ex)}

    def getnetworktopologylinklayer(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworktopologylinklayer'.
        Calls 'self.dashboard.getnetworktopologylinklayer' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworktopologylinklayer(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworktopologylinklayer: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworktopologylinklayer: {ex}")
            return {"error": str(ex)}

    def getnetworktraffic(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworktraffic'.
        Calls 'self.dashboard.getnetworktraffic' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworktraffic(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworktraffic: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworktraffic: {ex}")
            return {"error": str(ex)}

    def getnetworktrafficanalysis(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworktrafficanalysis'.
        Calls 'self.dashboard.getnetworktrafficanalysis' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworktrafficanalysis(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworktrafficanalysis: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworktrafficanalysis: {ex}")
            return {"error": str(ex)}

    def getnetworktrafficshapingapplicationcategories(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworktrafficshapingapplicationcategories'.
        Calls 'self.dashboard.getnetworktrafficshapingapplicationcategories' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworktrafficshapingapplicationcategories(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworktrafficshapingapplicationcategories: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworktrafficshapingapplicationcategories: {ex}")
            return {"error": str(ex)}

    def getnetworktrafficshapingdscptaggingoptions(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworktrafficshapingdscptaggingoptions'.
        Calls 'self.dashboard.getnetworktrafficshapingdscptaggingoptions' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworktrafficshapingdscptaggingoptions(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworktrafficshapingdscptaggingoptions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworktrafficshapingdscptaggingoptions: {ex}")
            return {"error": str(ex)}

    def getnetworkvlanprofile(self, networkId, iname) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkvlanprofile'.
        Calls 'self.dashboard.getnetworkvlanprofile' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param iname: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkvlanprofile(networkId, iname)
        except APIError as e:
            logging.error(f"API Error in getnetworkvlanprofile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkvlanprofile: {ex}")
            return {"error": str(ex)}

    def getnetworkvlanprofiles(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkvlanprofiles'.
        Calls 'self.dashboard.getnetworkvlanprofiles' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkvlanprofiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkvlanprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkvlanprofiles: {ex}")
            return {"error": str(ex)}

    def getnetworkvlanprofilesassignmentsbydevice(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkvlanprofilesassignmentsbydevice'.
        Calls 'self.dashboard.getnetworkvlanprofilesassignmentsbydevice' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkvlanprofilesassignmentsbydevice(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkvlanprofilesassignmentsbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkvlanprofilesassignmentsbydevice: {ex}")
            return {"error": str(ex)}

    def getnetworkwebhookshttpserver(self, networkId, httpServerId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwebhookshttpserver'.
        Calls 'self.dashboard.getnetworkwebhookshttpserver' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param httpServerId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwebhookshttpserver(networkId, httpServerId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwebhookshttpserver: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwebhookshttpserver: {ex}")
            return {"error": str(ex)}

    def getnetworkwebhookshttpservers(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwebhookshttpservers'.
        Calls 'self.dashboard.getnetworkwebhookshttpservers' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwebhookshttpservers(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwebhookshttpservers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwebhookshttpservers: {ex}")
            return {"error": str(ex)}

    def getnetworkwebhookspayloadtemplate(self, networkId, payloadTemplateId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwebhookspayloadtemplate'.
        Calls 'self.dashboard.getnetworkwebhookspayloadtemplate' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param payloadTemplateId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwebhookspayloadtemplate(networkId, payloadTemplateId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwebhookspayloadtemplate: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwebhookspayloadtemplate: {ex}")
            return {"error": str(ex)}

    def getnetworkwebhookspayloadtemplates(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwebhookspayloadtemplates'.
        Calls 'self.dashboard.getnetworkwebhookspayloadtemplates' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwebhookspayloadtemplates(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwebhookspayloadtemplates: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwebhookspayloadtemplates: {ex}")
            return {"error": str(ex)}

    def getnetworkwebhookswebhooktest(self, networkId, webhookTestId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwebhookswebhooktest'.
        Calls 'self.dashboard.getnetworkwebhookswebhooktest' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param webhookTestId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwebhookswebhooktest(networkId, webhookTestId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwebhookswebhooktest: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwebhookswebhooktest: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessairmarshal(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessairmarshal'.
        Calls 'self.dashboard.getnetworkwirelessairmarshal' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessairmarshal(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessairmarshal: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessairmarshal: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessalternatemanagementinterface(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessalternatemanagementinterface'.
        Calls 'self.dashboard.getnetworkwirelessalternatemanagementinterface' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessalternatemanagementinterface(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessalternatemanagementinterface: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessalternatemanagementinterface: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessbilling(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessbilling'.
        Calls 'self.dashboard.getnetworkwirelessbilling' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessbilling(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessbilling: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessbilling: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessbluetoothsettings(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessbluetoothsettings'.
        Calls 'self.dashboard.getnetworkwirelessbluetoothsettings' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessbluetoothsettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessbluetoothsettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessbluetoothsettings: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelesschannelutilizationhistory(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelesschannelutilizationhistory'.
        Calls 'self.dashboard.getnetworkwirelesschannelutilizationhistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelesschannelutilizationhistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelesschannelutilizationhistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelesschannelutilizationhistory: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessclientconnectionstats(self, networkId, clientId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessclientconnectionstats'.
        Calls 'self.dashboard.getnetworkwirelessclientconnectionstats' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clientId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessclientconnectionstats(networkId, clientId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessclientconnectionstats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessclientconnectionstats: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessclientconnectivityevents(self, networkId, clientId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessclientconnectivityevents'.
        Calls 'self.dashboard.getnetworkwirelessclientconnectivityevents' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clientId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessclientconnectivityevents(networkId, clientId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessclientconnectivityevents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessclientconnectivityevents: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessclientcounthistory(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessclientcounthistory'.
        Calls 'self.dashboard.getnetworkwirelessclientcounthistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessclientcounthistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessclientcounthistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessclientcounthistory: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessclientlatencyhistory(self, networkId, clientId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessclientlatencyhistory'.
        Calls 'self.dashboard.getnetworkwirelessclientlatencyhistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clientId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessclientlatencyhistory(networkId, clientId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessclientlatencyhistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessclientlatencyhistory: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessclientlatencystats(self, networkId, clientId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessclientlatencystats'.
        Calls 'self.dashboard.getnetworkwirelessclientlatencystats' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param clientId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessclientlatencystats(networkId, clientId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessclientlatencystats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessclientlatencystats: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessclientsconnectionstats(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessclientsconnectionstats'.
        Calls 'self.dashboard.getnetworkwirelessclientsconnectionstats' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessclientsconnectionstats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessclientsconnectionstats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessclientsconnectionstats: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessclientslatencystats(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessclientslatencystats'.
        Calls 'self.dashboard.getnetworkwirelessclientslatencystats' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessclientslatencystats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessclientslatencystats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessclientslatencystats: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessconnectionstats(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessconnectionstats'.
        Calls 'self.dashboard.getnetworkwirelessconnectionstats' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessconnectionstats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessconnectionstats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessconnectionstats: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessdataratehistory(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessdataratehistory'.
        Calls 'self.dashboard.getnetworkwirelessdataratehistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessdataratehistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessdataratehistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessdataratehistory: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessdevicesconnectionstats(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessdevicesconnectionstats'.
        Calls 'self.dashboard.getnetworkwirelessdevicesconnectionstats' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessdevicesconnectionstats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessdevicesconnectionstats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessdevicesconnectionstats: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessdeviceslatencystats(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessdeviceslatencystats'.
        Calls 'self.dashboard.getnetworkwirelessdeviceslatencystats' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessdeviceslatencystats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessdeviceslatencystats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessdeviceslatencystats: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelesselectronicshelflabel(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelesselectronicshelflabel'.
        Calls 'self.dashboard.getnetworkwirelesselectronicshelflabel' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelesselectronicshelflabel(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelesselectronicshelflabel: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelesselectronicshelflabel: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelesselectronicshelflabelconfigureddevices(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelesselectronicshelflabelconfigureddevices'.
        Calls 'self.dashboard.getnetworkwirelesselectronicshelflabelconfigureddevices' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelesselectronicshelflabelconfigureddevices(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelesselectronicshelflabelconfigureddevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelesselectronicshelflabelconfigureddevices: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessethernetportsprofile(self, networkId, profileId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessethernetportsprofile'.
        Calls 'self.dashboard.getnetworkwirelessethernetportsprofile' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param profileId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessethernetportsprofile(networkId, profileId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessethernetportsprofile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessethernetportsprofile: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessethernetportsprofiles(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessethernetportsprofiles'.
        Calls 'self.dashboard.getnetworkwirelessethernetportsprofiles' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessethernetportsprofiles(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessethernetportsprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessethernetportsprofiles: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessfailedconnections(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessfailedconnections'.
        Calls 'self.dashboard.getnetworkwirelessfailedconnections' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessfailedconnections(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessfailedconnections: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessfailedconnections: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelesslatencyhistory(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelesslatencyhistory'.
        Calls 'self.dashboard.getnetworkwirelesslatencyhistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelesslatencyhistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelesslatencyhistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelesslatencyhistory: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelesslatencystats(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelesslatencystats'.
        Calls 'self.dashboard.getnetworkwirelesslatencystats' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelesslatencystats(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelesslatencystats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelesslatencystats: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessmeshstatuses(self, networkId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessmeshstatuses'.
        Calls 'self.dashboard.getnetworkwirelessmeshstatuses' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessmeshstatuses(networkId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessmeshstatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessmeshstatuses: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessrfprofile(self, networkId, rfProfileId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessrfprofile'.
        Calls 'self.dashboard.getnetworkwirelessrfprofile' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param rfProfileId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessrfprofile(networkId, rfProfileId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessrfprofile: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessrfprofile: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessrfprofiles(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessrfprofiles'.
        Calls 'self.dashboard.getnetworkwirelessrfprofiles' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessrfprofiles(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessrfprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessrfprofiles: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelesssettings(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelesssettings'.
        Calls 'self.dashboard.getnetworkwirelesssettings' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelesssettings(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelesssettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelesssettings: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelesssignalqualityhistory(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelesssignalqualityhistory'.
        Calls 'self.dashboard.getnetworkwirelesssignalqualityhistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelesssignalqualityhistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelesssignalqualityhistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelesssignalqualityhistory: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssid(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssid'.
        Calls 'self.dashboard.getnetworkwirelessssid' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssid(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssid: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssid: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssidbonjourforwarding(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssidbonjourforwarding'.
        Calls 'self.dashboard.getnetworkwirelessssidbonjourforwarding' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssidbonjourforwarding(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssidbonjourforwarding: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssidbonjourforwarding: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssiddevicetypegrouppolicies(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssiddevicetypegrouppolicies'.
        Calls 'self.dashboard.getnetworkwirelessssiddevicetypegrouppolicies' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssiddevicetypegrouppolicies(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssiddevicetypegrouppolicies: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssiddevicetypegrouppolicies: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssideapoverride(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssideapoverride'.
        Calls 'self.dashboard.getnetworkwirelessssideapoverride' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssideapoverride(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssideapoverride: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssideapoverride: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssidfirewalll3firewallrules(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssidfirewalll3firewallrules'.
        Calls 'self.dashboard.getnetworkwirelessssidfirewalll3firewallrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssidfirewalll3firewallrules(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssidfirewalll3firewallrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssidfirewalll3firewallrules: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssidfirewalll7firewallrules(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssidfirewalll7firewallrules'.
        Calls 'self.dashboard.getnetworkwirelessssidfirewalll7firewallrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssidfirewalll7firewallrules(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssidfirewalll7firewallrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssidfirewalll7firewallrules: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssidhotspot20(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssidhotspot20'.
        Calls 'self.dashboard.getnetworkwirelessssidhotspot20' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssidhotspot20(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssidhotspot20: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssidhotspot20: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssididentitypsk(self, networkId, number, identityPskId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssididentitypsk'.
        Calls 'self.dashboard.getnetworkwirelessssididentitypsk' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :param identityPskId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssididentitypsk(networkId, number, identityPskId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssididentitypsk: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssididentitypsk: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssididentitypsks(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssididentitypsks'.
        Calls 'self.dashboard.getnetworkwirelessssididentitypsks' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssididentitypsks(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssididentitypsks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssididentitypsks: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssids(self, networkId) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssids'.
        Calls 'self.dashboard.getnetworkwirelessssids' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssids(networkId)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssids: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssids: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssidschedules(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssidschedules'.
        Calls 'self.dashboard.getnetworkwirelessssidschedules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssidschedules(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssidschedules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssidschedules: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssidsplashsettings(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssidsplashsettings'.
        Calls 'self.dashboard.getnetworkwirelessssidsplashsettings' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssidsplashsettings(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssidsplashsettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssidsplashsettings: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssidtrafficshapingrules(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssidtrafficshapingrules'.
        Calls 'self.dashboard.getnetworkwirelessssidtrafficshapingrules' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssidtrafficshapingrules(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssidtrafficshapingrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssidtrafficshapingrules: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessssidvpn(self, networkId, number) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessssidvpn'.
        Calls 'self.dashboard.getnetworkwirelessssidvpn' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param number: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessssidvpn(networkId, number)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessssidvpn: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessssidvpn: {ex}")
            return {"error": str(ex)}

    def getnetworkwirelessusagehistory(self, networkId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getnetworkwirelessusagehistory'.
        Calls 'self.dashboard.getnetworkwirelessusagehistory' with the same parameters.
        
        :param networkId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getnetworkwirelessusagehistory(networkId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getnetworkwirelessusagehistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getnetworkwirelessusagehistory: {ex}")
            return {"error": str(ex)}

    def getorganization(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganization'.
        Calls 'self.dashboard.getorganization' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganization(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganization: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganization: {ex}")
            return {"error": str(ex)}

    def getorganizationactionbatch(self, organizationId, actionBatchId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationactionbatch'.
        Calls 'self.dashboard.getorganizationactionbatch' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param actionBatchId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationactionbatch(organizationId, actionBatchId)
        except APIError as e:
            logging.error(f"API Error in getorganizationactionbatch: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationactionbatch: {ex}")
            return {"error": str(ex)}

    def getorganizationactionbatches(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationactionbatches'.
        Calls 'self.dashboard.getorganizationactionbatches' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationactionbatches(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationactionbatches: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationactionbatches: {ex}")
            return {"error": str(ex)}

    def getorganizationadaptivepolicyacl(self, organizationId, aclId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationadaptivepolicyacl'.
        Calls 'self.dashboard.getorganizationadaptivepolicyacl' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param aclId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationadaptivepolicyacl(organizationId, aclId)
        except APIError as e:
            logging.error(f"API Error in getorganizationadaptivepolicyacl: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationadaptivepolicyacl: {ex}")
            return {"error": str(ex)}

    def getorganizationadaptivepolicyacls(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationadaptivepolicyacls'.
        Calls 'self.dashboard.getorganizationadaptivepolicyacls' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationadaptivepolicyacls(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationadaptivepolicyacls: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationadaptivepolicyacls: {ex}")
            return {"error": str(ex)}

    def getorganizationadaptivepolicygroup(self, organizationId, id) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationadaptivepolicygroup'.
        Calls 'self.dashboard.getorganizationadaptivepolicygroup' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationadaptivepolicygroup(organizationId, id)
        except APIError as e:
            logging.error(f"API Error in getorganizationadaptivepolicygroup: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationadaptivepolicygroup: {ex}")
            return {"error": str(ex)}

    def getorganizationadaptivepolicygroups(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationadaptivepolicygroups'.
        Calls 'self.dashboard.getorganizationadaptivepolicygroups' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationadaptivepolicygroups(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationadaptivepolicygroups: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationadaptivepolicygroups: {ex}")
            return {"error": str(ex)}

    def getorganizationadaptivepolicyoverview(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationadaptivepolicyoverview'.
        Calls 'self.dashboard.getorganizationadaptivepolicyoverview' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationadaptivepolicyoverview(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationadaptivepolicyoverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationadaptivepolicyoverview: {ex}")
            return {"error": str(ex)}

    def getorganizationadaptivepolicypolicies(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationadaptivepolicypolicies'.
        Calls 'self.dashboard.getorganizationadaptivepolicypolicies' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationadaptivepolicypolicies(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationadaptivepolicypolicies: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationadaptivepolicypolicies: {ex}")
            return {"error": str(ex)}

    def getorganizationadaptivepolicypolicy(self, organizationId, id) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationadaptivepolicypolicy'.
        Calls 'self.dashboard.getorganizationadaptivepolicypolicy' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationadaptivepolicypolicy(organizationId, id)
        except APIError as e:
            logging.error(f"API Error in getorganizationadaptivepolicypolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationadaptivepolicypolicy: {ex}")
            return {"error": str(ex)}

    def getorganizationadaptivepolicysettings(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationadaptivepolicysettings'.
        Calls 'self.dashboard.getorganizationadaptivepolicysettings' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationadaptivepolicysettings(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationadaptivepolicysettings: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationadaptivepolicysettings: {ex}")
            return {"error": str(ex)}

    def getorganizationadmins(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationadmins'.
        Calls 'self.dashboard.getorganizationadmins' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationadmins(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationadmins: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationadmins: {ex}")
            return {"error": str(ex)}

    def getorganizationalertsprofiles(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationalertsprofiles'.
        Calls 'self.dashboard.getorganizationalertsprofiles' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationalertsprofiles(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationalertsprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationalertsprofiles: {ex}")
            return {"error": str(ex)}

    def getorganizationapirequests(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationapirequests'.
        Calls 'self.dashboard.getorganizationapirequests' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationapirequests(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationapirequests: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationapirequests: {ex}")
            return {"error": str(ex)}

    def getorganizationapirequestsoverview(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationapirequestsoverview'.
        Calls 'self.dashboard.getorganizationapirequestsoverview' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationapirequestsoverview(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationapirequestsoverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationapirequestsoverview: {ex}")
            return {"error": str(ex)}

    def getorganizationapirequestsoverviewresponsecodesbyinterval(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationapirequestsoverviewresponsecodesbyinterval'.
        Calls 'self.dashboard.getorganizationapirequestsoverviewresponsecodesbyinterval' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationapirequestsoverviewresponsecodesbyinterval(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationapirequestsoverviewresponsecodesbyinterval: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationapirequestsoverviewresponsecodesbyinterval: {ex}")
            return {"error": str(ex)}

    def getorganizationappliancesecurityevents(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationappliancesecurityevents'.
        Calls 'self.dashboard.getorganizationappliancesecurityevents' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationappliancesecurityevents(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationappliancesecurityevents: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationappliancesecurityevents: {ex}")
            return {"error": str(ex)}

    def getorganizationappliancesecurityintrusion(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationappliancesecurityintrusion'.
        Calls 'self.dashboard.getorganizationappliancesecurityintrusion' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationappliancesecurityintrusion(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationappliancesecurityintrusion: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationappliancesecurityintrusion: {ex}")
            return {"error": str(ex)}

    def getorganizationappliancetrafficshapingvpnexclusionsbynetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationappliancetrafficshapingvpnexclusionsbynetwork'.
        Calls 'self.dashboard.getorganizationappliancetrafficshapingvpnexclusionsbynetwork' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationappliancetrafficshapingvpnexclusionsbynetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationappliancetrafficshapingvpnexclusionsbynetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationappliancetrafficshapingvpnexclusionsbynetwork: {ex}")
            return {"error": str(ex)}

    def getorganizationapplianceuplinksstatusesoverview(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationapplianceuplinksstatusesoverview'.
        Calls 'self.dashboard.getorganizationapplianceuplinksstatusesoverview' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationapplianceuplinksstatusesoverview(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationapplianceuplinksstatusesoverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationapplianceuplinksstatusesoverview: {ex}")
            return {"error": str(ex)}

    def getorganizationapplianceuplinkstatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationapplianceuplinkstatuses'.
        Calls 'self.dashboard.getorganizationapplianceuplinkstatuses' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationapplianceuplinkstatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationapplianceuplinkstatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationapplianceuplinkstatuses: {ex}")
            return {"error": str(ex)}

    def getorganizationapplianceuplinksusagebynetwork(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationapplianceuplinksusagebynetwork'.
        Calls 'self.dashboard.getorganizationapplianceuplinksusagebynetwork' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationapplianceuplinksusagebynetwork(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationapplianceuplinksusagebynetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationapplianceuplinksusagebynetwork: {ex}")
            return {"error": str(ex)}

    def getorganizationappliancevpnstats(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationappliancevpnstats'.
        Calls 'self.dashboard.getorganizationappliancevpnstats' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationappliancevpnstats(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationappliancevpnstats: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationappliancevpnstats: {ex}")
            return {"error": str(ex)}

    def getorganizationappliancevpnstatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationappliancevpnstatuses'.
        Calls 'self.dashboard.getorganizationappliancevpnstatuses' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationappliancevpnstatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationappliancevpnstatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationappliancevpnstatuses: {ex}")
            return {"error": str(ex)}

    def getorganizationappliancevpnthirdpartyvpnpeers(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationappliancevpnthirdpartyvpnpeers'.
        Calls 'self.dashboard.getorganizationappliancevpnthirdpartyvpnpeers' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationappliancevpnthirdpartyvpnpeers(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationappliancevpnthirdpartyvpnpeers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationappliancevpnthirdpartyvpnpeers: {ex}")
            return {"error": str(ex)}

    def getorganizationappliancevpnvpnfirewallrules(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationappliancevpnvpnfirewallrules'.
        Calls 'self.dashboard.getorganizationappliancevpnvpnfirewallrules' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationappliancevpnvpnfirewallrules(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationappliancevpnvpnfirewallrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationappliancevpnvpnfirewallrules: {ex}")
            return {"error": str(ex)}

    def getorganizationassurancealert(self, organizationId, id) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationassurancealert'.
        Calls 'self.dashboard.getorganizationassurancealert' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationassurancealert(organizationId, id)
        except APIError as e:
            logging.error(f"API Error in getorganizationassurancealert: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationassurancealert: {ex}")
            return {"error": str(ex)}

    def getorganizationassurancealerts(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationassurancealerts'.
        Calls 'self.dashboard.getorganizationassurancealerts' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationassurancealerts(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationassurancealerts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationassurancealerts: {ex}")
            return {"error": str(ex)}

    def getorganizationassurancealertsoverview(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationassurancealertsoverview'.
        Calls 'self.dashboard.getorganizationassurancealertsoverview' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationassurancealertsoverview(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationassurancealertsoverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationassurancealertsoverview: {ex}")
            return {"error": str(ex)}

    def getorganizationassurancealertsoverviewbynetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationassurancealertsoverviewbynetwork'.
        Calls 'self.dashboard.getorganizationassurancealertsoverviewbynetwork' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationassurancealertsoverviewbynetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationassurancealertsoverviewbynetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationassurancealertsoverviewbynetwork: {ex}")
            return {"error": str(ex)}

    def getorganizationassurancealertsoverviewbytype(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationassurancealertsoverviewbytype'.
        Calls 'self.dashboard.getorganizationassurancealertsoverviewbytype' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationassurancealertsoverviewbytype(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationassurancealertsoverviewbytype: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationassurancealertsoverviewbytype: {ex}")
            return {"error": str(ex)}

    def getorganizationassurancealertsoverviewhistorical(self, organizationId, segmentDuration, tsStart, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationassurancealertsoverviewhistorical'.
        Calls 'self.dashboard.getorganizationassurancealertsoverviewhistorical' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param segmentDuration: (Inferred from the method signature)
        :param tsStart: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationassurancealertsoverviewhistorical(organizationId, segmentDuration, tsStart, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationassurancealertsoverviewhistorical: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationassurancealertsoverviewhistorical: {ex}")
            return {"error": str(ex)}

    def getorganizationbrandingpolicies(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationbrandingpolicies'.
        Calls 'self.dashboard.getorganizationbrandingpolicies' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationbrandingpolicies(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationbrandingpolicies: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationbrandingpolicies: {ex}")
            return {"error": str(ex)}

    def getorganizationbrandingpoliciespriorities(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationbrandingpoliciespriorities'.
        Calls 'self.dashboard.getorganizationbrandingpoliciespriorities' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationbrandingpoliciespriorities(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationbrandingpoliciespriorities: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationbrandingpoliciespriorities: {ex}")
            return {"error": str(ex)}

    def getorganizationbrandingpolicy(self, organizationId, brandingPolicyId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationbrandingpolicy'.
        Calls 'self.dashboard.getorganizationbrandingpolicy' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param brandingPolicyId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationbrandingpolicy(organizationId, brandingPolicyId)
        except APIError as e:
            logging.error(f"API Error in getorganizationbrandingpolicy: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationbrandingpolicy: {ex}")
            return {"error": str(ex)}

    def getorganizationcameraboundariesareasbydevice(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcameraboundariesareasbydevice'.
        Calls 'self.dashboard.getorganizationcameraboundariesareasbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcameraboundariesareasbydevice(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationcameraboundariesareasbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcameraboundariesareasbydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationcameraboundarieslinesbydevice(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcameraboundarieslinesbydevice'.
        Calls 'self.dashboard.getorganizationcameraboundarieslinesbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcameraboundarieslinesbydevice(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationcameraboundarieslinesbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcameraboundarieslinesbydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationcameracustomanalyticsartifact(self, organizationId, artifactId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcameracustomanalyticsartifact'.
        Calls 'self.dashboard.getorganizationcameracustomanalyticsartifact' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param artifactId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcameracustomanalyticsartifact(organizationId, artifactId)
        except APIError as e:
            logging.error(f"API Error in getorganizationcameracustomanalyticsartifact: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcameracustomanalyticsartifact: {ex}")
            return {"error": str(ex)}

    def getorganizationcameracustomanalyticsartifacts(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcameracustomanalyticsartifacts'.
        Calls 'self.dashboard.getorganizationcameracustomanalyticsartifacts' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcameracustomanalyticsartifacts(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationcameracustomanalyticsartifacts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcameracustomanalyticsartifacts: {ex}")
            return {"error": str(ex)}

    def getorganizationcameradetectionshistorybyboundarybyinterval(self, organizationId, boundaryIds, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcameradetectionshistorybyboundarybyinterval'.
        Calls 'self.dashboard.getorganizationcameradetectionshistorybyboundarybyinterval' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param boundaryIds: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcameradetectionshistorybyboundarybyinterval(organizationId, boundaryIds, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationcameradetectionshistorybyboundarybyinterval: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcameradetectionshistorybyboundarybyinterval: {ex}")
            return {"error": str(ex)}

    def getorganizationcameraonboardingstatuses(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcameraonboardingstatuses'.
        Calls 'self.dashboard.getorganizationcameraonboardingstatuses' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcameraonboardingstatuses(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationcameraonboardingstatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcameraonboardingstatuses: {ex}")
            return {"error": str(ex)}

    def getorganizationcamerapermission(self, organizationId, permissionScopeId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcamerapermission'.
        Calls 'self.dashboard.getorganizationcamerapermission' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param permissionScopeId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcamerapermission(organizationId, permissionScopeId)
        except APIError as e:
            logging.error(f"API Error in getorganizationcamerapermission: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcamerapermission: {ex}")
            return {"error": str(ex)}

    def getorganizationcamerapermissions(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcamerapermissions'.
        Calls 'self.dashboard.getorganizationcamerapermissions' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcamerapermissions(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationcamerapermissions: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcamerapermissions: {ex}")
            return {"error": str(ex)}

    def getorganizationcamerarole(self, organizationId, roleId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcamerarole'.
        Calls 'self.dashboard.getorganizationcamerarole' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param roleId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcamerarole(organizationId, roleId)
        except APIError as e:
            logging.error(f"API Error in getorganizationcamerarole: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcamerarole: {ex}")
            return {"error": str(ex)}

    def getorganizationcameraroles(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcameraroles'.
        Calls 'self.dashboard.getorganizationcameraroles' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcameraroles(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationcameraroles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcameraroles: {ex}")
            return {"error": str(ex)}

    def getorganizationcellulargatewayesimsinventory(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcellulargatewayesimsinventory'.
        Calls 'self.dashboard.getorganizationcellulargatewayesimsinventory' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcellulargatewayesimsinventory(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationcellulargatewayesimsinventory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcellulargatewayesimsinventory: {ex}")
            return {"error": str(ex)}

    def getorganizationcellulargatewayesimsserviceproviders(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcellulargatewayesimsserviceproviders'.
        Calls 'self.dashboard.getorganizationcellulargatewayesimsserviceproviders' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcellulargatewayesimsserviceproviders(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationcellulargatewayesimsserviceproviders: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcellulargatewayesimsserviceproviders: {ex}")
            return {"error": str(ex)}

    def getorganizationcellulargatewayesimsserviceprovidersaccounts(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcellulargatewayesimsserviceprovidersaccounts'.
        Calls 'self.dashboard.getorganizationcellulargatewayesimsserviceprovidersaccounts' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcellulargatewayesimsserviceprovidersaccounts(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationcellulargatewayesimsserviceprovidersaccounts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcellulargatewayesimsserviceprovidersaccounts: {ex}")
            return {"error": str(ex)}

    def getorganizationcellulargatewayesimsserviceprovidersaccountscommunicationplans(self, organizationId, accountIds) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcellulargatewayesimsserviceprovidersaccountscommunicationplans'.
        Calls 'self.dashboard.getorganizationcellulargatewayesimsserviceprovidersaccountscommunicationplans' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param accountIds: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcellulargatewayesimsserviceprovidersaccountscommunicationplans(organizationId, accountIds)
        except APIError as e:
            logging.error(f"API Error in getorganizationcellulargatewayesimsserviceprovidersaccountscommunicationplans: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcellulargatewayesimsserviceprovidersaccountscommunicationplans: {ex}")
            return {"error": str(ex)}

    def getorganizationcellulargatewayesimsserviceprovidersaccountsrateplans(self, organizationId, accountIds) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcellulargatewayesimsserviceprovidersaccountsrateplans'.
        Calls 'self.dashboard.getorganizationcellulargatewayesimsserviceprovidersaccountsrateplans' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param accountIds: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcellulargatewayesimsserviceprovidersaccountsrateplans(organizationId, accountIds)
        except APIError as e:
            logging.error(f"API Error in getorganizationcellulargatewayesimsserviceprovidersaccountsrateplans: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcellulargatewayesimsserviceprovidersaccountsrateplans: {ex}")
            return {"error": str(ex)}

    def getorganizationcellulargatewayuplinkstatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationcellulargatewayuplinkstatuses'.
        Calls 'self.dashboard.getorganizationcellulargatewayuplinkstatuses' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationcellulargatewayuplinkstatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationcellulargatewayuplinkstatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationcellulargatewayuplinkstatuses: {ex}")
            return {"error": str(ex)}

    def getorganizationclientsbandwidthusagehistory(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationclientsbandwidthusagehistory'.
        Calls 'self.dashboard.getorganizationclientsbandwidthusagehistory' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationclientsbandwidthusagehistory(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationclientsbandwidthusagehistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationclientsbandwidthusagehistory: {ex}")
            return {"error": str(ex)}

    def getorganizationclientsoverview(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationclientsoverview'.
        Calls 'self.dashboard.getorganizationclientsoverview' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationclientsoverview(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationclientsoverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationclientsoverview: {ex}")
            return {"error": str(ex)}

    def getorganizationclientssearch(self, organizationId, mac, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationclientssearch'.
        Calls 'self.dashboard.getorganizationclientssearch' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param mac: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationclientssearch(organizationId, mac, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationclientssearch: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationclientssearch: {ex}")
            return {"error": str(ex)}

    def getorganizationconfigtemplate(self, organizationId, configTemplateId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationconfigtemplate'.
        Calls 'self.dashboard.getorganizationconfigtemplate' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param configTemplateId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationconfigtemplate(organizationId, configTemplateId)
        except APIError as e:
            logging.error(f"API Error in getorganizationconfigtemplate: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationconfigtemplate: {ex}")
            return {"error": str(ex)}

    def getorganizationconfigtemplates(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationconfigtemplates'.
        Calls 'self.dashboard.getorganizationconfigtemplates' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationconfigtemplates(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationconfigtemplates: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationconfigtemplates: {ex}")
            return {"error": str(ex)}

    def getorganizationconfigtemplateswitchprofileport(self, organizationId, configTemplateId, profileId, portId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationconfigtemplateswitchprofileport'.
        Calls 'self.dashboard.getorganizationconfigtemplateswitchprofileport' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param configTemplateId: (Inferred from the method signature)
        :param profileId: (Inferred from the method signature)
        :param portId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationconfigtemplateswitchprofileport(organizationId, configTemplateId, profileId, portId)
        except APIError as e:
            logging.error(f"API Error in getorganizationconfigtemplateswitchprofileport: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationconfigtemplateswitchprofileport: {ex}")
            return {"error": str(ex)}

    def getorganizationconfigtemplateswitchprofileports(self, organizationId, configTemplateId, profileId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationconfigtemplateswitchprofileports'.
        Calls 'self.dashboard.getorganizationconfigtemplateswitchprofileports' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param configTemplateId: (Inferred from the method signature)
        :param profileId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationconfigtemplateswitchprofileports(organizationId, configTemplateId, profileId)
        except APIError as e:
            logging.error(f"API Error in getorganizationconfigtemplateswitchprofileports: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationconfigtemplateswitchprofileports: {ex}")
            return {"error": str(ex)}

    def getorganizationconfigtemplateswitchprofiles(self, organizationId, configTemplateId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationconfigtemplateswitchprofiles'.
        Calls 'self.dashboard.getorganizationconfigtemplateswitchprofiles' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param configTemplateId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationconfigtemplateswitchprofiles(organizationId, configTemplateId)
        except APIError as e:
            logging.error(f"API Error in getorganizationconfigtemplateswitchprofiles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationconfigtemplateswitchprofiles: {ex}")
            return {"error": str(ex)}

    def getorganizationconfigurationchanges(self, organizationId, total_pages=1, direction='prev', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationconfigurationchanges'.
        Calls 'self.dashboard.getorganizationconfigurationchanges' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationconfigurationchanges(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationconfigurationchanges: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationconfigurationchanges: {ex}")
            return {"error": str(ex)}

    def getorganizationdevices(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationdevices'.
        Calls 'self.dashboard.getorganizationdevices' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationdevices(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationdevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationdevices: {ex}")
            return {"error": str(ex)}

    def getorganizationdevicesavailabilities(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationdevicesavailabilities'.
        Calls 'self.dashboard.getorganizationdevicesavailabilities' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationdevicesavailabilities(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationdevicesavailabilities: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationdevicesavailabilities: {ex}")
            return {"error": str(ex)}

    def getorganizationdevicesavailabilitieschangehistory(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationdevicesavailabilitieschangehistory'.
        Calls 'self.dashboard.getorganizationdevicesavailabilitieschangehistory' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationdevicesavailabilitieschangehistory(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationdevicesavailabilitieschangehistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationdevicesavailabilitieschangehistory: {ex}")
            return {"error": str(ex)}

    def getorganizationdevicesoverviewbymodel(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationdevicesoverviewbymodel'.
        Calls 'self.dashboard.getorganizationdevicesoverviewbymodel' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationdevicesoverviewbymodel(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationdevicesoverviewbymodel: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationdevicesoverviewbymodel: {ex}")
            return {"error": str(ex)}

    def getorganizationdevicespowermodulesstatusesbydevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationdevicespowermodulesstatusesbydevice'.
        Calls 'self.dashboard.getorganizationdevicespowermodulesstatusesbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationdevicespowermodulesstatusesbydevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationdevicespowermodulesstatusesbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationdevicespowermodulesstatusesbydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationdevicesprovisioningstatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationdevicesprovisioningstatuses'.
        Calls 'self.dashboard.getorganizationdevicesprovisioningstatuses' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationdevicesprovisioningstatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationdevicesprovisioningstatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationdevicesprovisioningstatuses: {ex}")
            return {"error": str(ex)}

    def getorganizationdevicesstatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationdevicesstatuses'.
        Calls 'self.dashboard.getorganizationdevicesstatuses' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationdevicesstatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationdevicesstatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationdevicesstatuses: {ex}")
            return {"error": str(ex)}

    def getorganizationdevicesstatusesoverview(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationdevicesstatusesoverview'.
        Calls 'self.dashboard.getorganizationdevicesstatusesoverview' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationdevicesstatusesoverview(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationdevicesstatusesoverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationdevicesstatusesoverview: {ex}")
            return {"error": str(ex)}

    def getorganizationdevicesuplinksaddressesbydevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationdevicesuplinksaddressesbydevice'.
        Calls 'self.dashboard.getorganizationdevicesuplinksaddressesbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationdevicesuplinksaddressesbydevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationdevicesuplinksaddressesbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationdevicesuplinksaddressesbydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationdevicesuplinkslossandlatency(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationdevicesuplinkslossandlatency'.
        Calls 'self.dashboard.getorganizationdevicesuplinkslossandlatency' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationdevicesuplinkslossandlatency(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationdevicesuplinkslossandlatency: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationdevicesuplinkslossandlatency: {ex}")
            return {"error": str(ex)}

    def getorganizationearlyaccessfeatures(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationearlyaccessfeatures'.
        Calls 'self.dashboard.getorganizationearlyaccessfeatures' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationearlyaccessfeatures(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationearlyaccessfeatures: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationearlyaccessfeatures: {ex}")
            return {"error": str(ex)}

    def getorganizationearlyaccessfeaturesoptin(self, organizationId, optInId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationearlyaccessfeaturesoptin'.
        Calls 'self.dashboard.getorganizationearlyaccessfeaturesoptin' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param optInId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationearlyaccessfeaturesoptin(organizationId, optInId)
        except APIError as e:
            logging.error(f"API Error in getorganizationearlyaccessfeaturesoptin: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationearlyaccessfeaturesoptin: {ex}")
            return {"error": str(ex)}

    def getorganizationearlyaccessfeaturesoptins(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationearlyaccessfeaturesoptins'.
        Calls 'self.dashboard.getorganizationearlyaccessfeaturesoptins' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationearlyaccessfeaturesoptins(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationearlyaccessfeaturesoptins: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationearlyaccessfeaturesoptins: {ex}")
            return {"error": str(ex)}

    def getorganizationfirmwareupgrades(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationfirmwareupgrades'.
        Calls 'self.dashboard.getorganizationfirmwareupgrades' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationfirmwareupgrades(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationfirmwareupgrades: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationfirmwareupgrades: {ex}")
            return {"error": str(ex)}

    def getorganizationfirmwareupgradesbydevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationfirmwareupgradesbydevice'.
        Calls 'self.dashboard.getorganizationfirmwareupgradesbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationfirmwareupgradesbydevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationfirmwareupgradesbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationfirmwareupgradesbydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationfloorplansautolocatedevices(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationfloorplansautolocatedevices'.
        Calls 'self.dashboard.getorganizationfloorplansautolocatedevices' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationfloorplansautolocatedevices(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationfloorplansautolocatedevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationfloorplansautolocatedevices: {ex}")
            return {"error": str(ex)}

    def getorganizationfloorplansautolocatestatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationfloorplansautolocatestatuses'.
        Calls 'self.dashboard.getorganizationfloorplansautolocatestatuses' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationfloorplansautolocatestatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationfloorplansautolocatestatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationfloorplansautolocatestatuses: {ex}")
            return {"error": str(ex)}

    def getorganizationinsightapplications(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationinsightapplications'.
        Calls 'self.dashboard.getorganizationinsightapplications' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationinsightapplications(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationinsightapplications: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationinsightapplications: {ex}")
            return {"error": str(ex)}

    def getorganizationinsightmonitoredmediaserver(self, organizationId, monitoredMediaServerId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationinsightmonitoredmediaserver'.
        Calls 'self.dashboard.getorganizationinsightmonitoredmediaserver' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param monitoredMediaServerId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationinsightmonitoredmediaserver(organizationId, monitoredMediaServerId)
        except APIError as e:
            logging.error(f"API Error in getorganizationinsightmonitoredmediaserver: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationinsightmonitoredmediaserver: {ex}")
            return {"error": str(ex)}

    def getorganizationinsightmonitoredmediaservers(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationinsightmonitoredmediaservers'.
        Calls 'self.dashboard.getorganizationinsightmonitoredmediaservers' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationinsightmonitoredmediaservers(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationinsightmonitoredmediaservers: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationinsightmonitoredmediaservers: {ex}")
            return {"error": str(ex)}

    def getorganizationinventorydevice(self, organizationId, serial) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationinventorydevice'.
        Calls 'self.dashboard.getorganizationinventorydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param serial: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationinventorydevice(organizationId, serial)
        except APIError as e:
            logging.error(f"API Error in getorganizationinventorydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationinventorydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationinventorydevices(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationinventorydevices'.
        Calls 'self.dashboard.getorganizationinventorydevices' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationinventorydevices(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationinventorydevices: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationinventorydevices: {ex}")
            return {"error": str(ex)}

    def getorganizationinventorydevicesswapsbulk(self, organizationId, id) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationinventorydevicesswapsbulk'.
        Calls 'self.dashboard.getorganizationinventorydevicesswapsbulk' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationinventorydevicesswapsbulk(organizationId, id)
        except APIError as e:
            logging.error(f"API Error in getorganizationinventorydevicesswapsbulk: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationinventorydevicesswapsbulk: {ex}")
            return {"error": str(ex)}

    def getorganizationinventoryonboardingcloudmonitoringimports(self, organizationId, importIds) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationinventoryonboardingcloudmonitoringimports'.
        Calls 'self.dashboard.getorganizationinventoryonboardingcloudmonitoringimports' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param importIds: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationinventoryonboardingcloudmonitoringimports(organizationId, importIds)
        except APIError as e:
            logging.error(f"API Error in getorganizationinventoryonboardingcloudmonitoringimports: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationinventoryonboardingcloudmonitoringimports: {ex}")
            return {"error": str(ex)}

    def getorganizationinventoryonboardingcloudmonitoringnetworks(self, organizationId, deviceType, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationinventoryonboardingcloudmonitoringnetworks'.
        Calls 'self.dashboard.getorganizationinventoryonboardingcloudmonitoringnetworks' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param deviceType: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationinventoryonboardingcloudmonitoringnetworks(organizationId, deviceType, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationinventoryonboardingcloudmonitoringnetworks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationinventoryonboardingcloudmonitoringnetworks: {ex}")
            return {"error": str(ex)}

    def getorganizationlicense(self, organizationId, licenseId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationlicense'.
        Calls 'self.dashboard.getorganizationlicense' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param licenseId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationlicense(organizationId, licenseId)
        except APIError as e:
            logging.error(f"API Error in getorganizationlicense: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationlicense: {ex}")
            return {"error": str(ex)}

    def getorganizationlicenses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationlicenses'.
        Calls 'self.dashboard.getorganizationlicenses' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationlicenses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationlicenses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationlicenses: {ex}")
            return {"error": str(ex)}

    def getorganizationlicensesoverview(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationlicensesoverview'.
        Calls 'self.dashboard.getorganizationlicensesoverview' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationlicensesoverview(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationlicensesoverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationlicensesoverview: {ex}")
            return {"error": str(ex)}

    def getorganizationlicensingcotermlicenses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationlicensingcotermlicenses'.
        Calls 'self.dashboard.getorganizationlicensingcotermlicenses' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationlicensingcotermlicenses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationlicensingcotermlicenses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationlicensingcotermlicenses: {ex}")
            return {"error": str(ex)}

    def getorganizationloginsecurity(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationloginsecurity'.
        Calls 'self.dashboard.getorganizationloginsecurity' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationloginsecurity(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationloginsecurity: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationloginsecurity: {ex}")
            return {"error": str(ex)}

    def getorganizationnetworks(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationnetworks'.
        Calls 'self.dashboard.getorganizationnetworks' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationnetworks(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationnetworks: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationnetworks: {ex}")
            return {"error": str(ex)}

    def getorganizationopenapispec(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationopenapispec'.
        Calls 'self.dashboard.getorganizationopenapispec' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationopenapispec(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationopenapispec: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationopenapispec: {ex}")
            return {"error": str(ex)}

    def getorganizationpolicyobject(self, organizationId, policyObjectId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationpolicyobject'.
        Calls 'self.dashboard.getorganizationpolicyobject' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param policyObjectId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationpolicyobject(organizationId, policyObjectId)
        except APIError as e:
            logging.error(f"API Error in getorganizationpolicyobject: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationpolicyobject: {ex}")
            return {"error": str(ex)}

    def getorganizationpolicyobjects(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationpolicyobjects'.
        Calls 'self.dashboard.getorganizationpolicyobjects' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationpolicyobjects(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationpolicyobjects: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationpolicyobjects: {ex}")
            return {"error": str(ex)}

    def getorganizationpolicyobjectsgroup(self, organizationId, policyObjectGroupId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationpolicyobjectsgroup'.
        Calls 'self.dashboard.getorganizationpolicyobjectsgroup' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param policyObjectGroupId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationpolicyobjectsgroup(organizationId, policyObjectGroupId)
        except APIError as e:
            logging.error(f"API Error in getorganizationpolicyobjectsgroup: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationpolicyobjectsgroup: {ex}")
            return {"error": str(ex)}

    def getorganizationpolicyobjectsgroups(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationpolicyobjectsgroups'.
        Calls 'self.dashboard.getorganizationpolicyobjectsgroups' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationpolicyobjectsgroups(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationpolicyobjectsgroups: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationpolicyobjectsgroups: {ex}")
            return {"error": str(ex)}

    def getorganizations(self, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizations'.
        Calls 'self.dashboard.getorganizations' with the same parameters.
        
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizations(total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizations: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizations: {ex}")
            return {"error": str(ex)}

    def getorganizationsaml(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsaml'.
        Calls 'self.dashboard.getorganizationsaml' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsaml(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationsaml: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsaml: {ex}")
            return {"error": str(ex)}

    def getorganizationsamlidp(self, organizationId, idpId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsamlidp'.
        Calls 'self.dashboard.getorganizationsamlidp' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param idpId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsamlidp(organizationId, idpId)
        except APIError as e:
            logging.error(f"API Error in getorganizationsamlidp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsamlidp: {ex}")
            return {"error": str(ex)}

    def getorganizationsamlidps(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsamlidps'.
        Calls 'self.dashboard.getorganizationsamlidps' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsamlidps(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationsamlidps: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsamlidps: {ex}")
            return {"error": str(ex)}

    def getorganizationsamlrole(self, organizationId, samlRoleId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsamlrole'.
        Calls 'self.dashboard.getorganizationsamlrole' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param samlRoleId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsamlrole(organizationId, samlRoleId)
        except APIError as e:
            logging.error(f"API Error in getorganizationsamlrole: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsamlrole: {ex}")
            return {"error": str(ex)}

    def getorganizationsamlroles(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsamlroles'.
        Calls 'self.dashboard.getorganizationsamlroles' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsamlroles(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationsamlroles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsamlroles: {ex}")
            return {"error": str(ex)}

    def getorganizationsensorreadingshistory(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsensorreadingshistory'.
        Calls 'self.dashboard.getorganizationsensorreadingshistory' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsensorreadingshistory(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsensorreadingshistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsensorreadingshistory: {ex}")
            return {"error": str(ex)}

    def getorganizationsensorreadingslatest(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsensorreadingslatest'.
        Calls 'self.dashboard.getorganizationsensorreadingslatest' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsensorreadingslatest(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsensorreadingslatest: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsensorreadingslatest: {ex}")
            return {"error": str(ex)}

    def getorganizationsmadminsrole(self, organizationId, roleId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsmadminsrole'.
        Calls 'self.dashboard.getorganizationsmadminsrole' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param roleId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsmadminsrole(organizationId, roleId)
        except APIError as e:
            logging.error(f"API Error in getorganizationsmadminsrole: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsmadminsrole: {ex}")
            return {"error": str(ex)}

    def getorganizationsmadminsroles(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsmadminsroles'.
        Calls 'self.dashboard.getorganizationsmadminsroles' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsmadminsroles(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsmadminsroles: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsmadminsroles: {ex}")
            return {"error": str(ex)}

    def getorganizationsmapnscert(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsmapnscert'.
        Calls 'self.dashboard.getorganizationsmapnscert' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsmapnscert(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationsmapnscert: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsmapnscert: {ex}")
            return {"error": str(ex)}

    def getorganizationsmsentrypoliciesassignmentsbynetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsmsentrypoliciesassignmentsbynetwork'.
        Calls 'self.dashboard.getorganizationsmsentrypoliciesassignmentsbynetwork' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsmsentrypoliciesassignmentsbynetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsmsentrypoliciesassignmentsbynetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsmsentrypoliciesassignmentsbynetwork: {ex}")
            return {"error": str(ex)}

    def getorganizationsmvppaccount(self, organizationId, vppAccountId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsmvppaccount'.
        Calls 'self.dashboard.getorganizationsmvppaccount' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param vppAccountId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsmvppaccount(organizationId, vppAccountId)
        except APIError as e:
            logging.error(f"API Error in getorganizationsmvppaccount: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsmvppaccount: {ex}")
            return {"error": str(ex)}

    def getorganizationsmvppaccounts(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsmvppaccounts'.
        Calls 'self.dashboard.getorganizationsmvppaccounts' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsmvppaccounts(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationsmvppaccounts: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsmvppaccounts: {ex}")
            return {"error": str(ex)}

    def getorganizationsnmp(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsnmp'.
        Calls 'self.dashboard.getorganizationsnmp' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsnmp(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationsnmp: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsnmp: {ex}")
            return {"error": str(ex)}

    def getorganizationsplashasset(self, organizationId, id) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsplashasset'.
        Calls 'self.dashboard.getorganizationsplashasset' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param id: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsplashasset(organizationId, id)
        except APIError as e:
            logging.error(f"API Error in getorganizationsplashasset: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsplashasset: {ex}")
            return {"error": str(ex)}

    def getorganizationsplashthemes(self, organizationId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsplashthemes'.
        Calls 'self.dashboard.getorganizationsplashthemes' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsplashthemes(organizationId)
        except APIError as e:
            logging.error(f"API Error in getorganizationsplashthemes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsplashthemes: {ex}")
            return {"error": str(ex)}

    def getorganizationsummaryswitchpowerhistory(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsummaryswitchpowerhistory'.
        Calls 'self.dashboard.getorganizationsummaryswitchpowerhistory' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsummaryswitchpowerhistory(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsummaryswitchpowerhistory: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsummaryswitchpowerhistory: {ex}")
            return {"error": str(ex)}

    def getorganizationsummarytopappliancesbyutilization(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsummarytopappliancesbyutilization'.
        Calls 'self.dashboard.getorganizationsummarytopappliancesbyutilization' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsummarytopappliancesbyutilization(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsummarytopappliancesbyutilization: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsummarytopappliancesbyutilization: {ex}")
            return {"error": str(ex)}

    def getorganizationsummarytopapplicationsbyusage(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsummarytopapplicationsbyusage'.
        Calls 'self.dashboard.getorganizationsummarytopapplicationsbyusage' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsummarytopapplicationsbyusage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsummarytopapplicationsbyusage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsummarytopapplicationsbyusage: {ex}")
            return {"error": str(ex)}

    def getorganizationsummarytopapplicationscategoriesbyusage(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsummarytopapplicationscategoriesbyusage'.
        Calls 'self.dashboard.getorganizationsummarytopapplicationscategoriesbyusage' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsummarytopapplicationscategoriesbyusage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsummarytopapplicationscategoriesbyusage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsummarytopapplicationscategoriesbyusage: {ex}")
            return {"error": str(ex)}

    def getorganizationsummarytopclientsbyusage(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsummarytopclientsbyusage'.
        Calls 'self.dashboard.getorganizationsummarytopclientsbyusage' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsummarytopclientsbyusage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsummarytopclientsbyusage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsummarytopclientsbyusage: {ex}")
            return {"error": str(ex)}

    def getorganizationsummarytopclientsmanufacturersbyusage(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsummarytopclientsmanufacturersbyusage'.
        Calls 'self.dashboard.getorganizationsummarytopclientsmanufacturersbyusage' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsummarytopclientsmanufacturersbyusage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsummarytopclientsmanufacturersbyusage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsummarytopclientsmanufacturersbyusage: {ex}")
            return {"error": str(ex)}

    def getorganizationsummarytopdevicesbyusage(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsummarytopdevicesbyusage'.
        Calls 'self.dashboard.getorganizationsummarytopdevicesbyusage' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsummarytopdevicesbyusage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsummarytopdevicesbyusage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsummarytopdevicesbyusage: {ex}")
            return {"error": str(ex)}

    def getorganizationsummarytopdevicesmodelsbyusage(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsummarytopdevicesmodelsbyusage'.
        Calls 'self.dashboard.getorganizationsummarytopdevicesmodelsbyusage' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsummarytopdevicesmodelsbyusage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsummarytopdevicesmodelsbyusage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsummarytopdevicesmodelsbyusage: {ex}")
            return {"error": str(ex)}

    def getorganizationsummarytopnetworksbystatus(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsummarytopnetworksbystatus'.
        Calls 'self.dashboard.getorganizationsummarytopnetworksbystatus' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsummarytopnetworksbystatus(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsummarytopnetworksbystatus: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsummarytopnetworksbystatus: {ex}")
            return {"error": str(ex)}

    def getorganizationsummarytopssidsbyusage(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsummarytopssidsbyusage'.
        Calls 'self.dashboard.getorganizationsummarytopssidsbyusage' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsummarytopssidsbyusage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsummarytopssidsbyusage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsummarytopssidsbyusage: {ex}")
            return {"error": str(ex)}

    def getorganizationsummarytopswitchesbyenergyusage(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationsummarytopswitchesbyenergyusage'.
        Calls 'self.dashboard.getorganizationsummarytopswitchesbyenergyusage' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationsummarytopswitchesbyenergyusage(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationsummarytopswitchesbyenergyusage: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationsummarytopswitchesbyenergyusage: {ex}")
            return {"error": str(ex)}

    def getorganizationswitchportsbyswitch(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationswitchportsbyswitch'.
        Calls 'self.dashboard.getorganizationswitchportsbyswitch' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationswitchportsbyswitch(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationswitchportsbyswitch: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationswitchportsbyswitch: {ex}")
            return {"error": str(ex)}

    def getorganizationswitchportsclientsoverviewbydevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationswitchportsclientsoverviewbydevice'.
        Calls 'self.dashboard.getorganizationswitchportsclientsoverviewbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationswitchportsclientsoverviewbydevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationswitchportsclientsoverviewbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationswitchportsclientsoverviewbydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationswitchportsoverview(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationswitchportsoverview'.
        Calls 'self.dashboard.getorganizationswitchportsoverview' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationswitchportsoverview(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationswitchportsoverview: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationswitchportsoverview: {ex}")
            return {"error": str(ex)}

    def getorganizationswitchportsstatusesbyswitch(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationswitchportsstatusesbyswitch'.
        Calls 'self.dashboard.getorganizationswitchportsstatusesbyswitch' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationswitchportsstatusesbyswitch(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationswitchportsstatusesbyswitch: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationswitchportsstatusesbyswitch: {ex}")
            return {"error": str(ex)}

    def getorganizationswitchportstopologydiscoverybydevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationswitchportstopologydiscoverybydevice'.
        Calls 'self.dashboard.getorganizationswitchportstopologydiscoverybydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationswitchportstopologydiscoverybydevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationswitchportstopologydiscoverybydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationswitchportstopologydiscoverybydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationuplinksstatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationuplinksstatuses'.
        Calls 'self.dashboard.getorganizationuplinksstatuses' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationuplinksstatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationuplinksstatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationuplinksstatuses: {ex}")
            return {"error": str(ex)}

    def getorganizationwebhooksalerttypes(self, organizationId, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwebhooksalerttypes'.
        Calls 'self.dashboard.getorganizationwebhooksalerttypes' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwebhooksalerttypes(organizationId, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwebhooksalerttypes: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwebhooksalerttypes: {ex}")
            return {"error": str(ex)}

    def getorganizationwebhookscallbacksstatus(self, organizationId, callbackId) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwebhookscallbacksstatus'.
        Calls 'self.dashboard.getorganizationwebhookscallbacksstatus' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param callbackId: (Inferred from the method signature)
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwebhookscallbacksstatus(organizationId, callbackId)
        except APIError as e:
            logging.error(f"API Error in getorganizationwebhookscallbacksstatus: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwebhookscallbacksstatus: {ex}")
            return {"error": str(ex)}

    def getorganizationwebhookslogs(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwebhookslogs'.
        Calls 'self.dashboard.getorganizationwebhookslogs' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwebhookslogs(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwebhookslogs: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwebhookslogs: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessairmarshalrules(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessairmarshalrules'.
        Calls 'self.dashboard.getorganizationwirelessairmarshalrules' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessairmarshalrules(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessairmarshalrules: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessairmarshalrules: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessairmarshalsettingsbynetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessairmarshalsettingsbynetwork'.
        Calls 'self.dashboard.getorganizationwirelessairmarshalsettingsbynetwork' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessairmarshalsettingsbynetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessairmarshalsettingsbynetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessairmarshalsettingsbynetwork: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessclientsoverviewbydevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessclientsoverviewbydevice'.
        Calls 'self.dashboard.getorganizationwirelessclientsoverviewbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessclientsoverviewbydevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessclientsoverviewbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessclientsoverviewbydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessdeviceschannelutilizationbydevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessdeviceschannelutilizationbydevice'.
        Calls 'self.dashboard.getorganizationwirelessdeviceschannelutilizationbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessdeviceschannelutilizationbydevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessdeviceschannelutilizationbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessdeviceschannelutilizationbydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessdeviceschannelutilizationbynetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessdeviceschannelutilizationbynetwork'.
        Calls 'self.dashboard.getorganizationwirelessdeviceschannelutilizationbynetwork' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessdeviceschannelutilizationbynetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessdeviceschannelutilizationbynetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessdeviceschannelutilizationbynetwork: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessdeviceschannelutilizationhistorybydevicebyinterval(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessdeviceschannelutilizationhistorybydevicebyinterval'.
        Calls 'self.dashboard.getorganizationwirelessdeviceschannelutilizationhistorybydevicebyinterval' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessdeviceschannelutilizationhistorybydevicebyinterval(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessdeviceschannelutilizationhistorybydevicebyinterval: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessdeviceschannelutilizationhistorybydevicebyinterval: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessdeviceschannelutilizationhistorybynetworkbyinterval(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessdeviceschannelutilizationhistorybynetworkbyinterval'.
        Calls 'self.dashboard.getorganizationwirelessdeviceschannelutilizationhistorybynetworkbyinterval' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessdeviceschannelutilizationhistorybynetworkbyinterval(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessdeviceschannelutilizationhistorybynetworkbyinterval: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessdeviceschannelutilizationhistorybynetworkbyinterval: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessdevicesethernetstatuses(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessdevicesethernetstatuses'.
        Calls 'self.dashboard.getorganizationwirelessdevicesethernetstatuses' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessdevicesethernetstatuses(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessdevicesethernetstatuses: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessdevicesethernetstatuses: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessdevicespacketlossbyclient(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessdevicespacketlossbyclient'.
        Calls 'self.dashboard.getorganizationwirelessdevicespacketlossbyclient' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessdevicespacketlossbyclient(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessdevicespacketlossbyclient: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessdevicespacketlossbyclient: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessdevicespacketlossbydevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessdevicespacketlossbydevice'.
        Calls 'self.dashboard.getorganizationwirelessdevicespacketlossbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessdevicespacketlossbydevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessdevicespacketlossbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessdevicespacketlossbydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessdevicespacketlossbynetwork(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessdevicespacketlossbynetwork'.
        Calls 'self.dashboard.getorganizationwirelessdevicespacketlossbynetwork' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessdevicespacketlossbynetwork(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessdevicespacketlossbynetwork: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessdevicespacketlossbynetwork: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessdeviceswirelesscontrollersbydevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessdeviceswirelesscontrollersbydevice'.
        Calls 'self.dashboard.getorganizationwirelessdeviceswirelesscontrollersbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessdeviceswirelesscontrollersbydevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessdeviceswirelesscontrollersbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessdeviceswirelesscontrollersbydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessrfprofilesassignmentsbydevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessrfprofilesassignmentsbydevice'.
        Calls 'self.dashboard.getorganizationwirelessrfprofilesassignmentsbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessrfprofilesassignmentsbydevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessrfprofilesassignmentsbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessrfprofilesassignmentsbydevice: {ex}")
            return {"error": str(ex)}

    def getorganizationwirelessssidsstatusesbydevice(self, organizationId, total_pages=1, direction='next', **kwargs) -> Dict[str, Any]:
        """Auto-generated method for 'getorganizationwirelessssidsstatusesbydevice'.
        Calls 'self.dashboard.getorganizationwirelessssidsstatusesbydevice' with the same parameters.
        
        :param organizationId: (Inferred from the method signature)
        :param total_pages: (Inferred from the method signature)
        :param direction: (Inferred from the method signature)
        :param kwargs: Additional request parameters
        :return: Dict[str, Any] containing the API response or an error."""
        try:
            return self.dashboard.getorganizationwirelessssidsstatusesbydevice(organizationId, total_pages, direction, **kwargs)
        except APIError as e:
            logging.error(f"API Error in getorganizationwirelessssidsstatusesbydevice: {e}")
            return {"error": str(e)}
        except Exception as ex:
            logging.error(f"Unknown error in getorganizationwirelessssidsstatusesbydevice: {ex}")
            return {"error": str(ex)}

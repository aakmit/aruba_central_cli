
from pycentral.url_utils import ConfigurationUrl, urlJoin, AOS10_URL
from pycentral.base_utils import console_logger

urls = AOS10_URL()
DEVICE_TYPES = ["IAP", "ArubaSwitch", "CX", "MobilityController"]
logger = console_logger("CONFIGURATION")


class AOS10(object):

    def get_config_committed(self, conn,group_name,limit=0,offset=0):
        path = urls.GATEWAY["GET_CONFIG"]        
        
        params = {
            "limit": 0, 
            "offset": 0, 
            "group_name": group_name
        }
        resp = conn.command(apiMethod="GET", apiPath=path, apiParams=params)
        return resp
    
    def get_config_effective(self, conn,group_name,limit=0,offset=0):
        path = urls.GATEWAY["GET_CONFIG"]        
        
        params = {
            "limit": 0, 
            "offset": 0, 
            "group_name": group_name
        }
        resp = conn.command(apiMethod="GET", apiPath=path, apiParams=params)
        return resp
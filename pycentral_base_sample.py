# MIT License
#
# Copyright (c) 2020 Aruba, a Hewlett Packard Enterprise company

# Import Aruba Central Base

from pycentral.base import ArubaCentralBase
""" Define pycentral from folder-name"""
from pycentral.workflows.workflows_utils import *  
from pycentral.device_inventory import Inventory
from pprint import pprint
import json

# Create an instance of ArubaCentralBase using API access token
# or API Gateway credentials.
central_info = {
                
    "base_url": "https://internal-apigw.central.arubanetworks.com",
    #"base_url": "https://apigw-apaceast.central.arubanetworks.com",
    "token" : {"access_token": "uunhVv1r4Yr0NM3Zf5P8G54YUee1hScC"}
}
ssl_verify = True
central = ArubaCentralBase(central_info=central_info,
                           ssl_verify=ssl_verify)
#central_data1= "central_data.yml"
#central = get_conn_from_file(central_data1,account="vorawut_sg", logger=None)

# Sample API call using 'ArubaCentralBase.command()'
# GET groups from Aruba Central
#data1 = Inventory()
#resp = data1.get_inventory(central,sku_type="all",limit=0,offset=0)
#pprint (resp)
from pycentral.msp_config import Tenant
from pycentral.configuration_bak import *
from pycentral.monitoring import *

g = Groups()
ap = Wlan()
ap_conf = ApConfiguration()
wlan_body = {
  "wlan": {
    "essid": "Telkom-WiFi",
    "type": "employee",
    "hide_ssid": False,
    "vlan": "1",
    "wpa_passphrase": "Admin@123",
    "wpa_passphrase_changed": True,
    "is_locked": False,
    "captive_profile_name": "",
    "bandwidth_limit_peruser_up": "5000",
    "bandwidth_limit_peruser_down": "5000",

    "access_rules": [
      {
        "action": "allow",
        "eport": "any",
        "ipaddr": "any",
        "match": "match",
        "netmask": "any",
        "protocol": "any",
        "service_name": "",
        "service_type": "network",
        "sport": "any"
      }
    ]
  }
}
with open('wlan_config.json','r') as config_file:
    data = json.load(config_file)

#with open('cid.yaml', 'r') as file:
#    cinfo = yaml.safe_load(file)
print (data)
#module_resp = ap.update_wlan(central,"SG_SEATH_AOS10","Telkom",wlan_body)
#pprint(module_resp)


#module_resp = ap.create_wlan(central,"SG_SEATH_AOS10","Telkom",wlan_body)
#pprint(module_resp)

#module_resp = g.get_groups(central)
#pprint(module_resp)


#msp_info = Groups()
#msp_info = Tenant()
#resp = msp_info.get_gw_config(central,"SG_SEATH_AOS10")
#resp = msp_info.get_groups(central)
#resp = msp_info.get_tenant_info(central)
#resp2= msp_info.delete_tenant(central,"2c00eb68627311eea30596155699184f")
#resp = msp_info.create_tenant(central,"INDO-training1")
#pprint (resp)
"""
x = len(resp["msg"]["customers"])

for i in range(x):
    pprint (resp["msg"]["customers"][i]["customer_name"])
    pprint (resp["msg"]["customers"][i]["customer_id"])
    print ("\n")
#pprint (resp["msg"]["customers"][0])
"""

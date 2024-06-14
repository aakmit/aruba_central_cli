
#
# Copyright (c) 2020 Aruba, a Hewlett Packard Enterprise company
from pprint import pprint
import json
import typer
import pwinput
from rich import print
from rich.console import Console

# Import Aruba Central Base
""" Define pycentral from folder-name"""
from pycentral.push_config import *
from pycentral.base import ArubaCentralBase
from pycentral.aos10_gw import *
from pycentral.configuration import *
from pycentral.monitoring import *
from pycentral.audit_logs import *
from pycentral.rapids import *
from pycentral.workflows.workflows_utils import *  # Get central_information from file by calling this module 
from pycentral.device_inventory import Inventory

# Create an instance of ArubaCentralBase using API access token
# or API Gateway credentials.

#central_acct = input("Enter your Central Account name: ")
central_data1= "central_data.yml"
account_name = "vorawut_sg"
central = get_conn_from_file(central_data1,account=account_name, logger=None)
#central = get_conn_from_file(central_data1,account="central_acct, logger=None)

group = Groups()
wlan = Wlan()
ap_conf = ApConfiguration()
ap_setup = ApSettings()
devices = Devices()
audit = Audit()
rapids = Rogues()
console = Console()
gateway= AOS10()

app = typer.Typer(help="show AP neighbor under global level or specific group ")

@app.command()
def show_group(offset: int = typer.Option(default=0),limit: int = typer.Option(default=20)):
  module_resp = group.get_groups(central,offset,limit)
  pprint(module_resp)


@app.command()
def assign_license(license_type: str = typer.Argument(help="type of license ie: foundation_ap"),
                   device_sn: str = typer.Argument(help=" ap serial in json format ap_sn.json ")):

  with open(device_sn,'r') as config_file:
    ap_sn = json.load(config_file)
  
  wlan_data = {}
  wlan_data.update(ap_sn)
  wlan_data['services']=[license_type]

  apiPath = "/platform/licensing/v1/subscriptions/assign"  
  apiMethod = "POST" 
  apiData = wlan_data
  base_resp = central.command(apiMethod=apiMethod,
                              apiPath=apiPath,
                              apiData=apiData
                              )
  pprint(base_resp)

@app.command()
def show_rapid(group: str = typer.Option(default=""),
                         label: str = typer.Option(default="")):
  resp = rapids.list_interfering_aps(central,group=group,label=label)
  pprint(resp)

@app.command()
def show_interference_ap(group: str = typer.Option(default=""),
                         label: str = typer.Option(default="")):



  apiPath = "/rapids/v1/interfering_aps"
  apiMethod = "GET" 
  apiParams = {"group":group,"label":label}
  base_resp = central.command(apiMethod=apiMethod,
                              apiPath=apiPath,
                              apiParams=apiParams
                              )
  pprint(base_resp)

if __name__ == "__main__":
    app()

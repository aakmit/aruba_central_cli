import json

from rich import print
from pprint import pprint
from rich.console import Console
from pycentral.base import ArubaCentralBase
from pycentral.workflows.workflows_utils import *  # Get central_information from file by calling this module 


console = Console()

def caas_push_configuration(group_name,config_file,token,central_info,account_name):
    central = get_conn_from_file(central_info,account=account_name, logger=None)
    central_data = get_file_contents (central_info)
    
    with open(config_file,'r') as payload:
      gw_data = json.load(payload)

    apiPath = "/caasapi/v1/exec/cmd"
    apiMethod = "POST"    
    apiParams = {
            "cid": central_data[account_name]["customer_id"],
            "group_name": group_name,
        }
    apiHeaders = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token["access_token"]}",  # type: ignore
        }
    apiData=gw_data

    print(f"[bold]You are about to push changes to the account[/bold] [#ff8300]{account_name}[/#ff8300]!")
    confirm = console.input(f"Type`[bold red]confirm[/bold red]` to [red]push[/red] changes in file \
                '[cyan]{config_file}[/cyan]' to [yellow]{group_name}[/yellow]: "
        )
    if confirm == "confirm":
        print("\nConfirmation recieved!")
        print(f"Pushing configuration in [blue]{config_file}[/blue] to [green]{group_name}[/green]...\n")
                
        resp = central.command(apiMethod=apiMethod,
                           headers=apiHeaders,     
                           apiPath=apiPath, 
                           apiParams=apiParams,
                           apiData=apiData)
        
        if resp["code"] != 200:
          pprint(f"[red]Error Status Code: {resp['code']} : {resp['msg']}[/red]")
        else:
          print (resp["msg"])
    else:
      print("Aborting changes...")
      resp = ""
      exit(1)
    return 
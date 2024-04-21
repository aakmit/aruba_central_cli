#!/usr/bin/python3

from curses import raw
from re import X
from textwrap import indent
from tokenize import group
import requests
import json,csv
import base64
import yaml
import argparse
from pycentral.msp_config import Tenant
from pycentral.configuration_bak import *
from pycentral.base import ArubaCentralBase
""" Define pycentral from folder-name"""
from pycentral.workflows.workflows_utils import *  
from pycentral.device_inventory import Inventory
from pprint import pprint

class def_args():

    ## define_arguments for CLI ###
    def __init__(self):
        pass    
    
    def define_arguments():
        parser = argparse.ArgumentParser(description='############ API to get or push data to Aruba-central ############')
        subparser = parser.add_subparsers(dest='command')
        
        get_tenant_info = subparser.add_parser('get_tenant_info',help=' :Use this command to get a tenant infomations')
        get_tenant_info.add_argument('--customer_name', type=str, required=True,help='MSP customer-name can be found on Central yaml file')


        del_tenant = subparser.add_parser('del_tenant',help=':Use this command to delete a tenant on central')
        del_tenant.add_argument('--customer_name', type=str, required=True,help='MSP customer-name can be found on Central yaml file')
        del_tenant.add_argument('--tenant_id', type=str, required=True, help=' Tenant ID to be deleted')

        create_tenant = subparser.add_parser('create_tenant',help=':Use this command to create a tenant on central')
        create_tenant.add_argument('--cid', type=str, required=True,help='MSP customer-id can be found on Central')
        create_tenant.add_argument('--zone', type=str, required=True,help='cluster zone')
        create_tenant.add_argument('--customer_name', type=str, required=True, help= "a Tenant name")

        return parser
    
    def api_cmd(self,cmd):

        api_data = Tenant()
        if (cmd.command =="get_tenant_info"):
            central_info= "central_data.yml"
            central = get_conn_from_file(central_info,account=cmd.customer_name, logger=None)
            resp=api_data.get_tenant_info(central)
            x = len(resp["msg"]["customers"])
            for i in range(x):
                pprint (resp["msg"]["customers"][i]["customer_name"])
                pprint (resp["msg"]["customers"][i]["customer_id"])
                print("\n")

        elif (cmd.command =="del_tenant"):
            central_info= "central_data.yml"
            central = get_conn_from_file(central_info,account=cmd.customer_name, logger=None)
            #customer_id=cmd.tenant_id
            print (cmd)
            resp=api_data.delete_tenant(central,cmd.tenant_id)
            pprint (resp)


if __name__ == '__main__':
    parser = def_args.define_arguments()
    args = parser.parse_args()
    api_data = def_args()
    api_data.api_cmd(args)




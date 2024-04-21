# MIT License
#
# Copyright (c) 2020 Aruba, a Hewlett Packard Enterprise company
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
from pycentral.url_utils import ConfigurationUrl,TenantUrl, urlJoin
from pycentral.base_utils import console_logger
logger = console_logger("CONFIGURATION")

urls = TenantUrl()
"""
class Tenant(object):
    def get_tenant_info(self,conn):
        path = urls.TENANTS["GET_TENANT_INFO"]
        resp = conn.command(apiMethod="GET", apiPath=path, apiParams=None)
        return resp
"""

class Tenant(object):

    def get_tenant_info(self, conn, offset=0, limit=20):
        path = urls.TENANTS["GET_TENANT_INFO"]
        #path = urls.GROUPS["GET_ALL"]
        params = {
            "offset": offset,
            "limit": limit
        }
        resp = conn.command(apiMethod="GET", apiPath=path, apiParams=params)
        return resp

    def create_tenant(self, conn, customer_name):
        
        path = urls.TENANTS["CREATE_TENANT"]
        data = self._build_tenant_payload(customer_name)
        
        resp = conn.command(apiMethod="POST", apiPath=path, apiData=data)
        return resp

    def delete_tenant(self, conn, customer_id):
        path = urls.TENANTS["DELETE_TENANT"]+"/"+customer_id
        print (path)
        resp = conn.command(apiMethod="DELETE", apiPath=path, apiData=None)
        return resp

    def get_gw_config(self, conn, group_name):
        path = urls.GATEWAY["GET_CONFIG"]
        
        payload_json = {
            "group_name": group_name
            }

        resp = conn.command(apiMethod="GET", apiPath=path, apiData=payload_json)
        return resp



    def _build_tenant_payload(
            self,
            customer_name):
  
        payload_json = {
            "customer_name": customer_name,
            "group": {"name": "default"},
            "description" : customer_name
            }
        return payload_json
    

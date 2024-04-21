# pycentral_cli
using pycentral to create CLI command  to get, update, delete configuration in central
we are tested with Python3.12

# Download or clone this project 
```
git clone https://github.com/aakmit/aruba_central_cli.git
```

# install virtualenv 
```
cd pycentral_cli/Pycentral
virtualenv -p python3 venv 
```

# activate virtualenv
```
source ./venv/bin/activate 
```
# install package requirements
```
pip3 install -r requirements.txt
```
# update Aruba central information 
```
you have to update Aruba Central information before run the script, 
edit central_data.yml file, ie client_id,client_secret,customer_id, base URL

Note:leave the password field blank, the script will prompt to ask the password when you run the script

############################ central_data.yml sample config ###############
central_acc1:
  username: "vorawut.k@arubaseath.com"
  password: "xxxx"        --> add any dummy password, it will prompt to ask password when running the script 
  client_id: "XXXX"
  client_secret: "XXXX"
  customer_id: "XXXX"
  base_url: "https://internal-apigw.central.arubanetworks.com"

singapore_seath:
  username: "vorawut.k@arubaseath.com"
  password: "xxxx"        --> add any dummy password, it will prompt to ask password when running the script 
  client_id: "XXXXX"
  client_secret: "XXX"
  customer_id: "XXXX"
  base_url: "https://apigw-apaceast.central.arubanetworks.com"

token_store:
  type: "local"
  path: "temp"
ssl_verify: true
#######################################################################
```


# using pycentral-CLI

Note: after updated the Central information, you have to update which central-account name that you want to access.

edit the file name "pycentral_function.py" (find the row below)

central_data1= "central_data.yml"

central = get_conn_from_file(central_data1,account="**_account-name-from central_data.yml_**", logger=None)

```
python3 pycentral_call.py --help

Usage: pycentral_call.py [OPTIONS] COMMAND [ARGS]...                                                                                                                                       
                                                                                                                                                                                            
 show AP neighbor under global level or specific group                                                                                                                                      
                                                                                                                                                                                            
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                                                                  │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                                                           │
│ --help                        Show this message and exit.                                                                                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ change-wlan-status                                                                                                                                                                       │
│ clone-group                                                                                                                                                                              │
│ create-new-wlan                                                                                                                                                                          │
│ delete-device                                                                                                                                                                            │
│ list-aps                                                                                                                                                                                 │
│ move-device                                                                                                                                                                              │
│ replace-ap-config                        Replace All AP configuration from Group level                                                                                                   │
│ show-ap-config                           show All AP configuration from Group level                                                                                                      │
│ show-ap-settings                         show ap setting individual by Serial number                                                                                                     │
│ show-events-detail                                                                                                                                                                       │
│ show-group                                                                                                                                                                               │
│ show-neighbor-aps                                                                                                                                                                        │
│ update-11a-radio                                                                                                                                                                         │
│ update-11g-radio                                                                                                                                                                         │
│ update-ap-settings                       Update individual AP ie hostname,ip-address etc.                                                                                                │
│ update-config-wlan                       update basic wlan config ie. ESSID, policy firewall, BW control etc.                                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

# Sample output show AP-group 
```
python3 pycentral_call.py show-group

'msg': {'data': [['AIS-AOS10'],
                  ['AIS-Test'],
                  ['AOS10-GW-only'],
                  ['default'],
                  ['Microbranch-Deployment'],
                  ['SDBranch-SAAS'],
                  ['SEATH_VPNC'],
                  ['SG_SEATH_AOS10'],
                  ['Telkom-POC'],
                  ['TH_SEATH_AOS10'],
                  ['TH_Supalai_AOS10'],
                  ['unprovisioned']],
         'total': 12}}
(venv_2024) vorawut@Vorawuts-MacBook-Pro-2 pycentral % 
```

import requests
import json

url = 'http://192.168.2.16/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}

# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1
# }

# to aquire token

# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }

# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "filter": {
#             "host": [
#                 "Zabbix server",
#                 "Linux server"
#             ]
#         }
#     },
#     "auth": "ed512e79e1ae8e9ab939f57c240af41c",
# #     "id": 1
# }

# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "ed512e79e1ae8e9ab939f57c240af41c",
#     "id": 1
# }


# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "ed512e79e1ae8e9ab939f57c240af41c",
#     "id": 1
# }


data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "pyadd_host",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.2.11",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10081"
            }
        ],
        "inventory_mode": 0,    #host list----host asset records
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "ed512e79e1ae8e9ab939f57c240af41c",
    "id": 1
}


r = requests.post(url, headers = headers, data = json.dumps(data))
print(r.json())


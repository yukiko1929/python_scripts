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

# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }

data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "filter": {
            "host": [
                "Zabbix server",
                "Linux server"
            ]
        }
    },
    "auth": "2ad0573d4f39d852a98b10e37808eb15",
    "id": 1
}

r = requests.post(url, headers = headers, data = json.dumps(data))
print(r.json())
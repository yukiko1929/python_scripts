import json
import requests
#import sys


def send_msg(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": True,   # 不@所有人
        },
        "text": {
            "content": msg,   # 消息正文
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == '__main__':
    msg = '别闹了皮皮虾'
    reminders = ['17711625186']  # 特殊提醒要查看的人,就是@某人一下
    url = 'https://oapi.dingtalk.com/robot/send?access_token=a660d286370aa3a82e1e8e16f4186abd86553d4746bc3ab28ba51eaf724a9714'
    print(send_msg(url, reminders, msg))
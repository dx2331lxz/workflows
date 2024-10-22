import json

import requests

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send"

headers = {
    "Content-Type": "application/json",
}

params = {
    "key": "6157cdf4-08b7-4513-a30c-2ed9378f1c2f"
}

# {
#     "user":"linchunming",
#     "items":[
#         {
#             "id":1,
#             "content": "组织新生吃饭，叫学长（本届的同学多拉拉，毕竟是情况，拉人越多均摊越少）",
#             "ddl": "2024-10-24"
#         },
#         {
#             "id":2,
#             "content":"搭建教学计划网站",
#             "ddl":"2024-10-26"
#         }
#     ]
# }
def getmsg():
    # 打开todo.json
    with open("todo.json", "r") as f:
        todo = json.load(f)

    # 获取用户
    user = todo["user"]
    # 获取items
    items = todo["items"]
    content = ''
    for item in items:
        # 获取id
        id = item["id"]
        # 获取content
        content = item["content"]
        # 获取ddl
        ddl = item["ddl"]
        content = content + f"{id}\ncontent: {content}\nddl: {ddl}\n"

    return user, content
        
        

user, content = getmsg()

data = {
    "msgtype": "text",
    "text": {
        "content": "今日待办事项:\n" + content,
        "mentioned_list": [user],
    }
}

response = requests.post(url, headers=headers, params=params, json=data)
if response.status_code == 200:
    print("发送成功")
else:
    # 记录日志
    with open("log.txt", "a") as f:
        f.write(json.dumps(response.json()) + "\n")

    print("发送失败")
    print(response.json())



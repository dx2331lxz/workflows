import json
import requests

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send"

headers = {
    "Content-Type": "application/json",
}

params = {
    "key": "6157cdf4-08b7-4513-a30c-2ed9378f1c2f"
}

def getmsg():
    try:
        # 打开todo.json
        with open("todo.json", "r") as f:
            todo = json.load(f)
    except FileNotFoundError:
        print("todo.json 文件未找到")
        return None, None

    # 获取用户
    user = todo["user"]
    # 获取items
    items = todo["items"]

    # 初始化content
    content = ''
    for item in items:
        # 获取id, content 和 ddl
        id = item["id"]
        item_content = item["content"]
        ddl = item["ddl"]
        # 正确拼接消息内容
        content += f"ID: {id}\n内容: {item_content}\n截止日期: {ddl}\n\n"

    return user, content

user, content = getmsg()

if user and content:
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
        # 记录失败的日志
        with open("log.txt", "a") as f:
            f.write(json.dumps(response.json(), ensure_ascii=False) + "\n")

        print("发送失败")
        print(response.json())
else:
    print("用户或待办事项内容获取失败")
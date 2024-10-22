import json

import requests

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send"

headers = {
    "Content-Type": "application/json",
}

params = {
    "key": "6157cdf4-08b7-4513-a30c-2ed9378f1c2f"
}

data = {
    "msgtype": "text",
    "text": {
        "content": "别忘记提交今天的日报",
        "mentioned_list": ["luxiuzhe"],
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



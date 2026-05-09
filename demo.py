import requests

url =  "http://localhost:11434"

headers = {
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek-r1:1.5b",
    "messages":[{
        "role":"system",
        "content":"必须使用中文回复"
    },
    {
    "role":"user",
    "content":"hello,world"}],
    "stream": False
}

response = requests.post(f"{url}/api/chat", json=data, headers=headers)

print(response.json())
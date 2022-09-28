
"""
1.接口地址
2.请求方法
3.请求参数
4.响应参数

get：param
没有请求体，param就是追加在url后面的查询参数

post；data，json
请求体
data：字典，对应的默认body格式：application/x-www-form-urlencoded
json: 字典。对应的默认body格式：application/json
"""

import requests

# requests.Response
url = "http://api.lemonban.com/futureloan/member/register"
data = {"mobile_phone":"18600001111","pwd":"12345678"}
headers = {'X-Lemonban-Media-Type':'lemonban.v2'}
resp = requests.post(url,json=data,headers=headers)

# 响应状态码
print(resp.status_code)
# 响应头
print(resp.headers)
# 响应体
body = resp.text
print(body)
print(type(body))

# 响应体转换为python的字典
body_j = resp.json()
print(body_j)
print(type(body_j))


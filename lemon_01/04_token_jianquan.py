"""
第一步：登陆，获取token值
登陆url: url = "http://api.lemonban.com/futureloan/member/login"
请求类型：post
请求数据：
    datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}
响应数据中获取token值：token = resp.json()["data"]["token_info"]["token"]

第二步：给上一步用户进行操作，请求头当中，Authorization中设置为Bearer {token}
充值url：http://api.lemonban.com/futureloan/member/recharge
请求类型：post
请求数据：datas = {"member_id": 200119, "amount": 2000}
"""

import requests

headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
login_url = "http://api.lemonban.com/futureloan/member/login"
login_datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}

# 登录，得到token
resp = requests.post(login_url,json=login_datas,headers=headers)
resp_dict = resp.json()
print(resp_dict)

token = resp_dict["data"]["token_info"]["token"]
member_id = resp_dict["data"]["id"]
print(token)

# 充值接口，将token添加到请求头（Authorization：Bearer token值）
headers["Authorization"] = "Bearer {}".format(token)
recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
recharge_data = {"member_id": member_id, "amount": 2000}
resp = requests.post(recharge_url,json=recharge_data,headers=headers)
print(resp.json())

"""
第一步：登陆，获取cookies
登陆url: https://www.ketangpai.com/UserApi/login
请求类型：post
请求体格式：application/x-www-form-urlencoded
请求数据：
    datas = {"email":"2501768591@qq.com",
             "password":"nmb_python",
             "remember":0}
响应结果：
{"status":1,"url":"\/Main\/index.html","token":"MDAwMDAwMDAwMMurrpWavLehhs1-mbKpfZSEzX_NfXV7qcRr2Z97n6Gas4Wt14LStKuYu4vZyKykzH_Nodx9dXuaxaa3m5Z8iGHHiZXQgs_VsIW4oN6yqYHahN2LlpeDbm0","isenterprise":0,"uid":"MDAwMDAwMDAwMLWGtdyH37-y"}
cookies在响应头当中，有一个set-cookie

第二步：获取用户信息
接口url: https://www.ketangpai.com/UserApi/getUserInfo
请求方法：get
请求参数：无

Session类：创建一个会话对象，发起请求，持续访问
"""

import requests

login_url = "https://www.ketangpai.com/UserApi/login"
login_datas = {"email":"2501768591@qq.com",
             "password":"nmb_python",
             "remember":0}
userinfo_url = "https://www.ketangpai.com/UserApi/getUserInfo"

# 第一种方式
# 实例化Session对象
s = requests.Session()
# 登陆，得到cookie鉴权
s.post(login_url,data=login_datas)
# 主动会将响应的set-cookies添加到s对象当中
print(s.cookies)
# 获取用户信息
resp = s.get(userinfo_url)
print(resp.json())

# 第二种方式
# 登陆，得到cookie鉴权
resp = requests.post(login_url,data=login_datas)
# 获取cookie
cookies = resp.cookies
# 获取用户信息
resp = requests.get(userinfo_url,cookies=cookies)
print(resp.json())
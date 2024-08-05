import requests

#-------------
# 请求  创建会话
url = 'http://10.0.5.159:8881/complaints/pc/main/login.do?'
req_data = {
   'strAccount' : '18300000001',
    'strPasswd' :'123@Qwe',
    'Qwe&strApp': 'hexi'
}

session = requests.Session()
res = session.get(url =url ,params = req_data)
print(res.text)


#-------------
# 请求  创建会话
url = 'http://10.0.5.17:9988/user/login?'
req_data = {
   'username' : 'admin',
    'password' :'Pass1word01!',
    'nonceStr' : '9716b914cfb044878fa03a7dd02e4363',
    'value':'82'
    }

session = requests.Session()
res = session.get(url =url ,params = req_data)
print(res.text)


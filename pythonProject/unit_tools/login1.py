import requests
# 导入cookie组件
from requests import utils
# 导入返回值编码模块
import re


class SendRequests:
    def __init__(self):
        pass

    # 封装request方法
    def send_request(self, **kwargs):
        # 创建一个会话
        session = requests.session()
        response = None
        try:
            # 请求
            response = session.request(**kwargs)
            # 获取返回值的cookie
            set_cookie = requests.utils.dict_from_cookiejar(response.cookies)
            if set_cookie:
                print(f'获取到cookie：{set_cookie}')




        except requests.exceptions.ConnectionError:
            print("接口请求异常，可能是request的连接数过多或者速度过快导致程序报错")
        except requests.exceptions.RequestException as e:
            print("请求异常，请检查系统或数据是否正常")

        return response

    # 封装执行请求
    def execute_api_request(self, api_name, url, method, header, case_name, cookie=None, file=None, **kwargs):
        # 此种注释的打印方式，按住shift，再按三次双引号键
        """
        :param api_name:接口名称
        :param url:接口地址
        :param method:请求方法
        :param header:请求头
        :param case_name:测试用例名称
        :param cookie:cookie
        :param file:文件上传
        :param kwargs:未知数量关键字参数
        :return:
        """
        # 调用封装的方法    verify 参数忽略https证书校验
        response = self.send_request(method=method,
                                     url=url,
                                     headers=header,
                                     cookies=cookie,
                                     files=file,
                                     timeout=10,
                                     verify=False,
                                     **kwargs
                                     )


if __name__ == '__main__':


    url_login = 'http://10.0.5.159:8881/complaints/pc/main/login.do?'
    data_login = {
        'strAccount': '18300000001',
        'strPasswd': '123@Qwe',
        'Qwe&strApp': 'hexi'
    }
    header_login = {
        'Accept': 'application/json, text/plain, */*'
    }

    method_login = 'get'

    send = SendRequests()
    response = send.execute_api_request(api_name=None, url=url_login, method=method_login, header=header_login,
                             case_name=None,
                             data=data_login)
    print(response.text)
'''

url = 'http://10.0.5.159:8881/complaints/pc/main/login.do?'
req_data = {
   'strAccount' : '18300000001',
    'strPasswd' :'123@Qwe',
    'Qwe&strApp': 'hexi'
}

session = requests.Session()
res = session.get(url =url ,params = req_data)
print(res.text)
'''


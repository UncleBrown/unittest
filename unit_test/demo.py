#coding:utf-8
import requests
import unittest
import json

class Case(unittest.TestCase):

    #注意，类的变量引用，采取class.var
    url = 'http://192.168.16.223:10001/vmis/push_info'
    #request请求中需要json.dumps格式化字典
    data = [{
        "site_id": 27,
        "channel_name": "",
        "priority":1,
        "push_sum":-1
    }]
    headers = {
        'Content-Type':'application/json'
    }

    def test_case01(self):
        #post请求：请求正文是application/x-www-form-urlencoded
        response = requests.post(url=Case.url,data=json.dumps(Case.data),headers=Case.headers)

        #unittest断言方法~
        self.assertEqual(response.status_code,200,'返回状态错误，不为200')
        print('接口正常')

    @unittest.skip('跳过用例')
    def test_case02(self):
        response = requests.get(url='xxx')
        # print(response1.text)
        self.assertEqual(response.status_code, 400, '返回状态错误，不为400')
        print('接口正常')

#if __name__ == '__main__':
#    unittest.main()
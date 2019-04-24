import requests

#对requests进行二次封装
class Runmain:

    #发送post请求
    def send_post(self,url,data,headers):
        response = requests.post(url=url,data=data,headers=headers).json()
        return response
        # return json.dumps(response,sort_keys=True,indent=4)

    #发送get请求
    def send_get(self,url,params,headers):
        response = requests.get(url=url,params=params,headers=headers).json()
        return response
        # return json.dumps(response,sort_keys=True,indent=4)

    #根据请求方法自行选择
    def run_main(self,url,params,data,headers,method):
        respose = None
        if method == 'GET':
            response = self.send_get(url,params,headers)
        elif method == 'POST':
            response = self.send_post(url,data,headers)
        else:
            print("[info]:Method err")
        return response

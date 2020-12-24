import requests

class RunMethod:

    def run_main(self,method,url,data=None,headers=None):
        method = method.lower()
        res = None
        if method =='post':
            if headers != None:
                res = requests.post(url=url,data=data,headers=headers,timeout=10,verify=False)
            else:
                res = requests.post(url=url,data=data,timeout=10,verify=False)

        elif method=='jsonpost':
            if headers != None:
                res=requests.post(url=url,data=data,headers=headers,timeout=10,verify=False)
            else:
                res=requests.post(url=url,data=data,timeout=10,verify=False)

        elif method=='get':
            if headers != None:
                res=requests.get(url=url,data=data,headers=headers,timeout=10,verify=False)
            else:
                res=requests.get(url=url,data=data,timeout=10,verify=False)
        elif method == 'paramsget':
            if headers != None:
                res = requests.get(url=url, params=data, headers=headers, timeout=10, verify=False)
            else:
                res = requests.get(url=url, params=data, timeout=10, verify=False)
        else:
            print('没有这个类型的请求')
        return res
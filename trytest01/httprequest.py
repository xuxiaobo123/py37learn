import requests
import unittest

url='http://apis.juhe.cn/lottery/query?lottery_id=ssq&lottery_no=&key=3d2205fa2ac13db3e3d9c6a7cb036df2'
#简单的get post请求
#get
print(requests.get(url))
#返回http状态码

print(type(requests.get(url).text)) #返回str值
response=requests.get(url).json()   #dict--推荐返回dict值    可以根据key取值

#进行get  post    参数与URL分开传递  json    dict    方式去传参
url_2='http://apis.juhe.cn/lottery/query'
param_2={'lottery_id':'ssq','key':'3d2205fa2ac13db3e3d9c6a7cb036df2'}
response_2=requests.post(url_2,param_2).json()
print(response_2)

print(1)

print("hello")
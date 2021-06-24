import requests
import time
a=requests.post("http://okr.35.com/api/v2/create_member_daily",data={'token':'1deea547538ff668b03b803a748ad41ab0683b9f','plan':'11111','summary':'22222','improvement':'33333','date':time.strftime("%Y-%m-%d", time.localtime()),'status':1})
print(a.text)
print(a.request.body)
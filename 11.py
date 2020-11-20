import requests
u='http://118.24.105.78:2333/showversion'    #新测谈网地址
res=requests.get(url=u)
assert  res.status_code==200
assert  res.json()['status']==200
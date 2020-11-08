import requests
# http://192.144.148.91:2333/showversion
u='http://192.144.148.91:2333/showversion'
res=requests.get(url=u)
assert  res.status_code==200
assert  res.json()['status']==200
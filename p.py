import requests
URL = "http://127.0.0.1:8000/pm/"
r=requests.get(url=URL)
data=r.json()
print(data)

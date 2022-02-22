import requests
import json
#Headers={'Accept':'*/*','Content-Type':'application/json'}
#r=requests.get('http://localhost:8000/#/model/c812adb0-9e5c-49b8-b737-5632947df03a',headers=Headers)
r=requests.get('https://eggplant-partners.dai.eggplant.cloud/models')
print(r.status_code)
print(r.reason)
print(r.text)
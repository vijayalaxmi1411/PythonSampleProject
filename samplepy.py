import requests
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get("http://dummy.restapiexample.com/api/v1/employees",headers=headers)
print(response.status_code)

# import requests
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# response = requests.get("http://dummy.restapiexample.com/api/v1/employees",headers=headers)
# print(response.status_code)
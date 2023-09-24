import requests
import json
import jsonpath

response = requests.get("https://reqres.in/api/users?page=2")
# print(response.status_code)
# print(response.content)
# print(response.headers)
jsonData = json.loads(response.text)
#print(jsonData)
pages=jsonpath.jsonpath(jsonData,"total_pages")
print(pages)
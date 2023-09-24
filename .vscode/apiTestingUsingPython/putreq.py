import requests
import json
import jsonpath

file = open("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\.vscode\\apiTestingUsingPython\\inputdataupdated.json",'r')
jsonInput=file.read()
jsonData=json.loads(jsonInput)
response=requests.put("https://reqres.in/api/users/2",jsonData)
#print(response.status_code)
resData = json.loads(response.text)
data=jsonpath.jsonpath(resData,"job")
print(data)
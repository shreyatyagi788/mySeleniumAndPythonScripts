import requests
import json

def test_createNewUser():
    file = open("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\.vscode\\apiTestingUsingPython\\inputdata.json",'r')
    jsonInput=file.read()
    jsonData=json.loads(jsonInput)
    print(jsonData)
    response=requests.post("https://reqres.in/api/users",jsonData)
    print(response.content)
    print(response.status_code)
    print(response.headers.get('content-type'))
    resData=json.loads(response.text)
    id = resData.get('id')
    print(id)


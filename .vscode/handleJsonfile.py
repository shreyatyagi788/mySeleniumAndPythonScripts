import json
file=open("store.json","r")
finalData=file.read()
x=json.loads(finalData) #json.loads fn loads/converts the json data in dict format
# print(finalData)
# print(type(finalData)) 
z=json.dumps(finalData) #json.dumps loads/converts the data in string format
# print(type(z))
# print(z)
print(x)
print(type(x))

with open('writejsonfile','w') as a:
    a.writelines(z)

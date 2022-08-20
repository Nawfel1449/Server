import requests
import json
import time

url1 = "http://127.0.0.1:5000/?ID="
url = "http://127.0.0.1:5000/list?ID="




f = open('EphKeys_1024.json', 'r') 
data = f.read()
records = json.loads(data)
start = time.time()


for record in records:
    requests.get(url1+record['ID']).json()
end = time.time()

print("single request took :", end-start)


####send a list to request

start = time.time()

IDs = ''
for record in records:
    IDs += record['ID']
    IDs += ','

requests.get(url+IDs).json()
end = time.time()
print("list request took :", end-start)

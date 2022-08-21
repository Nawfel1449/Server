import requests
import json
import time

#url1 = "http://127.0.0.1:5000/?ID="
#url = "http://127.0.0.1:5000/list?ID="

url1 = "https://pfe-art-blockchain.herokuapp.com/?ID="
url2 = "https://pfe-art-blockchain.herokuapp.com/list?ID="


url3 = "http://127.0.0.1:5000/?ID="
url4 = "http://127.0.0.1:5000/keys?keys="


for i in range(1,14) :
    start = time.time() 
    print(requests.get(url4+str(pow(2, i))))
    end = time.time()
    print("took", end - start)
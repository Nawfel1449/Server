import requests
import json
import time
from ART import *

#url1 = "http://127.0.0.1:5000/?ID="
#url = "http://127.0.0.1:5000/list?ID="

url1 = "https://pfe-art-blockchain.herokuapp.com/?ID="
url2 = "https://pfe-art-blockchain.herokuapp.com/list?ID="


url3 = "http://127.0.0.1:5000/?ID="
url4 = "http://127.0.0.1:5000/keys?keys="

url5 = "https://pfe-art-blockchain.herokuapp.com/keys?keys="

setup = randint(1, int(P-1))
SETUP = pow(G, setup, P)

url6 = "http://127.0.0.1:5000/SetTree?tree="
url7 = "https://pfe-art-blockchain.herokuapp.com/SetTree?tree="

requests.get(url6+"?tree=156451,5654")



for i in range(1,11) :
    print("*"*40)
    print("number of keys : ", pow(2, i))
    start = time.time() 
    keyss = requests.get(url4+str(pow(2, i))).json()
    end = time.time()
    print("took", end - start)


    getting_keys_time = end - start

    start = time.time()
    NumberOfKeys = pow(2, i)
    PublicKeys = list()
    for key in keyss:
        PublicKeys.append(int(key))
    leafkeys = LeafKeys(PublicKeys, setup)
    #print("[i]leaf Keys            :",leafkeys[0])
    PrivateTree = Tree_To_Array(TreeBasedGroupDiffieHellman(leafkeys, NumberOfKeys)) 
    pubtree = Public_Tree(PrivateTree)
    tree = ""
    end = time.time()
    ART_TIME = end- start
    for t in pubtree:
        tree =tree + str(t) +','
    params = {'tree': pubtree}


    start = time.time()
    ers =requests.get(url6+tree).content
    end = time.time()
    req = end-start
    print("request took :", end-start)
  

    print("[i] Number of groupe participants :" , NumberOfKeys)
    print("[!] Time took to request {} keys : {} s".format(NumberOfKeys, getting_keys_time))
    print("[i]ART tree creation Time         : ", ART_TIME)
    print("[i]Totale Time :",getting_keys_time+ART_TIME+req)
   


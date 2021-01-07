import requests
import json
URL = "http://127.0.0.1:8000/pm/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    d=r.json()
    print(d)
#get_data()

def post_data():
    data={'name':'golu','roll':22,'city':'varanasi'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    d=r.json()
    print(d)
#post_data()

def update_data():
    data={'id':5,'name':'raman','city':'varanasi'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    d=r.json()
    print(d)
#update_data()

def delete_data():
    data={'id':6}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    d=r.json()
    print(d)
#delete_data()


if __name__ == "__main__" :
    print("1.Get_data\n2.insert_data\n3.update_data\n4.delete_data\n")
    n=int(input("Enter the choice:  "))
    if(n==1): get_data()
    elif(n==2): post_data()
    elif(n==3): update_data()
    elif(n==4): delete_data()
    else: print("invalid number\n")
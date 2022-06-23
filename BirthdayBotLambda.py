import csv
from datetime import date
import os
from twilio.rest import Client

today = date.today().strftime("%m/%d/20%y")
birthday = ""
validBirthday = False

with open('birthdaySheet.csv', newline= '') as f:
    r = csv.DictReader(f)
    for row in r:
        if row["Date"] == today and row["Name"] != "":
            birthday = row["Name"]
            validBirthday = True
            break
print(birthday)
print(bool(validBirthday))

if validBirthday:
    account_sid = os.environ["account-sid"]
    auth_token  = os.environ["auth-token"]
    
    
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=os.environ["destination-num"], 
        from_=os.environ["twil-num"],
        body="Today is " + birthday +"'s Birthday")

    print(message.sid)



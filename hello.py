import csv
from datetime import date
import os
from twilio.rest import Client

today = date.today().strftime("%m/%d")
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
    account_sid = "AC43e6c1f96fe54febfef95ffa4d3a4c9f"
    auth_token  = "fc1c8bc246e97e8603423046b71478e5"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+17723189401", 
        from_="+15189753388",
        body="Today is " + birthday +"'s Birthday")

    print(message.sid)



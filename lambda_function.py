import base64
import json
import csv
from datetime import date
import os
import urllib
from urllib import request, parse


TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

def lambda_handler(event, context):
    to_number = os.environ['To']
    from_number = os.environ['From']

    if not TWILIO_ACCOUNT_SID:
        return "Unable to access Twilio Account SID."
    elif not TWILIO_AUTH_TOKEN:
        return "Unable to access Twilio Auth Token."
    elif not to_number:
        return "The function needs a 'To' number in the format +12023351493"
    elif not from_number:
        return "The function needs a 'From' number in the format +19732644156"

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
    #print(birthday)
    #print(bool(validBirthday))

    if validBirthday:

        # insert Twilio Account SID into the REST API URL
        populated_url = TWILIO_SMS_URL.format(TWILIO_ACCOUNT_SID)
        post_params = {"To": to_number, "From": from_number, "Body": ("Today is "+ birthday + "'s birthday!")}

        # encode the parameters for Python's urllib
        data = parse.urlencode(post_params).encode()
        req = request.Request(populated_url)

        # add authentication header to request based on Account SID + Auth Token
        authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        base64string = base64.b64encode(authentication.encode('utf-8'))
        req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))

        try:
            # perform HTTP POST request
            with request.urlopen(req, data) as f:
                print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
        except Exception as e:
            # something went wrong!
            return e

        return "SMS sent successfully!"
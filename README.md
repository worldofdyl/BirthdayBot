# BirthdayBot
Automated Python program to send messages via SMS through Twilio to send birthday date reminders. Hosted on AWS Lambda

lambda_function.py uses a locally stored csv on Lambda. CSV and function.py can be added to Lambda using a ZIP.
lambda_function2.py uses a csv stored on an S3 Bucket. Ensure to remove the 2.

Set 4 Lambda Environment Variables:
    "FROM" with the value of your Twilio Number
    "TO" to the recieving number
    "TWILIO_ACCOUNT_SID" with you Twilio Account SID
    "TWILIO_AUTH_TOKEN" with you Twilio Auth Token
    These values can be found on your Twilio configuration console

If using an S3 Bucket, ensure the Lamda function is created with S3 read permissions.

CSV file should follow the same format, with row[0] containing the date, and row[1] containing the name.

While the function was initially created to serve as a birthday reminder system, it can be used to send reminders on any date.
My preferred Lambda trigger method is a CloudWatch EventBridge, in order run the function consistently at a set time.



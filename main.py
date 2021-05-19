# Download the helper library from https://www.twilio.com/docs/python/install
# import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN  = ""
FROM               = ""

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# ---------------DOESN't WORKING------------------------
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# ------------------------------------------------------

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
body   = None

if client is not None:
    to = input('To(ex +54 111 111-1111).......: ')
    while body is None:
        print('--- Write a message ---')
        body = input('Message.......................: ')
    message = client.messages.create(body=body, from_=FROM, to=to)
    print(message.sid)
else:
    print("Couldn't connect to Twilio API")
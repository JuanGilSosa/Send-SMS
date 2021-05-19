# Download the helper library from https://www.twilio.com/docs/python/install
# import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "AC548f864222337b0cf61371a42cfb02e7"
TWILIO_AUTH_TOKEN  = "1c39241a77205b2f92232e4c2a524a27"
FROM               = '+12158762861'

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
#!/usr/bin/python


# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token = ""
sTwilioNumber = "+"

client = TwilioRestClient(account_sid, auth_token)
 
#number = client.phone_numbers.purchase(voice_url="http://demo.twilio.com/docs/voice.xml",
#    phone_number="+15005550006")
#print number.sid

url = ""

mms = client.messages.create(
    body="MMS, Hi from RRPServer",
    to="",
    from_="",
    media_url=url)
print mms.sid


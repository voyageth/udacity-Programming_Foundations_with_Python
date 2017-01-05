# coding=utf-8
from twilio.rest import TwilioRestClient

account_sid = "1234"  # Your Account SID from www.twilio.com/console
auth_token = "1234"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="1234",
                                 to="+1234",  # Replace with your phone number
                                 from_="+1234")  # Replace with your Twilio number

print(message.sid)

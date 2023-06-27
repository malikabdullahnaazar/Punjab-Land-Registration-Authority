from twilio.rest import Client

account_sid = 'ACe6eafa17fb6916e2a4cca5350100c0a7'
auth_token = '161622e7e14e9b6cee4a1165e021bdde'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+15417256454',
  body='Your OTP is 4566. Do not share your OTP with anyone.',
  to='+923223545701'
)

print(message.sid)
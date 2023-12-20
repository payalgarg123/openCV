
from twilio.rest import Client

account_sid = "ACe532e5a335f8c4bc21d2c176daed57ac"
auth_token = "9bf86ce8a44a6cb4fc4604008ce78683"
client = Client(account_sid, auth_token)

message = client.messages.create (
    body = "Hello my name is Ashish Chauhan",
    from_ = "whatsapp:+14155238886",
    to= "whatsapp:+91-9205401132"
)
print(message.sid)

# pip install twilio
from twilio.rest import Client

# client credential are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN

client=Client()

# this is twilio sandbox testing number
from_whatsapp_number='whatsapp:+919760016365'
# replace this number with your own whatsapp messenging number
to_whatsapp_number='whatsapp:+917017910632'

client.messages.create(body='Hello World',from_=from_whatsapp_number,to=to_whatsapp_number)
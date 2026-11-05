
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Using a .env file to retrieve the phone numbers and tokens.
load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TWILIO_TO_NUMBER = os.getenv("TWILIO_TO_NUMBER")

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_= TWILIO_FROM_NUMBER,
            body=message_body,
            to=TWILIO_TO_NUMBER
        )
        # Prints if successfully sent.
        print(message.sid)

from twilio.rest import Client

Twilo_sid = "AC3a4beed28f8eac1d4a8e1c89fe705840"
Twilo_token = "2ecf5133a74cdc4618734baa08fb8427"
twilo_virtual = "+14847026182"
user_number = "+919154630718"

class NotificationManager:

    def __init__(self):
        self.client = Client(Twilo_sid, Twilo_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilo_virtual,
            to=user_number,
        )
        # Prints if successfully sent.
        print(message.sid)

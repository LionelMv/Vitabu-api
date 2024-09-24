import africastalking
from decouple import config

# Initialize SDK
africastalking.initialize(config('SMS_USERNAME'), config('SMS_API_KEY'))

# Get the SMS service
sms = africastalking.SMS

def send_sms_alert(phone_number, message):
    try:
        response = sms.send(message, [phone_number])
        print(f"SMS sent successfully: {response}")
        return response
    except Exception as e:
        print(f"Failed to send SMS: {e}")
        return None

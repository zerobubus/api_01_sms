import time
import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv 
load_dotenv()


token = os.getenv('Token')
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
my_number = os.getenv('NUMBER_TO')
twilio_number = os.getenv('NUMBER_FROM')
version = os.getenv('version')
client = Client(account_sid, auth_token)

def get_status(user_id):

    params = {'v': version,
           'access_token': token,
           'user_ids': user_id,
           'fields': 'online'
    }
    status = requests.post(f'https://api.vk.com/method/users.get', params=params)
    return status.json()['response'][0]['online']


def sms_sender(sms_text):

    message = client.messages.create(
                              body=sms_text,
                              from_=twilio_number,
                              to=my_number
                          )

    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)

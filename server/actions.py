import requests
import json
from pprint import pprint
from twilio.rest import TwilioRestClient
from requests.auth import HTTPBasicAuth

account_sid = "AC9568bf793a849cc44080274f2d87a303"
auth_token = "e41444c4a72004173b1707b5841a9626"
client = TwilioRestClient(account_sid, auth_token)

twilio_phone_number = "+12014310707"

def send_sms(text, numbers):
    client.messages.create(to=numbers[0],
                           from_=twilio_phone_number,
                           body=text)
    
def send_voice_message(voice_url, numbers):
    call = client.calls.create(url=voice_url,
							    to=numbers[0],
							    from_=twilio_phone_number)
    print('call.sid is ' + call.sid)

def get_records():
    phonenumbers = []

    r = requests.get("https://api.twilio.com/2010-04-01/Accounts/AC9568bf793a849cc44080274f2d87a303/Calls.json", data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('AC9568bf793a849cc44080274f2d87a303', 'e41444c4a72004173b1707b5841a9626'))
    if (r.status_code == 200):
        for a in json.loads(r.content)["calls"]:
            print ""
            phonenumbers.append(str(a["from"]))
    else:
        print ":("

    print phonenumbers

    return ', '.join(phonenumbers)
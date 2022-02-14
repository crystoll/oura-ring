import json
import os
import requests 


from datetime import date, timedelta
from oura import OuraClient
from dotenv import load_dotenv

load_dotenv()

oura_token = os.getenv('OURA_TOKEN')

# Heartrate

url = 'https://api.ouraring.com/v2/usercollection/heartrate' 
params={ 
    'start_datetime': '2022-01-01T00:00:00-08:00', 
    'end_datetime': '2022-01-31T00:00:00-08:00' 
}
headers = { 
  'Authorization': 'Bearer ' + oura_token,
}
response = requests.request('GET', url, headers=headers, params=params) 
print(response.text)

# Workouts (if you have them)
# url = 'https://api.ouraring.com/v2/usercollection/workout' 
# params={ 
#     'start_date': '2022-01-01', 
#     'end_date': '2022-02-01' 
# }
# headers = { 
#   'Authorization': 'Bearer ' + oura_token,
# }
# response = requests.request('GET', url, headers=headers, params=params) 
# print(response.text)
import json
import os

from datetime import date, timedelta
from oura import OuraClient
from dotenv import load_dotenv

load_dotenv()

oura_token = os.getenv('OURA_TOKEN')
oura_client = OuraClient(personal_access_token=oura_token)

who_am_i = oura_client.user_info()

week_past = str(date.today() - timedelta(days=7)) 
sleep_summary = oura_client.sleep_summary(start=week_past)
print (sleep_summary)

with open('result.json', 'w') as fp:
    json.dump(sleep_summary, fp, indent=4)


import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OANDA_API")
ACCOUNT_ID = os.getenv("OANDA_ACC_ID")
OANDA_URL = 'https://api-fxpractice.oanda.com/v3'

SECURE_HEADER = {
    'Authorization': 'Bearer {key}'.format(key=API_KEY)
}

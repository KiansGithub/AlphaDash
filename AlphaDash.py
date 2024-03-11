import requests 
import os 
from dotenv import load_dotenv

load_dotenv()

def get_stock_data(symbol):
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY') 
    base_url = 'https://www.alphavantage.co/query?'
    function = 'TIME_SERIES_DAILY'
    url = f"{base_url}function={function}&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data 



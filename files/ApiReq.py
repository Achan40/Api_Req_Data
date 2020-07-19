import requests
import pandas as pd
import os

API_SECRET_KEY = os.environ['SECRET_KEY']
HTTP_BASE = 'https://cloud.iexapis.com/v1'
endpoint = 'UNRATE' #Unemployment Rate

time_range = '2y' #See https://iexcloud.io/docs/api/#time-series for range values

HTTP_REQUEST = HTTP_BASE+'/time-series/economic/'+endpoint+'?range='+time_range+'&token='+API_SECRET_KEY
response = requests.get(HTTP_REQUEST)
data = response.json()
#IEX_data = pd.DataFrame.from_dict(data)
#IEX_data.to_csv('test.csv')


import requests
import pandas as pd
import os

API_SECRET_KEY = os.environ['SECRET_KEY_TEST']
HTTP_BASE = 'https://sandbox.iexapis.com/stable'
HTTP_ID = '/time-series/'
HTTP_Key = 'economic'
endpoint = 'UNRATE' #Unemployment Rate
time_range = '2y' #See https://iexcloud.io/docs/api/#time-series for range values

HTTP_REQUEST = HTTP_BASE+'/time-series/economic/'+endpoint+'?range='+time_range+'&token='+API_SECRET_KEY
response = requests.get(HTTP_REQUEST)

#this function is used to return a dataframe from an HTTP request
def json_to_dat(HTTP):
    response = requests.get(HTTP)
    data = response.json()
    print(response)
    IEX_data = pd.DataFrame.from_dict(data)
    return IEX_data

class EconData:
    def __init__(self):
        print("Endpoint Required")
    def endpoints(self):
        #http request for all endpoints under certain HTTP ID and KEY
        HTTP = HTTP_BASE+HTTP_ID+HTTP_Key+'?token='+API_SECRET_KEY
        IEX_data = json_to_dat(HTTP)
        #Return endpoint names only
        print(IEX_data['id'])

qwer = EconData()
qwer.endpoints()
import requests
import pandas as pd
import os

#required to set your API secret key as SECRET_KEY_TEST
API_SECRET_KEY = os.environ['SECRET_KEY']
HTTP_BASE = 'https://cloud.iexapis.com/stable'
HTTP_ID = '/time-series/'
HTTP_Key = 'economic'

#this function is used to return a dataframe from an HTTP request
def json_to_df(HTTP):
    response = requests.get(HTTP)
    data = response.json()
    print(response)
    IEX_data = pd.DataFrame.from_dict(data)
    return IEX_data

class EconData:
    def __init__(self):
        print('Set API secret key as environment variable SECRET_KEY={yourapisecretkeyhere')
        print('Default http path is ' + HTTP_BASE + HTTP_ID + HTTP_Key)

    def keys(self,HTTP_BASE = HTTP_BASE,HTTP_ID = HTTP_ID):
        #http request for all HTTP keys under certain ID
        HTTP = HTTP_BASE + HTTP_ID[0:-1] + '?token=' + API_SECRET_KEY
        IEX_data = json_to_df(HTTP)
        #Return endpoint names (all of them)
        print(IEX_data['id'])

    def endpoints(self,HTTP_BASE = HTTP_BASE,HTTP_ID = HTTP_ID,HTTP_Key = HTTP_Key):
        #http request for all endpoints under certain HTTP ID and KEY
        HTTP = HTTP_BASE + HTTP_ID + HTTP_Key + '?token=' + API_SECRET_KEY
        IEX_data = json_to_df(HTTP)
        #Return endpoint names (all of them)
        print(IEX_data['id'])

    def getcsv(self,endpoint,HTTP_BASE = HTTP_BASE,HTTP_ID = HTTP_ID,HTTP_Key = HTTP_Key,time_range='1y'):
        endpoint = '/'+endpoint
        HTTP = HTTP_BASE + HTTP_ID + HTTP_Key + endpoint + '?range=' + time_range + '&token=' + API_SECRET_KEY
        IEX_data = json_to_df(HTTP)
        endpoint = endpoint[-6:]
        #outputs csv file into your working directory
        IEX_data.to_csv(endpoint+'.csv')
# Api_Req_Data

A module Using [IEX Cloud API](https://iexcloud.io/docs/api/) to gather some time-series data into csv file

#How to use
Set your API key to the variable SECRET_KEY

The default API URL is: https://cloud.iexapis.com/stable/time-series/economic this can be changed by arguements (HTTP_BASE, HTTP_ID, HTTP_Key) within the definitions of the class.

Create a new instance of the class EconData() by assigning it to a variable. 

The instance object .keys() will list the available HTTP_Keys within the API. Optional arguements (HTTP_BASE, HTTP_ID) can be used to change the HTTP base and ID, currently only ids available in IEX Cloud API are time-series and data-points

The instance object .endpoints() will list the available endpoints within the API HTTP key. Optional arguements (HTTP_BASE, HTTP_ID, HTTP_key) can be used to change the HTTP base, ID and key.


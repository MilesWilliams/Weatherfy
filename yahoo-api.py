import sys
import urllib3
import bs4
from urllib.parse import urlencode
import json
import requests


def WeatherApi():
    # http = urllib3.PoolManager()
    # # baseurl = "https://query.yahooapis.com/v1/public/yql?"
    # # yql_query = "select * from weather.forecast where woeid= 1591691"
    # # yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
    # # result = http.request('GET', yql_url)
    # # data = json.loads(result.data.decode('utf-8'))
    # # print(data)
    # # print (data['query']['results'])

    url = requests.get("https://query.yahooapis.com/v1/public/yql?q=select * from weather.forecast where woeid= 1591691&format=json")
    content = url.json()
    with open('data.json', 'w') as outfile:
        json.dump(content, outfile)

    print(content['query']['results']['channel']['item']['forecast'][0]['date'])
WeatherApi()

#libraries
import json
import pandas as pd
import datetime
import calendar
import random
import time
import requests

#functions
def jsonDf(filepaths):
    data=list()
    for filepath in filepaths:
        file=open(filepath)
        jsonData=json.load(file)
        data+=jsonData
    df=pd.DataFrame(data)
    return df
def getLocation(ip):
    ip_address = ip
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data
def findSong(year, month, day):
    if year == 0:
        print("This may take awhile...")
        
def guessingGame():
    print("Welcome to the Guessing Game! ©")
    time.sleep(1)
    print("We will provide you with a location ")
def explore():
    year, month, day = input("Provide a date in the form '1996:07:26'                   ").split(sep=":")
    year, month, day = int(year), int(month), int(day)
    findSong(year, month, day)



filepaths=["/Users/lukebeebe/Desktop/Amiri Data/endsong_0.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_1.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_2.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_3.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_4.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_5.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_6.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_7.json"]

#jsonDf
spotifyDf=jsonDf(filepaths)
spotifyDf['ts']=pd.to_datetime(spotifyDf['ts'])
game=""
while ("exp" not in game) and ("gues" not in game):
    game=input("Would you like to explore your data or play the Guessing Game?  ").lower()
    time.sleep(1)
    if ("ex" not in game) and ("g" not in game):
        print("Try again")
        time.sleep(1)
if "ex" in game:
    explore()
else:
    guessingGame()
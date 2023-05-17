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
    highestTime=0
    if year == 0:
        print(str(len(spotifyDf['master_metadata_album_artist_name'].unique()))+" unique artists")
        for artist in spotifyDf['master_metadata_album_artist_name'].unique():
            artistTime=sum(spotifyDf["ms_played"][spotifyDf["master_metadata_album_artist_name"]==artist])
            print(str(artistTime)+" "+artist)
        if artistTime>highestTime:
            mostPopular=artist
            highestTime=artistTime
            print(mostPopular+" "+str(artistTime))
        hours=round(highestTime/1000/60/60,1)
        print(mostPopular+" "+str(hours)+" hours")
def guessingGame():
    print("Welcome to the Guessing Game! ©")
    time.sleep(1)
    print("We will provide you with a location ")
def explore():
    year, month, day = input("Provide a date in the form '1996:07:26'                         ").split(sep=":")
    year, month, day = int(year), int(month), int(day)
    findSong(year, month, day)



filepaths=["/Users/lukebeebe/Desktop/Amiri Data/endsong_0.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_1.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_2.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_3.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_4.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_5.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_6.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_7.json"]

#jsonDf
spotifyDf=jsonDf(filepaths)
spotifyDf=spotifyDf['ts',]
spotifyDf['ts']=pd.to_datetime(spotifyDf['ts'])
game=""
while ("ex" not in game) and ("g" not in game):
    game=input("Would you like to explore your data or play the Guessing Game?  ").lower()
    time.sleep(1)
    if ("ex" not in game) and ("g" not in game):
        print("Try again")
        time.sleep(1)
if "ex" in game:
    explore()
else:
    guessingGame()

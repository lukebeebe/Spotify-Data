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

def findSong(spotifyDf):
    artists=spotifyDf['master_metadata_album_artist_name'].unique()
    times=[]
    print(str(len(artists))+" unique artists")
    for artist in artists:
        time=round(sum(spotifyDf["ms_played"][spotifyDf["master_metadata_album_artist_name"]==artist])/1000/60/60,1)
        times.append(time)
    timesArtists=sorted(zip(times,artists),reverse=True)
    return timesArtists


def explore(spotifyDf):
    year, month, day = 0, 0, 0
    while (year not in spotifyDf.ts.dt.year.unique()) or (month not in spotifyDf.ts.dt.month.unique() or (day not in spotifyDf.ts.dt.day.unique())):
        year, month, day = input("Provide a date in the form '1996:07:26'                         ").split(sep=":")
        print(year+" "+month+" "+day)
        year, month, day = int(year), int(month), int(day)
        try:
            spotifyDf=spotifyDf[(spotifyDf.ts.dt.year==year) and (spotifyDf.ts.dt.month==month) and (spotifyDf.ts.dt.day==day)]
        except:
            print("Invalid day or month or year")
            try:
                spotifyDf=spotifyDf[(spotifyDf.ts.dt.year==year) and (spotifyDf.ts.dt.month==month)]
            except:
                print("Invalid month or year")
                try:
                    spotifyDf=spotifyDf[(spotifyDf.ts.dt.year==year)]
                except:
                    print("Invalid year")
    popular=findSong(spotifyDf)
    print(popular[0:5])




filepaths=["/Users/lukebeebe/Desktop/Amiri Data/endsong_0.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_1.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_2.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_3.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_4.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_5.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_6.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_7.json"]

#jsonDf
spotifyDf=jsonDf(filepaths)
spotifyDf=spotifyDf[["ts","master_metadata_album_artist_name","ms_played","ip_addr_decrypted"]].dropna()
spotifyDf['ts']=pd.to_datetime(spotifyDf['ts'])

print("Welcome to the Guessing Game! ©")
time.sleep(1)
print("We will provide you with a location and day.")
time.sleep(1)
print("You have three tries to guess an artist you listened to.")
time.sleep(1)

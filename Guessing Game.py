#libraries
import json
import pandas as pd
import datetime
import calendar
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

keepPlaying='y'
while keepPlaying=="y":
    filepaths=["/Users/lukebeebe/Desktop/Amiri Data/endsong_0.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_1.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_2.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_3.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_4.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_5.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_6.json","/Users/lukebeebe/Desktop/Amiri Data/endsong_7.json"]
    remember=""
    #jsonDf
    spotifyDf=jsonDf(filepaths)
    spotifyDf=spotifyDf[["ts","master_metadata_track_name","master_metadata_album_artist_name","ms_played","ip_addr_decrypted"]].dropna()
    spotifyDf['ts']=pd.to_datetime(spotifyDf['ts'])
    spotifyDf=spotifyDf[spotifyDf["master_metadata_album_artist_name"]!=remember]
    print("Welcome to the Guessing Game ©")
    time.sleep(1)
    print("We provide you with a date")
    time.sleep(1)
    print("You name an artist you listened to on that day")
    time.sleep(1)
    print("You have three attempts. Good luck!")
    time.sleep(2)
    song=spotifyDf.sample()
    year=song.ts.dt.year.tolist()[0]
    month=song.ts.dt.month.tolist()[0]
    monthName=calendar.month_name[month]
    day=song.ts.dt.day.tolist()[0]
    date=monthName+" "+str(day)+", "+str(year)
    print(date)
    spotifyDf=spotifyDf[(spotifyDf.ts.dt.year==year) & (spotifyDf.ts.dt.month==month) & (spotifyDf.ts.dt.day==day)]
    artists=spotifyDf['master_metadata_album_artist_name'].unique()
    artistString=""
    for artist in artists:
        artistString+=artist
        artistString+=" "
    artistString=artistString.lower().replace(",","")
    for i in range(0,3):
        if i==2:
            song=spotifyDf.sample()
            hint=song['master_metadata_track_name'].values[0]
            print("Hint: "+hint)
            time.sleep(2)
        guess=input("").lower().replace(",","")
        if (guess in artistString) & (len(guess.lower()) > 3):
            print("Correct!")
            correct=True
            time.sleep(1)
            break
        else:
            print("Incorrect "+str(i+1))
            correct=False
            time.sleep(1)
    if (i>=2) and (correct==False):
        print(hint+" was by "+song['master_metadata_album_artist_name'].values[0])
        time.sleep(2)
    print("You could have named:")
    for artist in artists:
        print(" "+artist)
        time.sleep(0.2)
        if guess in artist.lower().replace(",",""):
            remember=artist
    print("")
    time.sleep(2)

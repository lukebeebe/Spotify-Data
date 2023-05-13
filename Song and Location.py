import json
import pandas as pd
import datetime
import calendar
import random
import time

# open json data
f0 = open("/Users/lukebeebe/Desktop/Amiri Data/endsong_0.json")
f1 = open("/Users/lukebeebe/Desktop/Amiri Data/endsong_1.json")
f2 = open("/Users/lukebeebe/Desktop/Amiri Data/endsong_2.json")
f3 = open("/Users/lukebeebe/Desktop/Amiri Data/endsong_3.json")
f4 = open("/Users/lukebeebe/Desktop/Amiri Data/endsong_4.json")
f5 = open("/Users/lukebeebe/Desktop/Amiri Data/endsong_5.json")
f6 = open("/Users/lukebeebe/Desktop/Amiri Data/endsong_6.json")
f7 = open("/Users/lukebeebe/Desktop/Amiri Data/endsong_7.json")
# load json data
data_f0 = json.load(f0)
data_f1 = json.load(f1)
data_f2 = json.load(f2)
data_f3 = json.load(f3)
data_f4 = json.load(f4)
data_f5 = json.load(f5)
data_f6 = json.load(f6)
data_f7 = json.load(f7)
# master file
data = data_f0 + data_f1 + data_f2 + data_f3 + data_f4 + data_f5 + data_f6 +data_f7
# pandas df
spotifyDf = pd.DataFrame(data)
# timestamp to datetime and playtime to min
spotifyDf['ts']=pd.to_datetime(spotifyDf['ts'])

# madlibs approach
adjectives=["violent","maniacal","suicidal","silly","surprising","savage","alpha","giddy","deranged","adulterous","alcoholic","confused","frisky","hateful","idiotic","smart","insecure","maniacal","niggardly","misunderstood","naked","pea-brained","twisted","zippy","jewish","vengeful","useless","witty","curious","gay","cumloaded"]
names=["Fidero","Nico","Assho","Mysterio","Cheerio","Ho","Mommo","Gyro"]
verbs=["screw","fool","cry","laugh"]
nouns=["dumpster","Popeyes","gas station"]

myName=random.choice(names)
name=input("Hey there, I'm "+myName+", brother of "+myName[:-1]+"a. Who am I speaking to?\n")
time.sleep(1)
print(name+"? Hmm. "+name.upper()+". I know some things about you.")
time.sleep(2)
print("Or rather, I know some people who know some things about you.")
time.sleep(2)
# choose year, find most popular artist
year=0
while year not in spotifyDf.ts.dt.year.unique():
    year=int(input("Type in a year from "+str(sorted(spotifyDf.ts.dt.year.unique()))+"\n"))
    time.sleep(1)
    if year not in spotifyDf.ts.dt.year.unique():
        print("Don't know squat about year "+str(year))
        time.sleep(1)
spotifyDf=spotifyDf[spotifyDf.ts.dt.year==year]
print("That was a "+random.choice(adjectives)+" year for me. Gimme a sec to snoop.\n")
highestTime=0
for name in spotifyDf["master_metadata_album_artist_name"].unique():
    artistTime=sum(spotifyDf["ms_played"][(spotifyDf.ts.dt.year==year) & (spotifyDf["master_metadata_album_artist_name"]==name)])
    if artistTime>highestTime:
        mostPopular=name
        highestTime=artistTime
print("Your top artist in "+str(year)+" was "+mostPopular.upper()+" and you listened to them for "+str(round(highestTime/1000/60/60,1))+" HOURS.")
time.sleep(1)
if highestTime/1000/60/60<1:
    print("That's "+str(round(highestTime/1000/60,1))+" MINUTES.\n\n")
else:
    print("")
# choose month, find most popular artist
month=0
while month not in spotifyDf.ts.dt.month.unique():
    month=int(input("Test me further, choose a month from "+str(year)+". Choose from "+str(sorted(spotifyDf.ts.dt.month.unique()))+"\n"))
    time.sleep(1)
    if month not in spotifyDf.ts.dt.month.unique():
        print("Did you type that in right?")
        time.sleep(1)
spotifyDf=spotifyDf[spotifyDf.ts.dt.month==month]
monthName=calendar.month_name[month]
time.sleep(2)
print(random.choice(adjectives).capitalize()+" choice!")
time.sleep(1)
highestTime=0
for name in spotifyDf["master_metadata_album_artist_name"][(spotifyDf.ts.dt.year==year) & (spotifyDf.ts.dt.month==month)].unique():
    artistTime=sum(spotifyDf["ms_played"][(spotifyDf.ts.dt.year==year) & (spotifyDf.ts.dt.month==month) & (spotifyDf["master_metadata_album_artist_name"]==name)])
    if artistTime > highestTime:
        mostPopular=name
        highestTime=artistTime
print("Your top artist in "+monthName.upper()+" "+str(year)+" was "+mostPopular.upper()+" and you listened to them for "+str(round(highestTime/1000/60/60,1))+" HOURS.")
if highestTime/1000/60/60<1:
    print("That's "+str(round(highestTime/1000/60,1))+" MINUTES.\n\n")
else:
    print("")
# choose day, find most popular artist
print("This might sound weird, but I'd like you to choose something else for me")
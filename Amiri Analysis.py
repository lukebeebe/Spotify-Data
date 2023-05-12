import json
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
import datetime

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
spotifyDf['hours_played']=spotifyDf['ms_played']/1000/60/60
timeDf=pd.DataFrame(columns=["Year","Month","Morning","Afternoon","Night","Most Popular","Minutes Listened"])

# create df seperating years, months, days of week
for year in range(2019,2024):
    print(year)
    for month in range(1,13):
        morning=round(sum(spotifyDf['hours_played'][(spotifyDf.ts.dt.year==year) & (spotifyDf.ts.dt.hour<=12) & (spotifyDf.ts.dt.month==month)]),1)
        afternoon=round(sum(spotifyDf['hours_played'][(spotifyDf.ts.dt.year==year) & (spotifyDf.ts.dt.hour<=19) & (spotifyDf.ts.dt.hour>12) & (spotifyDf.ts.dt.month==month)]),1)
        night=round(sum(spotifyDf['hours_played'][(spotifyDf.ts.dt.year==year) & (spotifyDf.ts.dt.hour<=24) & (spotifyDf.ts.dt.hour>19) & (spotifyDf.ts.dt.month==month)]),1)
        # find most popular artist for a given month
        highestTime=0
        for name in spotifyDf["master_metadata_album_artist_name"][(spotifyDf.ts.dt.year==year) & (spotifyDf.ts.dt.month==month)].unique():
            artistTime=sum(spotifyDf["ms_played"][(spotifyDf.ts.dt.year==year) & (spotifyDf.ts.dt.month==month) & (spotifyDf["master_metadata_album_artist_name"]==name)])
            if artistTime > highestTime:
                mostPopular=name
                highestTime=artistTime
        if highestTime==0:
            mostPopular="NA"
        else:
            highestTime=round(highestTime/1000/60/60,1)
        print(" "+str(month)+" "+mostPopular+" "+str(highestTime)+" hours")
        list=[year,month,morning,afternoon,night,mostPopular,highestTime]
        timeDf.loc[len(timeDf)]=list
# create Time column
timeDf["Time"]=round(timeDf["Year"]+timeDf["Month"]/12,1)
# Df from 2019 until 2023
timeDf2019=timeDf[(timeDf["Time"]>=2019) & (timeDf["Time"]<=2023)]
# barchart
timeDf2019.plot.barh(x="Time",y=["Morning","Afternoon","Night"],stacked=True)
plt.title("Amiri's Listening Distribution")
plt.xlabel("Hours per Month")
plt.ylabel("Years")
ax = plt.gca()
ax.set_yticks(ax.get_yticks()[::10])
# add most popular to barchart, WORK ON DIMENSIONS
for bar, name in zip(ax.patches, timeDf2019["Most Popular"][::3]):
    ax.text(0.1, bar.get_y()+bar.get_height()/2, name, color = 'black', ha = 'left', va = 'center')
plt.show()


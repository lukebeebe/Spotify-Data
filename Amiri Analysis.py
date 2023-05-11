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
print(list(spotifyDf.columns.values))
timeDf=pd.DataFrame(columns=["Year","Month","Morning","Afternoon","Night"])
# create df seperating years, months, days of week
for year in range(2014,2024):
    for month in range(1,12):
        morning=round(sum(spotifyDf['hours_played'][(spotifyDf.ts.dt.year==year) & (spotifyDf.ts.dt.hour<=12) & (spotifyDf.ts.dt.month>=month) & (spotifyDf.ts.dt.month<month+1)]),1)
        afternoon=round(sum(spotifyDf['hours_played'][(spotifyDf.ts.dt.year==year) & (spotifyDf.ts.dt.hour<=19) & (spotifyDf.ts.dt.hour>12) & (spotifyDf.ts.dt.month>=month) & (spotifyDf.ts.dt.month<month+1)]),1)
        night=round(sum(spotifyDf['hours_played'][(spotifyDf.ts.dt.year==year) & (spotifyDf.ts.dt.hour<=24) & (spotifyDf.ts.dt.hour>19) & (spotifyDf.ts.dt.month>=month) & (spotifyDf.ts.dt.month<month+1)]),1)
        list=[year,month,morning,afternoon,night]
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
plt.locator_params(axis='y',nbins=10)
plt.show()

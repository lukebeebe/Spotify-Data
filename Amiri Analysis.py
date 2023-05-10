import json
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime as dt

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
df = pd.DataFrame(data)
# timestamp to datetime and playtime to min
ts=df.loc[:,"ts"]
pt=df.loc[:,"ms_played"]/1000/60
print(ts.head())
print(pt.head())

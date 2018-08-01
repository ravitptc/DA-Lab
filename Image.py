import pandas as pd
df1 = pd.read_csv("C:/Users/umarm/Downloads/MovieGenre.csv",encoding='latin-1')
df2=df1['Genre']
s = set();
for var in range(2,300):
    l1=df2[var].split("|");
    for var1 in l1:
        s.add(var1);

import os;
os.chdir("C:/Users/umarm/Desktop/DA/f2")

for var in s:
    os.mkdir(var);

df2=df1['Poster']
df3=df1['Genre']

import urllib.request
v="C:/Users/umarm/Desktop/DA/f2/";
for var in range(2,300):
    l1=df3[var].split("|");
    for var1 in l1:
        v1=v+str(var1)+"/"+str(var)+".jpg";
        print(v1)
        try:
            print(df2[var]);
            urllib.request.urlretrieve(df2[var],v1)
        except:
            pass;

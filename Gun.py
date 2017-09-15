
# coding: utf-8

# In[1]:

import csv
f = open ("guns.csv","r")
csvreader = csv.reader(f)
data = list(csvreader)


# In[2]:

headers = data[0]
data = data[1:len(data)]
headers


# In[3]:

data


# In[4]:

years = [element[1] for element in data]
len(years)


# In[5]:

year_counts = {}
for element2 in years:
    if element2 in year_counts:
        year_counts[element2]=year_counts[element2]+1
    else:
        year_counts[element2] =+ 1
print(year_counts)


# In[6]:

import datetime
for monthyear in data:
    yearinteger = int(monthyear[1])
    monthyear[1] = yearinteger
for monthyear in data:
    monthinteger = int(monthyear[2])
    monthyear[2] = monthinteger
dates = [datetime.datetime(year = element3[1],month = element3[2], day = 1 ) for element3 in data]

date_counts = {}
for datelement in dates:
    if datelement in date_counts:
        date_counts[datelement]=date_counts[datelement]+1
    else:
        date_counts[datelement]=+1
sex_counts = {}
race_counts = {}
for sex in data:
    if sex [5] in sex_counts:
        sex_counts[sex[5]]=sex_counts[sex[5]]+1
    else:
        sex_counts[sex[5]] =+ 1
            
for race in data:
    if race [7] in race_counts:
        race_counts[race[7]]=race_counts[race[7]]+1
    else:
        race_counts[race[7]] =+ 1

race_counts


# In[7]:

print(sex_counts)


# In[8]:

date_counts


# In[9]:

import csv
f2 = open("census.csv","r")
csvreader2 = csv.reader(f2)
census = list(csvreader2)
census


# In[10]:

censusdata = census[1]

Total = int(censusdata[9])
White = int(censusdata[10])
Hispanic = int(censusdata[11])
Black = int(censusdata[12])
AI = int(censusdata[13])
Asian = int(censusdata[14])
NH = int(censusdata[15])


# In[11]:

mapping = {'Asian/Pacific Islander': Asian+NH,
 'Black': Black,
 'Hispanic': Hispanic,
 'Native American/Native Alaskan': AI,
 'White': White}
mapping


# In[12]:

race_per_hundredk = {}
for racekey in race_counts:
    percentage = race_counts[racekey]/mapping[racekey]
    per100000 = percentage*100000
    race_per_hundredk[racekey] = per100000
race_per_hundredk


# In[13]:

intents = []
for intention in data:
    intent = intention[3]
    intents.append(intent)
intents


# In[14]:

races = []
for race in data:
    racetype = race[7]
    races.append(racetype)
races


# In[25]:

homicide_race_per_hundredk = {}
for i, race in enumerate(races):
    if race not in homicide_race_per_hundredk:
        homicide_race_per_hundredk[race]=0
    if intents[i] == 'Homicide':
        homicide_race_per_hundredk[race] += 1
homicide_race_per_hundredk


# In[26]:

for racekey in homicide_race_per_hundredk:
    percentage = homicide_race_per_hundredk[racekey]/mapping[racekey]
    per100000 = percentage*100000
    homicide_race_per_hundredk[racekey] = per100000
homicide_race_per_hundredk


# In[ ]:




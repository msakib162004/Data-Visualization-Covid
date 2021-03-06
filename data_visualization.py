# -*- coding: utf-8 -*-
"""Data Visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rvKRYaqXBguNQu3gFO0DVQBhW9jNtpzS
"""

from google.colab import files 
  
  
uploaded = files.upload()

import pandas as pd 
import io 
  
df = pd.read_csv(io.BytesIO(uploaded['April18_to_September20.csv'])) 
print(df)

for colum in df:
  print(colum , df[colum].isnull().values.any())

from sklearn.impute import SimpleImputer
for colum in df:
  if df[colum].isnull().values.any() == True:
    si = SimpleImputer(strategy='mean')
    si.fit(df[[colum]])
    df[colum] = si.transform(df[[colum]]).flatten()

for colum in df:
  print(colum , df[colum].isnull().values.any())

pd.set_option("display.max.columns", None)

df.head()

df.tail()

#df['Population'].mean()
df['Total Tests'].mean()
#df['Total Cases'].mean()
#df['Total Deaths'].mean()
#df['Total Recovered'].mean()
#df['Serious or Critical'].mean()
#df['Active Cases'].mean()

df['Total Tests'].median()

df.describe()

df['Total Tests']

df.plot()

df = pd.DataFrame(df)
print(df.shape)

import plotly.express as px
fig = px.line(df, x = 'Total Tests', y = 'Total Cases', title='Total Tests Vs Total Cases')
fig.show()

import plotly.express as px
fig = px.line(df, x = 'Country', y = 'Total Cases', title='Country Vs Total Cases')
fig.show()

import plotly.express as px
fig = px.line(df, x = 'Country', y = 'Total Deaths', title='Country Vs Total Deaths')
fig.show()

import plotly.express as px
fig = px.line(df, x = 'Country', y = 'Total Recovered', title='Country Vs Total Recovered')
fig.show()

total_test = df['Total Tests'].tolist()
country = df['Country'].tolist()

total_cases = df['Total Cases'].tolist()
population = df['Population'].tolist()

total_deaths = df['Total Deaths'].tolist()
total_recovered = df['Total Recovered'].tolist()

serious_or_critical = df['Serious or Critical'].tolist()
active_cases = df['Active Cases'].tolist()
date = df['Date'].tolist()

from matplotlib import pyplot as plt 
  

  
name = df['Country'].head(20) 
t_test = df['Total Tests'].head(20) 
  
# Figure Size 
fig = plt.figure(figsize =(30, 8)) 
  
# Horizontal Bar Plot 
plt.bar(name[0:20], t_test[0:20]) 
plt.xlabel('Country Name')
plt.ylabel('Total Test')
plt.title('Country Name Vs Total Test\n')
# Show Plot 
plt.show()

from matplotlib import pyplot as plt 
  

  
name = df['Country']
t_deaths = df['Total Deaths'] 
  
# Figure Size 
fig = plt.figure(figsize =(30, 8)) 
  
# Horizontal Bar Plot 
plt.bar(name[0:30], t_deaths[0:30]) 
plt.xlabel('Country Name')
plt.ylabel('Total Deaths')
plt.title('Country Name Vs Total Deaths\n')
# Show Plot 
plt.show()

#import pandas as pd 
from matplotlib import pyplot as plt 


name = df['Country'].head(30) 
t_deaths = df['Total Deaths'].head(30) 
  
# Figure Size 
fig, ax = plt.subplots(figsize =(16, 9)) 
  
# Horizontal Bar Plot 
ax.barh(name, t_deaths) 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
ax.set_title('Country Name Vs Total Deaths', 
             loc ='left', ) 
  
# Add Text watermark 
fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.7) 
plt.xlabel('Total Deaths') 
plt.ylabel('Country Name')
#plt.title('Country Name Vs Total Deaths\n')
# Show Plot 
plt.show()

#import pandas as pd 
from matplotlib import pyplot as plt 


name = df['Country'].head(30) 
price = df['Total Tests'].head(30) 

# Figure Size 
fig, ax = plt.subplots(figsize =(16, 9)) 
  
# Horizontal Bar Plot 
ax.barh(name, price) 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
ax.set_title('Country name vs Test', 
             loc ='left', ) 
  
# Add Text watermark 
fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.7) 
plt.xlabel('Country Name') 
plt.ylabel('Total Tests')  
# Show Plot 
plt.show()

import matplotlib.pyplot as plt
plt.hist(df['Total Tests'], bins=[0,10,20,30,40,50,60,70,80,90,99,110,120,130,140,150,160,170,180,190])
plt.title('Total Test\n')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

plt.scatter(df['Total Recovered'], df['Total Deaths'])

plt.xlabel('Total Recovered')
plt.ylabel('Total Deaths')
plt.title('Total Recovered Vs Total Deaths\n')

plt.show()

plt.scatter(df['Total Cases'], df['Total Deaths'])
plt.xlabel('Total Cases')
plt.ylabel('Total Deaths')
plt.title('Total Cases Vs Total Deaths\n')

plt.scatter(df['Total Tests'], df['Total Cases'])
plt.xlabel('Total Tests')
plt.ylabel('Total Cases')
plt.title('Total Tests Vs Total Cases\n')

x = df['Population']
y = df['Total Recovered']
plt.scatter(x, y)

plt.xlabel('Population')
plt.ylabel('Total Recovered')
plt.title('Population Vs Total Recovered\n')

plt.show()

x = df['Population']
y = df['Total Deaths']
plt.scatter(x, y)

plt.xlabel('Population')
plt.ylabel('Total Deaths')
plt.title('Population Vs Total Deaths\n')

plt.show()

x = df['Population']
y = df['Total Tests']
plt.subplot(2, 2, 1)
plt.scatter(x, y)
x = df['Population']
y = df['Total Cases']
plt.subplot(2, 2, 2)
plt.scatter(x, y)
############
x = df['Population']
y = df['Total Deaths']
plt.subplot(2, 2, 3)
plt.scatter(x, y)
x = df['Population']
y = df['Total Recovered']
plt.subplot(2, 2, 4)
plt.scatter(x, y)
plt.show()

import numpy as np
import pandas as pd

#np.random.seed(2345)
#df = pd.DataFrame(np.random.randn(20,4),
#                 columns=['C1', 'C2', 'C3', 'C4'])
boxplot = df.head(25).boxplot(column=['Total Cases', 'Total Deaths'])
#df.columns

df.head(20).plot.pie(y='Total Cases', figsize=(10, 10))

# Creating plot 
fig = plt.figure(figsize =(10, 10)) 
plt.pie(df['Total Deaths'].head(10), labels = df['Country'].head(10)) 
  
# show plot
plt.title('Country Vs Total Deaths pie chart')

#plt.set_title("Country Vs Total Deaths pie chart") 
plt.show()

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))

country = df['Country'].head(40)

data = df['Total Deaths'].head(40)

wedges, autotexts = ax.pie(data,textprops=dict(color="w"))

ax.legend(wedges, country,
          title="Countries",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Country Vs Total Death pie chart")

plt.show()

countries = df['Country'].head(5)
tt = df['Total Tests'].head(5)
tc = df['Total Cases'].head(5)
ac = df['Active Cases'].head(5)
ind = [x for x, _ in enumerate(countries)]

plt.bar(ind, ac, width=1.8, label='Total Tests', color='gold', bottom=tt+tc)
plt.bar(ind, tc, width=1.8, label='Total Cases', color='silver', bottom=tc)
plt.bar(ind, tt, width=1.8, label='Active Cases', color='#CD853F')

plt.xticks(ind, countries)
plt.ylabel("Cases")
plt.xlabel("Countries")
plt.legend(loc="upper right")
plt.title("Country wise Total tests, Total cases and Active cases")

plt.show()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = df['Country'].head(25)
t_cases = df['Total Cases'].head(25)
at_cases = df['Active Cases'].head(25)

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(25,5))
rects1 = ax.bar(x - width/2, t_cases, width, label='Total Cases')
rects2 = ax.bar(x + width/2, at_cases, width, label='Active_Cases')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cases')
ax.set_title('Total and Active cases')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


#autolabel(rects1)
#autolabel(rects2)
#plt.fig(figsize=(502,502))
fig.tight_layout()

plt.show()

import matplotlib.pyplot as plt

f, ax = plt.subplots(figsize=(18,5)) # set the size that you'd like (width, height)
plt.bar([1,2,3,4,5,6,7,8,9,10], df['Total Cases'].head(10), label = 'Total Cases')
plt.bar([13,14,15,16,17,18,19,20,21,22], df['Active Cases'].head(10), label = 'Active Cases')
ax.legend(fontsize = 14)

#ts = pd.Series(df['Total Cases'], index=df['Date'], periods=1000))
ts = df['Total Cases']
ts = ts.cumsum()
ts.plot()

ts = df['Total Recovered']
ts = ts.cumsum()
ts.plot()

import seaborn as sns
sns.set()
plt.style.use('classic')
sns.pairplot(df.head(50), hue='Country', size=3.5);

with sns.axes_style(style='ticks'):
    g = sns.factorplot("Total Tests", "Total Cases", "Country", data=df.head(5), kind="box")

sns.jointplot("Total Tests", "Total Cases", data=df, kind='reg');

sns.distplot(df['Total Tests'], kde=False);
plt.axvline(0, color="k", linestyle="--");

from pandas.api.types import is_string_dtype
for col in df.columns:
  if is_string_dtype(df[col].dtype):
    df[col] = df[col].str.strip()

#df.drop(subset=['Date'], inplace=True)
df.drop('Date', inplace=True, axis=1)
df.drop('Country', inplace=True, axis=1)

from sklearn.model_selection import train_test_split

x = df.loc[:, df.columns != 'Total Cases']
y = df['Total Cases']

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1, random_state=1)

print(train_x)
print(train_y)

data = pd.get_dummies(df, drop_first=True)

data

data = pd.get_dummies(data, drop_first=True)

data

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

train_x = sc.fit_transform(train_x)
test_x = sc.fit_transform(test_x)

from sklearn.svm import SVC

svm = SVC(random_state=1, verbose=1)
svm.fit(train_x, train_y)
predict_y = svm.predict(test_x)

#acc = accuracy_score(test_y, q_si_predict)
#print(acc)

from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier(n_estimators=20, random_state=0)
RF.fit(train_x, train_y)

"""total_test = df['Total Tests'].tolist()
country = df['Country'].tolist()

total_cases = df['Total Cases'].tolist()
population = df['Population'].tolist()

total_deaths = df['Total Deaths'].tolist()
total_recovered = df['Total Recovered'].tolist()

serious_or_critical = df['Serious or Critical'].tolist()
active_cases = df['Active Cases'].tolist()
date = df['Date'].tolist()


"""
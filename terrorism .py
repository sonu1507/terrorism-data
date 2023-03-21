#!/usr/bin/env python
# coding: utf-8

# In[46]:


print('Terrorism Attacks')


# In[47]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')


# In[48]:


data = pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\python csv\\internship\\terrorism.csv", encoding='ISO-8859-1', low_memory=False)


# In[49]:


data.head()


# In[50]:


data.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type','weaptype1_txt':'Weapon_type','motive':'Motive'},inplace=True)


# In[51]:


data=data[['Year','Month',
           'Day','Country',
           'Region','city',
           'latitude','longitude',
           'AttackType','Killed',
           'Wounded','Target',
           'Summary','Group',
           'Target_type',
           'Weapon_type','Motive']]


# In[52]:


data.head()


# In[53]:


data.isnull().sum()


# In[54]:


plt.figure(figsize=(12,8))
sns.heatmap(data.isnull())


# In[55]:


plt.figure(figsize=(20,8))
sns.countplot(data=data, x=data.Year)
plt.xticks(rotation = 270)
plt.title("Number Of Terrorist Activities Each Year")


# In[56]:


data.Region.value_counts()


# In[57]:


plt.subplots(figsize=(20,10))
sns.barplot(data=top_contries, x=top_contries.Country, y=top_contries.Count, palette='vlag')
plt.title("Top Affected Countries")
plt.xlabel("Countries")
plt.ylabel("Count")


# In[ ]:


top_contries = data.Country.value_counts()[:20].to_frame().reset_index()
top_contries.columns = ['Country', 'Count']
top_contries


# In[58]:


data.Region.value_counts()


# In[60]:


data['casualities']=data['Killed']+data['Wounded']
data.head()


# In[61]:


data.columns


# In[62]:


data.AttackType.value_counts()


# In[63]:


top_weapons = data.Weapon_type.value_counts()[:5].to_frame().reset_index()
top_weapons.columns = ['Weapon_Type', 'Count']

top_weapons


# In[64]:


plt.subplots(figsize=(16,5))
sns.barplot(data=top_weapons, 
              x=top_weapons.Weapon_Type,
              y=top_weapons.Count,
              palette='vlag')

plt.title("Top Weapons Used")
plt.xlabel("Weapon Type")
plt.ylabel("Count")
plt.grid()


# In[65]:


plt.figure(figsize=(12,8))
top5_weapons=data.Weapon_type.value_counts()[:5]
top5_weapons.plot(kind='pie',autopct="%1.1f%%")


# In[66]:


data.casualities.head(10)


# In[67]:


casualities_count = data.groupby("Country").casualities.sum().to_frame().reset_index().sort_values(by= 'casualities', ascending=False)[:10]

casualities_count


# In[68]:


plt.subplots(figsize=(15,6))
sns.barplot(data=casualities_count, 
            x=casualities_count.casualities,
            y=casualities_count.Country,
            palette='vlag')

plt.title("Number of Total Casualities in Each Contry")
plt.xlabel("Country")
plt.ylabel("Casualities")


# In[69]:


top5_region = data.Region.value_counts()[:6]
top5_region.plot(kind='pie', autopct = "%1.1f%%", figsize= (12,8))


# In[70]:


mid_nor = data[data.Region == "Middle East & North Africa"]

mid_nor.head()


# In[71]:


india = data[data.Country == "India"]

india.head()


# In[72]:


india


# In[73]:


x=india.AttackType.value_counts()[:6]
x


# In[74]:


x.plot(kind='pie', autopct = "%1.1f%%", figsize= (12,8))


# In[75]:


city_count=india.city.value_counts()[:15].to_frame().reset_index()
city_count.columns=['state','count']
city_count


# In[76]:


plt.figure(figsize=(20,8))
sns.countplot(data=data, x=data.Year)
plt.xticks(rotation = 270)
plt.title("Number Of Terrorist Activities Each Year")


# In[77]:


x=data['Year']
x


# In[78]:


casualities_count = data.groupby("Year").casualities.sum().to_frame().reset_index().sort_values(by= 'casualities', ascending=False)
casualities_count


# In[79]:


asia = data[data.Region == "South Asia"]

asia.head()


# In[80]:


asia.count()


# In[81]:


data = asia.Country.value_counts().reset_index()
data.columns = ['Country', 'Count']

data


# In[82]:


plt.subplots(figsize=(15,6))
sns.barplot(data=data, x=data.Country, y=data.Count)
plt.xticks(rotation = 90)
plt.title("Number Of Terrorist Activities asia Each Year")
plt.grid()


# In[83]:


data.count()


# In[84]:


asia.Month.value_counts().sort_values()


# In[85]:


plt.subplots(figsize=(15,6))
sns.countplot(data=asia, x=asia.Month)
plt.grid()
plt.title("Number of Terrorist Acctivities in asia Each Month")


# In[86]:


top6_country = asia.Country.value_counts()[:6]

top6_country


# In[87]:


top5_country.plot(kind='pie', autopct="%1.1f%%",figsize=(6,6))


# In[88]:


top20_ter_group = asia.Group.value_counts()[:20].reset_index()
top20_ter_group.columns = ["TerroristGroups", "Count"]
top20_ter_group.head()


# In[89]:


plt.subplots(figsize=(15,6))
sns.barplot(data=top20_ter_group, x=top20_ter_group.TerroristGroups, y=top20_ter_group.Count)
plt.xticks(rotation=90)
plt.title("Top 20 Terrorist Groups")


# In[90]:


died_year = asia.groupby('Year')['Killed'].sum().sort_values().to_frame().reset_index()

died_year


# In[91]:


plt.figure(figsize=(15,6))
sns.barplot(data=died_year, x=died_year.Year, y=died_year.Killed)
plt.grid()
plt.xticks(rotation=90)
plt.title("Number of People Died Each Year")
plt.xlabel("Year")
plt.ylabel("Killed")


# In[92]:



asia.Summary.value_counts().head()


# In[ ]:


print('The End')


# In[ ]:





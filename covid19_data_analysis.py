#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[2]:


os.listdir('E:\covid19 data analysis')


# In[3]:


files1 = (os.listdir('E:\covid19 data analysis'))[-7:]


# In[4]:


files1


# In[5]:


files1


# In[6]:


files1.remove('drive-download-20210621T195539Z-001.zip')


# In[7]:


files1


# In[ ]:





# In[8]:


def read_data(path,filename):
    return pd.read_csv(path+'/'+filename)


# In[9]:


path = 'E:\covid19 data analysis'
filename = 'worldometer_data.csv'
world_data = read_data(path,filename)


# In[10]:


world_data.head()


# In[11]:


day_wise= read_data(path,files1[2])


# In[12]:


grouped_data = read_data(path,files1[3])


# In[13]:


usa_data = read_data(path,files1[4])


# In[14]:


day_wise.head()


# In[15]:


day_wise.shape


# In[16]:


country_wise_data = read_data(path,files1[0])


# In[17]:


country_wise_data.shape


# In[18]:


province_data = read_data(path,files1[1])


# province_data.head()

# In[19]:


province_data.shape


# ## which country has maximum total cases,deaths,recovered and active cases?

# In[20]:


world_data.head()


# In[21]:


world_data.shape


# In[22]:


world_data.columns


# In[23]:


import plotly.express as px


# In[24]:


columns = ['TotalCases', 'TotalDeaths','TotalRecovered','ActiveCases']


# In[25]:


fig1=px.treemap(world_data,values=columns[0],path=['Country/Region'],title='Treemap representaion of total cases in a country')


# In[26]:


fig1.show()


# In[27]:


fig2 = px.treemap(world_data,values=columns[1],path=['Country/Region'],title='treemap representation of total deaths is a countries ')


# In[28]:


fig2.show()


# In[29]:


fig3 = px.treemap(world_data,values=columns[2],path=['Country/Region'],title='treemap represention of total recovered cases in a country')


# In[30]:


fig3.show()


# In[31]:


fig4 = px.treemap(world_data,values=columns[3],path=['Country/Region'],title='treemap representation of total active cases in a country')


# In[32]:


fig4.show()


# In[ ]:





# ### what is the trend of confirmed Deaths,Recovered and Active cases?

# In[33]:


day_wise.head()


# In[34]:


fig5=px.line(day_wise,x='Date',y='Confirmed',title='covid Confirmed case w.r.to date',template='plotly_dark')


# In[35]:


fig5


# In[36]:


fig6 = px.line(day_wise,x='Date',y='Deaths',title='covid death w.r.to date',template='plotly_dark')


# In[37]:


fig6


# In[38]:


fig7 = px.line(day_wise, x='Date', y='Recovered',title='covid recovered cases w.r.to date',template='plotly_dark')


# In[39]:


fig7


# In[40]:


fig8 = px.line(day_wise,x='Date',y='Active',title='covid active cases w.r.to date ',template='plotly_dark')


# In[41]:


fig8


# In[42]:


#now let us see a combined graph
fig9 = px.line(day_wise,x='Date',y=['Confirmed','Deaths','Recovered','Active'],title='combined data of covid w.r.to date',template='plotly_dark')


# In[43]:


fig9


# In[ ]:





# ### visualise population to tests done ratio.

# In[44]:


world_data.head()


# In[45]:


pop_to_tests_ratio = world_data['Population']/world_data['TotalTests'][0:20]


# In[46]:


pop_to_tests_ratio


# In[47]:


fig10=px.bar(world_data[0:20],x='Country/Region',y=pop_to_tests_ratio[0:20],color='Country/Region',title='population to tests done ratio of top ')


# In[48]:


fig10


# ### 20 countries which are badly affected by corona

# In[49]:


world_data.head()


# In[ ]:





# In[50]:


world_data.columns


# In[51]:


fig11 = px.bar(world_data.iloc[0:20],x='Country/Region',y=['Serious,Critical', 'TotalDeaths','TotalRecovered','ActiveCases','TotalCases'])


# In[52]:


fig11


# In[ ]:





# ### worst 20 countries having maximum confirmed cases

# In[53]:


world_data.head()


# In[ ]:





# In[54]:


fig12 = px.bar(world_data.iloc[0:20],y='Country/Region',x='TotalCases',color='TotalCases',text='TotalCases')
fig12.update_layout(template='plotly_dark',title_text='top 20 countries with max confirmed cases')
fig12


# In[ ]:





# ### worst 20 countries having max total deaths

# In[55]:


world_data.sort_values(by='TotalDeaths',ascending=False)


# In[56]:


fig13 = px.bar(world_data.sort_values(by='TotalDeaths',ascending=False).iloc[0:20],y='Country/Region',x='TotalDeaths',color='TotalDeaths',text='TotalDeaths')
fig13.update_layout(template='plotly_dark',title_text='top 20 countries with max deaths due to covid19')
fig13.show()


# In[ ]:





# ### top 20 countries having max Active cases

# In[57]:


fig14 = px.bar(world_data.sort_values(by='ActiveCases',ascending=False)[0:20],y='Country/Region',x='ActiveCases',color='ActiveCases',text='ActiveCases')
fig14.update_layout(template='plotly_dark',title_text='top 20 countries with max active cases of covid19 virus')
fig14.show()


# ### worst 20 countries having max Recovered Cases

# In[58]:


fig15 = px.bar(world_data.sort_values(by='TotalRecovered',ascending=False)[0:20],y='Country/Region',x='TotalRecovered',color='TotalRecovered',text='TotalRecovered')
fig15.update_layout(template='plotly_dark',title_text='top 20 countries with max total recovered cases of covid19 virus')
fig15.show()


# In[ ]:





# In[ ]:





# ### automating the analysis for each country

# In[ ]:





# In[66]:


from plotly.subplots import make_subplots
import plotly.graph_objects


# In[61]:


grouped_data.head()


# In[67]:


def country_visualisation(df, country):
    data = df[df['Country/Region']==country]
    data2 = data.loc[:,['Date','Confirmed','Deaths','Recovered','Active']]
    figure=make_subplots(rows=1,cols=4,subplot_titles=('confirmed','deaths','recoverd','active'))
    figure.add_trace(plotly.graph_objects.scatter(name='Confirmed',x=data2['Date'],y=data2['Confirmed']),row=1,col=1)
    
    figure.add_trace(plotly.graph_objects.scatter(name='Deaths',x=data2['Date'],y=data2['Deaths']),row=1,col=2)
    
    figure.add_trace(plotly.graph_objects.scatter(name='Recovered',x=data2['Date'],y=data2['Recovered']),row=1,col=3)
    figure.add_trace(plotly.graph_objects.scatter(name='Active',x=data2['Date'],y=data2['Active']),row=1,col=4)
    
    figure.update_layout(height=1000,width=1200,title_text = 'Date vs recoreded cases of {}'.format(country),template='plotly_dark')
    
    figure.show()
    


# In[68]:


country_visualisation(grouped_data,'Brazil')


# In[ ]:





# In[ ]:





# In[ ]:





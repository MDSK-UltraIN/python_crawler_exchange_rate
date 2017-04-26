
# coding: utf-8

# In[2]:

import pandas
dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')


# In[3]:

type(dfs)


# In[4]:

len(dfs)


# In[6]:

currency = dfs[0]


# In[11]:

type(currency)


# In[13]:

currency = currency.ix[:,0:5]


# In[18]:

currency.columns = [u'幣別',u'現金匯率-本行買入',u'現金匯率-本行賣出',u'即期匯率-本行買入',u'即期匯率-本行賣出']


# In[24]:

currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')


# In[26]:

currency


# In[28]:

currency.to_excel('currency.xlsx')


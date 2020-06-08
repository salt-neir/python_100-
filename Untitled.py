#!/usr/bin/env python
# coding: utf-8

# In[26]:


True == False


# In[27]:


True != 0


# In[28]:


False == 0


# In[29]:


True or False


# In[82]:


1 =='1'


# In[84]:


False and True


# In[31]:


eng = 'Korea COVID 19'
eng.lower()


# In[86]:


eng = 'Korea COVID 19'
eng.upper()


# In[87]:


eng='korea'
eng.upper()


# In[19]:


data = []
data.append('java')
data.append('python')
data.append('c++')
data.append('crytek')
data


# In[20]:


data[0], data[-1], data[1:], data[:2]


# In[98]:


data.sort()
data


# In[96]:


game = []
game.append('crysis1')
game.append('crysis2')
game.append('crysis3')
game


# In[23]:





# In[36]:


b=(1,2,3, '사', '오')
c=1,2,3
type(b), type(c)


# In[41]:


b[3] = 4


# In[42]:


print(b[3:], b[1:4])


# In[ ]:





# In[39]:


dic = {'name1' :'경민', '학번1':20103, 'name2' :'경민2', '학번2':20104}
print(dic.get('name1'))
print(dic.keys())
print(dic.values())


# In[33]:


lunch = {'햄버거', '치킨', '라면', '콜라', 10000}
dinner = {'피자', '족발', '라면', '콜라', 10000}


# In[34]:


lunch & dinner


# In[43]:


dinner | lunch


# In[44]:


pip install pandas


# In[46]:


import pandas as pd


# In[47]:


li = [1,2,3]
li


# In[49]:


type(li)


# In[51]:


s1 = pd.core.series.Series(li)
s1


# In[53]:


s2 = pd.core.series.Series(['일','이','삼'])
s2


# In[54]:


data=dict(num=s1, word=s2)
data


# In[56]:


pd.DataFrame(data)


# In[64]:


data = pd.DataFrame([['a',100],['b',200],['c',300]])
data.info()


# In[67]:


data.head(2)


# In[69]:


data.tail(2)


# In[70]:


col = ['1군','2군']


# In[73]:


pd.DataFrame([['a',100],['b',200],['c',300]],columns=col)


# In[79]:


man= [{'name':'은주','age':20, 'job':'j1'}, {'name':'민서','age':30, 'job':'j2'}, {'name':'경민','age':15, 'job':'j1'}]
pd.DataFrame(man, index=[1,2,3])


# In[89]:


a=[1,2,3]
b=[4,5,6]
df = [a,b]
dd=pd.DataFrame(df, index=[1,2], columns=['A', 'B', 'C'])
dd


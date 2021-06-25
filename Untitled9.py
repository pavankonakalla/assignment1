#!/usr/bin/env python
# coding: utf-8

# In[2]:


rows = int(input("Enter no of rows"))

for i in range(rows):
    for j in range(0, i + 1):
        print('*', end = '')
    print()

for i in range(1, rows):
    for j in range(i, rows):
        print('*', end = '')
    print()


# In[5]:


a=input("enter a name")
b=a[::-1]
b


# In[ ]:





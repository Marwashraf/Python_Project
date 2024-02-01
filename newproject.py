#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  time
def generate_id():
    "generate random id "
    id= time.time()
    # print(round(id))
    return round(id)


# In[2]:


def p_title(message):
    title=input(message)
    while True:
        if title.isalpha():
            return title
        print("----- please enter title again -----")
            


# In[3]:


def p_details(message):
    details=input(message)
    while True:
        if details.isalpha():
            return details
        print("----- please enter title again -----")


# In[4]:


def p_target(message):
    target=input(message)
    while True:
        if target.isdigit():
            return target
        print("----- please enter title again -----")


# In[5]:


import datetime as dt


# In[6]:


def S_date(message):
    while True:
        try:
            startD=input(message)
            startD = dt.datetime.strptime(startD, '%Y-%m-%d').date()
            return startD
        except ValueError:
            print("enter the right date again")


# In[7]:


def E_date(message):
    while True:
        try:
            endD=input(message)
            endD = dt.datetime.strptime(endD, '%Y-%m-%d').date()
            return endD
        except ValueError:
            print("enter the right date again")


# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[10]:


import  time
def generate_id():
    "generate random id "
    id= time.time()
    # print(round(id))
    return round(id)


# In[11]:


def f_name(message):
    while True:
        fname=input(message)
        if fname.isalpha():
            return fname
        print("----- please enter valid name -----")


# In[12]:


def l_name(message):
    while True:
        lname=input(message)
        if lname.isalpha():
            return lname
        print("----- please enter valid name -----")


# In[13]:


import re 


# In[14]:


import re 
def u_email(message):
    while True:
        email=input(message)
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(email_pattern,email):
            return email
        print("----- please enter valid email -----")


# In[15]:


def u_password(message):
    while True:
        password=input(message)
        if password.isdigit():
            password=int(password)
            return password
        print("----- please enter password again -----")


# In[16]:


def u_cpassword(message):
    while True:
        con_pass=input(message)
        if con_pass.isdigit():
            con_pass=int(con_pass)
            return con_pass
        print("----- please enter password again -----")


# In[17]:


def u_phone(message):
    while True:
        phone=input(message)
        if phone.isdigit() and len(phone)==11:
            phone=int(phone)
            return phone
        print("----- please enter vaild phone -----")


# In[18]:


def askforid(message):
    while True:
        try:
            id = int(input(message))
        except Exception as e:
            print("---- please enter an integer: ")
        else:
            return id


# In[ ]:





# In[ ]:





# In[ ]:





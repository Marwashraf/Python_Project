#!/usr/bin/env python
# coding: utf-8

# In[18]:


import  json
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, dt.date):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


# In[19]:


import datetime as dt


# In[20]:



def get_all_data():
    try:
        fildata = open("data.json", "r")
    except Exception as e:
        print(e)
    else:
        data = fildata.read() 
        fildata.close()
        data= data.strip('\n')
        if data:
            file_data = json.loads(data)
            return  file_data
        return []


# In[21]:


def save_new_data(userdata: dict):
    old_data = get_all_data()  
    old_data.append(userdata)
    valid_data = json.dumps(old_data, indent=2,cls=DateTimeEncoder)
    try:
        filed = open("data.json", "w")
    except Exception as e:
        return  False
    else:
        filed.write(valid_data)
        filed.close()
        return  True


# In[22]:


def search_user(userId):
    all_data= get_all_data()
    for index, user in enumerate(all_data):
        if user['id']==userId:
            print('found')
            return  index, user
    else:
        print("==== not found =====")
        return False


# In[23]:


def get_all_project():
    try:
        project_data = open("projects.json", "r")
    except Exception as e:
        print(e)
    else:
        data = project_data.read() 
        project_data.close()
        data= data.strip('\n')
        if data:
            project_data = json.loads(data)
            return  project_data
        return []


# In[24]:


def save_new_pdata(projectdata: dict):
    old_data = get_all_project()  
    old_data.append(projectdata)
    for project in old_data:
        project["Start Date"] = project["Start Date"].strftime('%Y-%m-%d')
        project["End Date"] = project["End Date"].strftime('%Y-%m-%d')
    valid_data = json.dumps(old_data, indent=2,cls=DateTimeEncoder)
    try:
        filed = open("projects.json", "w")
    except Exception as e:
        return  False
    else:
        filed.write(valid_data)
        filed.close()
        return  True


# In[25]:


def save_npdata(projectdata: dict):
    old_data = get_all_project()  
    old_data.append(projectdata)
    valid_data = json.dumps(old_data, indent=2,cls=DateTimeEncoder)
    try:
        filed = open("projects.json", "w")
    except Exception as e:
        return  False
    else:
        filed.write(valid_data)
        filed.close()
        return  True


# In[26]:


def search_pro(proId):
    all_data=get_all_project()
    for index, pro in enumerate(all_data):
        if pro['id']==proId:
            print('found')
            return  index, pro
    else:
        print("==== not found =====")
        return False


# In[27]:


def askforid(message):
    while True:
        try:
            id = int(input(message))
        except Exception as e:
            print("---- please enter an integer: ")
        else:
            return id


# In[28]:


def search_by_D_S(target_date):
    with open('projects.json', 'r') as file:
        data = json.load(file)
        found_projects = []
        for index, project in enumerate(data):
            if project.get('Start Date') == target_date:
                found_projects.append((index, project))
        return found_projects


# In[29]:


def search_by_D_E(target_date):
    with open('projects.json', 'r') as file:
        data = json.load(file)
        found_projects = []
        for index, project in enumerate(data):
            if project.get('End Date') == target_date:
                found_projects.append((index, project))
        return found_projects


# In[30]:


def get_all_pd():
    try:
        fildata = open("User_projeact.json", "r")
    except Exception as e:
        print(e)
    else:
        data = fildata.read() 
        fildata.close()
        data= data.strip('\n')
        if data:
            file_data = json.loads(data)
            return  file_data
        return []


# In[31]:


def save_new_u_p(userdata: dict):
    old_data = get_all_pd()  
    old_data.append(userdata)
    valid_data = json.dumps(old_data, indent=2,cls=DateTimeEncoder)
    try:
        filed = open("User_projeact.json", "w")
    except Exception as e:
        return  False
    else:
        filed.write(valid_data)
        filed.close()
        return  True


# In[32]:


def search_u_p(userId):
    all_data= get_all_pd()
    for index, user in enumerate(all_data):
        if user['id']==userId:
            print('found')
            return  index, user
    else:
        print("==== not found =====")
        return False


# In[ ]:





# In[33]:


#if __name__ == "__main__":
 #   search_pro(1701275247)


# In[ ]:





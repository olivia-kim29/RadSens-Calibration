#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import math


# In[32]:


data = pd.read_csv("calibration_data/Calibrated_Data.csv")


# In[33]:


#gets CPM and dose in array list
with open("calibration_data/Calibrated_Data.csv", 'r') as file:
    lines = file.readlines()
    uSv_h = []
    CPM = []
    for line in range(len(lines)):
        if line < 5:
            continue
        i = lines[line].find('Every Second')+13
        #j = lines[line].find('Every Second')+19
        k = 1
        temp = lines[line][i:i+10]
        comma = True
        while comma:
            if ',' in temp:
                temp = temp[:-1]
            else:
                comma = False
                break
        temp2 = len(temp)
        j = i+temp2+1
        
        temp3 = lines[line][j:j+10]
        comma = True
        while comma:
            if ',' in temp3:
                temp3 = temp3[:-1]
            else:
                comma = False
                break
        #while (lines[line][j + k] != ','): 
            #k+=1
        uSv_h.append(float(temp))
        CPM.append(temp3)
    print('uSv_h:', uSv_h)
    print('CPM:', CPM)


# In[34]:


data


# In[35]:


#calculates the average of the constant factor in the equation CPM * N = DOSE
n = []
for i in range(len(uSv_h)):
    n.append(float(uSv_h[i])/float(CPM[i]))
print("The n of CPM * N = DOSE is", sum(n)/len(n))


# In[36]:


PG_data = pd.read_csv("calibration_data/data-log.txt")
print(PG_data.columns[1])


# In[37]:


PG_data.loc[21] = [PG_data.columns[0],float(PG_data.columns[1]),float(PG_data.columns[2])]
PG_data


# In[38]:


PG_data.columns
PG_data.rename(columns={PG_data.columns[0]:'TimeStamp',PG_data.columns[1]:'CPM',
                          PG_data.columns[2]:'uncertainty'}, 
                 inplace=True)


# In[39]:


PG_data.columns
PG_data


# In[49]:


cpm_data = np.array(PG_data.CPM)
cpm_data


# In[50]:


c = np.mean(cpm_data)
u = np.mean(uSv_h)
u_e= np.std(uSv_h)
print(u)
print(u_e)
c


# In[69]:


#user input collection time
data_collection_time = 24
c_e = np.sqrt(c * data_collection_time)/data_collection_time
print(c_e)
k = c_e/c
print(k)


# In[56]:


PG_Calibration = u/c
print('PG_Calibration is', PG_Calibration)


# In[58]:


#propogating uncertainty
calibrated_uncertainty = np.sqrt((1/c)**2 * u_e**2 + ((u)/(c)**2)**2 * c_e**2)
print('calibrated_uncertainty is',calibrated_uncertainty)


# In[67]:


percent_uncertainty = calibrated_uncertainty/PG_Calibration
print("percent_uncertainty is", percent_uncertainty)


# In[ ]:





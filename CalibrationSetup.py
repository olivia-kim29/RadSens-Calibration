#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import math


# In[7]:


data = pd.read_csv("~/Desktop/RadSens-Calibration/calibration_data/20191023_15_26_43.csv")


# In[8]:


#gets CPM and dose in array list
with open("/Users/oliviakim/Desktop/RadSens-Calibration/calibration_data/20191023_15_26_43.csv", 'r') as file:
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
        uSv_h.append(temp)
        CPM.append(temp3)
    print('uSv_h:', uSv_h)
    print('CPM:', CPM)


# In[9]:


data


# In[10]:


#calculates the average of the constant factor in the equation CPM * N = DOSE
n = []
for i in range(len(uSv_h)):
    n.append(float(uSv_h[i])/float(CPM[i]))
print("The n of CPM * N = DOSE is", sum(n)/len(n))


# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:42:57 2018

@author: Administrator
"""

# coding: utf-8

# In[37]:


def counts(n):
    
    maxim=max(n)
    if maxim>len(n):
        print('choose other sorting techniques')
        return
    
    l=[0]*(maxim+1)
    
    for i in n:
        l[i]+=1
    
    n=[]
    for j in range(maxim+1):
        if l[j]!=0:
            n+=[j]*l[j]
    
    return n


# In[38]:


def ins(list):
    for i in range(1,len(list)):
        val=list[i]
        j=i
        while val<list[j-1] and j!=0:
                list[j]=list[j-1]
                j-=1
        list[j]=val
    return list


# In[39]:


import datetime as dt
import random as rd


def compare(n):
    z=[]
    for i in range(n):
        r=rd.randint(0,100)
        z.append(r)


    t1=dt.datetime.now()
    (counts(z))
    t2=dt.datetime.now()



    t3=dt.datetime.now()
    (ins(z))
    t4=dt.datetime.now()



    print('counting sort:',t2-t1)
    print('insertion sort:',t4-t3)
    return

compare(5000)
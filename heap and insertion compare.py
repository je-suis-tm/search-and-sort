# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:44:55 2018

@author: Administrator
"""

def heap(n):
    i=0
    maxlen=len(n)
    if maxlen<2:
        return n
    
    while maxlen>2**i:
        maxlen-=2**i
        i+=1
  
    for j in range(i+1,-1,-1):
            right=j*2+2
            left=j*2+1
            try:
                if n[left]<n[j]:
                    n[left],n[j]=n[j],n[left]
                
                try:
                    if n[right]<n[j]:
                        n[right],n[j]=n[j],n[right]
                      
                    if n[right]<n[left]:
                        n[right],n[left]=n[left],n[right]
                        
                except Exception:
                    pass
            except Exception:
                pass
         
    n[1:]=heap(n[1:])        
    return n


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
    (heap(z))
    t2=dt.datetime.now()



    t3=dt.datetime.now()
    (ins(z))
    t4=dt.datetime.now()



    print('heap sort:',t2-t1)
    print('insertion sort:',t4-t3)
    return

compare(1000)
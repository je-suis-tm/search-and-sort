# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:42:57 2018

@author: Administrator
"""

# coding: utf-8

# In[37]:
#counting sort is kinda different
#it works the best when there is large quantity of duplicates
#when the maximum value is larger than the length of list
#it is not economical to use counting sort
#counting sort is counting how many times each element has repeatedly showed up
#we create a list of the size of maximum value
#each index of the list represents the value of elements
#each value of the list represents the frequency of elements
#in the end we concatnate each element and its frequency
#simplest sort among all

def counts(n):
    #first we get the maximum value
    #if maximum value is larger than the length of the list
    #we would create a list with a huge space complexity
    #its not worth it
    #we can use a better sort
    maxim=max(n)
    if maxim>len(n):
        print('choose other sorting techniques')
        return
    
    #we create a list to store the frequency of each element
    #note that we use maximum value +1
    #as zero is also taken into consideration
    l=[0]*(maxim+1)
    
    #this is the calculation of the frequency
    for i in n:
        l[i]+=1
    
    #lets clear the original list
    #we add each element and its frequency back to the list
    n=[]
    for j in range(maxim+1):
        if l[j]!=0:
            n+=[j]*l[j]
    
    return n


# In[38]:
#the rest is just comparison with our benchmark insertion sort
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

#the time complexity for counting sort is o(n+k)
#k is determined by the maximum value
#its easy to see that counting sort easily beats o(n^2)
#however its time complexity is much larger

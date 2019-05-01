# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:42:57 2018

@author: Administrator
"""

# coding: utf-8

# In[1]:


#counting sort is kinda different from other sorts in this repo
#it works the best when there is large quantity of duplicates
#when the maximum value is larger than the length of list
#it is not economical to use counting sort
#counting sort is counting how many times each element has repeatedly showed up
#we create a list of the size of maximum value
#each index of the list represents the value of elements
#each value of the list represents the frequency of elements
#in the end we concatenate each element and its frequency
#simplest sort among all

def counting_sort(target):
    
    #first we get the maximum value
    #if maximum value is larger than the length of the list
    #we would create a list with a huge space complexity
    #its not worth it
    #we can use a better sort
    maxim=max(target)
    if maxim>len(target):
        print('choose other sorting techniques')
        return
    
    #we create a list to store the frequency of each element
    #note that we use maximum value +1
    #as zero is also taken into consideration
    l=[0]*(maxim+1)
    
    #this is the calculation of the frequency
    for i in target:
        l[i]+=1
    
    #lets clear the original list
    #we add each element and its frequency back to the list
    output=[]
    for j in range(maxim+1):
        if l[j]!=0:
            output+=[j]*l[j]
    
    return output



#the time complexity for counting sort is o(n+k)
#k is determined by the maximum value
#its easy to see that counting sort easily beats o(n^2)
#however its space complexity is really large


for i in range(100):
    
    target=rd.sample([i for i in range(1000)],100)

    if counting_sort(target)!=sorted(target):
        print('Erreur')

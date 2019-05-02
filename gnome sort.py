
# coding: utf-8

# In[1]:


import random as rd


# In[2]:


#gnome sort is another variation from bubble sort
#go the link below to check out the details of bubble sort
# https://github.com/je-suis-tm/search-and-sort/blob/master/bubble,%20selection%20and%20insertion%20sort.py
#similar to bubble sort, it does comparison and swap from one side to the other
#the different part is, once the swap occurs, it will reduce one step
#to make sure the newly swapped element is in the right spot of this partially sorted left part
#the concept is kinda like depth first search in graph theory
def gnome_sort(target):
    
    i=1
    maxval=len(target)

    while i<maxval:
        
        if target[i]>target[i-1]:
            i+=1
        else:
            target[i],target[i-1]=target[i-1],target[i]
            
            #this step is to ensure the index to stay in the range
            if i>1:
                i-=1
            else:
                i+=1
            
    return target


# In[3]:


for i in range(100):
    
    target=rd.sample([i for i in range(1000)],100)

    if gnome_sort(target)!=sorted(target):
        print('Erreur')


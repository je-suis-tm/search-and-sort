
# coding: utf-8

# In[1]:


import random as rd


# In[2]:


def cocktail_shaker_sort(target):

    left=0
    right=len(target)-1
    swap=True


    while left<right or not swap:
    
        swap=False

        for i in range(left+1,right+1):
            if target[i]<target[i-1]:
                target[i],target[i-1]=target[i-1],target[i]
                swap=True
        right-=1
        
        if not swap:
            return target
        
        swap=False
        
        for j in range(right,left,-1):
            if target[j]<target[j-1]:
                target[j],target[j-1]=target[j-1],target[j]
                swap=True

        left+=1
    
    return target


# In[3]:


for i in range(100):
    
    target=rd.sample([i for i in range(1000)],100)

    if cocktail_shaker_sort(target)!=sorted(target):
        print('Erreur')


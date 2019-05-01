
# coding: utf-8

# In[1]:


import random as rd


# In[2]:

#shaker sort, or cocktail sort, or cocktail shaker sort
#in this script, we will call it cocktail shaker sort
#with so many names, it is merely a variation of bubble sort
#go the link below to check out the details of bubble sort
# https://github.com/je-suis-tm/search-and-sort/blob/master/bubble,%20selection%20and%20insertion%20sort.py
#bubble sort repeatedly takes comparison from one side to the other
#usually left to right, takes n*(n-1) steps, assuming n is the size
#cocktail shaker sort has a similar mechanism
#except it compares its elements from left to right
#then right to left, later left to right
#the process looks like a cocktail shaker (not really)
#that is how the sort gets its name
#in theory, for a partially sorted list
#cocktail shaker sort takes less time than a bubble sort
def cocktail_shaker_sort(target):
    
    #we use left and right to define each round's start and end point
    left=0
    right=len(target)-1
    swap=True
    
    while left<right or not swap:
    
        swap=False
        
        #as usual, we start from left to right
        for i in range(left+1,right+1):
            if target[i]<target[i-1]:
                target[i],target[i-1]=target[i-1],target[i]
                swap=True
        right-=1
        
        #swap is the key to increase the efficiency
        #once there is no swap happened in the loop
        #we can conclude the target list is fully sorted
        if not swap:
            return target
        
        swap=False
        
        #then right to left
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


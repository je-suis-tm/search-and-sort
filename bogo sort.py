
# coding: utf-8

# In[1]:


import random as rd
import copy
import matplotlib.pyplot as plt


# In[2]:


#bogo, what the heck does it even mean
#i d call it bullocks sort
#it is not really sorting
#it keeps shuffling the list until the list is sorted
#kinda feel like monte carlo simulation
#the time complexity is (n+1)!
#for a large list, we may never wait for the day it gets sorted
def bogo_sort(target):
    
    counter=0
    
    play=copy.deepcopy(target)
    
    while play!=sorted(target):
        rd.shuffle(play)
        counter+=1
        
    return counter    


# In[3]:


target=rd.sample([i for i in range(1000)],5)
stats=[bogo_sort(target) for i in range(100000)]


# In[4]:


#visualize the ridiculous result of bogo sort by histogram
#it can go as far as 1400 times of shuffle to get it sorted from my test
#this is merely a five-element list
ax=plt.figure(dpi=100).add_subplot(111)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.hist(stats,bins=100,color='#01abaa',rwidth=0.7)
plt.title('Distribution of Bogo Sort')
plt.ylabel('Frequency')
plt.xlabel('Times of Shuffle')
plt.show()


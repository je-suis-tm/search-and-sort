
# coding: utf-8

# In[1]:


using Random
using Plots


# In[2]:


#bogo, what the heck does it even mean
#i d call it bullocks sort
#it is not really sorting
#it keeps shuffling the list until the list is sorted
#kinda feel like monte carlo simulation
#the time complexity is (n+1)!
#for a large list, we may never wait for the day it gets sorted


# In[3]:


function bogo_sort(arr)
    
    #deep copy is crucial
    arr_copy=deepcopy(arr)
    sort!(arr_copy)
    counter=0
    
    while arr_copy!=arr
    
        shuffle!(arr)
        counter+=1
        
    end
    
    return counter

end


# In[4]:


test_arr=rand(0:100,5)

#dont forget to deep copy
test_stats=[bogo_sort(deepcopy(test_arr)) for i in 1:100000]


# In[5]:


#visualize the ridiculous result of bogo sort by histogram
#it can go as far as 1400 times of shuffle to get it sorted from my test
#this is merely a five-element list


# In[6]:


#just out of curiosity
#could this be a power law distribution
histogram(test_stats,bins=10000,
    normed=:true,fill=(:blue, true),
    la=0,legend=:none,
    xlabel="iterations to reach sorted state",
    ylabel="frequency in 100k simulations")


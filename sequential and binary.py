
# coding: utf-8

# In[4]:



#sequential search is the easiest
#basically it is just doing a traversal on all items
def f(n,list):
    i=0
    #we create a boolen value to control the loop
    #when we find the value in list
    #we reset found so we break the loop
    #in the end the output is found
    found=False
    #note that while function does one extra iteration
    #so it is i<len(list) instead of i<=len(list)
    while i<len(list) and not found:
        if list[i]==n:
            found=True
        i+=1
    return found
        


# In[6]:


f(1,[4,5,1])


# In[11]:


#binary search is a bit more efficient
#the trouble is that it only works on sorted list
#when the list is large, sorting could take more time than doing a traversal
#sequential search could be more efficient
def bina(n,list):
    f=0
    #for binary search
    #we create the first and the last index
    #binary search starts from the middle
    #if the middle value is larger, we search the lower half, vice versa
    #we do the same trick on the lower half recursively the accurate number
    #note that l=len(list)+1 to get
    l=len(list)+1
    list=sorted(list)
    found=False
    while f<=l and not found:
        #to get the middle point of any length
        #we need to get the half of the sum of first and last index
        #so we use (f+l)//2 to get thhe middle value for any length
        i=(f+l)//2
        if list[i]==n:
            found=True
            #if the middle value is larger than the target
            #we search the lower half
            #we set l=i-1
            #cuz item i has already been checked
            #we just need the upper limit to get the middle next value
        elif list[i]>n:
            l=i-1
        else:
            #vice versa
            f=i+1
    return found


# In[13]:


bina(1,[4,5,7,9,24])


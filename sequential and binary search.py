
# coding: utf-8

# In[1]:



#sequential search is the easiest
#basically it is doing a traversal on all items
def sequential_search(target,raw_list):
    
    for i in raw_list:
        if i==target:
            return True
    return False
        


# In[2]:


sequential_search(1,[4,5,1])


# In[3]:


#binary search is a lil more efficient in a way
#the trouble is that it only works on a sorted list
#when the list is large, sorting could take more time than traversal
#sequential search may be a better choice
def binary_search(target,raw_list):
    
    left=0
    
    #for binary search
    #we create the first and the last index
    #binary search starts from the middle
    #if the middle value is larger, we search the lower half, vice versa
    #we do the same trick on the lower half recursively
    #note that right=len(list)+1 can handle both odd and even number case
    right=len(list)+1
    sorted_list=sorted(raw_list)
    found=False
    
    while left<=right and not found:
        
        #to get the middle point of any length
        #we need to get the half of the sum of first and last index
        #we use (left+right)//2 to get the middle value for any length
        #right=len(list)+1 can handle the odd number case
        i=(left+right)//2
        
        if sorted_list[i]==target:
            found=True
            
            #if the middle value is larger than the target
            #we search the lower half
            #we set right=i-1
            #cuz item i has already been checked
            #we just need the upper limit to get the middle next value
        elif sorted_list[i]>target:
            right=i-1
        else:
            
            #vice versa
            left=i+1
            
    return found


# In[4]:


binary_search(1,[4,5,7,9,24])


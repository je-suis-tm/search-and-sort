
# coding: utf-8

# In[1]:


#details of insertion sort can be found in the following link
# https://github.com/je-suis-tm/search-and-sort/blob/master/bubble%2C%20selection%20and%20insertion%20sort.jl
function insertion_sort(arr)
    
    for i in 2:length(arr)
        
        target=arr[i]
        
        j=i
        
        while (j!=1) && (target<arr[j-1])
            
            arr[j]=arr[j-1]
            j-=1
        end
        
        arr[j]=target
                
    end
    
    return arr
    
end


# In[2]:


#shell sort is a variation of insertion sort
#slicing method [i:group:length(arr)] is the key
#we gotta cut the original list into a few small groups

#assume we have a list of n elements
#the first step, we get a few sublists by [i:group:length(arr)]
#we apply insertion sort on those sublists and concatenate
#next, we do group/default
#and we obtain a few new sublists by [i:group:length(arr)]
#we apply insertion sort on new sublists and concatenate
#we keep using /default method and do insertion sort and concatenate
#til group reaches zero
#we concatenate sublists and do a final insertion sort
#we shall end up with a sorted list
#the time complexity is quite difficult to calculate
#it falls somewhere between linear and quadratic


# In[3]:


function shell_sort(arr,default=3)
    
    #the first step is to initialize default value
    #we will use this variable to divide the list and do slicing
    #in this case, default equals to 3
    #you can change the default number to any digit
    #bear in mind that this variable keeps the size of each sublist reasonable
    #we keep group divided by 3 until it reaches zero
    group=Int32(floor(length(arr)/default))
    
    while group>0
        
        for i in 1:group
            
            #equivalent to [i::group] in python
            subset=arr[i:group:length(arr)]
            
            #instead of reinventing the wheel
            #i directly call it in shell sort   
            subset=insertion_sort(subset)
            
            arr[i:group:length(arr)]=subset
            
        end
        
        group=Int32(floor(group/default))
        
    end
    
    return insertion_sort(arr)
    
end


# In[4]:


for _ in 1:100
    
    test_arr=rand(1000)

    if !(shell_sort(test_arr)==sort(test_arr))
        printstyled("Erreur",color=:red)
    end

end


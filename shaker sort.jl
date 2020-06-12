
# coding: utf-8

# In[1]:


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


# In[2]:


function cocktail_shaker_sort(arr)
    
    swap=true
    
    #we use left and right to define each round's start and end point
    left=1
    right=length(arr)
    
    while (left<right) || !(swap)
        
        swap=false
        
        #as usual, we start from left to right
        for i in left+1:right
            
            if arr[i]<arr[i-1]
                
                arr[i],arr[i-1]=arr[i-1],arr[i]
                swap=true
                
            end
            
        end
        
        right-=1
        
        #swap is the key to increase the efficiency
        #once there is no swap happened in the loop
        #we can conclude the target list is fully sorted
        if !(swap)
            return arr
        end
        
        swap=false
        
        #then right to left
        for i in right:-1:left+1
            
            if arr[i]<arr[i-1]
                
                arr[i],arr[i-1]=arr[i-1],arr[i]
                swap=true
                
            end
            
        end
        
        left+=1
        
    end
    
    return arr
    
end


# In[3]:


for _ in 1:100
    
    test_arr=rand(1000)

    if !(cocktail_shaker_sort(test_arr)==sort(test_arr))
        printstyled("Erreur",color=:red)
    end

end


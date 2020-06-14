
# coding: utf-8

# In[1]:


#gnome sort is another variation from bubble sort
#go the link below to check out the details of bubble sort
# https://github.com/je-suis-tm/search-and-sort/blob/master/bubble,%20selection%20and%20insertion%20sort.jl
#similar to bubble sort, it does comparison and swap from one side to the other
#the different part is, once the swap occurs, it will reduce one step
#to make sure the newly swapped element is in the right spot of this partially sorted left part
#the concept is kinda like depth first search in graph theory


# In[2]:


function gnome_sort(arr)

    i=2
    
    maxval=length(arr)
    
    while i<=maxval
    
        if arr[i]>arr[i-1]
            i+=1
        else
            arr[i],arr[i-1]=arr[i-1],arr[i]
            
            #this step is to ensure the index to stay in the range
            #this is the crucial step
            #repeatedly move the smallest to the front
            if i>2
                i-=1
            else
                i+=1
            end
        end
    
    end
    
    return arr
    
end


# In[3]:


for _ in 1:100
    
    test_arr=rand(1000)

    if !(gnome_sort(test_arr)==sort(test_arr))
        printstyled("Erreur",color=:red)
    end

end


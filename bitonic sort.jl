
# coding: utf-8

# In[1]:


#bitonic sort is my special feature in this repository!!!
#bitonic sort is cool as well as difficult to understand
#if you look for detailed explanation, you should check out geeksforgeeks
# https://www.geeksforgeeks.org/bitonic-sort/
#its python version is written in recursion
#which i found it really difficult to understand what the heck it was doing
#so i spent the whole day scratching my head to finish this non-recursive version
#a more straight forward explanation is the visualization from wikipedia
# https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/BitonicSort1.svg/843px-BitonicSort1.svg.png

#enjoy~~~


# In[2]:


function bitonic_sort(arr)
    
    if length(arr)==1
    
        return arr
    
    end
    
    i=1
    
    #primary iteration
    while 2^(i-1)<length(arr)/2+1
    
        j=2^i
    
        direction=get_direction(j,length(arr))
        
        #secondary iteration
        while j>=2
            
            #double loop helps us to find out who is comparing with who for each round
            #the sorting order is given by another function called get_direction
            for k in 1:j:length(arr)
                
                #k+Int32(j/2)-1 is crucial
                #make sure it doesnt go out of bound
                for l in k:k+Int32(j/2)-1
                    
                    if (arr[l]>arr[l+Int32(j/2)]) && (direction[l]==1)
                    
                        arr[l],arr[l+Int32(j/2)]=arr[l+Int32(j/2)],arr[l]
                        
                    end
                        
                    if (arr[l]<arr[l+Int32(j/2)]) && (direction[l]==-1)
                    
                        arr[l],arr[l+Int32(j/2)]=arr[l+Int32(j/2)],arr[l]
                        
                    end
                        
               end
            
            end
            
            #Int32 is important
            #list indices dont support float
            #when u do /, we get float by default
            j=Int32(j/2)
            
        end
     
        i+=1
        
    end
                
    return arr

end


# In[3]:


#the annoying part of bitonic sort is that
#some parts of the sequence are sorted by descending order
#other parts of the sequence are sorted by ascending order
#for each primary iteration, we create a sorting order sequence for each element
#for each secondary iteration inside a primary iteration
#the sorting order for each element is the same
function get_direction(iteration_number,len)
    
    direction=[0 for _ in 1:len]
    
    ind=[i for i in 1:iteration_number:len]
    
    for i in ind[1:2:length(ind)]
    
        direction[i]=1
        
    end
    
    for i in ind[2:2:length(ind)]
    
        direction[i]=-1
        
    end
    
    for i in 1:length(direction)
        
        if direction[i]==0
        
            direction[i]=direction[i-1]
            
        end
            
    end
            
    return direction

end


# In[4]:


#bitonic sort only works on a list with 2^n elements
for _ in 1:100
    
    test_arr=rand(2^rand(1:10))

    if !(bitonic_sort(test_arr)==sort(test_arr))
        printstyled("Erreur",color=:red)
    end

end


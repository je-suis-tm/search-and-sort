
# coding: utf-8

# In[1]:


#bubble
#bubble sort is the brute calculation
#the time complexity can go to n*(n-1), quadratic
#basically we create iterations to compare each element
#for the first round, we try to compare item i with the item right next to it
#we swap the place of two items if the item next to item i is smaller
#we keep applying this rule to the list during the traversal
#in the end, we must have placed the largest item at the end of list
#for the next iteration, we do the same trick
#except the length of traversal is reduced by one
#cuz we have already placed the largest item at the end of list
#we just need to find the second largest and place it right next to the end
#for the third iteration, we try to find the third largest item, etc


# In[2]:


function bubble_sort(arr)
    
    #for each round n, we find the nth largest number
    #we use reverse order from 1 to end
    #dont forget range starts from 1 in julia
    for i in reverse(1:length(arr))
        
        #given n, we go through n items in the list
        #compare then swap
        #range always includes the first and the last        
        #very different from python
        #thus we use i-1 in the inner loop
        for j in 1:i-1
            
            #if the item is larger than the one before it
            #we do a simultaneous swap
            if arr[j]>arr[j+1]
                arr[j],arr[j+1]=arr[j+1],arr[j]
            end
            
        end
        
    end
    
    return arr
    
end


# In[3]:


for _ in 1:100
    
    test_arr=rand(1000)

    if !(bubble_sort(test_arr)==sort(test_arr))
        printstyled("Erreur",color=:red)
    end

end


# In[4]:


#selection
#selection sort is a simplified version of bubble sort
#selection sort tries to find the nth largest number for each round n
#the next round is n-1, the same as bubble sort
#however, we only do traversal for each round
#we dont make any swap at all
#we simply use extra variable for the largest number and its index throughout traversal
#once we complete the traversal
#we move the largest number to the end of the list with the index we stored
#we repeat this process for each round


# In[5]:


function selection_sort(arr)
   
    #the first loop is similar bubble sort
    #the difference is that we are not going to use 1
    #we use 2 instead
    #the reason is that we would be left with one element for the last round
    #there is no point of doing so
    for i in reverse(2:length(arr))
        
        max_value=-Inf
        max_index=NaN
        
        #the second loop is the same as bubble sort
        for j in 1:i
            
            #if the value is larger than the extra one
            #we replace the extra value and its index
            if arr[j]>max_value
                max_value=arr[j]
                max_index=j
            end        
        end
        
        #once we find out the ith largest number
        #we swap it with the item at the end of unsorted list
        arr[max_index],arr[i]=arr[i],arr[max_index]
        
    end
    return arr
end


# In[6]:


for _ in 1:100
    
    test_arr=rand(1000)

    if !(selection_sort(test_arr)==sort(test_arr))
        printstyled("Erreur",color=:red)
    end

end


# In[7]:


#insertion
#insertion sort is like the reverse of bubble sort
#for bubble sort, you find nth largest number and
#put it at the end throughout iterations
#then we do the same trick on the unsorted part
#insertion is quite the opposite
#we are always dealing with the sorted list
#we start from the first two item
#we do comparison and swap if necessary
#after that we expand the sorted list
#we introduce the next item to the sorted list
#as the sorted list is sorted
#we can reduce the rounds of comparison
#as long as we find where the new item truly belongs to
#we insert it there


# In[8]:


function insertion_sort(arr)
    
    #finally! we are doing ascending order range function
    #it is straight forward
    #we dont wanna waste memory with one item so we start at 2
    for i in 2:length(arr)
        
        #we need to create an extra value to store the next item
        target=arr[i]
        
        #we still use j for second loop
        #we use while instead of if this time
        #we run a descending order loop on j
        #so we initialize j with i
        #which is the length of sorted target
        j=i
        
        #we do comparison and use j-=1 as iteration
        #j!=1 is to make sure the iteration doesnt go outta the length of the target
        while (j!=1) && (target<arr[j-1])
            
            #we dont swap
            #we simply shift it backwards
            arr[j]=arr[j-1]
            j-=1
        end
        
        #when we finish comparison and find out the index where we need to insert
        #we insert it
        arr[j]=target
        
        
    end
    
    return arr
    
end


# In[9]:


for _ in 1:100
    
    test_arr=rand(1000)

    if !(insertion_sort(test_arr)==sort(test_arr))
        printstyled("Erreur",color=:red)
    end

end


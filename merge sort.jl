
# coding: utf-8

# In[1]:


#merge sort is so called advanced sort
#its like a binary search in a way
#we keep dividing the list into two parts
#until it reaches base case when there are only two elements
#we sort the two elements and combine two sublists together 
#we do a traversal on both sublists
#we run through elements one by one
#we compare two lists with each other and insert into the bigger list
#its like shuffling poker deck
#say u got 1 and 2 from two different sublists
#1 is smaller than 2
#we insert 1 back to the bigger list
#the second element is 1.5
#it is still smaller than 2
#we keep inserting elements from a sorted sublist
#until the element is larger than 2
#now we insert 2 into the bigger list
#we keep doing the same procedure until we come back to the whole list
#we do a final sort, its all done

#from my description, u can easily tell that we need recursion
#i assume that is why its slowing down the sorting


# In[2]:


function merge_sort(arr)
    
    #so this is to check the base case
    #we wanna make sure the base case is a sublist with two elements
    #otherwise we got nothing to sort
    if length(arr)>1
        
        #this is how we keep splitting the list into two halves
        ind=Int32(floor(length(arr)/2))
        
        #we define each half as an individual list
        #then we run the same trick on each half recursively
        left=arr[1:ind]
        right=arr[ind+1:end]
        left=merge_sort(left)
        right=merge_sort(right)
        
        #let me denote ind_left as the index in left list
        #ind_right as the index in right list
        #ind_combined as the index in right and left combined list
        ind_left=1
        ind_right=1
        ind_combined=1
        
        #now we have three scenarios
        #the first case is both indexes are under list length
        #so we can compare two elements
        #we put the larger one into a bigger list
        #assuming an item from right side goes to a bigger list
        #we increase the right side index by 1 
        #and come back to the loop to see which element is bigger
        while (ind_left<=length(left)) && (ind_right<=length(right))
            if left[ind_left]<right[ind_right]
                arr[ind_combined]=left[ind_left]
                ind_left+=1
                ind_combined+=1
            else
                arr[ind_combined]=right[ind_right]
                ind_right+=1
                ind_combined+=1
            end
        end
        
        #the second case is when one index is outta list length
        #the other isnt
        #it can occur under two scenarios
        #one is that we use // method to divide a list into half
        #for a list with an odd number of elements
        #we definitely have one side bigger than the other
        #the other scenario is more common
        #assume it is an extreme case
        #we have two list, left and right
        #all the elements in left is smaller than the smallest element in right
        #so we have placed all elements in left into a bigger list
        #the index of right list hasnt increased even one bit
        #thats when we use the below section to add elements in right into a bigger list
        while (ind_left<=length(left)) && (ind_right>length(right))
            arr[ind_combined]=left[ind_left]
            ind_left+=1
            ind_combined+=1
        end
        
        #vice versa
        while (ind_left>length(left)) && (ind_right<=length(right))
            arr[ind_combined]=right[ind_right]
            ind_right+=1
            ind_combined+=1
        end
    end
    
    return arr
    
end


# In[3]:


for _ in 1:100
    
    test_arr=rand(1000)

    if !(merge_sort(test_arr)==sort(test_arr))
        printstyled("Erreur",color=:red)
    end

end


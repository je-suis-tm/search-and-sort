arr=[12,56,32,86,23,87]

#sequential search is the easiest
#basically it is doing a traversal on all items
function sequential_search(target,arr)
    for i in arr
        if i==target
            return true
        end
    end
    return false
end

sequential_search(23,arr)

#binary search is a lil more efficient in a way
#the trouble is that it only works on a sorted list
#when the list is large, sorting could take more time than traversal
#sequential search may be a better choice
function binary_search(target,arr)
    
    array=sort(arr)
    
    #unlike python
    #julia starts from 1 to end
    left=1
    right=length(array)
        
    #for binary search
    #we create the first and the last index
    #binary search starts from the middle
    #if the middle value is larger, we search the lower half, vice versa
    #we do the same trick on the lower half recursively
    while left<=right
        
        #to get the middle point of any length
        #we need to get the half of the sum of first and last index
        #we use (left+right)/2 to get the middle value for any length
        #we rounddown the number and make sure it is int32
        ind=Int32(round((left+right)/2,RoundDown))
        
        #if the middle value is smaller than the target
        #we search the upper half
        #we set left=ind+1
        #cuz ind has already been checked
        #we just need the lower limit to get the middle next value
        if target>array[ind]
            
            #crucial
            #the left has to add one 
            #so that the left can surpass the right
            #if nothing is found
            left=ind+1
            
        elseif target==array[ind]            
            return true
        
        #vice versa
        else
            
            #the same applies to right
            right=ind-1
        end
        
    end
    return false
    
end

binary_search(22,arr)





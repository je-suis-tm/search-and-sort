
# coding: utf-8

# In[1]:


#okay. the epic one!
#quick sort, mmm, not so quick
#the idea of quick sort is be the quickest
#first thing first, we gotta pick a pivot number for the list
#normally, people use the first element as pivot number
#however, we may encounter a case that the first element is the largest or the smallest
#that would make our sorting a total failure
#here i use the median of 3 approach
#take the first, the last and the one in the middle
#and get the median of the three
#we use the median as a pivot number
#after that, we do the same trick as merge sort
#we have a left index and a right index
#we do traversal on both indices
#say the left index comes from the left part
#the right index comes from the right part
#we compare two elements with pivot number at the same time
#there are four cases assuming that we dont have any duplicate values in the list
#first case, left is larger than pivot, right is smaller than pivot
#so we swap both
#second case, left is larger than pivot, right is larger than pivot as well
#we freeze the left, and move right side index one step backwards
#right=right-1
#then if left is larger than pivot, right is smaller than pivot
#we back to the first case
#if it is still the second case, we repeat this procedure until we move to first case
#or left and right indices cross, we stop the sorting
#third case, left is smaller than pivot, right is smaller than pivot
#it is the opposite case of the second case
#fourth case, left is smaller than pivot, right is larger than pivot
#great, we do nothing but moving both indices closer to the centre
#these are four basic scenarios when we do both traversals
#when left and right indices cross, we stop the sorting
#and we insert the pivot number in where indices cross
#the next step is just like merge sort
#we divide the list in two halves (excluding the pivot number)
#we perform the same trick on both halves recursively
#until we reach the base case when there are only two elements in the list
#we sort those two elements with simple comparison


# In[2]:


function quick_sort(arr)
    
    #the first step is to get a pivot number
    #it only works on list with more than two elements
    #otherwise there is no point of getting a pivot number
    if length(arr)>2
    
        #we take three elements, first, last and middle
        #we create a new list
        three_element=[arr[1],arr[end],arr[Int32(floor((1+length(arr))/2))]]
        
        #get the median
        #remove the max and the min
        #what is left is the pivot
        maxvalue=max(three_element[1],three_element[2],three_element[3])
        minvalue=min(three_element[1],three_element[2],three_element[3])
        setdiff!(three_element,maxvalue)
        setdiff!(three_element,minvalue)
        pivot=three_element[1]
        
        #move the pivot to the beginning of the list
        setdiff!(arr,pivot)
        insert!(arr,1,pivot)
        
        #initialize
        #first index is at 2, cuz we wanna exclude pivot number
        left=2
        right=length(arr)
        
        #here comes the real deal
        #when left and right dont cross
        #excluding a case when two indices equal to each other
        while left-1<right
                        
            #case 4
            if (arr[left]<pivot) && (arr[right]>pivot)
                left+=1
                right-=1
            
            #case 3
            elseif (arr[left]<pivot) && (arr[right]<pivot)
                left+=1
            
            #case 2
            elseif (arr[left]>pivot) && (arr[right]>pivot)
                right-=1
                
            #case 1
            else
                arr[left],arr[right]=arr[right],arr[left]
            end                     
                
        end
        
        #when left and right indices cross
        #when indices cross, we are one step after the input list is sorted
        #therefore, we insert pivot at left-1 instead of left
        if left>=right
            setdiff!(arr,pivot)
            insert!(arr,left-1,pivot)
        end
        
        #the recursive part
        #we do the same trick on two halves
        arr[left:end]=quick_sort(arr[left:end])
        arr[1:left-2]=quick_sort(arr[1:left-2])
        
    end
    
    #the base case
    #when we are left with two elements in a sublist
    #we just compare and return in reverse order
    #u might ask, what about one element
    #well, we dont have to do anything so no codes needed
    if length(arr)==2
        if arr[1]>arr[2]
            arr[1],arr[2]=arr[2],arr[1]
        end
    end
    
    return arr

end


# In[3]:


#there is a constraint for quick sort
#duplicate values would jeopardize everything we have built
#to solve that issue, we must amend the criteria for selecting pivot number
#for simplicity, i remove duplicates from our test list
#to handle duplicate values which might affect pivot
#my idea is to insert an extra if function
#if elements not at position 0 equal to pivot
#we create a temporary list to collect them
#when we plan to insert pivot
#we insert the temporary list to the full list 

#since we have recursive functions
#this approach to get a quick sort
#is kinda different from my textbook
#to see the alternative version
#plz click the link below
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html


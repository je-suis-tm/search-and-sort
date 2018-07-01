# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:13:45 2018

"""
#bubble
#bubble sort is the brute calculation
#basically we create iterations
#for the first round we try to compare the item next to item i iwth item i
#we swap the order if the the item next to item i is smaller
#we keep applying this rule to the list while we are doing the first traversal
#in the end, we must have placed the largest item at the end of list
#for the next iteration, we do the same trick
#except the length of traversal is reduced by one
#cuz we have already placed the largest item at the end of list
#we just need to find the second largest and place it at the end
#for the third iteration, we tried to find the third largest item etc

def bub(list):
    
    #each round n we find the n th largest number
    #so we descending order on range function
    #remember that range function always include the first variable and ignore the last
    #we use len(list) instead of len(list)-1 is because we are using j-1 to get i-1 below
    #the same applies to zero in the middle
    for i in range(len(list),0,-1):
        
        #given each n, we do a traversal on all of n items
        #compare then swap
        #cuz we are using j-1 below, so we start at 1
        #pior to len(list) above, we can place i at the end without missing any variable
        for j in range(1,i):
            
            #if the item is larger than the one before it
            #we do simultaneous swap
            if list[j]<list[j-1]:
                list[j],list[j-1]=list[j-1],list[j]
                
    return list
        
print(bub([641,455,3348,953,247,34,9,2634,845]))

#selection
#selection sort is a simplified version of bubble sort
#selection sort try to find the nth largest number for each round n
#the next round is n-1
#however, we only do traversal for each round
#we dont swap any order
#we simply use extra variable for the largest number and its index throughout traversal
#once we complete the traversal
#we move the largest number to the end of the list with the index we stored
#we repeat this for each round

def sel(list):
    
    #this is the first loop as bubble sort
    #the difference is that we are not going to use len(list)
    #so we use len(list)-1, which is a common practise
    #we dont use -1 simply becuz we would be left with one element for the last round
    #there is no point of doing so
    for i in range(len(list)-1,0,-1):
        
        #as we dont swap order
        #we need extra variables to store the maximum value and its index
        #we initialize it with the first element
        maxval=list[0]
        index=0
        
        #note that im using i+1
        #remember that range function always include the first variable and ignore the last
        #i wanna make sure i cover the whole list
        #as this is in ascending order, i dont need to worry about 0 or 1
        for j in range(i+1):
            
            #if the value is larger than the extra one
            #we replace the extra value and its index
            if list[j]>maxval:
                maxval=list[j]
                index=j
                
                #once we find out the i th largest number
                #we swap it with the item at the end
        list[index],list[i]=list[i],list[index]
        
    return list

print(sel([641,455,3348,953,247,34,9,2634,845]))

#insertion
#insertion sort is like the reverse of bubble sort
#for bubble sort, you find n th largest number and
#put it at the end throughout iterations
#then we do the same trick on the unsorted part
#insertion is quite the opposite
#we are always dealing with the sorted list
#we start from the first two item
#we do comparison and swap
#after that we expand the sorted list
#we introduce the next item to the sorted list
#as the sorted list is sorted, basically we do comparison and dont swap
#til we find where the next item truly belongs
#we insert it there
def ins(list):
    
    #finally! we are doing ascending order range function
    #it is straight forward
    #we dont wanna waste memory on step 0 with one item so we start at 1
    #and the len(list)-1 is the last item we need
    for i in range(1,len(list)):
        
        #we need create an extra value to store the next item
        val=list[i]
        
        #we still use j for second loop
        #we use while instead of if this time
        #cuz i spent whole afternoon and couldnt get if right
        #we run a descending order loop on j
        #so we initialize j with i
        #which is the length of sorted list
        j=i
        
        #we do comparison and use j-=1 as iteration
        #j!=0 is to make sure the iteration doesnt go outta the length of the list
        while val<list[j-1] and j!=0:
            
            #we dont swap order
            #we simply shift it backwards
                list[j]=list[j-1]
                j-=1
        
        #when we finish comparison and find out the index where we need to insert
        #we insert it
        list[j]=val
        
    return list

print(ins([641,455,3348,953,247,34,9,2634,845]))                

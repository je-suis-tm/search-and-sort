# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:13:45 2018

"""

import random as rd

#bubble
#bubble sort is the brute calculation
#the time complexity can go to n*(n-1)
#basically we create iterations to compare each element
#for the first round, we try to compare item i with the item right next to it
#we swap the place of two items if the the item next to item i is smaller
#we keep applying this rule to the list during the traversal
#in the end, we must have placed the largest item at the end of list
#for the next iteration, we do the same trick
#except the length of traversal is reduced by one
#cuz we have already placed the largest item at the end of list
#we just need to find the second largest and place it right next to the end
#for the third iteration, we try to find the third largest item, etc
def bubble_sort(target):
    
    #for each round n, we find the nth largest number
    #so we apply descending order on range function
    #remember that range function always include the first variable and ignore the last
    #we use len(target) instead of len(target)-1
    for i in range(len(target),0,-1):
        
        #given n, we go through n items in the list
        #compare then swap
        #we are using j-1 below, so we start at 1
        #prior to len(target) above, we can place i at the end of range function
        for j in range(1,i):
            
            #if the item is larger than the one before it
            #we do a simultaneous swap
            if target[j]<target[j-1]:
                target[j],target[j-1]=target[j-1],target[j]
                
    return target
        
for i in range(100):
    
    target=rd.sample([i for i in range(1000)],100)

    if bubble_sort(target)!=sorted(target):
        print('Erreur')

        
#selection
#selection sort is a simplified version of bubble sort
#selection sort try to find the nth largest number for each round n
#the next round is n-1, the same as bubble sort
#however, we only do traversal for each round
#we dont make any swap at all
#we simply use extra variable for the largest number and its index throughout traversal
#once we complete the traversal
#we move the largest number to the end of the list with the index we stored
#we repeat this process for each round
def selection_sort(target):
    
    #the first loop is the same as bubble sort
    #the difference is that we are not going to use len(target)
    #we use len(target)-1 instead
    #the reason is that we would be left with one element for the last round
    #there is no point of doing so
    for i in range(len(target)-1,0,-1):
        
        #as we dont swap
        #we need extra variables to store the maximum value and its index
        #we initialize it with the first element
        maxval=target[0]
        index=0
        
        #note that im using i+1
        #remember that range function always include the first variable and ignore the last
        #i wanna make sure i cover the whole target list
        #as this is in ascending order, i dont need to worry about 0 or 1
        for j in range(i+1):
            
            #if the value is larger than the extra one
            #we replace the extra value and its index
            if target[j]>maxval:
                maxval=target[j]
                index=j
                
                #once we find out the ith largest number
                #we swap it with the item at the end of unsorted list
        target[index],target[i]=target[i],target[index]
        
    return target


for i in range(100):
    
    target=rd.sample([i for i in range(1000)],100)

    if selection_sort(target)!=sorted(target):
        print('Erreur')
        
        

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
def insertion_sort(target):
    
    #finally! we are doing ascending order range function
    #it is straight forward
    #we dont wanna waste memory on step 0 with one item so we start at 1
    #and the len(target)-1 is the last item we need
    for i in range(1,len(target)):
        
        #we need to create an extra value to store the next item
        val=target[i]
        
        #we still use j for second loop
        #we use while instead of if this time
        #we run a descending order loop on j
        #so we initialize j with i
        #which is the length of sorted target
        j=i
        
        #we do comparison and use j-=1 as iteration
        #j!=0 is to make sure the iteration doesnt go outta the length of the target
        while val<target[j-1] and j!=0:
            
            #we dont swap
            #we simply shift it backwards
                target[j]=target[j-1]
                j-=1
        
        #when we finish comparison and find out the index where we need to insert
        #we insert it
        target[j]=val
        
    return target


for i in range(100):
    
    target=rd.sample([i for i in range(1000)],100)

    if insertion_sort(target)!=sorted(target):
        print('Erreur')

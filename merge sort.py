# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:13:17 2018


"""

import random as rd

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
def merge_sort(target):
    
    #so this is to check the base case
    #we wanna make sure the base case is a sublist with two elements
    #otherwise we got nothing to sort
    if len(target)>1:
        
        #this is how we keep splitting the list into two halves
        ind=len(target)//2
        
        #we define each half as an individual list
        #then we run the same trick on each half recursively
        left=target[:ind]
        right=target[ind:]
        merge_sort(left)
        merge_sort(right)
        
        #let me denote i as the index in left list
        #j as the index in right list
        #k as the index in right and left combined list
        i=0
        j=0
        k=0
        
        #now we have three scenarios
        #the first case is both indexes are under list length
        #so we can compare two elements
        #we put the larger one into a bigger list
        #assuming an item from right side goes to a bigger list
        #we increase the right side index by 1 
        #and come back to the loop to see which element is bigger
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                target[k]=left[i]
                i+=1
                k+=1
            else:
                target[k]=right[j]
                j+=1
                k+=1
        
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
        while i<len(left) and j>=len(right):
            target[k]=left[i]
            i+=1
            k+=1
        
        #vice versa
        while i>=len(left) and j<len(right):
            target[k]=right[j]
            j+=1
            k+=1
        
        return target
        

 for i in range(100):
    
    target=rd.sample([i for i in range(1000)],100)

    if merge_sort(target)!=sorted(target):
        print('Erreur')

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:13:17 2018


"""

#merge sort is so called advance sort
#basically its like a binary search
#we keep dividing the list into two parts
#until it reaches base case there are only two elements
#we sort the two elements and combine two sublists together 
#we do a traversal on both sublists
#we run through elements one by one
#we compare two lists with each other and insert into the bigger list
#its like shuffling poker
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

#from my description, u can easily tell that we may need recursion
#i assume that is why its slowing down the sorting
#if we replace recursion with memory or iterations
#it is supposed to be faster than insertion
def mer(list):
    
    #so this is to check the base case
    #we wanna make sure the base case is a sublist with two elements
    #otherwise we got nothing to sort
    if len(list)>1:
        
        #this is how we keep splitting the list into two halves
        ind=len(list)//2
        
        #we set each half as an individual list
        #then we run the same trick on each half recursively
        left=list[:ind]
        right=list[ind:]
        mer(left)
        mer(right)
        
        #let me denote i as the index in left list
        #j as the index in right list
        #k as the index in right and left combined list
        i=0
        j=0
        k=0
        
        #now we have three scenarios
        #the first case is both indexes are under list length
        #so we can compare two element in the list
        #we put the larger one into a bigger list
        #we increase the index by 1 
        #which we just moved the element to a bigger list
        #we come back to the loop to see which element is bigger
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                list[k]=left[i]
                i+=1

                k+=1
            else:
                list[k]=right[j]
                j+=1
                k+=1
        
        #the second case is when one index is outta list length
        #the other isnt
        #it can occur under two scenarios
        #one is that we use // method to divide a list into half
        #for a list with odd number length
        #we definitely have one list bigger than the other
        #the other scenario is more common
        #assume it is an extreme case
        #we have two list, left and right
        #all the elements in left is smaller than the smallest element in right
        #so we have placed all elements in left into a bigger list
        #the index of right list hasnt increased even one bit
        #thats when we use the below section to add elements in right into a bigger list
        while i<len(left) and j>=len(right):
            list[k]=left[i]
            i+=1
            k+=1
        
        #vice versa
        while i>=len(left) and j<len(right):
            list[k]=right[j]
            j+=1
            k+=1
        
        return list
        
#insertion basically is my benchmark now
#details can be found here
#https://github.com/tattooday/search-and-sort/blob/master/bubble%2C%20selection%20and%20insertion%20sort.py
def ins(list): 
    for i in range(1,len(list)): 
            
           val=list[i] 
            
           j=i 
           while val<list[j-1] and j!=0: 
                
                   list[j]=list[j-1] 
                   j-=1 
            
           list[j]=val 
    return list 

import datetime as dt 
import random as rd 
 
 

def compare(n): 
    z=[] 
    for i in range(n):
        r=rd.randint(0,7000) 
        z.append(r) 
    
    t1=dt.datetime.now() 
    (mer(z)) 
    t2=dt.datetime.now() 
  
 
    t3=dt.datetime.now() 
    (ins(z)) 
    t4=dt.datetime.now() 
  
 
    
    print(((t2-t1).microseconds)) 
    print(((t4-t3).microseconds)) 

#unsurprisingly, the recursion sort is much slower
#so far, insertion seems to be the fastest sorting method
compare(10000)

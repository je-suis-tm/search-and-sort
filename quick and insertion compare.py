# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:32:34 2018

@author: Administrator
"""

#okay. the epic one!
#quick sort, mmm, not so quick
#the idea of quick sort is be the quickest
#firstly, we have to choose a pivot number for the list
#normally, people use the first element as pivot number
#however, we may encounter a case that the first element is the largest or the smallest
#that would make our sorting a total failure
#so i use the median of 3 approach
#i take the first, the last and the one in the middle
#and i get the median of the three
#i use it as a pivot number
#after that, we do the same trick as merge sort
#we have a first index and a last index
#we do traversal on both indices
#say the first index comes from left part, the last comes from the right
#we compare two elements with pivot number at the same time
#there are four cases assuming that we dont have any duplicate values in the list
#first, left is larger than pivot, right is smaller than pivot
#so we swap both
#second,left is larger than pivot, right is larger than pivot
#so we freeze the left, and move right index last one step back
#so its actually l=l-1
#then if left is larger than pivot, right is smaller than pivot
#we back to the first case
#if it is still the same, we keep doing this procedure until we move to first case
#or f and l indices cross, we stop the sorting
#third, left is smaller than pivot, right is smaller than pivot
#it is the opposite case of second case, so vice versa
#fourth, left is smaller than pivot, right is larger than pivot
#great, we do nothing but moving both indices closer to the centre
#so these are four basic scenarios when we do both traversals
#when f and l indices cross, we stop the sorting
#and we insert the pivot number in where indices cross
#the next step is just like merge sort
#so we divide the list in two halves (excluding the pivot number)
#we perform the same trick on both halves recursively
#until we reach the base case that there are only two elements in the list
#we sort those two elements with simple comparison

def qui(list):


    #so the first step is to get a pivot number
    #it only works on list with more than two elements
    #otherwise there is no point of getting a pivot number
    if len(list)>2:
        
        #so we take three elements, first, last and middle
        #we get a new list
        test=[list[0],list[len(list)//2],list[-1]]
        
        #this is how we get the median
        #there are only 3 elements
        #so the sum of indices is 3
        #all we need to do is to deduct the maximum and the minimum ones indices
        #we get the median one index
        pivotindex=3-test.index(max(test))-test.index(min(test))
        
        #this part is very confusing
        #mostly due to simultaneous swap
        #its actually just swapping
        #if the median number index is 0
        #we do nothing
        #cuz we initialize pivot number at index 0 later
        #if not
        #we do a swap
        #so we use slicing method to get the median number index in original list
        #we use that index we got to get the actual element
        #then we swap it with element 0
        if pivotindex!=0:
            list[list.index(test[pivotindex])] , list[0] = list[0] , list[list.index(test[pivotindex])]

            

            
        #so we initialize pivot number at position 0
        pivot=list[0]
        
        #first index is at 1, cuz we wanna exclude pivot number
        f=1
        
        #last index is at the end of the list
        l=len(list)-1




#here comes the real deal
#when f and l doesnt cross
#excluding a case when they equal to each other
#note that unlike f is from the beginning 
#l is from the end, so its l-=1
        while f-1<l:

            #case 1
            if list[f]>pivot and list[l]<pivot:
                list[f],list[l]=list[l],list[f]
                l-=1
                
            #case 3
            if list[f]<pivot and list[l]<pivot:
                f+=1

            #case 2
            if list[f]>pivot and list[l]>pivot:
                l-=1

            #case 4
            if list[f]<pivot and list[l]>pivot:
                f+=1
                l-=1

            

            
#this is when they cross
#we pop the pivot number and insert it at position f-1
#the key is that indices cross, its already one step after the list is sorted
#therefore, we insert pivot at f-1 instead of f
        if f>=l:
            list.insert(f-1,list.pop(0))

        
#this is the recursive part
#we do the same trick on two halves
        list[:f-1]=qui(list[:f-1])
        list[f:]=qui(list[f:])
        

    
#this is the base case
#when we left with two elements in a sublist
#we just compare and return in reverse order
#u might ask, what about one element
#well, we dont have to do anything so no codes needed
    if len(list)==2:
        if list[0]>list[1]:
            return list[::-1]
        
 

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

#its time to compare two sorting methods
def compare(n): 

    z=[] 

    for i in range(n):
        r=rd.randint(0,7000) 
        
        #the only difference from other sorting comparison
        #is that with duplicate value
        #the way we handle pivot number must be altered
        #for simplicity, i remove duplicates from our test list
        
        #to handle duplicate values which might affect pivot
        #my idea is to insert an extra if function
        #if elements not at position 0 equal to pivot
        #we create a new list to collect them
        #when we plan to insert pivot
        #we insert as many as was in the list
        if r not in z:
            z.append(r) 

    

    t1=dt.datetime.now() 
    test1=(qui(z)) 
    t2=dt.datetime.now() 

  
    t3=dt.datetime.now() 
    test2=(ins(z)) 
    t4=dt.datetime.now() 

  

    print(((t2-t1).microseconds)) 
    print(((t4-t3).microseconds)) 
    print('quick sort:',test1==sorted(z))
    print('insertion sort:',test2==sorted(z))


compare(100000)

#as i have predicted
#its slower than insertion sort
#cuz we have recursive functions
#my approach to get a quick sort
#is kinda different from my textbook
#to see the alternative
#go to
#http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html



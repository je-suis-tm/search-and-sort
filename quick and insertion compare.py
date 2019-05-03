# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:32:34 2018

@author: Administrator
"""

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
#the right index comes from the right paart
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
def quick_sort(target):


    #the first step is to get a pivot number
    #it only works on list with more than two elements
    #otherwise there is no point of getting a pivot number
    if len(target)>2:
        
        #we take three elements, first, last and middle
        #we get a new list
        test=[target[0],target[len(target)//2],target[-1]]
        
        #this is how we get the median
        #there are only 3 elements
        #so the sum of indices is 3
        #0+1+2
        #all we need to do is to exclude the maximum and the minimum indices
        #we get the median s index
        pivotindex=3-test.index(max(test))-test.index(min(test))
        
        #this part is very confusing
        #mostly due to simultaneous swap
        #it is merely swapping
        #if the median number index is 0
        #we do nothing
        #cuz we initialize pivot number at index 0 later
        #if not
        #we make a swap
        #we use slicing method to get the index of the median in original list
        #we use that index to get the actual element
        #then we swap it with element 0
        if pivotindex!=0:
            target[target.index(test[pivotindex])] , target[0] = target[0] , target[target.index(test[pivotindex])]

            
        #with the previous swap, we initialize pivot number at position 0
        pivot=target[0]
        
        #first index is at 1, cuz we wanna exclude pivot number
        left=1
        
        #last index is at the end of the list
        right=len(target)-1


        #here comes the real deal
        #when left and right dont cross
        #excluding a case when two indices equal to each other
        while left-1<right:

            #case 1
            if target[left]>pivot and target[right]<pivot:
                target[left],target[right]=target[right],target[left]
                l-=1
                
            #case 3
            if target[left]<pivot and target[right]<pivot:
                left+=1

            #case 2
            if target[left]>pivot and target[right]>pivot:
                right-=1

            #case 4
            if target[left]<pivot and target[right]>pivot:
                left+=1
                right-=1            

            
        #when left and right indices cross
        #we pop the pivot number and insert it at position left-1
        #when indices cross, we are one step after the input list is sorted
        #therefore, we insert pivot at left-1 instead of left
        if left>=right:
            target.insert(left-1,target.pop(0))

        
        #the recursive part
        #we do the same trick on two halves
        target[:left-1]=quick_sort(target[:left-1])
        target[left:]=quick_sort(target[left:])
        

    
    #the base case
    #when we are left with two elements in a sublist
    #we just compare and return in reverse order
    #u might ask, what about one element
    #well, we dont have to do anything so no codes needed
    if len(target)==2:
        if target[0]>target[1]:
            return target[::-1]
        
 

    return target


        
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


for i in range(100):
    
    target=rd.sample([i for i in range(1000)],100)

    if quick_sort(target)!=sorted(target):
        print('Erreur')

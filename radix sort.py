## -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:48:39 2018

@author: Administrator
"""
import random as rd

#radix sort is fun
#there are two ways to do it
#the first approach is we start from the right
#the second one is to start from the left
#in this context, i choose the first approach
#they are equivalent
#we get the first digit of all elements
#sort these elements based upon the first digit
#for instance, 215 and 19
#9 for 19 is larger than 5 for 215
#for the first round, we get 215,19
#we move on to the second digit of all elements from the right
#we apply the same technique of sorting based upon the second digit
#until we reach to the very left digit of the maximum value in the list
#the sort is completed
#for instance, the second round would be 215,19
#since the second digit of both numbers are 1
#the final round is 19,215
#as 0 for 19 is smaller than 2 for 215
#period

#to implement this method in python
#we can apply //10%10 technique
#for the first round, //10%10 gets the first digit from the left
#for the second round, //100%10 gets the second digit from the left
#and so on
#i personally prefer to use a dictionary to store elements in its rightful place
#i use digits from 0-9 as the key of dictionary
#there are other elegant solutions, plz check the link at the very end
def radix_sort(target):
    
    #the first part is to find the largest element in the list
    #next, we find out the length of it
    #so we can use the length in a loop to control how many digits we need to obtain
    temp=len(str(max(target)))
    
    for i in range(temp):
        
        #each time, we clear the dictionary
        dictionary={'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
        
        #this is a traversal on all elements in the list
        for j in range(len(target)):
            
            z=target[j]
            radix=10**i
            
            #(z//radix)%10) is the technique to get digits
            #when we get it, we turn it into string
            #so that we can use dictionary slicing
            #to store the element in its rightful place
            (dictionary[str((z//radix)%10)]).append(z)
            
        #we have to empty the list after we put all elements into the dictionary
        target=[]
        
        #this loop is unnecessary
        #we can use target=dictionary[0]+...+dictionary[9]
        #again, i am a lazy person
        #cut me some slack, s’il vous plaît
        for k in range(10):
            target+=dictionary[str(k)]
   
    return target



#surprisingly, the radix sort is really fast
#the time complexity of radix sort is o(k*n)
#k depends on the digits of the maximum value in the list
#well, its harder to get a number like 10^1000 than getting a list with 10^1000 elements
#when we get a list with smaller n and larger k
#radix sort may be a terrible choice

#there are other ways of writing radix sort
#i believe my way has too much space complexity
#this one is rather smart and elegant
# https://www.geeksforgeeks.org/radix-sort/


for i in range(100):
    
    target=rd.sample([i for i in range(1000)],100)

    if radix_sort(target)!=sorted(target):
        print('Erreur')

## -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:48:39 2018

@author: Administrator
"""
import random as rd
import datetime as dt 

#radix sort is fun
#there are two ways to do it
#the first approach is we start from the right
#the second one is to start from the left
#in this context, i choose the first approach
#they are equivalent
#lets see we get the first digits of all elements
#sort these elements based on the first digits
#for instance, 215 and 19
#9 for 19 is larger than 5 for 215
#for the first round, we get 215,19
#we move on to the second digits of all elements from the right
#we apply the same technique of sorting based on digits
#until we reach to the very left digit of the maximum value in the list
#the sort is completed
#for our instance, the second round would be 215,19
#since they both are 1
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
def rad(n):
    
    #the first part is to find the largest element in the list
    #next, we find out the length of it
    #so we can use the length in a loop to control how many digits we need to obtain
    temp=len(str(max(n)))
    for i in range(temp):
        
        #each time, we clear the dictionary
        dictionary={'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
        
        #this is traversal on all elements in the list
        for j in range(len(n)):
            z=n[j]
            radix=10**i
            
            #(z//radix)%10) is the technique to get digits
            #when we get it, we turn it into string
            #so that we can use dictionary slicing
            #to store the element in its rightful place
            (dictionary[str((z//radix)%10)]).append(z)
            
            #we have to empty the list after we put all elements into the dictionary
        n=[]
        
        #this loop is unnecessary
        #we can use n=dictionary[0]+...+dictionary[9]
        #again, i am a lazy person
        #cut me some slack, plz
        for k in range(10):
            n+=dictionary[str(k)]
   
    return n

#

def ins(list): 

    for i in range(1,len(list)): 
           val=list[i]
           j=i 
           while val<list[j-1] and j!=0: 
                   list[j]=list[j-1]
                   j-=1 
           list[j]=val 
    return list 


#next, its our comparison with insertion sort
def compare(n): 

    z=[] 
    for i in range(n):
        r=rd.randint(0,1000000000000) 
        z.append(r) 

    
#
    t1=dt.datetime.now() 

    a=(rad(z)) 

    t2=dt.datetime.now() 

 

    t3=dt.datetime.now() 

    b=(ins(z)) 

    t4=dt.datetime.now() 

# 
    if a==b:
        print(((t2-t1).microseconds)) 
        print(((t4-t3).microseconds)) 



#surprisingly, the radix sort is faster

#insertion is supposed to be o(n^2)
#radix is o(k*n)
#k depends on the digits of the maximum value in the list
#well, its harder to get a number like 10^1000 than getting a list with 10^1000 elements
#which makes radix sort is faster than insertion sort in this scenario
#when we get a list with smaller n and larger k
#insertion would be much faster!

#there are other ways of writing radix sort
#i believe my way has too much space complexity
#this one is actually smart and elegant
# https://www.geeksforgeeks.org/radix-sort/

compare(1000)
        

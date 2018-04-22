# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:48:39 2018

@author: Administrator
"""
import random as rd
import datetime as dt 


def rad(n):
    temp=len(str(max(n)))
    for i in range(temp):
        dictionary={'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
        for j in range(len(n)):
            z=n[j]
            radix=10**i
            (dictionary[str((z//radix)%10)]).append(z)
        n=[]
        
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


#
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
#radix should depend on the digits of the maximum value in the list
#well, its harder to get a number like 10^1000 than getting a list with 10^1000 elements
#which makes radix sort is faster than insertion sort in this scenario
#there are other ways of writing radix sort
#i believe my way has too much space complexity
#this one is actually smart and elegant
# https://www.geeksforgeeks.org/radix-sort/

compare(1000)
        
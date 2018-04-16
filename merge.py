# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:13:17 2018


"""

def mer(list):
    
    
    if len(list)>1:
        ind=len(list)//2
        left=list[:ind]
        right=list[ind:]
        mer(left)
        mer(right)
        i=0
        j=0
        k=0
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                list[k]=left[i]
                i+=1
                k+=1
            else:
                list[k]=right[j]
                j+=1
                k+=1
                
        while i<len(left) and j>=len(right):
            list[k]=left[i]
            i+=1
            k+=1
        
        while i>=len(left) and j<len(right):
            list[k]=right[j]
            j+=1
            k+=1
        
        return list
        
       

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

compare(10000)
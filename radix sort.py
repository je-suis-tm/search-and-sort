# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:48:39 2018

@author: Administrator
"""
import random as rd


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



def ran(n):
    temp=[]
    for i in range(n):
        x=rd.randint(0,500)
        temp.append(x)
        
    print(temp)
    print(rad(temp))
    return

ran(10)
        
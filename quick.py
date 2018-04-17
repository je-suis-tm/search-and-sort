# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:53:56 2018


"""



def qui(list):

    if len(list)>2:
        test=[list[0],list[len(list)//2+1],list[-1]]
        pivotindex=3-test.index(max(test))-test.index(min(test))
        if pivotindex!=0:
            list[list.index(test[pivotindex])],list[0]=list[0],list[list.index(test[pivotindex])]
            
            
        pivot=list[0]
        f=1
        l=len(list)-1
        while f-1<l:
            
            if list[f]>pivot and list[l]<pivot:
                list[f],list[l]=list[l],list[f]
                l-=1
            if list[f]<pivot and list[l]<pivot:
                f+=1
            if list[f]>pivot and list[l]>pivot:
                l-=1
            if list[f]<pivot and list[l]>pivot:
                f+=1
                l-=1
            
            
        if f>=l:
            list.insert(f-1,list.pop(0))
        
        print(pivot)
        print(list,f)
        print(list[:f-1])
        print(list[f:])
        list[:f-1]=qui(list[:f-1])
        list[f:]=qui(list[f:])
    
    if len(list)==2:
        if list[0]>list[1]:
            return list[::-1]
    

            
    return list

import random as rd
z=[]
for i in range(20):
    z.append(rd.randint(1,500))
z=list(set(z))    
print(qui(z))

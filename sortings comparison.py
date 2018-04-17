# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:31:58 2018

@author: Administrator
"""


#this is basically a collection of all sorting methods from my textbook
#so far i tried all sortings from my textbook
#i found out all those advanced sorting methods are slower than insertion sort
#selection sort is somewhere close to insertion sort
#but a bit slower
#shell sort is a variation of insertion sort
#but its slower than both selection and insertion
#merge sort and quick sort are recursive
#they turn out to be even worse
#the worst one is bubble sort, undoubtedly
#i have gathered all sorting methods together and check the efficiency

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)
   return alist

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
   return alist

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
   return alist

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      

      sublistcount = sublistcount // 2
      
    return alist

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

def mergeSort(alist):
    
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist


import random as rd
import datetime as dt

def compare(n): 

    z=[] 

    for i in range(n):
        r=rd.randint(0,7000) 
        if r not in z:
            z.append(r) 

    t1=dt.datetime.now()
    (quickSort(z)) 
    t2=dt.datetime.now() 

    t3=dt.datetime.now() 
    (insertionSort(z)) 
    t4=dt.datetime.now() 
    
    t5=dt.datetime.now() 
    (bubbleSort(z)) 
    t6=dt.datetime.now()
    
    t7=dt.datetime.now()
    (selectionSort(z)) 
    t8=dt.datetime.now()
    
    t9=dt.datetime.now() 
    (shellSort(z)) 
    t10=dt.datetime.now()
    
    t11=dt.datetime.now() 
    (mergeSort(z)) 
    t12=dt.datetime.now()

  

    print(('quick sort:',(t2-t1).microseconds)) 
    print(('insertion sort:',(t4-t3).microseconds)) 
    print(('bubble sort:',(t6-t5).microseconds)) 
    print(('selection sort:',(t8-t7).microseconds)) 
    print(('shell sort:',(t10-t9).microseconds))
    print(('merge sort:',(t12-t11).microseconds))


compare(20000)
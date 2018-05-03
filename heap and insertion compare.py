# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:44:55 2018

@author: Administrator
"""

#heap sort is the alternative way of selection sort
#the difference is that sorting implements on binary heap instead of list
#well, u can argue binary heap is expressed in list
#binary heap basically is a complete binary tree
#for each node it has no more than two children
#the tree is as far left as possible
#the difference with binary tree is that we keep minimum or maximum at root
#in this case we keep minimum at root
#similar to selection sort
#we only need to get the smallest number for each round
#and our list keep shrinking until we are left with one element for final round
#however, the traversal is kinda different from selection sort
#what we do is to compare two children with parent node
#we keeps the smallest among the family of three as parent node for each node
#until we reach the root and we successfully keep the smallest at root
#next step is to remove the root and we get the new tree to sort
#we would do that recursively
#otherwise we would have to use loops in loops

def heap(n):
    #denote i as the height of the tree
    i=0
    maxlen=len(n)
    #when we are left with one element
    #that is the base case for recursion
    if maxlen<2:
        return n
    
    #this part is to find out how many layers we got for binary heap
    #note that i starts from 0
    while maxlen>2**i:
        maxlen-=2**i
        i+=1
        
    #as i starts from zero
    #we have to use i+1 to make sure each height has been traveled
    #until we reach the base case, height 0, the root
    for j in range(i+1,-1,-1):
        #the special character of binary heap is that 
        #right child is alway even number index
        #and left child, vice versa
            right=j*2+2
            left=j*2+1
            #we have to use try in case the node is the leaf
            #and if there is no left child
            #there wont be right child
            #far left principle of binary heap
            #we compare the parent with two children
            #we swap and keep the smallest as parent 
            try:
                if n[left]<n[j]:
                    n[left],n[j]=n[j],n[left]
                
                try:
                    if n[right]<n[j]:
                        n[right],n[j]=n[j],n[right]
                      
                    if n[right]<n[left]:
                        n[right],n[left]=n[left],n[right]
                        
                except Exception:
                    pass
            except Exception:
                pass
    
    #recursively, we shrink the size of the list
    #by removing its root which is the smallest element for each iteration
    n[1:]=heap(n[1:])        
    return n

#now lets compare
def ins(list):
    for i in range(1,len(list)):
        val=list[i]
        j=i
        while val<list[j-1] and j!=0:
                list[j]=list[j-1]
                j-=1
        list[j]=val
    return list


# In[39]:


import datetime as dt
import random as rd


def compare(n):
    z=[]
    for i in range(n):
        r=rd.randint(0,100)
        z.append(r)


    t1=dt.datetime.now()
    (heap(z))
    t2=dt.datetime.now()



    t3=dt.datetime.now()
    (ins(z))
    t4=dt.datetime.now()



    print('heap sort:',t2-t1)
    print('insertion sort:',t4-t3)
    return

compare(1000)

#heap sort is somewhat faster than insertion sort
#its time complexity is o(nlogn)
#however, this is written in recursive function
#we can use iterations to replace recursion

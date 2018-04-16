
# coding: utf-8

# In[68]:

#details of insertion sort can be found here
# https://github.com/tattooday/search-and-sort/blob/master/bubble%2C%20selection%20and%20insertion%20sort.py
def ins(list):
   
    for i in range(1,len(list)):
        
        val=list[i]
        
        j=i
        while val<list[j-1] and j!=0:
            
                list[j]=list[j-1]
                j-=1
        
        list[j]=val
        
    return list

#shell sort is a variation of insertion sort
#basically i have to use slicing methond [a::b]
#to cut the list into a few small groups
#assume we have a list of n elements
#the first step, we do b=n//a, we get a few list[a::b]
#we apply insertion sort on those sublists and concatenate
#next, we do b=b//a, and we get a few new list[a::b]
#we apply insertion sort on new sublists and concatenate
#we keep using //a method and do insertion sort and concatenate
#til b reaches zero
#we concatenate sublists and do a final insertion sort
#we obtain a sorted list
#the time complexity is quite difficult to calculate

def shel(list):
   #the first step is to initialize a
   #we will use it to divide the list and do slicing
   #in this case, i use 4
   #we keep b divided by 4 until it reaches zero
    a=4
    b=len(list)//a
    while b>0:
         #instead of rewriting insertion sort
         #i directly use it in shell sort     
        for i in range(b):
            temp=ins(list[i::b])
            #the final loop is actually the slicing of [a::b]
            #[a::b] equals to [a+j*b] j for j in range()
            for j in range(len(temp)):
                list[i+j*b]=temp[j]
        b=b//a
    return ins(list)


# In[118]:


import datetime as dt
import random as rd

#we run two functions to see which one is faster
#we set n to generate n random variables
#we concatenate them and pass the list to two different sorts
#we store the information of each function's processing time
def compare(n):
    z=[]
    for i in range(n):
        r=rd.randint(0,7000)
        z.append(r)

    t1=dt.datetime.now()
    (shel(z))
    t2=dt.datetime.now()

    t3=dt.datetime.now()
    (ins(z))
    t4=dt.datetime.now()

    output=[]
    output.append(((t2-t1).microseconds))
    output.append(((t4-t3).microseconds))
    return output


# In[133]:


#i run 20 times for one function
#then take the population mean
#eventually print how long each function takes to sort
def avg(n):
    l1=0
    l2=0
    for i in range(20):
        l1+=(compare(n)[0])
        l2+=(compare(n)[1])
    print('for %d elements'%(n))
    print('shell:',l1/20)
    print('insertion:',l2/20,'\n')


# In[140]:
#theoretically shell sort should be faster
#but my code for shell sort is definitely o(n^3)
#undoubtedly shell sort is slower
#i tried many codes by others
#they still seem to be slower than insertion
#so why?

avg(10)
avg(100)
avg(500)
avg(800)
avg(1000)
avg(1200)
avg(1500)


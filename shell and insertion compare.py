
# coding: utf-8

# In[68]:


def ins(list):
   
    for i in range(1,len(list)):
        
        val=list[i]
        
        j=i
        while val<list[j-1] and j!=0:
            
                list[j]=list[j-1]
                j-=1
        
        list[j]=val
        
    return list


def shel(list):
    
    b=len(list)//4
    while b>0:
        final=[0]*len(list)
        for i in range(b):
            temp=ins(list[i::b])
            for j in range(len(temp)):
                final[i+j*b]=temp[j]
        b=b//4
    return ins(final)


# In[118]:


import datetime as dt
import random as rd

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


avg(10)
avg(100)
avg(500)
avg(800)
avg(1000)
avg(1200)
avg(1500)


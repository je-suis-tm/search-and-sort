
# coding: utf-8

# In[1]:


import random as rd


# In[2]:


def bitonic_sort(target):

    i=1
    while 2**(i-1)<len(target)/2+1:
    
        j=2**i
    
        direction=get_direction(j,len(target))
    
        while j>=2:
        
            for k in range(0,len(target),j):            
                for l in range(k,k+int(j/2)):
                    if target[l]>target[l+int(j/2)] and                     direction[l]==1:
                        target[l],target[l+int(j/2)]=target[l+int(j/2)],target[l]
                    if target[l]<target[l+int(j/2)] and                     direction[l]==-1:
                        target[l],target[l+int(j/2)]=target[l+int(j/2)],target[l]
            
            j=int(j/2)
     
        i+=1
                
    return target
    
    

def get_direction(iteration_number,length):
    
    temp=iteration_number
    
    direction=[0]*length
    
    ind=[i for i in range(0,length,temp)]
    
    for i in ind[0::2]:
        direction[i]=1
    for i in ind[1::2]:
        direction[i]=-1
    
    for i in range(len(direction)):
        if direction[i]==0:
            direction[i]=direction[i-1]
            
    return direction
    


# In[3]:


for j in range(100):
    
    target=[rd.randint(0,100) for i in range(2**rd.randint(1,10))]
    if bitonic_sort(target)!=sorted(target):
        print('Erreur')


# In[4]:


#https://www.geeksforgeeks.org/bitonic-sort/
#https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/BitonicSort1.svg/843px-BitonicSort1.svg.pngR


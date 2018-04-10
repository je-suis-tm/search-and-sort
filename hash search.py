
# coding: utf-8

# In[1]:


#hash chaining

def hash(li):
    k={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
    for i in li:
        if k[i%11]=='':
            k[i%11]=i
        else:
            temp=[]
            temp.append(k[i%11])
            temp.append(i)
            k[i%11]=temp
    
    return k
        

def hashsearch(n,li):
    hashli=hash(li)
    temp=hashli[n%11]
    if type(temp)==list:
        
        if n in temp:
            return True
        else:
            return False
    elif temp==n:
        return True
    else:
        return False


# In[2]:


hashsearch(55,[21,55,89,67])


# In[11]:


#linear probing
def hash(li):
    k={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
    temp=[]
    badhash=[]
    for i in li:
        if k[i%11]=='':
            k[i%11]=i
        else:
            temp.append(i)
    
    while len(temp)>0:
        pop=temp.pop()
        j=pop%11
        c=0
        while c<10:
            if k[j]!='':
                j+=1
                if j>10:
                    j=0
            else:
                k[j]=pop
                pop=''
            c+=1
        
        
        if pop!='':
            badhash.append(pop)
            pop=''
    
    if len(badhash)>0:
        print(badhash)       
    
    return k
        

def hashsearch(n,li):
    hashli=hash(li)
    temp=n%11
    c=0
    if hashli[temp]==n:
        return True
    else:
        while c<10:
            if hashli[temp]!=n:
                temp+=1
                if temp>10:
                    temp=0
            else:
                return True
            c+=1
        return False
            


# In[15]:


hashsearch(67,[21,55,89,67,12,12])


# In[16]:


#quadratic probing
def hash(li):
    k={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
    temp=[]
    badhash=[]
    for i in li:
        if k[i%11]=='':
            k[i%11]=i
        else:
            temp.append(i)
    
    while len(temp)>0:
        pop=temp.pop()
        j=pop%11
        c=0
        x=1
        while c<10:
            if k[j]!='':
                j+=x**2
                if j>10:
                    j=j%11
            else:
                k[j]=pop
                pop=''
            c+=1
            x+=1
        
        
        if pop!='':
            badhash.append(pop)
            pop=''
    
    if len(badhash)>0:
        print(badhash)       
    
    return k
        

def hashsearch(n,li):
    hashli=hash(li)
    temp=n%11
    c=0
    x=1
    if hashli[temp]==n:
        return True
    else:
        while c<10:
            if hashli[temp]!=n:
                temp+=x**2
                if temp>10:
                    temp=temp%11
            else:
                return True
            c+=1
            x+=1
        return False
            


# In[22]:


hashsearch(67,[21,55,89,67,12,12,12,12,12,12,12,12,12,12,78])


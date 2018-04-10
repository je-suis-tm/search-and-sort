
# coding: utf-8

# In[1]:

#i would recommend to read algorith and data structure before getting to know hashtable
# http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html
#i use the hash function described in the book, which is mod eleven %11
#so i apply hash function to all the values in a given list(which i created)
#then i get the output value
#and assuming this is a perfect hash function
#each value from the list should have a unique hash value
#i would create a dictionary based on the unique hash value
#and assign all the values from the list into dictionary
#when i wanna search for something
#i just need to apply hash function to the target
#and check the dictionary for that particular hash value
#O(1), simple AF, not really...
#we could have the same hash value for different values from the list
#this is so called hash collision
#there are three ways of solving hash collision in the book
#which are chaining, linear probing and quadratic probing
#i deliberately create an imperfect hash function to see how it goes


#hash chaining
#the easiest one
#basically stack all the collision together
#form a list under that hash value
#does it make search easier?
#not really, if the list gets too large
#it would slow down the search
#the good thing about it is that you always have all the values in the dictionary
#for other methods, you either have to increase hash table size or drop values


#the first function is to create a dictionary
#assign values from the list based on hash value
def hash(li):
    k={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
    for i in li:
        #this is to check if there is already a value stored under that hash value
        #if no, its fine
        #if yes, we create a list and append the collision
        if k[i%11]=='':
            k[i%11]=i
        else:
            #note that we append both values into the list
            #the first one is already there
            #thats when we realize there is collision so we gotta keep both
            temp=[]
            temp.append(k[i%11])
            temp.append(i)
            k[i%11]=temp
    
    return k
        
#now its the search part
#we just apply hash function on target and get hash value
#we look up the hash value in dictionary
def hashsearch(n,li):
    hashli=hash(li)
    temp=hashli[n%11]
    #we gotta check if there is collision under this hash value
    #if dictionary keeps a list under this hash value
    #we have to check the list
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


# In[11]:True




#linear probing
#when collision occurs, we try to find the next empty slot to store it
#it sounds reasonable but it is also trouble
#what if we run through the whole dictionary
#and there is no slot?
#i choose to drop the values
#or we can reset the hash function or expand the dictionary
#in best cases, it is faster than chaining
#in worst case, it is slower

#forgive me for using the same variable name
#i just copy and paste from the previous one
#note that i create a temporary list to append collision items
def hash(li):
    k={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
    temp=[]
    badhash=[]
    for i in li:
        if k[i%11]=='':
            k[i%11]=i
        else:
            temp.append(i)
    
    #the first loop is to make sure every collision item will be popped
    while len(temp)>0:
        pop=temp.pop()
        j=pop%11
        #c is a counter
        #in the second loop
        #c is to determine whether we have gone through the entire list
        c=0
        while c<10:
            #when the next one isnt empty, we keep iterating
            #when j exceeds ten, we return it to 0
            #alternatively we can use mod eleven %11
            if k[j]!='':
                j+=1
                if j>10:
                    j=0
            else:
                k[j]=pop
                #after value is assigned
                #we clear the value
                pop=''
            c+=1
        
        #the reason of checking this temporary variable called pop
        #is to make sure that we will print out those items which didnt get assigned
        #we append them to a list called badhash and print
        if pop!='':
            badhash.append(pop)
            pop=''
    #if the hashing is imperfect, we print out badhash list
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


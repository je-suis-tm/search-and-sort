
# coding: utf-8

# In[1]:

#i would recommend you to read algorithm and data structure before messing with hashtable
# http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html
#this script features the hash function described in the book, which is mod eleven %11
#we apply hash function to all the values in a given list
#we shall obtain the output value for each element
#and assuming this is a perfect hash function
#each value from the list should have a unique hash value
#we can create a dictionary based on the unique hash value
#and assign all the values from the list into dictionary
#when we wanna search for something
#we just need to apply hash function to the target
#and make query on the dictionary for that particular hash value
#O(1), simple AF, not really...
#we could encounter the same hash value for different values from the list
#this is so called hash collision
#there are three ways of solving hash collision in the book
#which are chaining, linear probing and quadratic probing
#lets deliberately create an imperfect hash function to see how it goes


#hash chaining
#the easiest one
#basically stack all the collision together
#form a list under that hash value
#does it make search easier?
#not really, if the list under one hash value gets too large
#it would slow down the search
#the good thing about this method is that you always have all the values in the dictionary
#for other methods, you either have to increase hash table size or drop values


#the first function is to create a dictionary
#assign values from the list to the dictionary based on hash value
def hash(raw_list):
    
    hashtable={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
    
    for i in raw_list:
        
        #check if there is already a value stored under that hash value
        #if no, its fine
        #if yes, we create a list and append the collision
        if hashtable[i%11]=='':
            hashtable[i%11]=i
            
        else:
            
            #note that we append both values into the list
            temp=[]
            temp.append(hashtable[i%11])
            temp.append(i)
            hashtable[i%11]=temp
    
    return hashtable
        
#now its the search part
#we just apply hash function on target and get hash value
#we look up the hash value in dictionary
def hashsearch(target,raw_list):
    hashtable=hash(raw_list)
    temp=hashtable[n%11]
    
    #we gotta check if there is collision under this hash value
    #if dictionary keeps a list under this hash value
    #we have to further check the list
    if type(temp)==list:
        
        if target in temp:
            return True
        else:
            return False
        
    elif temp==target:
        return True
    else:
        return False


# In[2]:


hashsearch(55,[21,55,89,67])


# In[3]:


#linear probing
#when collision occurs, we try to find the next empty slot to store it
#it sounds reasonable but it is also trouble
#what if we run through the whole dictionary
#and there is no slot?
#we can choose to drop the values
#or we can reset the hash function or expand the dictionary
#in the best case, it is faster than chaining
#in the worst case, it is slower

#note that i create a temporary list to append collision items
def hash(raw_list):
    
    hashtable={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
    temp=[]
    badhash=[]
    
    for i in raw_list:
        if hashtable[i%11]=='':
            hashtable[i%11]=i
        else:
            temp.append(i)
    
    #the first loop is to make sure every collision will be popped
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
            if hashtable[j]!='':
                j+=1
                if j>10:
                    j=0
            else:
                hashtable[j]=pop
                
                #after the value is assigned
                #we clear the value
                pop=''
                
            c+=1
        
        #the reason of checking this temporary variable called pop
        #is to make sure that we will print out those items which didnt get assigned
        if pop!='':
            badhash.append(pop)
            pop=''
    
    #if the hashing is imperfect, we print out badhash list
    if len(badhash)>0:
        print(badhash)       
    
    return hashtable
        
#the search part is very similar to the chaining one
def hashsearch(target,raw_list):
    
    hashtable=hash(raw_list)
    temp=target%11
    c=0
    
    if hashtable[temp]==target:
        return True
    else:
        
        #when we cannot find the value at hash value
        #we begin our linear probing
        #its the same process as the hash function
        #except we only need to return T/F
        while c<10:
            if hashtable[temp]!=target:
                temp+=1
                if temp>10:
                    temp=0
            else:
                return True
            c+=1
        return False
            


# In[4]:


hashsearch(67,[21,55,89,67,12,12])


# In[5]:

#quadratic probing
#it sounds math intensive with the word quadratic
#as a matter of fact, it is simple AF
#we just replace the add one method with add quadratic values
#the difference is that we need an extra variable to store quadratic value
def hash(raw_list):
    
    hashtable={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
    temp=[]
    badhash=[]
    
    for i in raw_list:
        if hashtable[i%11]=='':
            hashtable[i%11]=i
        else:
            temp.append(i)
    
    while len(temp)>0:
        pop=temp.pop()
        j=pop%11
        c=0
        
        #x is where we store quadratic value
        x=1
        while c<10:
            if hashtable[j]!='':
                
                #the loop is basically the same as linear probing
                #except we add quadratic value
                #note that its quite difficult 
                #to determine whether we have been through the entire list
                #so i still set counter limit at 10
                j+=x**2
                
                if j>10:
                    
                    #note that i use mod eleven %11 when iteration exceeds hash table size
                    j=j%11
            else:
                hashtable[j]=pop
                pop=''
            c+=1
            x+=1
        
        
        if pop!='':
            badhash.append(pop)
            pop=''
    
    if len(badhash)>0:
        print(badhash)       
    
    return hashtable
        
    
#the search is basically the same as linear probing
#except linear part is substituted with quadratic
def hashsearch(target,raw_list):
    
    hashtable=hash(raw_list)
    temp=target%11
    c=0
    x=1
    
    if hashtable[temp]==target:
        return True
    else:
        while c<10:
            if hashtable[temp]!=target:
                temp+=x**2
                if temp>10:
                    temp=temp%11
            else:
                return True
            c+=1
            x+=1
        return False
            


# In[6]:

hashsearch(67,[21,55,89,67,12,12,12,12,12,12,12,12,12,12,78])

#we get False in the end
#its quite interesting that for the same hash value 67,12,78
#we can store 78 in hash table but not 67
#given the fact that 67 appears first of 78


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


# In[2]:


arr=[21,55,89,67,12,12]


# In[3]:


#hash chaining
#the easiest one
#basically stack all the collision together
#form a list under that hash value
#does it make search easier?
#not really, if the list under one hash value gets too large
#it would slow down the search
#the good thing about this method is that you always have all the values in the dictionary
#for other methods, you either have to increase hash table size or drop values


# In[4]:


#the first function is to create a dictionary
#assign values from the list to the dictionary based on hash value
function create_hashtable(arr,default=11)
        
    #create hashtable
    hashtable=Dict()
    
    #initialize
    for i in 0:(default-1)
        hashtable[i]=[]
    end
    
    #add value into hashtable
    #using folding method
    for i in arr
        push!(hashtable[i%default],i)
    end

    return hashtable
end


# In[5]:


#now its the search part
#we just apply hash function on target and get hash value
#we look up the hash value in dictionary
function hash_search(target,arr,default=11)
    
    #get hashtable
    hashtable=create_hashtable(arr,default)
    
    #find value through hash value
    if target in hashtable[target%default]
        return true
    else
        return false
    end
end


# In[6]:


hash_search(12,arr)


# In[7]:


#linear probing
#when collision occurs, we try to find the next empty slot to store it
#it sounds reasonable but it is also trouble
#what if we run through the whole dictionary
#and there is no slot?
#we can choose to drop the values
#or we can reset the hash function or expand the dictionary
#in the best case, it is faster than chaining
#in the worst case, it is slower


# In[8]:


#the first function is to create a dictionary
#assign values from the list to the dictionary based on hash value
function create_hashtable(arr,default=11)
        
    #create hashtable
    hashtable=Dict()
    
    
    #unwanted is a temporary list to append collision items
    unwanted=[]
    
    #keep track of values with no allocation
    badhash=[]
    
    #initialize
    for i in 0:(default-1)
        hashtable[i]=""
    end
    
    #add value into hashtable
    for i in arr
        if hashtable[i%default]==""
            hashtable[i%default]=i
        else
            #make sure every collision will be tracked
            push!(unwanted,i)
        end
    end
        
    for i in unwanted
        
        #c is a counter
        #in the inner loop
        #c is to determine whether we have gone through the entire list
        c=0
        modnumber=i%default
        stop=false
            
        while !stop && c<=default-1
            
            
            #when modnumber exceeds ten, we return it to 0
            #alternatively we can use mod eleven %11
            modnumber+=1
            if modnumber>default-1
                modnumber=0
            end
            
            #when the next slot isnt empty, we keep iterating
            if hashtable[modnumber]==""
                hashtable[modnumber]=i
                stop=true
            end
                
            c+=1
        end
        
        #make sure that we will print out those items which didnt get assigned
        if !stop
            push!(badhash,i)
        end
    end
    
    #if the hashing is imperfect, we print out badhash list
    if !isempty(badhash)
        println(badhash)
    end
    
    return hashtable
end


# In[9]:


#the search part is very similar to the chaining one
function hash_search(target,arr,default=11)
    
    #get hashtable
    hashtable=create_hashtable(arr,default)
    
    #find value through hash value
    modnumber=target%default
    if target in hashtable[modnumber]
        return true
    else
        
        #when we cannot find the value at hash value
        #we begin our linear probing
        #its the same process as the hash function
        #except we only need to return T/F
        counter=0
        
        while counter<=default-1
            modnumber+=1
            
            if modnumber>default-1
                modnumber=0
            end
            
            if target==hashtable[modnumber]
                return true            
            end
            counter+=1
        end
    end
    return false
end


# In[10]:


hash_search(89,arr)


# In[11]:


#quadratic probing
#it sounds math intensive with the word quadratic
#as a matter of fact, it is simple AF
#we just replace the add one method with add quadratic values


# In[12]:


#the first function is to create a dictionary
#assign values from the list to the dictionary based on hash value
function create_hashtable(arr,default=11)
        
    #create hashtable
    hashtable=Dict()
    
    unwanted=[]
    badhash=[]
    
    #initialize
    for i in 0:(default-1)
        hashtable[i]=""
    end
    
    #add value into hashtable
    for i in arr
        if hashtable[i%default]==""
            hashtable[i%default]=i
        else
            push!(unwanted,i)
        end
    end
    
    
    for i in unwanted
        c=1
        modnumber=i%default
        stop=false
        
        #the loop is basically the same as linear probing
        #except we add quadratic value
        #note that its quite difficult 
        #to determine whether we have been through the entire list
        #so i still set counter limit at 10
        while !stop && c<=default
            
            modnumber+=c^2
                        
            #note that i use mod eleven %11 when iteration exceeds hash table size
            if modnumber>default-1                                
                modnumber=modnumber%default
            end
                            
            if hashtable[modnumber]==""
                hashtable[modnumber]=i
                stop=true
            end
                
            c+=1
        end
        
        if !stop
            push!(badhash,i)
        end
    end
    
    if !isempty(badhash)
        println(badhash)
    end
    
    return hashtable
end


# In[13]:


#the search is basically the same as linear probing
#except linear part is substituted with quadratic
function hash_search(target,arr,default=11)
    
    #get hashtable
    hashtable=create_hashtable(arr,default)
    
    #find value through hash value
    modnumber=target%default
    if target in hashtable[modnumber]
        return true
    else
        counter=1
        
        while counter<=default
            modnumber+=counter^2
            
            if modnumber>default-1
                modnumber=modnumber%default
            end
            
            if target==hashtable[modnumber]
                return true            
            end
            counter+=1
        end
    end
    return false
end


# In[14]:


hash_search(78,[21,55,89,67,12,12,12,12,12,12,12,12,12,12,78])


# In[15]:


#we get False in the end
#its quite interesting that for the same hash value 67,12,78
#we can store 67 in hash table but not 78
#67 and 12 are processed earlier than 78
#quadratic probing doesnt iterate through all slots
#all empty slots we can iterate have been occupied by the time we reach 78


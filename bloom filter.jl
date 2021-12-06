#!/usr/bin/env python
# coding: utf-8


# In[1]:


#fowler–noll–vo hash function
#pseudo code can be found in the link below
# https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function#FNV-1_hash    
function fnv1(text,
              offset_basis=0xcbf29ce484222325,
              prime=0x100000001b3)       
    
        hash_value=offset_basis
        for letter in text
            hash_value*=prime
        
            #for some unknown reasons,large int xor in julia is different from python
            hash_value=hash_value ⊻ codepoint(letter)
        
        end    
    
        return hash_value
    
end
    

# In[2]:


#jenkins one at a time hash function
#pseudo code can be found in the link below
# https://en.wikipedia.org/wiki/Jenkins_hash_function#one_at_a_time
#actual code can be found in the link below
# https://stackoverflow.com/a/51730837
function one_at_a_time(text)
    
    hash_value=0
    
    for letter in text
        hash_value+=codepoint(letter)
        hash_value=hash_value & 0xFFFFFFFF
        hash_value+=hash_value<<10
        hash_value=hash_value & 0xFFFFFFFF
        hash_value=hash_value ⊻ hash_value>>6
        hash_value=hash_value & 0xFFFFFFFF
    end
    
    hash_value+=hash_value<<3
    hash_value=hash_value & 0xFFFFFFFF
    hash_value=hash_value ⊻ hash_value>>11
    hash_value=hash_value & 0xFFFFFFFF
    hash_value+=hash_value<<15
    hash_value=hash_value & 0xFFFFFFFF
        
    return hash_value
    
end


# In[3]:


#compute hash value from two different functions
#update the underlying cells in hashtable
function update_hashtable(text,hashtable,verbose=true)
        
    #use extra computation to shrink hashtable size
    fnv_hash=Int64(round(fnv1(text)^0.0625))
    jenkins_hash=Int64(round(one_at_a_time(text)^0.25))
        
    #prevent overflow
    if max(fnv_hash,jenkins_hash)<=hashtable_size
            
        #update hashtable
        hashtable[fnv_hash]=1
        hashtable[jenkins_hash]=1
        if verbose
            println("Hashtable updated.")
        end
            
    else        
        if verbose
            println("Hash value exceeds hashtable size!")        
        end
    end
    
    return hashtable
    
end
 

# In[4]:


#compute hash value from two different functions
#check the underlying cells in hashtable
function search_hashtable(text,hashtable)
        
    #use extra computation to shrink hashtable size
    fnv_hash=Int64(round(fnv1(text)^0.0625))
    jenkins_hash=Int64(round(one_at_a_time(text)^0.25))
        
    #check hashtable
    if hashtable[fnv_hash]==1 && hashtable[jenkins_hash]==1
        return true
    else
        return false
    end
    
end


# In[5]:


#initialize
hashtable_size=500
hashtable=[0 for _ in 1:hashtable_size];
update_list=["raison d'être","porte-voix","prêt-à-gouverner",
             "proxénétisme","hydroxychloroquine"];


# In[6]:


#update hashtable
for text in update_list
    hashtable=update_hashtable(text,hashtable)
end


# In[7]:


#true negative
println(search_hashtable("raison d’être",hashtable))
println(search_hashtable("raison d être",hashtable))
println(search_hashtable("raison d\"être",hashtable))

#true positive
println(search_hashtable("raison d'être",hashtable))

#false positive
println(search_hashtable("rajson d'être",hashtable))



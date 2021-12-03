#!/usr/bin/env python
# coding: utf-8

# In[1]:


#bloom filter is a space-efficient probabilistic data structure
#it is commonly used for query in large dataset
#the query can possibly return false positive matches but never false negative matches
#the workflow is very straight forward
#for each string in the database, it has to go through k number of hash functions
#k hash value would be allocated to the hashtable accordingly
#to make any query,the query string has to go through k number of hash functions as well
#if every underlying cell has been occupied in the hashtable
#the query returns positive matches
class bloom_filter:
      
    
    #initialize
    def __init__(self,hashtable_size):        
        self.hashtable_size=hashtable_size
        self.hashtable=[0 for _ in range(self.hashtable_size)]
        

    #fowler–noll–vo hash function
    #pseudo code can be found in the link below
    # https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function#FNV-1_hash    
    def fnv1(self,text,offset_basis=0xcbf29ce484222325,
            prime=0x100000001b3):        
        hash_value=offset_basis
        for letter in text:
            hash_value*=prime
            hash_value^=ord(letter)
        return hash_value
    
    
    #jenkins one at a time hash function
    #pseudo code can be found in the link below
    # https://en.wikipedia.org/wiki/Jenkins_hash_function#one_at_a_time
    #actual code can be found in the link below
    # https://stackoverflow.com/a/51730837
    def one_at_a_time(self,text):    
        hash_value=0
        for i in range(len(text)):
            hash_value+=ord(text[i])
            hash_value&=0xFFFFFFFF
            hash_value+=hash_value<<10
            hash_value&=0xFFFFFFFF
            hash_value^=hash_value>>6
            hash_value&=0xFFFFFFFF
        hash_value+=hash_value<<3
        hash_value&=0xFFFFFFFF
        hash_value^=hash_value>>11
        hash_value&=0xFFFFFFFF
        hash_value+=hash_value<<15
        hash_value&=0xFFFFFFFF
        
        return hash_value
    
    
    #compute hash value from two different functions
    #update the underlying cells in hashtable
    def update_hashtable(self,text,verbose=True):
        
        #use extra computation to shrink hashtable size
        fnv_hash=int(self.fnv1(text)**0.00390625)
        jenkins_hash=int(self.one_at_a_time(text)**0.25)
        
        #prevent overflow
        if max(fnv_hash,jenkins_hash)<=hashtable_size:
            
            #update hashtable
            self.hashtable[fnv_hash]=1
            self.hashtable[jenkins_hash]=1
            if verbose:
                print('Hashtable updated.')
            
        else:            
            if verbose:
               print('Hash value exceeds hashtable size!')        
        return
    
    
    #compute hash value from two different functions
    #check the underlying cells in hashtable
    def search_hashtable(self,text):
        
        #use extra computation to shrink hashtable size
        fnv_hash=int(self.fnv1(text)**0.00390625)
        jenkins_hash=int(self.one_at_a_time(text)**0.25)
        
        #check hashtable
        if self.hashtable[fnv_hash]==1 and self.hashtable[jenkins_hash]==1:
            return True
        else:
            return False

    
# In[2]:
    

#initialize
update_list=["raison d'être","porte-voix","prêt-à-gouverner",
             "proxénétisme","hydroxychloroquine"]
hashtable_size=500


# In[3]:


#create query and update hashtable
query=bloom_filter(hashtable_size)
for text in update_list:
    query.update_hashtable(text,verbose=False)
    
#true negative
print(query.search_hashtable("raison d’être"))
print(query.search_hashtable("raison d être"))
print(query.search_hashtable("raison d\"être"))

#true positive
print(query.search_hashtable("raison d'être"))

#false positive
print(query.search_hashtable("raison d'etre"))
    

    
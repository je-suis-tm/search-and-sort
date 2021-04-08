
# coding: utf-8

# In[1]:


#rabin karp is a string search algorithm
#it is useful for string pattern matching
#particularly in plagiarism detection
#this algorithm leverages hash function instead of direct substring matching
#in theory. a wise choice of hash function
#can make its execution hypersonic compared to naïve search
#more details of hash function can be found in the link below
# https://github.com/je-suis-tm/search-and-sort/blob/master/hash%20search.py


# In[2]:


pattern='bene'
rawtext="""(Wo-oh-oh-oh-oh)
(Oh-oh-oh-oh-oh, ooh)
Yeah, ah

Wo-wo-oh, lei labbra da sommelier, mami
Ush, no, ha purple meches, sa di lean, wo-oh
Oh, ma prega, bless, le mie in CD, eh, eh
Bro, va tutto bene bene grazie a Dio
Wo-wo-oh, lei labbra da sommelier, mami
Ush, no, ha purple meches, sa di lean, wo-oh
Oh, ma prega, bless, le mie in CD, eh, eh
Bro, va tutto bene bene grazie a Dio

Ehi, faccio un tiro vedo color
Tu mani in mano, dico grazie a me
Sì, faccio tardi tardi e dico "No"
Non so più fare un regalo che
Poi non ci dormi la notte
Io resto a fare i din din din
Poi non mi fai "Buonanotte", oh-wo-oh, ehi
Che fai? Non lo so
Giriamo un po' qui
Gi-giriamo un po', ehi
Sto-sto nella vie
Ma non tu non lo sai, sono un bandito
Wow mi fai "Wow", sono wow
Sto distante qui come sto, no
Non lo so, no, non lo so, yeah

Wo-wo-oh, lei labbra da sommelier, mami
Ush, no, ha purple meches, sa di lean, wo-oh
Oh, ma prega, bless, le mie in CD, eh, eh
Bro, va tutto bene bene grazie a Dio
Wo-wo-oh, lei labbra da sommelier, mami
Ush, no, ha purple meches, sa di lean, wo-oh
Oh, ma prega, bless, le mie in CD, eh, eh
Bro, va tutto bene bene grazie a Dio

Wo-wo-oh, lei labbra da sommelier, mami
Ush, no, ha purple meches, sa di lean, wo-oh
Oh, ma prega, bless, le mie in CD, eh, eh
Bro, va tutto bene bene grazie a Dio
Wo-wo-oh, lei labbra da sommelier, mami
Ush, no, ha purple meches, sa di lean, wo-oh
Oh, ma prega, bless, le mie in CD, eh, eh
Bro, va tutto bene bene grazie a Dio"""


# In[3]:


#simple hash function according to wikipedia
# https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
def hash_function(word,prime_num=101):
    
    hash_value=sum([ord(val)*(prime_num**ind) for ind,val in enumerate(word)])
    
    return hash_value


# In[4]:


#naïve search iterates the letter one by one
def naive_search(pattern,rawtext):
    
    len_pattern=len(pattern)
    len_rawtext=len(rawtext)
    output=[]    
    
    #this part is stupid
    #as python allows us to do 
    #rawtext[i:i+len_pattern]==pattern
    for i in range(len_rawtext-len_pattern+1):
        ignore=False
        j=0
        while not ignore:
            if rawtext[i+j]!=pattern[j]:
                ignore=True
            j+=1
            if j==len_pattern:
                ignore=True
                output.append(i)
                
    return output


# In[5]:


#instead of checking rawtext[i:i+len_pattern]==pattern
#rabin karp algorithm leverages hash function
def rabin_karp(pattern,rawtext,prime_num=101):

    output=[]
    len_pattern=len(pattern)
    len_rawtext=len(rawtext)
    hash_pattern=hash_function(pattern,prime_num)
    hash_rawtext=hash_function(rawtext[:len_pattern],prime_num)
          
    #hash
    for i in range(len_rawtext-len_pattern+1):
        
        #rolling hash
        #however there is an issue with rolling hash in python
        #a large hash value will be reduced to the form of 1.5e+30
        #the emitted digits will cause 'false' in hash_rawtext==hash_pattern
        #it makes more sense to do hash_function(rawtext[i:i+len_pattern])
        if i>0:
            hash_rawtext-=hash_function(rawtext[i-1],prime_num)
            hash_rawtext/=prime_num
            hash_rawtext+=hash_function(rawtext[i+len_pattern-1],
                                        prime_num)*(prime_num**(len_pattern-1))
            
        if hash_rawtext==hash_pattern:
            output.append(i)
            
    return output


# In[6]:


print(rabin_karp(pattern,rawtext)==naive_search(pattern,rawtext))


# In[7]:


get_ipython().run_line_magic('timeit', 'rabin_karp(pattern,rawtext)')


# In[9]:


#ironically, naïve search seems to be a lot faster than rabin karp...
get_ipython().run_line_magic('timeit', 'naive_search(pattern,rawtext)')


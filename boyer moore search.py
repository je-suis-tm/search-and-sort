
# coding: utf-8

# In[1]:


#boyer moore is a string search algorithm
#the main objective is to skip as many loops as possible
#the skipping depends on two heuristics
#bad character and good suffix
#a more detailed tutorial can be found in jhu material
# https://www.cs.jhu.edu/~langmea/resources/lecture_notes/strings_matching_boyer_moore.pdf


# In[2]:


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
                if not ignore:
                    output.append(i)
                ignore=True
                
                
    return output


# In[3]:


#preprocess for bad character
#for each index
#look back and search for every distinct letter in front of the index
#find the nearest index (as opposed to the current index)
#where every distinct letter occurs
def get_hbc(pattern):
    heuristics_bc=[]
    for i in range(len(pattern)):
        bc={}
        for j in range(i-1,-1,-1):
            if pattern[j] not in bc and pattern[j]!=pattern[i]:
                bc[pattern[j]]=i-j
        heuristics_bc.append(bc)
        
    return heuristics_bc


# In[4]:


#the concept of good suffix is very similar to lps in kmp algo
#the only difference is bm algo starts from the right side of the pattern
#u can check kmp for reference
# https://github.com/je-suis-tm/search-and-sort/blob/master/knuth%20morris%20pratt%20search.py
def get_hgs(pattern):
    
    #initialize
    heuristics_gs=[0]*len(pattern)
    
    #iterate
    for i in range(len(pattern)-1):
        stop=False
        left=0
        right=1
        counter=0
        while not stop:
            
            #compute the longest proper prefix
            if pattern[left]==pattern[i+right]:
                left+=1
                right+=1
                counter+=1
            
            #if no match
            else:
                
                #no suffix exists
                #increment right side and keep trying
                if counter==0:
                    right+=1                    
                    
                #longest proper suffix has been matched
                else:
                    stop=True  
            
            if i+right==len(pattern):
                
                #longest proper suffix has been matched
                if counter!=0:
                    heuristics_gs[i]=i+right-1-(left-1)
                    stop=True
                    continue
                
                #avoid index error
                right=1
                left+=1
                
            #avoid index error
            if left>i:
                stop=True
            
            #update good suffix
            if stop:                
                if counter!=0:  
                    heuristics_gs[i]=i+right-1-(left-1)
    
    #the last one is always one
    heuristics_gs[-1]=1
    
    return heuristics_gs


# In[5]:


#bm algo with bad character and good suffix heuristics
def boyer_moore(pattern,rawtext):

    #get heuristics
    heuristics_bc=get_hbc(pattern)
    heuristics_gs=get_hgs(pattern)

    #initialize
    i=len(pattern)-1
    j=len(pattern)-1
    pos=[]
    
    #iterate
    while i<len(rawtext):
        
        #if no match,take the maximum skip from two different heuristics
        if pattern[j]!=rawtext[i]:
            if rawtext[i] in heuristics_bc[j]:
                hbc=heuristics_bc[j][rawtext[i]]
            else:
                hbc=len(pattern)
            hgs=heuristics_gs[j]
            i+=max(hbc,hgs)
            j=len(pattern)-1
            
        #keep matching
        else:
            i-=1
            j-=1

        #if matched,create output
        if j==-1:        
            i+=1
            pos.append(i)
            i+=len(pattern)
            j=len(pattern)-1
            
    return pos


# In[6]:


#solidarity with ua
rawtext="""Знаменитості продовжують підтримувати Україну у війні, яку веде Російська Федерація. Серед них - актори, ведучі, співаки, письменники та найбагатші люди планети.
Третій тиждень триває повномасштабне вторгнення російських загарбників на територію України. За цей час висловили підтримку та надали фінансову допомогу українцям, зокрема, канадський бізнесмен Ілон Маск, американська акторка українського походження Міла Куніс з чоловіком-колегою Ештоном Кутчером, американська артистка Мадонна, голлівудська кінозірка Леонардо ді Капріо та інші. А британський актор Бенедикт Камбербетч запропонував власне житло для біженців з України."""
pattern='Украї'


# In[7]:


print(boyer_moore(pattern,rawtext)==naive_search(pattern,rawtext))


# In[8]:


# 213 µs ± 1.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
get_ipython().run_line_magic('timeit', 'naive_search(pattern,rawtext)')


# In[9]:


# 169 µs ± 1.62 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
#bm is really faster than naïve!
get_ipython().run_line_magic('timeit', 'boyer_moore(pattern,rawtext)')


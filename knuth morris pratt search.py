
# coding: utf-8

# In[1]:


#knuth–morris–pratt is a string search algorithm
#kmp is a modified version on naïve search
#instead of iterate the letter one by one
#kmp leverages the information in each inner loop to improve worst case scenario
#for instance,lets find "con" in "côte d'azur"
#at the second letter "ô" which is a mismatch
#we already know theres no point of starting a new iteration at "ô"
#since the pattern starts with letter "c"
#an efficient way is to skip "ô" and start the new iteration at "te d'azur"
#thats the spirit of kmp
#it seeks pattern inside the pattern to avoid duplicate effort in the raw text


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
                ignore=True
                output.append(i)
                
    return output


# In[3]:


#lps refers to the longest proper prefix is also a proper suffix
#since we are trying to find pattern inside the pattern
#we are merely seeking the case 
#where the postfix of last matching equals to the prefix of the pattern
def get_lps(pattern):

    lps=[0]*len(pattern)
    
    #starts with the second letter to see if there is a pattern within the pattern
    i=1
    while i<len(pattern):
        stop=False
        j=0
        while not stop:
            
            #compute the longest proper prefix
            if pattern[i+j]==pattern[j]:
                lps[i+j]=lps[i+j-1]+1
            
            #if no match,start over
            else:
                lps[i+j]=0
                stop=True
            j+=1
            
            #avoid index error
            if i+j>=len(pattern):
                stop=True
        
        #once lps is found,move onto the next starting point
        i=i+j

    return lps


# In[4]:


#actually kmp is not very different from naïve search
def kmp(pattern,rawtext):
    
    #get lps
    lps=get_lps(pattern)
    pos=[]
    i=0
    
    #normal naïve search
    while i<=(len(rawtext)-len(pattern)):
        bingo=True
        
        for j in range(len(pattern)):
            if rawtext[i+j]!=pattern[j]:
                bingo=False
                break
        if bingo:
            pos.append(i)
            i+=len(pattern)
        
        #until a mismatch
        #we leverage lps to skip unnecessary inner loops
        else:
            i=i+lps[j]+1
            
    return pos


# In[5]:


#solidarity with ua
rawtext="""Знаменитості продовжують підтримувати Україну у війні, яку веде Російська Федерація. Серед них - актори, ведучі, співаки, письменники та найбагатші люди планети.
Третій тиждень триває повномасштабне вторгнення російських загарбників на територію України. За цей час висловили підтримку та надали фінансову допомогу українцям, зокрема, канадський бізнесмен Ілон Маск, американська акторка українського походження Міла Куніс з чоловіком-колегою Ештоном Кутчером, американська артистка Мадонна, голлівудська кінозірка Леонардо ді Капріо та інші. А британський актор Бенедикт Камбербетч запропонував власне житло для біженців з України."""
pattern='Украї'


# In[6]:


print(naive_search(pattern,rawtext)==kmp(pattern,rawtext))


# In[7]:


#213 µs ± 915 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)
get_ipython().run_line_magic('timeit', 'naive_search(pattern,rawtext)')


# In[8]:


#592 µs ± 1.34 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
#as usual,naïve search by me is always faster than improvements...
get_ipython().run_line_magic('timeit', 'kmp(pattern,rawtext)')


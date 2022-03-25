#!/usr/bin/env julia
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
#check the link below for more details
# https://www.inf.hs-flensburg.de/lang/algorithmen/pattern/kmpen.htm


# In[2]:


#naïve search iterates the letter one by one
function naive_search(pattern,rawtext)
    
    len_pattern=length(pattern)
    len_rawtext=length(rawtext)
    output=[]   

    #this part is stupid
    #as julia allows us to do 
    #rawtext[i:i+len_pattern-1]==pattern
    for i in 1:(len_rawtext-len_pattern+1)
        ignore=false
        j=1
        while !ignore
            if rawtext[i+j-1]!=pattern[j]
                ignore=true
            end
            j+=1
            if j>len_pattern
                if !ignore
                    push!(output,i)
                end
                ignore=true
                
            end
        end
    end                
    return output    
end


# In[3]:


#lps refers to the longest proper prefix is also a proper suffix
#since we are trying to find pattern inside the pattern
#we are merely seeking the case 
#where the postfix of last matching equals to the prefix of the pattern
function get_lps(pattern)

    lps=[0 for i in 1:length(pattern)]
    
    #starts with the second letter to see if there is a pattern within the pattern
    i=2
    while i<length(pattern)
        stop=false
        j=0
        while !stop

            #compute the longest proper prefix
            if pattern[i+j]==pattern[j+1]
                lps[i+j]=lps[i+j-1]+1
            
            #if no match,start over
            else
                lps[i+j]=0
                stop=true
            end
            j+=1
            
            
            #avoid index error
            if i+j>length(pattern)
                stop=true
            end
            
        end
        
        #once lps is found,move onto the next starting point
        i=i+j
        
    end

    return lps
    
end


# In[4]:


#actually kmp is not very different from naïve search
function knuth_morris_pratt(pattern,rawtext)
    
    len_pattern=length(pattern)
    len_rawtext=length(rawtext)    
    output=[]   
    i=1
    
    #get lps
    lps=get_lps(pattern)

    #normal naïve search
    while i<=(len_rawtext-len_pattern+1)
        stop=true
        j=1
        while j<=len_pattern
            if rawtext[i+j-1]!=pattern[j]
                stop=false
                break
            end
            j+=1
        end
        
        #until a mismatch
        #we leverage lps to skip unnecessary inner loops
        if stop
            push!(output,i)
            i+=len_pattern
        else
            i=i+lps[j]+1            
        end
        
    end                
    return output    
end


# In[5]:


#for some strange reasons
#cyrillic letters dont work the same way in julia as in python
#have to convert to latin letters
cyrillic2latin=Dict([("а", "a"),
 ("б", "b"),
 ("в", "v"),
 ("г", "h"),
 ("ґ", "g"),
 ("д", "d"),
 ("е", "e"),
 ("є", "ye"),
 ("ж", "zh"),
 ("з", "z"),
 ("и", "y"),
 ("і", "i"),
 ("ї", "yi"),
 ("й", "y"),
 ("к", "k"),
 ("л", "l"),
 ("м", "m"),
 ("н", "n"),
 ("о", "o"),
 ("п", "p"),
 ("р", "r"),
 ("с", "s"),
 ("т", "t"),
 ("у", "u"),
 ("ф", "f"),
 ("х", "kh"),
 ("ц", "ts"),
 ("ч", "ch"),
 ("ш", "sh"),
 ("щ", "shch"),
 ("ь", "()"), 
 ("ю", "yu"),
 ("я", "ya"),
 ("А", "A"),
 ("Б", "B"),
 ("В", "V"),
 ("Г", "H"),
 ("Ґ", "G"),
 ("Д", "D"),
 ("Е", "E"),
 ("Є", "YE"),
 ("Ж", "ZH"),
 ("З", "Z"),
 ("И", "Y"),
 ("І", "I"),
 ("Ї", "YI"),
 ("Й", "Y"),
 ("К", "K"),
 ("Л", "L"),
 ("М", "M"),
 ("Н", "N"),
 ("О", "O"),
 ("П", "P"),
 ("Р", "R"),
 ("С", "S"),
 ("Т", "T"),
 ("У", "U"),
 ("Ф", "F"),
 ("Х", "KH"),
 ("Ц", "TS"),
 ("Ч", "CH"),
 ("Ш", "SH"),
 ("Щ", "SHCH"),     
 ("Ь", "()"),
 ("Ю", "YU"),
 ("Я", "YA")])
rawtext="Знаменитості продовжують підтримувати Україну у війні, яку веде Російська Федерація. Серед них - актори, ведучі, співаки, письменники та найбагатші люди планети.\nТретій тиждень триває повномасштабне вторгнення російських загарбників на територію України. За цей час висловили підтримку та надали фінансову допомогу українцям, зокрема, канадський бізнесмен Ілон Маск, американська акторка українського походження Міла Куніс з чоловіком-колегою Ештоном Кутчером, американська артистка Мадонна, голлівудська кінозірка Леонардо ді Капріо та інші. А британський актор Бенедикт Камбербетч запропонував власне житло для біженців з України."
pattern="Украї";


# In[6]:


#alphabet conversion
cleantext=[]
for i in rawtext
    if string(i) in keys(cyrillic2latin)
        push!(cleantext,cyrillic2latin[string(i)])
    else
        push!(cleantext,i)
    end
end

#list2string
clean_pattern=join([cyrillic2latin[string(i)] for i in pattern])
clean_text=join(cleantext);


# In[7]:


println(naive_search(clean_pattern,clean_text)==knuth_morris_pratt(clean_pattern,clean_text))


# In[8]:


#0.000011 seconds (3 allocations: 144 bytes)
@time naive_search(clean_pattern,clean_text);


# In[9]:


#0.000018 seconds (4 allocations: 272 bytes)
#as usual,naïve search by me is always faster than improvements...
@time knuth_morris_pratt(clean_pattern,clean_text);


# In[ ]:





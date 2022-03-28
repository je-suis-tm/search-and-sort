#!/usr/bin/env julia
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


#preprocess for bad character
#for each index
#look back and search for every distinct letter in front of the index
#find the nearest index (as opposed to the current index)
#where every distinct letter occurs
function get_hbc(pattern)
    heuristics_bc=[]
    for i in 1:length(pattern)
        bc=Dict()
        for j in i:-1:1
            if !(pattern[j] in keys(bc)) && pattern[j]!=pattern[i]
                bc[pattern[j]]=i-j
            end
        end
        push!(heuristics_bc,bc)
    end
    return heuristics_bc
end


# In[4]:


#the concept of good suffix is very similar to lps in kmp algo
#the only difference is bm algo starts from the right side of the pattern
#u can check kmp for reference
# https//github.com/je-suis-tm/search-and-sort/blob/master/knuth%20morris%20pratt%20search.jl
function get_hgs(pattern)
    
    #initialize
    heuristics_gs=zeros(Int8,length(pattern))
    
    #iterate
    for i in length(pattern)-1:-1:1
        stop=false
        left=i
        right=i+1
        while !stop
            
            #compute the longest proper prefix
            if pattern[left:left+length(pattern[right:end])-1]==pattern[right:end]
                stop=true
                break
            
            #if no match
            #increment right side and keep trying
            else
                right+=1
            end
            
            #if right side has reached its limit
            #try left side
            if right>length(pattern)
                left-=1
                right=i+1                
            end
                
            #avoid index error
            if left==0
                stop=true
                break
            end           
        end
        
        #remember to revert the pointer back to the end of the pattern
        heuristics_gs[i]=right-left+length(pattern)-i
    end
    
    #the last one is always one
    heuristics_gs[end]=1
    
    return heuristics_gs
end


# In[5]:


#bm algo with bad character and good suffix heuristics
function boyer_moore(pattern,rawtext)

    #get heuristics
    heuristics_bc=get_hbc(pattern)
    heuristics_gs=get_hgs(pattern)

    #initialize
    i=length(pattern)
    j=length(pattern)
    pos=[]
    
    #iterate
    while i<=length(rawtext)

        #if no match,take the maximum skip from two different heuristics
        if pattern[j]!=rawtext[i]
            if rawtext[i] in keys(heuristics_bc[j])
                hbc=heuristics_bc[j][rawtext[i]]
                hbc+=(length(pattern)-j)
            else
                hbc=length(pattern)
            end
            hgs=heuristics_gs[j] 
            
            #move the pointer to the end of the pattern before skipping
            i+=max(hbc,hgs)            
            j=length(pattern)
            
        #keep matching
        else
            i-=1
            j-=1
        end
        
        #if matched,create output
        if j==0        
            i+=1
            push!(pos,i)
            i+=length(pattern)
            j=length(pattern)
        end
    end
    
    return pos
end


# In[6]:


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


# In[7]:


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


# In[8]:


println(naive_search(clean_pattern,clean_text)==boyer_moore(clean_pattern,clean_text))


# In[9]:


#0.000008 seconds (3 allocations: 144 bytes)
@time naive_search(clean_pattern,clean_text);


# In[10]:


#0.000170 seconds (483 allocations: 12.703 KiB)
#as usual,naïve search by me is always faster than improvements...
#in python bm is actually faster
@time boyer_moore(clean_pattern,clean_text);


# In[ ]:





# In[ ]:





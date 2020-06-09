
# coding: utf-8

# In[1]:


#counting sort is kinda different from other sorts in this repo
#it works the best when there is large quantity of duplicates
#when the maximum value is larger than the length of list
#it is not economical to use counting sort
#counting sort is counting how many times each element has repeatedly showed up
#we create a list of the size of maximum value
#each index of the list represents the value of elements
#each value of the list represents the frequency of elements
#in the end we concatenate each element and its frequency
#simplest sort among all


# In[2]:


function counting_sort(arr)
    
    maxval=maximum(arr)
    
    #first we get the maximum value
    #if maximum value is larger than the length of the list
    #we would create a list with a huge space complexity
    #its not worth it
    #we can use a better sort
    if maxval>length(arr)
        printstyled("choose other sorting techniques",color=:red)
        return
    end
    
    #we create a list to store the frequency of each element
    #note that we use maximum value +1
    #as zero is also taken into consideration
    freq=zeros(maxval+1)
    
    #this is the calculation of the frequency
    #use i+1 becuz julia index starts from 1
    for i in arr
        freq[i+1]+=1
    end
    
    #lets clear the original list
    #we add each element and its frequency back to the list
    output=[]
    
    for i in 1:length(freq)
        
        #using i-1 prior to i+1 in the lines above
        #use Int32 to ensure freq[i] is int32
        temp=fill(i-1,Int32(freq[i]))
        append!(output,temp)
        
    end
    
    return output        

end


# In[3]:


#the time complexity for counting sort is o(n+k)
#k is determined by the maximum value
#its easy to see that counting sort easily beats o(n^2)
#however its space complexity is really large


# In[4]:


for _ in 1:100
    
    #usually we form a non-duplicate list
    #for counting sort, we need massive amount of duplicates
    test_arr=rand(0:100,1000)

    if !(counting_sort(test_arr)==sort(test_arr))
        printstyled("Erreur",color=:red)
    end

end


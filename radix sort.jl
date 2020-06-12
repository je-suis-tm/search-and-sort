
# coding: utf-8

# In[1]:


#radix sort is fun
#there are two ways to do it
#the first approach is we start from the right
#the second one is to start from the left
#in this context, i choose the first approach
#they are equivalent
#we get the first digit of all elements
#sort these elements based upon the first digit
#for instance, 215 and 19
#9 for 19 is larger than 5 for 215
#for the first round, we get 215,19
#we move on to the second digit of all elements from the right
#we apply the same technique of sorting based upon the second digit
#until we reach to the very left digit of the maximum value in the list
#the sort is completed
#for instance, the second round would be 215,19
#since the second digit of both numbers are 1
#the final round is 19,215
#as 0 for 19 is smaller than 2 for 215
#period

#to implement this method in python
#we can apply fld(x,10)%10 technique
#for the first round, fld(x,1)%10 gets the first digit from the left
#for the second round, fld(x,10)%10 gets the second digit from the left
#and so on
#we can use a nested list to store elements in its rightful place
#i use digits its index indicates its digit+1
#becuz julia starts from 1
#there are other elegant solutions, plz check the link at the very end


# In[2]:


function radix_sort(arr)

    maxval=maximum(arr)
    digits=0
    
    #the first part is to find the largest element in the list
    #next, we find out how many digits it contains
    #so we can determine how many times we need to divide in the later stage
    while maxval>=1
        maxval=maxval/10
        digits+=1
    end
    
    
    for digit in 1:digits
        
        #each time, we clear the nested list
        digit_sort=[[] for _ in 1:10]
        radix=10^(digit-1)
        
        #this is a traversal on all elements in the list
        for i in arr
            
            #fld(i,radix)%10 is the technique to get digits
            #when we get it, we use i+1 as index
            #so that we can store the element in its rightful place            
            ind=fld(i,radix)%10
            
            push!(digit_sort[ind+1],i)
            
        end
        
        #we have to empty the list after we put all elements into a nested list        
        arr=[]
        
        #this loop is unnecessary
        #we can use append(digit_sort[1],...digit_sort[10])
        #again, i am a lazy person
        #cut me some slack, s’il vous plaît        
        for j in 1:10            
            append!(arr,digit_sort[j])
        end
        
    end
    
    return arr

end


# In[3]:


#surprisingly, the radix sort is really fast
#the time complexity of radix sort is o(k*n)
#k depends on the digits of the maximum value in the list
#well, its harder to get a number like 10^1000 than getting a list with 10^1000 elements
#when we get a list with smaller n and larger k
#radix sort may be a terrible choice

#there are other ways of writing radix sort
#i believe my way has too much space complexity
#this one is rather smart and elegant
# https://www.geeksforgeeks.org/radix-sort/


# In[4]:


for _ in 1:100
    
    test_arr=rand(1:1000,100)

    if !(radix_sort(test_arr)==sort(test_arr))
        printstyled("Erreur",color=:red)
    end

end


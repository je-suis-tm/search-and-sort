
# coding: utf-8

# In[1]:


#heap sort is the alternative version of selection sort
#heap sort is implemented on a binary heap instead of a list
#well, u can argue binary heap is expressed in list
#binary heap is a complete binary tree
#for each node it has no more than two children
#the tree is as far left as possible
#for this binary heap, we keep minimum at root
#similar to selection sort
#we only need to get the smallest number for each round
#and our list keeps shrinking until we are left with one element for final round
#however, the traversal is kinda different from selection sort
#what we do is to compare two children with parent node
#we keep the smallest among the family of three as parent node for each node
#until we reach the root and we successfully keep the smallest at root
#next step is to remove the root and we find the minimum for the new tree
#we would do it recursively in this script
#otherwise we would have to use loops in loops

#in this version we use min heap
#if u intend to use max heap,check out geeks for geeks
# https://www.geeksforgeeks.org/heap-sort/


# In[2]:


function heap_sort(arr)
    
    #denote layer as the height of the tree
    layer=0
    maxlen=length(arr)
        
    #when we are left with one element
    #that is the base case for recursion
    if maxlen<2
    
        return arr
    
    end
    
    #this part is to find out how many layers we got for binary heap
    #note that layer starts from 1 in julia
    while maxlen>2^layer
        
        maxlen-=2^layer
        layer+=1
        
    end
    
    
    #as layer starts from 1
    #we have to use layer+1 to make sure each layer has been traveled
    #until we reach the base case, layer 1, the root
    for i in layer+1:-1:1
        
        #a special property of binary heap
        #the beginning of each layer equals to 2^(i-1)
        #each layer contains 2^(i-1) elements
        for j in 2^(i-1):2^i-1
            
            #a special property of binary heap as well
            #the index of left child is always even number
            #and for the right child, always odd number
            right=j*2+1
            left=j*2

            #we use try function in case the node is the leaf
            #and if there is no left child
            #there wont be right child
            #according to the far left principle of binary heap
            #we compare the parent with two children nodes
            #we only keep the smallest as parent node
            try
            
                if arr[left]<arr[j]
                
                    arr[left],arr[j]=arr[j],arr[left]
                    
                end

                try
                
                    if arr[right]<arr[j]
                    
                        arr[right],arr[j]=arr[j],arr[right]
                        
                    end

                    if arr[right]<arr[left]
                        
                        arr[right],arr[left]=arr[left],arr[right]
                        
                    end

                catch e
               
                    if !(isa(e,BoundsError))
                        
                        throw(e)
                    
                    end

                end

            catch e
               
                if !(isa(e,BoundsError))
                    
                    throw(e)
                    
                end
                
            end
            
        end
        
    end
    
    #recursively, we shrink the size of the list
    #by removing its root which is the smallest element for the current tree
    arr[2:end]=heap_sort(arr[2:end])      
    
    return arr
    
end


# In[3]:


#heap sort s time complexity is o(nlogn)
#however, this script is written in recursive function
#it may not achieve the same speed as iterations


# In[4]:


for _ in 1:100
    
    test_arr=rand(100)

    if !(heap_sort(test_arr)==sort(test_arr))
        printstyled("Erreur",color=:red)
    end

end



# coding: utf-8

# In[1]:

#details of insertion sort can be found in the following link
# https://github.com/je-suis-tm/search-and-sort/blob/master/bubble%2C%20selection%20and%20insertion%20sort.py
def insertion_sort(target):
   
    for i in range(1,len(target)):
        
        val=target[i]
        
        j=i
        
        while val<target[j-1] and j!=0:

                target[j]=target[j-1]
                j-=1

        target[j]=val
        
    return target


#shell sort is a variation of insertion sort
#slicing method [a::b] is the key
#we gotta cut the original list into a few small groups

#assume we have a list of n elements
#the first step, we do b=n//a, we get a few sublists by [a::b]
#we apply insertion sort on those sublists and concatenate
#next, we do b=b//a, and we obtain a few new sublists by [a::b]
#we apply insertion sort on new sublists and concatenate
#we keep using //a method and do insertion sort and concatenate
#til b reaches zero
#we concatenate sublists and do a final insertion sort
#we shall end up with a sorted list
#the time complexity is quite difficult to calculate

def shell_sort(target):
   
    #the first step is to initialize a
    #we will use this variable to divide the list and do slicing
    #in this case, i use 4, you can change the default number to any digit
    #bear in mind that this variable keeps the size of each sublist reasonable
    #we keep b divided by 4 until it reaches zero
    a=4
    b=len(target)//a
      
    while b>0:
         
        #instead of rebuilding the wheel
        #i directly call it in shell sort     
        for i in range(b):
            temp=insertion_sort(target[i::b])
            
            #the final loop is actually the slicing of [a::b]
            #[a::b] equals to [a+j*b] j for j in range(len(temp))
            for j in range(len(temp)):
                target[i+j*b]=temp[j]
        
         b=b//a
         
    return insertion_sort(target)


for i in range(100):
    
    target=rd.sample([i for i in range(1000)],100)

    if shell_sort(target)!=sorted(target):
        print('Erreur')

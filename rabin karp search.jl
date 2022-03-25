#!/usr/bin/env julia
# coding: utf-8

#rabin karp is a string search algorithm
#it is useful for string pattern matching
#particularly in plagiarism detection
#this algorithm leverages hash function instead of direct substring matching
#more details can be found in the link below
# http://www-igm.univ-mlv.fr/~lecroq/string/node5.html#SECTION0050
#in theory. a wise choice of hash function
#can make its execution hypersonic compared to naïve search
#more details of hash function can be found in the link below
# https://github.com/je-suis-tm/search-and-sort/blob/master/hash%20search.jl

pattern="Canary Wharf"

rawtext="""The main landlord in London's Canary Wharf financial district is considering scrapping plans for a new office skyscraper and building a 60-story apartment tower instead.

Canary Wharf Group is consulting with local authorities about the potential for building around 700 homes at its 1 Park Place site that would be purpose-built for tenants, according to an application on the Tower Hamlets council website. The firm had won initial permission in 2015 for a one million square foot office building, the equivalent of two Gherkin skyscrapers.

The reason for the potential switch to apartments wasn't disclosed in the document. A spokesperson for Canary Wharf declined to comment.

The pandemic has hammered London's commercial landlords, who have grappled with plunging rent collections and the ongoing uncertainty about whether white collar workers will return to the office en masse. Canary Wharf is facing a fall by as much as 15% in advertised office rents through 2021, the steepest throughout London, according to a forecast by broker Carter Jonas.

Read more: Canary Wharf Plans Bond as Offices Grapple With Empty Space

Focusing on rental homes, however, looks an increasingly safe bet as a housing shortage across the capital fuels demand for accommodation. DWS, the investment arm of Deutsche Bank AG, last month made its first acquisition in the U.K. build-to-rent sector with a development in South London, citing a lack of supply of good quality and affordable rental housing in the area.

Even before the pandemic, financial firms were reconsidering their real estate needs. HSBC Holdings Plc, which has its headquarters in Canary Wharf, said it expected to slash its global property footprint by 40%. So far, initial steps to ease lockdown restrictions haven't led to a rush back to the office: occupancy levels across the U.K. are around 30% this week, according to building software company Metrikus.

Still, a flurry of building approvals and recent leasings in the City of London, Canary's long-time rival district, suggest that there is still high demand for new offices in the capital. British Land Co. on Thursday said it had leased almost 30% of its planned 1 Broadgate redevelopment to Jones Lang LaSalle Inc. -- four years before the project's planned completion.

The Docklands area around Canary Wharf has staged a residential building boom in the past five years, with the construction of luxury apartment towers targeting young finance workers. Around 9% of new homes under construction across London at the end of last year were in the area's E14 postcode, according to data company Molior.

The news about Park Place was earlier reported by Estates Gazette."""

#simple hash function according to wikipedia
# https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
#my preference is to choose a small prime number
#a smaller prime number will not exceed float64 limit in julia
function hash_function(word,prime_num=3)
    
    hash_value=sum([Float64(word[i])*(prime_num^i) for i in 1:length(word)])
    
    return hash_value
    
end

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


#instead of checking rawtext[i:i+len_pattern-1]==pattern
#rabin karp algorithm leverages hash function
function rabin_karp(pattern,rawtext,prime_num=3)

    output=[]
    len_pattern=length(pattern)
    len_rawtext=length(rawtext)
    hash_pattern=hash_function(pattern,prime_num)
    hash_rawtext=hash_function(rawtext[1:len_pattern],
    prime_num)
          
    #hash
    for i in 1:(len_rawtext-len_pattern+1)
        
        #rolling hash
        if i>1
            hash_rawtext-=hash_function(rawtext[i-1:i-1],prime_num)
            hash_rawtext/=prime_num
            hash_rawtext+=hash_function(rawtext[i+len_pattern-1:i+len_pattern-1],
                                        prime_num)*(prime_num^(len_pattern-1))
        end

        if hash_rawtext==hash_pattern
            push!(output,i)
        end
    end
            
    return output
    
end

print(rabin_karp(pattern,rawtext)==naive_search(pattern,rawtext))

@time rabin_karp(pattern,rawtext)

#ironically, naïve search seems to be a lot faster than rabin karp...
@time naive_search(pattern,rawtext)



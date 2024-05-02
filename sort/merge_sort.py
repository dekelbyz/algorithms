'''
MERGE SORT:
TIME COMPLEXITY: o(n log n)
SPACE COMPLEXITY: o(n)

EXPLANATION:  
TIME: it takes o(log n) time complexity to 
break the list apart, although putting it back together 
takes o(n) since we have to iterate through each item of that list
which makes it a total of o(n log n) 

SPACE: unlike other sorting algorithms (bubble, selection, insertion etc), 
we do not operate on the original list, but rather creating a new list 
for each item featured in the original list, which brings it up to a 
total space complexity of o(n)

ADDITION: compared to other sorting algorithms such as the ones mentioned above,
this is by far the most efficient one introduced to us so far (in terms of time complexity)
the other ones operate with time complexity of o(n ^ 2). 

goes without saying, it is the worst one to use in terms of space complexity.
as mentioned above, with the other sorting algorithms we operate on the original list,
without having to manifest a list for every element of that list -
which makes it o(1) in space complexity.

but honestly? FUCK SPACE. time is passing by - even right now while I write this unecessary
description on 7AM that probably no one will ever read (that's a shame tbh) 
instead of sleeping. I can never get this time back. The space will be once
again available for me right after the execution

FUCK SPACE!!!
'''

def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1
              
    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    
    mid_index = len(my_list) // 2

    left = merge_sort(my_list[mid_index:])
    right = merge_sort(my_list[:mid_index])

    return merge(left, right)





original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)



"""
    EXPECTED OUTPUT:
    ----------------
    Original List: [3, 1, 4, 2]
    
    Sorted List: [1, 2, 3, 4]
    
 """
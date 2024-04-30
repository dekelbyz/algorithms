def first_non_repeating_char(str):
    frequeny_counter = {}
    lowest = {}
    final_char = None
    for i in range(len(str)):
        frequeny_counter[str[i]] = {
            'count': frequeny_counter.get(str[i], {}).get('count', 0) + 1,
            'index': frequeny_counter.get(str[i], {}).get('index', i)
        }

    for char in frequeny_counter:
        item = frequeny_counter[char]

        if item['count'] == 1:
            if item.get('index') < lowest.get('index', len(str) + 1):
                lowest = item
                final_char = char
    
    return final_char






# WRITE THE FUNCTION HERE #
#                         #
#                         #
#                         #
#                         #
###########################



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
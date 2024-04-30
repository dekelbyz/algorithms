def is_palindrome(int):
    if int < 0:
        return False
    string = str(int)
    for i, c in enumerate(string):
        if c != string[len(string) -1 -i]:
            return False
    return True

def second_is_palindrome(x):
    if x < 0:
        return False
    
    reversed_string = str(x)[::-1]
    return int(reversed_string) == x
        
print(second_is_palindrome(123454321))
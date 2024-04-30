def gcdOfStrings(str1, str2):
        len1, len2 = len(str1), len(str2)
        
        def is_divisor(l):
              if len1 % 1 or len2 % 1:
                    return False
              f1, f2 = len1 // l, len2 // l
              return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if is_divisor(l):
                  return str1[:l]
        return ""


print(gcdOfStrings('ABABAB', 'ABAB'))


# ========== #

def gcdOfStrings(string1, string2):
    # Calculate the length of both input strings
    lengthOfString1, lengthOfString2 = len(string1), len(string2)
    
    # Helper function to determine if a substring of length 'potentialDivisorLength'
    # can divide both strings completely to form the original strings
    def is_valid_divisor(potentialDivisorLength):
        # Check if 'potentialDivisorLength' is a divisor of both string lengths
        if lengthOfString1 % potentialDivisorLength != 0 or lengthOfString2 % potentialDivisorLength != 0:
            return False
        
        # Determine the number of times the divisor substring should repeat
        repeatCount1 = lengthOfString1 // potentialDivisorLength
        repeatCount2 = lengthOfString2 // potentialDivisorLength
        
        # Create the strings by repeating the substring and compare with the original strings
        divisorSubstring = string1[:potentialDivisorLength]
        if divisorSubstring * repeatCount1 == string1 and divisorSubstring * repeatCount2 == string2:
            return True
        return False

    # Start from the minimum of the two string lengths and check each possible divisor length
    for currentLength in range(min(lengthOfString1, lengthOfString2), 0, -1):
        if is_valid_divisor(currentLength):
            # Return the largest valid divisor substring
            return string1[:currentLength]
    
    # If no valid divisor is found, return an empty string
    return ""

# Example usage
print(gcdOfStrings('ABABAB', 'ABAB'))

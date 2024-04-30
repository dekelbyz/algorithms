class Solution(object):
    def reverseVowels(self, s: str):
        s = list(s)
        vowels = set('aeiouAEIOU')
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in vowels:
                i += 1
            
            elif s[j] not in vowels:
                j -= 1
        
            else:
                s[j], s[i] = s[i], s[j]
                i += 1
                j -= 1
                
        return "".join(s)


s = Solution()

b = s.reverseVowels('leetcode') # holle

print(b)
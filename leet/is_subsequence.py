class Solution(object):
    def is_subsequence(self, s, t):
        if len(s) > len(t): return False
        if len(s) == 0: return True

        l = list(s)
        for b in t:
            if b in l:
               l.remove(b)
        return len(l) == 0

s = Solution()
a = s.is_subsequence(s='axc', t='ahbgdc')
print(a)
# Input: s = "abc", t = "ahbgdc"
# Output: true
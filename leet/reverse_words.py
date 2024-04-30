class Solution(object):
    def reverseWords(self, s: str):
        s = s.split()
        left, right = 0, len(s) - 1

        while left < right:
            # Swap the words
            s[left], s[right] = s[right], s[left]
            # Move pointers
            left += 1
            right -= 1

        # Convert the list back to a string
        return ' '.join(s).strip()

s = Solution()

a = s.reverseWords('0 1 2 3 4 5 6 7 8 9 10')

print(a)
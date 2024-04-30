class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res = [False] * len(candies)
        max_candies = max(candies)
        for i, c in enumerate(candies):
            if c + extraCandies >= max_candies:
                res[i] = True
        return res

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        return [(curNum + extraCandies >= max_candies) for curNum in candies]

s = Solution()
print(s.kidsWithCandies([2,3,5,1,3,0], 3))
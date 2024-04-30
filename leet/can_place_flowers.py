class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        places = 0
        for i, f in enumerate(flowerbed):
            prev = flowerbed[i - 1] if i - 1 >= 0 else 0
            next = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0
            if f == 0 and next == 0 and prev == 0:
                places += 1
        return places >= n

s = Solution()

print(s.canPlaceFlowers([1,0,0,0,1], 1)) # true
print(s.canPlaceFlowers([1,0,0,0,1], 2)) # false
print(s.canPlaceFlowers([0,0,0], 2)) # trtue


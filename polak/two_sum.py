from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    map = {}
    solutions = []
    for index, num in enumerate(nums):
        leftover = target - num
        if leftover in map:
            solutions.append([map[leftover], index])
        map[num] = index
    return solutions

print(two_sum([0,1,2,3,4,5], 6))
    

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    _set = set()
    for num in nums:
        if num in _set:
            return True
        _set.add(num)
    return False
print(contains_duplicate([1,2,3]))
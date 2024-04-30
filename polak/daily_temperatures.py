from typing import List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    stack = []
    result = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)

    return result


print(daily_temperatures([73,74,75,71,69,72,76,73]))
    
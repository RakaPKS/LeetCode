from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for indexFirst, first in enumerate(nums):
        for indexSecond, second in enumerate(nums[indexFirst+1:]):
            if first + second == target:
                return [indexFirst, indexSecond+indexFirst+1]

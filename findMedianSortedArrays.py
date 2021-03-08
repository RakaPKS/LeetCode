from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums3 = nums1 + nums2
    nums3.sort()
    middle = nums3[len(nums3) // 2]
    if len(nums3) % 2 == 1:
        return middle
    else:
        return (middle + nums3[len(nums3) // 2 - 1]) / 2

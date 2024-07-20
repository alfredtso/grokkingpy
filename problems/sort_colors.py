from typing import List
from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        >>> s = Solution()
        >>> nums = [2,0,2,1,1,0]
        >>> s.sortColors(nums)
        >>> nums
        [0, 0, 1, 1, 2, 2]
        >>> s = Solution()
        >>> nums = [2,0,1]
        >>> s.sortColors(nums)
        >>> nums
        [0, 1, 2]
        >>> s = Solution()
        >>> nums = [1,2,0]
        >>> s.sortColors(nums)
        >>> nums
        [0, 1, 2]
        """
        ptr_z, ptr_curr, ptr_t = 0, 0, len(nums) - 1
        while ptr_curr <= ptr_t:
            if nums[ptr_curr] == 0: 
                tmp = nums[ptr_z]
                nums[ptr_z] = nums[ptr_curr]
                nums[ptr_curr] = tmp
                ptr_z += 1
            elif nums[ptr_curr] == 2:
                tmp = nums[ptr_t]
                nums[ptr_t] = nums[ptr_curr]
                nums[ptr_curr] = tmp
                ptr_t -= 1
            else:
                ptr_curr += 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()

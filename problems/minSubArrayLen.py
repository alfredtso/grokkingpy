from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        >>> sol = Solution()
        >>> target = 7
        >>> nums = [2,3,1,2,4,3]
        >>> sol.minSubArrayLen(target, nums)
        2
        >>> target = 4
        >>> nums = [1,4,4]
        >>> sol.minSubArrayLen(target, nums)
        1
        >>> target = 11
        >>> nums = [1,1,1,1,1,1,1,1]
        >>> sol.minSubArrayLen(target, nums)
        0
        """
        start, end = 0, 0
        min_len = len(nums) + 1
        tmp = target
        
        while end < len(nums):
            tmp = tmp - nums[end]
            end += 1

            # set this when 
            while tmp <= 0:
                tmp = tmp + nums[start]
                start += 1
                min_len = min(min_len, end - start + 1)

        if min_len == len(nums) + 1:
            return 0;
        else:
            return min_len

if __name__ == "__main__":
    import doctest
    doctest.testmod()


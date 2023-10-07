from bisect import bisect_left
from typing import List
from array import array

class Solution:
    def bisect_lis(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> nums = [10,9,2,5,3,7,101,18]
        >>> s.bisect_lis(nums)
        4
        """
        sub = array('i', [])
        for num in nums:
            # for tie it would return the left pos
            i = bisect_left(sub, num)

            # case 1: greater than all
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num

        return len(sub)

    def dp_lis(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> nums = [10,9,2,5,3,7,101,18]
        >>> s.dp_lis(nums)
        4
        """
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. 
        Each house has a certain amount of money stashed, the only constraint
        stopping you from robbing each of them is that adjacent houses have
        security systems connected and it will automatically contact the police
        if two adjacent houses were broken into on the same night.
        Given an integer array nums representing the amount of money of each house,
        return the maximum amount of money you can rob tonight without alerting the police.
        >>> s = Solution()
        >>> nums = [1,2,3,1]
        >>> s.rob(nums)
        4
        >>> nums = [2,7,9,3,1]
        >>> s.rob(nums)
        12
        """
        # DP States
        @lru_cache(None)
        def dp(house):
            # Base cases
            if house < 0:
                return 0

            return max(dp(house-2) + nums[house], dp(house-1))
        
        return dp(len(nums)-1)

    def rob_circle(self, nums: List[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. 
        Each house has a certain amount of money stashed, the only constraint
        stopping you from robbing each of them is that adjacent houses have
        security systems connected and it will automatically contact the police
        if two adjacent houses were broken into on the same night.
        All the houses are arrange in circle.
        Given an integer array nums representing the amount of money of each house,
        return the maximum amount of money you can rob tonight without alerting the police.
        >>> s = Solution()
        >>> nums = [2,3,2]
        >>> s.rob_circle(nums)
        3
        >>> nums = [1,2,3,1]
        >>> s.rob_circle(nums)
        4
        """

        return max(Solution.rob(self,nums[:-1]), Solution.rob(self,nums[1:]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()


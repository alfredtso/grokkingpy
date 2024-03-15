from typing import List
from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        >>> s = Solution()
        >>> nums = [1,2,3]
        >>> target = 4
        >>> s.combinationSum4(nums,target)
        7
        >>> nums = [1,2,3]
        >>> target = 4
        >>> s.combinationSum4(nums,target)
        7
        >>> nums = [9]
        >>> target = 3
        >>> s.combinationSum4(nums,target)
        0
        """
        nums.sort()
        # DP States
        @lru_cache(None)
        def dp(tgt):
            # Base cases
            if tgt < 0:
                return 0
             
            if tgt == 0:
                return 1

            sum = 0
            for num in nums:

                if num > target:
                    break
                # Recurrence
                sum += dp(tgt - num)

            return sum
        
        return dp(target)
                

if __name__ == "__main__":
    import doctest
    doctest.testmod()

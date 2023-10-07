from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        >>> s = Solution()
        >>> nums = [2,7,11,15]
        >>> target = 9
        >>> s.twoSum(nums,target)
        [0, 1]
        >>> nums = [3,2,4]
        >>> target = 6
        >>> s.twoSum(nums,target)
        [1, 2]
        >>> nums = [3,3]
        >>> target = 6
        >>> s.twoSum(nums,target)
        [0, 1]
        """
        d = dict()
        res = []
        for i, k in enumerate(nums):
            # check if the value target - k is in the dict, put if not
            v = target - k
            if v in d.keys():
                return [d[v],i]
            else:
                d[k] = i

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    s.twoSum(nums,target)

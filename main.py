from itertools import combinations
import time

def isPalindrome(s: str):
   """
   >>> s = "AD"
   >>> isPalindrome(s)
   False
   >>> s = "ADA"
   >>> isPalindrome(s)
   True
   """ 
   return s == s[::-1]

def findThreeSum(nums, target):
    """
    >>> nums = [1,-1,0]
    >>> target = -1
    >>> findThreeSum(nums, target)
    False
    >>> nums = [3,7,1,2,8,4,5]
    >>> target = 10
    >>> findThreeSum(nums, target)
    True
    >>> nums = [3,7,1,2,8,4,5]
    >>> target = 21
    >>> findThreeSum(nums, target)
    False
    >>> nums = [-1,2,1,-4,5,-3]
    >>> target = -8
    >>> findThreeSum(nums, target)
    True
    >>> nums = [-1,2,1,-4,5,-3]
    >>> target = 0
    >>> findThreeSum(nums, target)
    True
    """
    combo = combinations(nums, 3)
    for c in combo:
        if sum(c) == target:
            return True

    return False
    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
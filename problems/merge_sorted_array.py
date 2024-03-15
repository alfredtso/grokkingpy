from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        >>> s = Solution()
        >>> nums1 = [1,2,3,0,0,0]
        >>> nums2 = [2,5,6]
        >>> s.merge(nums1, 3, nums2, 3)
        [1, 2, 2, 3, 5, 6]
        >>> nums1 = [5,5,5,0,0,0]
        >>> nums2 = [1,1,1]
        >>> s.merge(nums1, 3, nums2, 3)
        [1, 1, 1, 5, 5, 5]
        >>> nums1 = [0]
        >>> nums2 = [1]
        >>> s.merge(nums1, 0, nums2, 1)
        [1]
        >>> nums1 = [1]
        >>> nums2 = []
        >>> s.merge(nums1, 1, nums2, 0)
        [1]
        >>> nums1 = [1,1,1,0,0,0]
        >>> nums2 = [5,5,5]
        >>> s.merge(nums1, 3, nums2, 3)
        [1, 1, 1, 5, 5, 5]
        """
        i = m-1
        j = n-1
        
        for w in range(n+m-1,-1,-1):
            if j < 0:
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[w] = nums1[i]
                i -= 1
            else:
                nums1[w] = nums2[j]
                j -= 1
    
        print(nums1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()



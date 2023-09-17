from typing import List
from collections import defaultdict

class Solution:
    def sort_by_bits(self, arr: List[int]) -> List[int]:
        """
        >>> arr= [1024,512,256,128,64,32,16,8,4,2,1]
        >>> arr= [1,2,4,8,16,32,64,128,256,512,1024]
        """
        # sort by number of 1 and length in binary rep
        arr =sorted(arr, key=lambda x: (x.bit_count(), x))
        print(arr)

if __name__ == '__main__':
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    sol = Solution()
    sol.sort_by_bits(arr)
    import doctest
    doctest.testmod()
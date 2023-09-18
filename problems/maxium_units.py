from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize:int) -> int:
        """
        >>> boxTypes = [[1,3],[2,2],[3,1]]
        >>> sol = Solution()
        >>> sol.maximumUnits(boxTypes, 4)
        8
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res = 0
        for box, units in boxTypes:
            if truckSize >= box:
                res += box * units
                truckSize -= box
            else:
                res += truckSize * units
                break
        return res

if __name__ == '__main__':
    import doctest
    doctest.testmod()
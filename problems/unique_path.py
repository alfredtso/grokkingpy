from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        >>> s = Solution()
        >>> m, n = 3, 7
        >>> s.uniquePaths(m,n)
        28
        >>> m, n = 3, 2
        >>> s.uniquePaths(m,n)
        3
        """
        @lru_cache(None)
        def grid(m,n):
            if m == 0 or n == 0:
                return 0
            if m == 1 and n == 1:
                return 1
            if m == 1 and n == 2:
                return 1
            if m == 2 and n == 1:
                return 1

            return grid(m-1,n) + grid(m,n-1)

        return grid(m,n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

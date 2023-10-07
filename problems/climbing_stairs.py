from array import array

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        >>> s = Solution()
        >>> n = 2
        >>> s.climbStairs(n)
        2
        >>> n = 3
        >>> s.climbStairs(n)
        3
        >>> n = 4
        >>> s.climbStairs(n)
        5
        >>> n = 5
        >>> s.climbStairs(n)
        8
        """
        dp = array('b', range(n+2))
        dp[1] = 1
        dp[2] = 2
        if n <= 2:
            return dp[n]

        for x in range(3,n+1):
            dp[x] = dp[x-1] + dp[x-2]

        return dp[n]

if __name__ == "__main__":
    import doctest
    doctest.testmod()


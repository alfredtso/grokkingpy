from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        >>> sol = Solution()
        >>> s = "12"
        >>> sol.numDecodings(s)
        2
        >>> s = "226"
        >>> sol.numDecodings(s)
        3
        >>> s = "06"
        >>> sol.numDecodings(s)
        0
        >>> s = "0"
        >>> sol.numDecodings(s)
        0
        >>> s = "10"
        >>> sol.numDecodings(s)
        1
        >>> s = "100"
        >>> sol.numDecodings(s)
        0
        """
        @lru_cache(None)
        def dp(i):

            # Base case
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0

            if i == len(s) -1:
                return 1

            res = 0
            # Recurrent relation
            first = s[i:i+1]
            if first != "0":
                res += dp(i+1)

            second = s[i:i+2]
            if first != "0" and int(second) <= 26:
                res += dp(i+2)

            return res

        return dp(0)

if __name__ == "__main__":
    sol = Solution()
    s = "226"
    sol.numDecodings(s)
    import doctest
    doctest.testmod()

import typing
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        >>> c = Solution()
        >>> s = "abcdefgheqwrtyuiopasd"
        >>> c.lengthOfLongestSubstring(s)
        16
        """
        inv = defaultdict(lambda: 0)
        start, end = 0, 0
        counter = 0
        res = 0

        while end < len(s):
            inv[s[end]] += 1
            if inv[s[end]] > 1:
                counter += 1

            while counter:
                inv[s[start]] -= 1
                if inv[s[start]] == 1:
                    counter -= 1
                start += 1

            # update max
            res = max(res, end - start +1)
            end += 1
            
        return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()

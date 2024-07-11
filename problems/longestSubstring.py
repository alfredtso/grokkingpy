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
        inv = set()
        start, end = 0, 0
        counter = 0
        res = 0

        while end < len(s):
            if not s[end] in inv:
                inv.add(s[end])
            else:
                counter += 1

            while counter:
                inv.remove(s[start])
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

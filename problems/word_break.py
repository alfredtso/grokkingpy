from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        >>> sol = Solution()
        >>> s = "applepenapple"
        >>> wordDict = ["apple", "pen"]
        >>> sol.wordBreak(s, wordDict)
        True
        >>> s = "helloworld"
        >>> wordDict = ["word", "hello"]
        >>> sol.wordBreak(s, wordDict)
        False
        >>> s = "helloworld"
        >>> wordDict = ["world", "hello"]
        >>> sol.wordBreak(s, wordDict)
        True
        """
        @lru_cache
        def dp(ptr):
            # because on lowest level match would result in -1
            if ptr < 0:
                return True

            for word in wordDict:
                # if match, check if the prev jump also true
                if s[ptr-len(word)+1:ptr+1] == word and dp(ptr - len(word)):
                    return True

            return False

        return dp(len(s)-1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

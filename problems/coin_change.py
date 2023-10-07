from functools import lru_cache
from typing import List
from time import perf_counter as pc

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        >>> s = Solution()
        >>> coins = [1,2,5]
        >>> amount = 11
        >>> s.coinChange(coins,amount)
        3
        >>> coins = [2]
        >>> amount = 3
        >>> s.coinChange(coins,amount)
        -1
        >>> coins = [1]
        >>> amount = 0
        >>> s.coinChange(coins,amount)
        0
        >>> coins = [186,419,83,408]
        >>> amount = 6249
        >>> s.coinChange(coins,amount)
        20
        """
        @lru_cache(None)
        def dfs(rem):
            if rem < 0:
              return -1
            if rem == 0:
              return 0
          
            min_cost = float('inf')
            for i in coins:
              res = dfs(rem-i)
              if res != -1:
                  min_cost = min(min_cost, res + 1)

            return min_cost if min_cost != float('inf') else -1

        start = pc();
        res = dfs(amount)
        elapsed = pc() - start;
        print(f"Used {elapsed}")
        return res

if __name__ == "__main__":
    s = Solution()
    coins = [1,2,5]
    amount = 11
    s.coinChange(coins, amount)
    import doctest
    doctest.testmod()


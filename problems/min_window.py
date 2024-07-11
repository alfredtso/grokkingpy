from collections import defaultdict
import pprint

class Solution:
    def debug(self, s, start, end, counter, inv):
        # viz
        padding = 7 + len(s)
        print(f'{s: >{padding}}')
        # end pointer viz
        # Make util class for visualization of similar 
        tmp_end_space = ['.'] * (len(s) - 1)
        tmp_end_space.insert(end, '_')
        tmp_end = ''.join(tmp_end_space)
        print(f'end:   {tmp_end}')
        # start pointer viz
        # Make util class for visualization of similar 
        tmp_start_space = ['.'] * (len(s) - 1)
        tmp_start_space.insert(start, '_')
        tmp_start = ''.join(tmp_start_space)
        print(f'start: {tmp_start}')
        # print others
        pprint.pp(inv.items())
        print(f'counter: {counter}')
        print(''.join(['-'] * 10))
        ### viz ###


    def minWindow(self, s: str, t: str):
        """
        >>> sol = Solution()
        >>> s = "ABBCA"
        >>> t = "ABC"
        >>> sol.minWindow(s,t)
        "BCA"
        >>> s = "ABBBCCABC"
        >>> t = "ABC"
        >>> sol.minWindow(s,t)
        "ABC"
        """
        inv = defaultdict(lambda: 0)
        for c in t:
            inv[c] += 1

        start, end = 0, 0
        min_win_len = len(s) + 1
        min_window_start = 0
        counter = len(t)

        while end < len(s):
            # comment this out
            self.debug(s,start,end,counter,inv)
            
            if s[end] in inv:
                # Then we can decrease the counter
                if inv[s[end]] > 0:
                    counter -= 1
                # Also decrement the inv 
                inv[s[end]] -= 1

            # When we see last the character in the current window
            # meaning that the counter is 0; why do we use while
            while counter == 0:
                
                """
                This is for the std record keeping
                We do one pass only, so it's necessary to keep the record
                """
                if end - start + 1 < min_win_len:
                    min_win_len = end - start + 1
                    min_win_start = start
                

                if s[start] in inv:
                    inv[s[start]] += 1
                    """
                    1. initialize inventory
                    2. move end ptr to find a valid window
                    3. once the window is found, start moving the start
                    4. keep track of the inv to see how far can we move the start
                    5. moving end ptr again once the window become invalid
                    """
                    
                    """
                    meaning that in the current sliding window, we ran out of
                    the character at s[start]. in the inv, negative value 
                    actually means surplus and + ops is actually taking away
                    the "buffer"
                    For the "ABBCA" case, we can see when the start ptr ran over
                    the char B twice, so for the B
                    """
                    if inv[s[start]] > 0:
                        counter += 1

                start += 1

            end += 1

        if min_win_len == len(s) + 1:
            return ""
        else:
            return s[min_win_start:min_win_start + min_win_len]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    

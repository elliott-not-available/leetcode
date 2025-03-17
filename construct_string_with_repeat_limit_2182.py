# construct_string_with_repeat_limit_2182
# https://leetcode.com/problems/construct-string-with-repeat-limit/description/?envType=daily-question&envId=2024-12-17

from collections import Counter

class Solution_og:
    # does not work
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        dok = Counter(s)
        ss = list(reversed(sorted(dok.keys())))

        res = ""
        
        for i, char in enumerate(ss):
            
            char_lim = 0

            while dok[char] > 0:

                if char_lim >= repeatLimit and i < (len(ss)-1):
                    res += ss[i+1]
                    dok[ss[i+1]] -= 1
                    char_lim = 0
                elif char_lim < repeatLimit:
                    res += char
                    dok[char] -= 1
                    char_lim += 1
                else:
                    return res
        return res


import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        mh = [(-ord(c), cnt) for c, cnt in count.items()]
        heapq.heapify(mh)

        res = []

        while mh:
            # state 1
            char, cnt = heapq.heappop(mh)
            char = chr(-char)
            cur_cnt = min(cnt, repeatLimit)
            res.append(char * cur_cnt)

            # state 2
            if cnt - cur_cnt > 0 and mh:
                n_char, n_cnt = heapq.heappop(mh)
                n_char = chr(-n_char)
                res.append(n_char)

                heapq.heappush(mh, (-ord(char), cnt - cur_cnt))

                if n_cnt > 1:
                    heapq.heappush(mh, (-ord(n_char), n_cnt - 1))

        return "".join(res)


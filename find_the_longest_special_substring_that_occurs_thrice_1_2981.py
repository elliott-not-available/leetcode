# find_the_longest_special_substring_that_occurs_thrice_1_2981
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description/?envType=daily-question&envId=2024-12-10

from collections import Counter, deque

class Solution:
    def maximumLength(self, s: str) -> int:
        # thinking deque bruteforce
        combos = []
        q = deque()

        for j in range(len(s)):
            if j < len(s)-1:
                q.append((j+1, s[j]))
            combos.append(s[j])


        while q:
            i, previous = q.pop()
            # print(combos, i)

            if previous != "" and s[i] == previous[-1]:
                new_c = previous+s[i]
                combos.append(new_c)
                if i < len(s)-1:
                    q.append((i+1, new_c))

        str_counter = Counter(combos)
        print(str_counter)

        max_l = -1
        for string in str_counter:
            if str_counter[string] >= 3:
                max_l = max(max_l, len(string))

        return max_l
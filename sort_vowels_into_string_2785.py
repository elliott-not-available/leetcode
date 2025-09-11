# https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2025-09-11

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        caps = [c.upper() for c in vowels]
        vowels += caps
        # could list all vowels from start
        # could list all vowels as a string instead of list


        to_sort = []
        for c in s:
            if c in vowels:
                to_sort.append(c)

        # early exit if to_sort = 0?

        to_sort.sort()

        s_list = list(s)
        count = 0

        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = to_sort[count]
                count += 1
        
        return "".join(s_list)
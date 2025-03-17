# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10

from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # # brain fried, not working, not understanding question 100%
        # # vowels = ["a", "e", "i", "o", "u"]
        # # vowels_c = [0, 0, 0, 0, 0]
        # vowels = {
        #     "a": 0,
        #     "e": 0,
        #     "i": 0,
        #     "o": 0,
        #     "u": 0,
        #     }

        # ss_len = 5 + k
        # l = 0
        # cons = 0
        # res = 0

        # def check_vowels() -> bool:
        #     for k in vowels.keys():
        #         if vowels[k] == 0:
        #             return False
        #     return True

        # for r in range(len(word)):

        #     if word[r] not in vowels:
        #         cons += 1
        #     elif word[r] in vowels:
        #         vowels[word[r]] += 1

        #     if r-l+1 == ss_len:
        #         if cons == k and check_vowels():
        #             print(f"{l} , {r}")
        #             res += 1
        #         continue

        #     if r-l+1 > ss_len:
        #         if word[l] not in vowels:
        #             cons -= 1
        #         elif word[l] in vowels:
        #             vowels[word[l]] -= 1
        #         l += 1
        #         continue

        # return res

        def atleastk(k):
            vowelcount = defaultdict(int)
            vowels = "aeiou"
            cons = 0
            res = 0
            l = 0

            for r in range(len(word)):
                if word[r] in vowels:
                    vowelcount[word[r]] += 1
                else:
                    cons += 1

                while len(vowelcount) == 5 and cons >= k:
                    res += len(word) - r
                    if word[l] in vowels:
                        vowelcount[word[l]] -= 1
                        if vowelcount[word[l]] == 0:
                            vowelcount.pop(word[l])
                    else:
                        cons -= 1
                    l += 1
            return res
        
        return atleastk(k) - atleastk(k + 1)
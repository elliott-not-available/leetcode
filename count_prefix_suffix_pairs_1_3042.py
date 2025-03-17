# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/?envType=daily-question&envId=2025-01-08
# neet does a very cool/very hard alternative

class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        # words.sort(key=len)

        def isPrefixSuffix(word1, word2) -> bool:
            n = len(word1)
            # can use startswith endswith
            if word1 == word2[:n] and word1 == word2[-n:]:
                return True
            return False
        
        res = 0
        N = len(words)

        for i in range(N):
            for j in range(i+1, N):
                if isPrefixSuffix(words[i], words[j]):
                    res += 1

        return res
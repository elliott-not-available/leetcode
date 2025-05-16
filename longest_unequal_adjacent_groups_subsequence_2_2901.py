# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/description/?envType=daily-question&envId=2025-05-16


class Solution:
    def getWordsInLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        if len(words) == 1:
            return words

        def hamtastic(word1, word2):
            if len(word1) != len(word2):
                return False
            
            dif = 0
            for a,b in zip(word1, word2):
                if a != b:
                    dif += 1

                if dif > 1:
                    return False
            return dif == 1
        
        N = len(words)
        dp = [1] * N
        p = [-1] * N
        max_i = 0

        for i in range(1,N):
            for j in range(i):

                if (
                    groups[i] != groups[j] and 
                    hamtastic(words[i], words[j]) and 
                    dp[i] < (dp[j]+1)
                ):
                    dp[i] = dp[j] + 1
                    p[i] = j

            max_i = max(max_i, dp[i])

        res = []
        for i in range(N):
            if dp[i] == max_i:
                while i != -1:
                    res.append(words[i])    
                    i = p[i]
                break

        # k = max_i
        # while k != -1:
        #     res.append(words[k])
        #     k = p[k]


        return res[::-1]
# https://leetcode.com/problems/find-the-original-typed-string-ii/description/?envType=daily-question&envId=2025-07-02

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7

        n, cnt, freq = len(word), 1, list()

        for i in range(1, n):
            if word[i] == word[i-1]:
                cnt+=1
            else:
                freq.append(cnt)
                cnt = 1

        freq.append(cnt)

        res = 1
        for f in freq:
            res = res * f %MOD

        if len(freq) >= k:
            return res
        
        f, g = [1] + [0] * (k-1), [1] * k
        for i in range(len(freq)):
            f_new = [0] * k
            for j in range(1, k):
                f_new[j] = g[j-1]
                if j - freq[i] -1 >= 0:
                    f_new[j] = (f_new[j] - g[j - freq[i] - 1]) % MOD
            g_new = [f_new[0]] + [0]*(k-1)
            for j in range(1, k):
                g_new[j] = (g_new[j-1] + f_new[j]) % MOD
            f, g = f_new, g_new

        return (res - g[k-1]) % MOD
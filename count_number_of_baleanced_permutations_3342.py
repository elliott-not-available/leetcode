# https://leetcode.com/problems/count-number-of-balanced-permutations/?envType=daily-question&envId=2025-05-09


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        # # brute force: go through all unique permutations and check if balanced O(n**n)
        # # ofc being a hard problem, bruteforce is not enough
        # visited = [] # set?

        # tot = sum(int(c) for c in num)
        # if tot % 2: return 0

        # def permutations(string, step=0):#, odd=0, even=0):
        #     if step == len(string):
        #         if string in visited:
        #             return 
        #         visited.append(string)
        #         # print("".join(string))

        #         # if check_balanced(string):
        #         #     return 1
            
        #     for i in range(step, len(string)):
        #         s_c = [c for c in string]
        #         s_c[step], s_c[i] = s_c[i], s_c[step]

        #         # if i % 2: odd += s_c[i]
        #         # else: even += s_c[i]

        #         # if step % 2: odd += s_c[step]
        #         # else: even += s_c[step]

        #         permutations(s_c, step + 1)

        # def check_balanced(string):
        #     odd = 0
        #     even = 0
        #     s = 0
        #     for c in string:
        #         if s % 2:
        #             odd += int(c)
        #         else:
        #             even += int(c)
        #         s += 1

        #     # print(string, even, odd)
        #     return odd == even
        
        # permutations(num)

        # res = 0        
        # for s in visited:
        #     if check_balanced(s):
        #         res += 1

        # return res
        ##########################################################
        # Dynamic programming and combinatorics - Jinwoo-solution

        MOD = 10**9 + 7
        N = len(num)


        tot = sum(int(c) for c in num) 
        if tot % 2: return 0

        # this get p heavy on the math side, not sure tbh
        fact = [1]*(N+1)
        inv = [1]*(N+1)
        invFact = [1]*(N+1)
        for i in range(1,N+1): fact[i] = fact[i-1]*i % MOD
        for i in range(2,N+1): inv[i] = MOD - (MOD//i)*inv[MOD%i] % MOD
        for i in range(1,N+1): invFact[i] = invFact[i-1]*inv[i] % MOD

        halfSum = tot//2
        halfLen = N//2
        dp = [[0]*(halfLen+1) for _ in range(halfSum+1)]
        dp[0][0] = 1

        # yeah lol no idea cba

        digits = [0]*10
        for c in num:
            d = int(c)
            digits[d] += 1
            for i in range(halfSum, d-1, -1):
                for j in range(halfLen, 0, -1):
                    dp[i][j] = (dp[i][j] + dp[i-d][j-1]) % MOD

        res = dp[halfSum][halfLen]
        res = res * fact[halfLen] % MOD * fact[N-halfLen] % MOD
        for cnt in digits: res = res * invFact[cnt] % MOD
        return res

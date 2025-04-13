class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # list of primes
        # 0 = even

        # n = length of number

        # for every 2 digits in string you will have
        # 5 (even choices) and 4 (prime choices)

        # surely this can be mathed
        # timelimit exceeded, guess the numbers are too large
        # if n == 1:
        #     return 5


        # MOD = (10**9)+7
        # odd = n & 1 
        # res = ((5 * 4) ** (n//2)) * (5) if odd else ((5 * 4) ** (n//2))

        # # print(odd)
        # # print(res)

        # # print(n//2)
        # return res % MOD

        #########################################################

        # editorial says this is faster, not sure why tho

        # even index has 5 choices
        # odd index has 4 choices

        # total choices is 5(n+1//2)*4(n//2)
        # n+1 because 0 is an "even" index

        # not 100% sure what quickmul is doing tho

        MOD = 10**9 +7

        def quickmul(x, y):
            ret, mul = 1, x

            while y > 0:
                if y % 2 == 1:
                    ret = ret*mul % MOD
                mul = mul*mul % MOD
                y //=2
            return ret
        return quickmul(5, (n+1)// 2)*quickmul(4, n//2) % MOD

        # i guess modding it during calc saves time somewhere?
        # still think first option should be faster (intuitively)
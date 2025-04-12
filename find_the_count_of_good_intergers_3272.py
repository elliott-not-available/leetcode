# https://leetcode.com/problems/find-the-count-of-good-integers/description/?envType=daily-question&envId=2025-04-12
from collections import Counter
from math import factorial
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        # # this is missing bits and does not work (leading trailing 0s and something else)
        # # divisible by k
        # # palindrome
        # # return k-palindromes with n digits
        # end = (10 ** n)
        # start = 10 ** (n - 1)
        # res = 0
        # cache = set()

        # def can_be_palindrome(i, cache):

        #     str_i = str(i)
        #     ss = "".join(sorted(str_i))
        #     if ss in cache:
        #         return True
        #     # S = len(str_i)
        #     # mid = (S // 2) - 1 if S % 2 else S // 2
        #     # for j in range(mid):
        #     # odd length, middle man

        #     one_odd = False
        #     if len(str_i) % 2 != 0:
        #         one_odd = True
        #     chars = Counter(str_i)

        #     # if chars in cache:
        #     #     return False

        #     for c in chars:
        #         if (chars[c] % 2 == 1) and not one_odd:
        #             return False
        #         if (chars[c] % 2 == 1) and one_odd:
        #             one_odd = False
        #     print(ss, i)
        #     cache.add(ss)
        #     return True


        # for i in range(start, end):
        #     if i % k == 0 and can_be_palindrome(i, cache):
        #         res += 1

        # return res
        ##############################################################

        # this is tough, copy and paste from the editorial
        # the naruto solution explains it pretty well

        # 1. Get palindroms of lenth n
        # 2. Check for divisibility by k
        # 3. count perms of digits using combinatorics (maths)
        # 4. remove combos starting with 0

        # things i dont understand in this solution:

        # 1. s += s[::-1][skip:] 
        # reverse string then skip n & 1? n & 1 => 1 if odd, 0 if even
        # 2.



        dictionary = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1
        # Enumerate the number of palindrome numbers of n digits
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            palindromicInteger = int(s)
            # If the current palindrome number is a k-palindromic integer
            if palindromicInteger % k == 0:
                sorted_s = "".join(sorted(s))
                dictionary.add(sorted_s)

        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        for s in dictionary:
            cnt = [0] * 10
            for c in s:
                cnt[int(c)] += 1
            # Calculate permutations and combinations
            tot = (n - cnt[0]) * fac[n - 1]
            for x in cnt:
                tot //= fac[x]
            ans += tot

        return ans
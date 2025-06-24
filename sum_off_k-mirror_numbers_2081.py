# https://leetcode.com/problems/sum-of-k-mirror-numbers/description/?envType=daily-question&envId=2025-06-23

class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def ispali(x):
            digit = []
            while x:
                digit.append(x % k)
                x //= k
            return digit == digit[::-1]
        
        left, cnt, ans = 1, 0, 0

        while cnt < n:

            right = left*10

            # op 0 = odd length
            # op 1 = even length
            for op in [0, 1]:
                for i in range(left, right):
                    if cnt == n:
                        break

                    combined = i

                    x = i//10 if op ==0 else i

                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if ispali(combined):
                        cnt += 1
                        ans += combined
            left = right



        return ans
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/?envType=daily-question&envId=2025-06-09

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def count_steps(n, pre1, pre2):
            steps = 0
            while pre1 <= n:
                steps += min(n+1, pre2) - pre1
                pre1 *= 10
                pre2 *= 10
            return steps
        
        cur = 1
        k -= 1

        while k > 0:
            step = count_steps(n, cur, cur+1)

            if step <= k:
                cur += 1
                k -= step
            else:
                cur *= 10
                k-=1
        
        return cur
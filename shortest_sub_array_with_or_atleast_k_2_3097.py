# shortest_sub_array_with_or_atleast_k_2_3097
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/?envType=daily-question&envId=2024-11-10

class Solution:
    # neeeted
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        res = float("inf")
        bits = [0]*32

        def bits_update(bits, n, diff):
            for i in range(32):
                # 0001 ---> 0010 ---> 0100 ...
                if n & (1 << i):
                    bits[i] += diff

        def bits_to_int(bits):
            res = 0
            for i in range(32):
                if bits[i]:
                    res += (1 << i)
            return res

        l = 0
        for r in range (len(nums)):
            bits_update(bits, nums[r], 1)
            cur_or = bits_to_int(bits)

            while cur_or >= k and l <= r:
                res = min(res, r-l + 1)
                bits_update(bits, nums[l], -1)
                cur_or = bits_to_int(bits)
                l += 1

        return -1 if res == float("inf") else res
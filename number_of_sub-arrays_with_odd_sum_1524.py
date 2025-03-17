# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/?envType=daily-question&envId=2025-02-25

class Solution:
    # timelimit exceeded
    def numOfSubarrays(self, arr: list[int]) -> int:

        N = len(arr)
        res = 0

        # get every subarray
        # if sum(subarray) % 2 == 1: res += 1

        for i in range(N):
            for j in range(i+1, N+1):
                s = sum(arr[i:j])
                if s % 2 == 1:
                    res += 1


        return res
    


# leet syays prefix sum / dynamic programing

class Solution:

    def numOfSubarrays(self, arr: list[int]) -> int:
        cur_sum = 0
        odd_cnt = 0
        evn_cnt = 0
        MOD = 10**9 + 7
        res = 0

        for n in arr:
            cur_sum += n

            if cur_sum % 2: # odd
                res +=1 + evn_cnt
                odd_cnt += 1
            else: # even
                res += odd_cnt
                evn_cnt += 1

        return res % MOD
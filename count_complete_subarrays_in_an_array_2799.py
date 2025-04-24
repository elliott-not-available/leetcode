# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/?envType=daily-question&envId=2025-04-24

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        # brute force O(n**2)
        N = len(nums)
        uniq = set(nums)
        print(uniq)
        res = 0
        for i in range(N-1):
            for j in range(i, N):
                if uniq == set(nums[i:j+1]):
                    # print(f"good {i, j}")
                    res += 1
                # else:
                #     print(f"bad {i, j}")

        if uniq == set([nums[-1]]):
            res += 1
        return res# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/?envType=daily-question&envId=2025-04-24

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        # brute force O(n**2)
        N = len(nums)
        uniq = set(nums)
        print(uniq)
        res = 0
        for i in range(N-1):
            for j in range(i, N):
                if uniq == set(nums[i:j+1]):
                    # print(f"good {i, j}")
                    res += 1
                # else:
                #     print(f"bad {i, j}")

        if uniq == set([nums[-1]]):
            res += 1
        return res# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/?envType=daily-question&envId=2025-04-24

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        # # brute force O(n**2) time limit exceeded
        # N = len(nums)
        # uniq = set(nums)
        # print(uniq)
        # res = 0
        # for i in range(N-1):
        #     for j in range(i, N):
        #         if uniq == set(nums[i:j+1]):
        #             # print(f"good {i, j}")
        #             res += 1
        #         # else:
        #         #     print(f"bad {i, j}")

        # if uniq == set([nums[-1]]):
        #     res += 1

        # # update set each time?
        # return res
        ##############################################
        # for each n move right pointer right until nums[n:r] contains needed elements
        # maintain set instead of call set
        # once match is found, all larger sequences of n:r+x will also work
        # add N - r + 1 to result beacause of this
        N = len(nums)
        res = 0
        uniq = len(set(nums))
        cur = {}
        r = 0
        for l in range(N):
            if l > 0:
                remove = nums[l - 1]
                cur[remove] -= 1
                if cur[remove] == 0:
                    cur.pop(remove)

            while r < N and len(cur) < uniq:
                add = nums[r]
                cur[add] = cur.get(add, 0) + 1
                r += 1
            if len(cur) == uniq:
                res += N - r + 1
        return res
# https://leetcode.com/problems/container-with-most-water/?envType=daily-question&envId=2025-10-04

class Solution:
    def maxArea(self, height: list[int]) -> int:

        # # brute force: timelimit exceeded
        # n = len(height)
        # cur_max = 0

        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         h = min(height[i], height[j])
        #         w = j - i - 1
        #         v = h * w
        #         cur_max = max(cur_max, v)

        # return cur_max
        
        l = 0
        r = len(height) -1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r += 1
        return res
    
    # saw this on fastest solution lol:
    # 
# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("00000"))
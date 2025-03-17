# https://leetcode.com/problems/alternating-groups-ii/description/?envType=daily-question&envId=2025-03-09

class Solution:
    
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        # colors loops
        # create function to check if list is alternating
        # for i in range(len(col)): res += is_alternating(cols[i:i+k])
        # will need to do some logic to create loop (smash to cols together?)


        # # initial solution, seems to work but timelimit exceeded
        # # optimised the solution to only run the function when necessary, otherwise sliding window
        # # this takes it from O(n**2) to somewere between O(n) < X < O(n**2)

        # # this is still very suboptimal, barely passes runtime check
        # N = len(colors)
        # colsmash = colors + colors

        # def is_alternating(binary_list: list[int]) -> int:
        #     prev = 69
        #     for i in binary_list:
        #         if i == prev:
        #             return 0
        #         prev = i
        #     return 1

        # res = 0
        # prev_res = 0

        
        # for i in range(N):
        #     if prev_res:
        #         prev_end_v = colsmash[i+k-2]
        #         cur_end_v = colsmash[i+k-1]
        #         if cur_end_v != prev_end_v:
        #             print(f"{i} prev +")
        #             res +=1
        #         else:
        #             print(f"{i} prev -")
        #             prev_res = 0
        #     else:
        #         print(f"{i} raw")
        #         prev_res = is_alternating(colsmash[i:i+k])
        #         res += prev_res

        # return res

        # full sliding window

        N = len(colors)
        l = 0
        res = 0

        for r in range(1, N + k-1):

            if colors[r % N] == colors[(r-1) % N]:
                l = r

            if r - l + 1 > k:
                l += 1

            if r - l + 1 == k:
                res += 1
            

        return res

        
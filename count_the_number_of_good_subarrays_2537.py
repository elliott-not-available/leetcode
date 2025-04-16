# https://leetcode.com/problems/count-the-number-of-good-subarrays/description/?envType=daily-question&envId=2025-04-16
# from collections import defaultdict

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:

        # brute force o(n**2) -- timelimit exceeded

        # N = len(nums)
        # res = 0
        # for i in range(N-1):
        #     x = nums[i]
        #     good_count = 0
        #     cur_elements = { x: 1 }
        #     for j in range(i+1, N):
        #         y = nums[j]
        #         # 2 = 1
        #         # 3 = 3
        #         # 4 = (3 + 3)
        #         # 5 = (6 + 4)
        #         # number of pairs = prev_count + (n-1)
        #         if y in cur_elements:
        #             cur_elements[y] += 1
        #             good_count += (cur_elements[y]-1)
        #         else:
        #             cur_elements[y] = 1

        #         if good_count >= k:
        #             res += 1

        # return res
        ####################################################

        N = len(nums)
        visited = [False] * N
        i = 0
        visited[0] = True
        j = 1
        cur_elements = { nums[i] : 1 }
        pairs = 0
        res = 0
        

        while i < (N-1):
            x = nums[i]
            y = nums[j]

            if y not in cur_elements:
                cur_elements[y] = 1
            elif not visited[j]:
                cur_elements[y] += 1
                pairs += (cur_elements[y]-1)
                visited[j] = True

                
            # 2 => 1 : 1 => 0   : -1
            # 3 => 2 : 3 => 1   : -2
            # 4 => 3 : 6 => 3   : -3
            # 5 => 4 : 10 => 6  ; -4
            if pairs >= k:
                # print(i, j)
                # print(cur_elements)
                res += (N - j)
                i += 1
                cur_elements[x] -= 1
                pairs -= cur_elements[x]
            elif j < (N-1):
                j += 1
            else:
                return res
        print("do i get here?") # no you dont
        
        return res
            


        
        
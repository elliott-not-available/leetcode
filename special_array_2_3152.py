# special_array_2_3152
# https://leetcode.com/problems/special-array-ii/description/?envType=daily-question&envId=2024-12-09

class Solution:
    # timelimit exceeded untill adding bin search
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        fail_arr = []
        
        for i in range(len(nums)-1):

            a = nums[i] % 2
            b = nums[i+1] % 2

            if a == b:
                fail_arr.append(i)

        def q_response(query: list[int]) -> bool:
            if query[0] == query[1]:
                return True
            
            
            l = 0
            r = len(fail_arr) - 1
            while l <= r:
                mid = l + (r - l)//2 # mid point
                fail_ind = fail_arr[mid] # middle value

                if fail_ind < query[0]: # if middle value less than query start, move left pointer right (increase next middle value)
                    l = mid + 1
                elif fail_ind > query[1] - 1: # if middle value greater than query end, move right pointer left (decrease next middle value)
                    r = mid - 1
                else:
                    return False
            return True

        return [q_response(q) for q in queries]
        
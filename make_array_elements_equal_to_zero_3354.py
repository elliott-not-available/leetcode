# https://leetcode.com/problems/make-array-elements-equal-to-zero/description/?envType=daily-question&envId=2025-10-28

class Solution:
    def countValidSelections(self, nums: list[int]) -> int:

        n = len(nums)
        def is_valid(inp_data, start_index, direction_start):
            i = start_index
            data = [inp for inp in inp_data]
            direction = direction_start

            if data[start_index] != 0:
                return 0

            while i >= 0 and i < n:
                if data[i]:
                    data[i] -= 1
                    direction *= -1
                i += direction

            # print(inp_data)
            # print(start_index, data, direction_start)
            # print(data, all(val == 0 for val in data))

            if all(val == 0 for val in data):
                return 1
            return 0

        res = 0

        for i in range(n):

            res += is_valid(nums, i, +1) + is_valid(nums, i, -1)
                

        return res
        
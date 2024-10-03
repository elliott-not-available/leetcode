import copy

def validation(array: list[int], p: int):
    if len(array) < 1 or len(array) > 10**5:
        raise ValueError(f"Array size : {len(array)} fails array size validation")
    if p < 1 or p> 10**9:
        raise ValueError(f"Value p : {p} fails p validation")
    
    # element validation 1 <= array[i] <= 10**5

# def recurs_remove_element(nums: list[int], p: int) -> int:
#     # remove element
#     # is it divisible by p?
#     # if yes return
#     # if no recurse

#     # this will return length of array which sum is divisible by p with minimal remove
#     if not nums:
#         return -1

#     for num in nums:
#         temp_nums = copy.deepcopy(nums)
#         popped = temp_nums.remove(num)
#         temp_sum = sum(temp_nums)

#         if p <= temp_sum:
#             x_r = temp_sum % p

#             if x_r == 0:
#                 # print(f"ending: {temp_nums}")
#                 return len(temp_nums)
            
#             if x_r in temp_nums:
#                 # print(f"ending: {temp_nums}")
#                 return len(temp_nums) - 1
            
#             recurs_remove_element(temp_nums, p)
#     return -1

# def rr(nums: list[int], sum_nums: int, sub_arr: list[int], p: int) -> int:
#     # stop infinite

#     if len(sub_arr) >= len(nums):
#         return -1
    
#     temp_sub_array = sub_arr.copy()

#     for i in range(len(nums)):
#         temp_sub_array = sub_arr.copy()
#         temp_sub_array.append(nums[i])

#         temp_sum_nums = sum_nums - sum(sub_arr)
#         num_r = temp_sum_nums % p

#         if num_r == 0:
#             return len(temp_sub_array)
#         else:
#             rr(nums, sum_nums, temp_sub_array, p)
#     return -1


class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        validation(nums, p)
        
        total_sum = sum(nums)

        if p > total_sum:
            return -1

        r = total_sum % p

        if r == 0:
            return 0
        
        if r in nums:
            return 1
        
        # # subarr_len = recurs_remove_element(nums, p)

        # # if subarr_len < 0:
        # #     return subarr_len
        
        # # return len(nums) - subarr_len

        # count = rr(nums, sum_nums, [], p)
        # return count

        p_mod = {0 : -1}
        p_sum = 0
        min_l = len(nums)

        for i, num in enumerate(nums):
            p_sum += num
            c_mod = p_sum % p
            t_mod = (c_mod - r + p) % p # mod needed to combo with r to mod 0

            if t_mod in p_mod:
                min_l = min(min_l, i - p_mod[t_mod])

            p_mod[c_mod] = i

        return min_l if min_l < len(nums) else -1



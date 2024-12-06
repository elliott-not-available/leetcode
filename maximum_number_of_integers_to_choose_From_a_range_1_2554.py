# maximum_number_of_integers_to_choose_From_a_range_1_2554
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/?envType=daily-question&envId=2024-12-06

class Solution_og:

    # this is apparently not efficient

    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        
        res = []
        cur_sum = 0
        max_res = 0


        for i in range(1, n+1):

            max_res = max(max_res, len(res))

            res.append(i)
            cur_sum += i

            if i in banned:
                res = []
                cur_sum = 0
                continue

            if cur_sum > maxSum:
                res = []
                cur_sum = 0
                break

            print(res)
        
        max_res = max(max_res, len(res))
        return max_res
        

class Solution:
    # this was the editorial "efficient" solution. i dont really understand it for now.
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        # Sort the banned list
        banned.sort()

        banned_idx = 0
        count = 0

        # Check each number from 1 to n while the sum is valid
        for num in range(1, n + 1):
            # Skip if the current number is in the banned list
            if banned_idx < len(banned) and banned[banned_idx] == num:
                # Handle duplicate banned numbers
                while banned_idx < len(banned) and banned[banned_idx] == num:
                    banned_idx += 1
            else:
                # Include the current number if possible
                maxSum -= num
                if maxSum >= 0:
                    count += 1
                else:
                    break

        return count
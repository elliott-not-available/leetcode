# find_score_of_an_array_after_mnarking_all_elements_2593
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description/?envType=daily-question&envId=2024-12-13

class Solution_og:
    # time exceeded
    def findScore(self, nums: list[int]) -> int:

        sorted_nums = sorted(nums)
        marked = set()
        score = 0

        for n in sorted_nums:
            for i in range(len(nums)):
                if nums[i] == n and i not in marked:
                    score += nums[i]

                    marked.add(i-1)
                    marked.add(i)
                    marked.add(i+1)
        return score
    
class Solution:
    def findScore(self, nums: list[int]) -> int:

        score = 0
        std = [(num, idx) for idx, num in enumerate(nums)]

        std.sort()
        marked = [False] * len(nums)

        for i in range(len(nums)):
            number = std[i][0]
            index = std[i][1]

            if not marked[index]:
                score += number
                marked[index] = True

                if index > 0:
                    marked[index - 1] = True
                if index + 1 < len(nums):
                    marked[index + 1] = True
        return score
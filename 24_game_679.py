# https://leetcode.com/problems/24-game/description/?envType=daily-question&envId=2025-08-18

class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        error_margin = 1e-6

        def dfs(nums: list[float]) -> bool:
            n = len(nums)

            if n == 1:
                print(nums)
                return abs(nums[0] - 24) < error_margin

            for i in range(n):
                for j in range(n):
                    if i ==j:
                        continue

                    nxt = [nums[k] for k in range(n) if k!=i and k!=j]

                    a, b = nums[i], nums[j]

                    ops = [a-b, b-a, a+b, a*b]

                    if abs(b) > error_margin: ops.append(a/b)
                    if abs(a) > error_margin: ops.append(b/a)

                    for v in ops:
                        if dfs(nxt + [v]):
                            return True
            return False
                        
        return dfs([float(c) for c in cards])
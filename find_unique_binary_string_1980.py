# https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2025-02-20

class Solution:
    # very very slow, how did it even pass. Backtracking would be more efficient
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        N = len(nums)
        def all_perms():
            cur = [["0"], ["1"]]
            n = 1

            while n < N:
                pre = cur
                cur = []
                for s in pre:
                   cur.append(s + ["0"])
                   cur.append(s + ["1"])
                n += 1
            return cur
        
        all_p = all_perms()

        for p in all_p:
            s = "".join(p)
            if s not in nums:
                return s


class Solution:
    # take opposite of ith digit of ith num - youtube comment xD
    def findDifferentBinaryString(self, nums: list[str]) -> str:

        res = []
        for i in range(len(nums)):
            opposite = (int(nums[i][i]) + 1) % 2
            res.append(str(opposite))

        return "".join(res)
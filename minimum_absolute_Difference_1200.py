# https://leetcode.com/problems/minimum-absolute-difference/description/?envType=daily-question&envId=2026-01-26

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        res = []
        cur_min = arr[-1] - arr[0]

        for i in range(len(arr)-1):
            cur = abs(arr[i+1] - arr[i])
            if cur < cur_min:
                cur_min = cur
                res = [[arr[i], arr[i+1]]]
            elif cur == cur_min:
                res.append([arr[i], arr[i+1]])

        

        return res
        
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description/?envType=daily-question&envId=2025-06-15

class Solution:
    def maxDiff(self, num: int) -> int:

        s_num = str(num)
        maxi = num
        mini = num

        for i in range(10):
            for j in range(10):

                tmp = s_num.replace(str(i), str(j))
                if tmp[0] != '0':
                    tmp = int(tmp)
                    maxi = max(maxi, tmp)
                    mini = min(mini, tmp)

        print(maxi)
        print(mini)
        return maxi - mini
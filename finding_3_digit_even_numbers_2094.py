# https://leetcode.com/problems/finding-3-digit-even-numbers/description/?envType=daily-question&envId=2025-05-12

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:

        # # brute force O(n**3)
        
        # N = len(digits)
        # res = set()

        # for k in range(N):
        #     if digits[k] % 2:
        #         continue
        #     for j in range(N):
        #         if j == k:
        #             continue 
        #         for i in range(N):
        #             if i == k or i == j or digits[i] == 0:
        #                 continue
        #             # cur = int(str(digits[i])+str(digits[j])+str(digits[k]))
        #             cur = digits[i] * 100 + digits[j] * 10 + digits[k]
        #             if cur in res:
        #                 continue
        #             res.add(cur)
        # return sorted(list(res))
        ##################################################
        # using enumeration - O(n + 10**3)
        d_map = [0] * 10
        for d in digits:
            d_map[d] += 1
        
        res = []

        for i in range(1, 10):
            if d_map[i] == 0:
                continue
            d_map[i] -= 1

            for j in range(10):
                if d_map[j] == 0:
                    continue
                d_map[j] -= 1

                for k in range(0, 10, 2):
                    if d_map[k] == 0:
                        continue
                    cur = i*100 + j*10 + k
                    res.append(cur)

                d_map[j] += 1
            d_map[i] += 1
        return res
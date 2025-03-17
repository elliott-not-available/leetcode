# defuse_the_bomb_1652
# https://leetcode.com/problems/defuse-the-bomb/description/?envType=daily-question&envId=2024-11-18

class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)
        if abs(k) > N:
            raise ValueError(
                f"k = {k} will not work as it is larger than length of the array {N}"
                ) 
        wrapped = code * 3
        res = [] # could initialise [0] * N
        for i in range(N):
            ap = 0
            if k > 0:
                start, end = N+i+1, N+i+k+1
                ap = sum(wrapped[start:end])
            if k < 0:
                start, end = N+i+k, N+i
                ap = sum(wrapped[start:end])

            res.append(ap)

        return res
        

class Solution_mod:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)
        res = [0]*N

        for i in range(N):
            if k > 0:
                for j in range(i+1, i+1+k):
                    res[i] += code[j % N]
            if k < 0:
                for j in range(i+k, i):
                    res[i] += code[j % N]

        return res
    

class Solution_sliding_window:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)
        res = [0] * N

        l = 0
        cur_sum = 0
        for r in range(N+abs(k)):
            cur_sum += code[r % N]

            if r - l + 1 > abs(k):
                cur_sum -= code[l % N]
                l = (l + 1) % N

            if r - l + 1 == abs(k):
                if k > 0:
                    res[(l - 1) % N] = cur_sum
                elif k < 0:
                    res[(r+l) % N] = cur_sum
                    
        return res
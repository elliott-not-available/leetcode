# https://leetcode.com/problems/fancy-sequence/?envType=daily-question&envId=2026-03-15


MOD = (10**9) + 7
# class Fancy:
#     # too slow

#     def __init__(self):
#         self.d = []
        

#     def append(self, val: int) -> None:
#         self.d.append(val)
#         # print(self.d)
        

#     def addAll(self, inc: int) -> None:
#         for i in range(len(self.d)):
#             self.d[i] += inc
#         # print(self.d)
        

#     def multAll(self, m: int) -> None:
#         for i in range(len(self.d)):
#             self.d[i] = self.d[i]*m
#         # print(self.d)

#     def getIndex(self, idx: int) -> int:
#         return self.d[idx] % MOD if idx < len(self.d) else -1
    

class Fancy:

    def __init__(self):
        self.d = []
        self.add = 0
        self.m = 1
        

    def append(self, val: int) -> None:
        x = val - self.add
        self.d.append(x * pow(self.m, MOD - 2, MOD) % MOD)
        
        

    def addAll(self, inc: int) -> None:
        self.add += inc
        

    def multAll(self, m: int) -> None:
        self.add *= m
        self.m *= m

    def getIndex(self, idx: int) -> int:

        return (self.d[idx]*self.m + self.add) % MOD if idx < len(self.d) else -1
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
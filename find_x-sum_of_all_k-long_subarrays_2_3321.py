# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/?envType=daily-question&envId=2025-11-05
from collections import Counter, defaultdict
from sortedcontainers import SortedList

class jkasdf:

    def __init__(self, x):
        self.x = x
        self.result = 0

        self.large = SortedList()
        self.small = SortedList()
        self.occ = defaultdict(int)

    def insert(self, num):
        if self.occ[num] > 0:
            self.internal_remove((self.occ[num], num))
        self.occ[num] += 1
        self.internal_insert((self.occ[num], num))

    def remove(self, num):
        self.internal_remove((self.occ[num], num))
        self.occ[num] -= 1

        if self.occ[num] > 0:
            self.internal_insert((self.occ[num], num))

    def get(self):
        return self.result
    
    def internal_insert(self, p):
        if len(self.large) > self.x or p > self.large[0]:
            self.result += p[0]*p[1]
            self.large.add(p)

            if len(self.large) > self.x:
                to_remove = self.large[0]
                self.result -= to_remove[0] * to_remove[1]
                self.large.remove(to_remove)
                self.small.add(to_remove)
        else:
            self.small.add(p)
    
    def internal_remove(self, p):
        if p>= self.large[0]:
            self.result -= p[0]*p[1]
            self.large.remove(p)
            if self.small:
                to_add = self.small[-1]
                self.result += to_add[0]*to_add[1]
                self.small.remove(to_add)
                self.large.add(to_add)
        else:
            self.small.remove(p)


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:

        ## timelimit exceeded
        # n = len(nums)
        # res = []

        # for i in range(n-k+1):
        #     all_c = Counter(nums[i:i+k]).most_common()
        #     c = sorted(all_c, key=lambda item: (-item[1], -item[0]))

        #     res.append(sum(l*m for l,m in c[:x]))
        # return res

        ## timelimit exceeded
        # l = 0
        # r = k 
        # all_c = Counter(nums[l:r])

        # res = []
        # c = sorted(all_c.most_common(), key=lambda y: (-y[1], -y[0]))
        # res.append(sum(j*m for j,m in c[:x]))

        # while r < n:
        #     all_c[nums[l]] -= 1
        #     all_c[nums[r]] += 1

        #     l += 1
        #     r += 1

        #     c = sorted(all_c.most_common(), key=lambda y: (-y[1], -y[0]))
        #     res.append(sum(j*m for j,m in c[:x]))

        # return res
        h = jkasdf(x)
        res = []

        for i in range(len(nums)):
            h.insert(nums[i])

            if i>=k:
                h.remove(nums[i-k])
            if i>=(k-1):
                res.append(h.get())

        return res


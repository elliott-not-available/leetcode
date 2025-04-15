# https://leetcode.com/problems/count-good-triplets-in-an-array/?envType=daily-question&envId=2025-04-15

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index <= (len(self.tree)-1):
            self.tree[index] += delta
            # ??? bitwise and with negative? google says somehting about shifting right
            index += index & -index

    def query(self, index):
        index += 1
        res = 0

        while index > 0:
            res += self.tree[index]
            index -= index & -index

        return res

class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        
        # # go through every 3 element subarray combination (Xi < Yi < Zi) in nums1
        # # are the elements still in order if the same array was made from nums2

        # # find all pairs whch work in both arrays
        # # count pairs where end == start

        # # 0(n**2 + n_pairs**2) - works but timelimit exceeded

        # N = len(nums1)
        # n2_m = {v:i for i,v in enumerate(nums2)}

        # valid_pair = []

        # for i in range(N-1):
        #     for j in range(i+1, N):
        #         cur_i = nums1[i]
        #         cur_j = nums1[j]
                
        #         if n2_m[cur_i] < n2_m[cur_j]:
        #             valid_pair.append((cur_i, cur_j))

        # res = 0

        # for i, j in valid_pair:
        #     for x, _ in valid_pair:

        #         if j == x:
        #             res += 1

        # return res
        #######################################################
        # editorial solution using FENWICH TREE

        # N = len(nums1)
        # pos2, reversed_index_map = [0] * N, [0] * N

        # for i, num2 in enumerate(nums2):
        #     pos2[num2] = i
        # for i, num1 in enumerate(nums1):
        #     reversed_index_map[pos2[num1]] = i

        # tree = FenwickTree(N)
        # res = 0

        # for v in range(N):
        #     pos = reversed_index_map[v]
        #     l = tree.query(pos)
        #     tree.update(pos, l)
        #     r = (N - 1 - pos) - (v - l)
        #     print(f"{l}, {r}")
        #     res += l*r
        # return res

        n = len(nums1)
        pos2, reversedIndexMapping = [0] * n, [0] * n
        for i, num2 in enumerate(nums2):
            pos2[num2] = i
        for i, num1 in enumerate(nums1):
            reversedIndexMapping[pos2[num1]] = i
        tree = FenwickTree(n)
        res = 0
        for value in range(n):
            pos = reversedIndexMapping[value]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n - 1 - pos) - (value - left)
            res += left * right
        return res
    

# should look into what this is, looks very cool
from bisect import bisect_left

class Solution_cool_solution_in_accpeted:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        nums2_index_map = {x: i for i,x in enumerate(nums2)}

        q = []
        counter = 0
        for (i,num) in enumerate(nums1):
            index = bisect_left(q, nums2_index_map[num])
            q.insert(index, nums2_index_map[num])
            counter += index*(n-1-nums2_index_map[num]-i+index)
        return counter
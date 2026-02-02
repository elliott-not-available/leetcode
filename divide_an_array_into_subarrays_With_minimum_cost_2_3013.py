# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/description/?envType=daily-question&envId=2026-02-02
from heapq import heappop, heappush, heapreplace

class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        heap_used, heap_unused, used = [], [], set()

        n = len(nums)
        s, res = 0, float('inf') #n*(10**5)+1

        for r in range(1, n):
            l = r - dist - 1

            if l > 0 and l in used:
                used.remove(l)
                s-=nums[l]

                while heap_unused and heap_unused[0][1] < l:
                    heappop(heap_unused)

                if heap_unused:
                    num, i = heappop(heap_unused)
                    heappush(heap_used, (-num, i))
                    used.add(i)
                    s += num

            if len(used) < k-1:
                heappush(heap_used, (-nums[r], r))
                used.add(r)
                s += nums[r]
            else:
                while heap_used[0][1] not in used:
                    heappop(heap_used)

                if nums[r] < -heap_used[0][0]:
                    num, i = heapreplace(heap_used, (-nums[r], r))
                    used.remove(i)
                    used.add(r)
                    s += num + nums[r]
                    heappush(heap_unused, (-num, i))
                else:
                    heappush(heap_unused, (nums[r], r))

            if l >=0:
                res = min(s, res)




        return nums[0] + res
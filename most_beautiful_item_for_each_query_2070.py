# most_beautiful_item_for_each_query_2070
# https://leetcode.com/problems/most-beautiful-item-for-each-query/description/?envType=daily-question&envId=2024-11-12

# time complexity of sorting nlogn

class Solution_bruteforce:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        res = [0]*len(queries)

        for i in range(len(queries)):
            for j in range(len(items)):
                if items[j][0] <= queries[i]:
                    if items[j][1] > res[i]:
                        res[i] = items[j][1]


        return res
    
# print(Solution().maximumBeauty([[1,2]], [1,2]))

class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])

        res = [0]* len(queries)
        max_beat = 0
        j = 0

        for q, i in queries:

            while j < len(items) and items[j][0] <= q:
                max_beat = max(max_beat, items[j][1])
                j += 1

            res[i] = max_beat

        return res

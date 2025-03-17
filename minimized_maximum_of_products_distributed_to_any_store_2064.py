# minimized_maximum_of_products_distributed_to_any_store_2064
# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/?envType=daily-question&envId=2024-11-14

class Solution_og:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        # out of range error cba

        quantities.sort()
    
        max_index = -1
        max_q = quantities[max_index]

        min_index = 0
        min_q = quantities[min_index]

        tot = sum(quantities)

        i = tot // n

        while i < max_q and min_index < len(quantities):
            mult = i*n

            if mult >= tot:

                if mult > min_q:
                    n -= 1
                    tot -= min_q

                    min_index += 1
                    min_q = quantities[min_index]
                else:
                    return i
                
            i += 1
        return max_q

import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def can_dist(x):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / x)
            return stores <= n
        
        l, r = 1, max(quantities)
        res = 0
        while l <= r:
            x = (l + r) // 2

            if can_dist(x):
                res = x
                r = x - 1
            else:
                l = x + 1

        return res
# maximum_xor_for_each_query_1829
# https://leetcode.com/problems/maximum-xor-for-each-query/description/?envType=daily-question&envId=2024-11-08

class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:

        # xor of all elements in array
    
        xor = 0
        for n in nums:
            xor ^= n

        mask = 2 ** maximumBit - 1
        answer = []
        for n in reversed(nums):
            answer.append(xor ^ mask)
            xor ^= n
        
        return answer
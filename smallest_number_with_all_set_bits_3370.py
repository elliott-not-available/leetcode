# https://leetcode.com/problems/smallest-number-with-all-set-bits/description/?envType=daily-question&envId=2025-10-29

class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = bin(n)[2:]
        set_bin = ["1" for _ in binary]

        # print(binary, set_bin)
        # print("".join(set_bin))
        return int("".join(set_bin), 2)
    

# # there is actually a pattern for set bits

# Enumerate integers that contain only set bits: 1,3,7,15.
# We can observe that the pattern of this sequence is that
# each number is obtained by multiplying the previous number
# by 2 and then adding 1.

# We initialize x=1. In each iteration of the loop, we
# update x as x=x×2+1. The loop continues until x becomes
# greater than or equal to n, and then we return the
# result.
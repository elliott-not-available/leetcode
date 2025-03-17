# maximum_swap_670
# https://leetcode.com/problems/maximum-swap/description/?envType=daily-question&envId=2024-10-17

# i think this solution is not expansion friendly
class Solution:
    def maximumSwap(self, num: int) -> int:

        inp = [int(n) for n in str(num)]
        sorted_inp = sorted(inp.copy(), reverse=True)

        if inp == sorted_inp:
            return num

        for i in range(len(inp)):
            if inp[i] != sorted_inp[i]:
                temp = inp[i]
                inp_r = inp[::-1]
                ind = len(inp) - inp_r.index(sorted_inp[i]) -1

                inp[i] = sorted_inp[i]
                inp[ind] = temp

                return int(''.join([str(n) for n in inp]))
            

class Solution_TOP:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of characters for easy manipulation
        num_list = list(str(num))
        
        # Track the last occurrence of each digit (0-9)
        last = {int(d): i for i, d in enumerate(num_list)}
        
        # Traverse the number from left to right
        for i, digit in enumerate(num_list):
            # Check for a larger digit to swap
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    # Swap and return the new number
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int(''.join(num_list))
        
        # If no swap occurred, return the original number
        return num
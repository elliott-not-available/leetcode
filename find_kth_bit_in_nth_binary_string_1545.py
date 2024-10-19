# find_kth_bit_in_nth_binary_string
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/?envType=daily-question&envId=2024-10-19

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        initial = "0"

        def invert(s: str) -> str:
            new_s = ""
            for c in s:
                if c == "0":
                    new_s += "1"
                else:
                    new_s += "0"
            return new_s
        
        cur_string = initial
        while len(cur_string) < k:
        # for _ in range(2, n+1):
            cur_string = cur_string + "1" + invert(cur_string)[::-1]
        
        return cur_string[k-1]


class Solution_r:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n - 1

        def recur(length, k):
            if length ==1:
                return "0"
            
            mid = length//2
            if k <= mid:
                return recur(mid, k)
            elif k > mid + 1:
                result = recur(mid, length - k + 1)
                return "0" if result == "1" else "1"
            else:
                return "1"
        
        return recur(length, k)

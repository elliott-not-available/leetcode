class Solution:
    def concatenatedBinary(self, n: int) -> int:
        store = ""

        for i in range(1, n+1):
            store += bin(i)[2:]
        
        return int(store, 2)
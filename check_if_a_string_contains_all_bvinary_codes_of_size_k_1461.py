# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/?envType=daily-question&envId=2026-02-23

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()

        for i in range(len(s)-k+1):
            st.add(s[i:i+k])
        return len(st) == 2**k
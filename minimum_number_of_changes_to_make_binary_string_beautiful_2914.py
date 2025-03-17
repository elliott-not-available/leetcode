# minimum_number_of_changes_to_make_binary_string_beautiful_2914
# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/?envType=daily-question&envId=2024-11-05

class Solution:
    def minChanges(self, s: str) -> int:
        chunks = [s[i:i+2] for i in range(0,len(s), 2)]
        beaut = 0 
        mix = 0
        for chunk in chunks:
            if chunk[0] == chunk[1]:
                beaut += 1
            else:
                mix += 1
        
        return mix
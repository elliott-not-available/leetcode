# string_compression_3_3163
# https://leetcode.com/problems/string-compression-iii/description/?envType=daily-question&envId=2024-11-04

class Solution:
    def compressedString(self, word: str) -> str:
        
        comp = ""
        count = [word[0], 1]

        for c in word[1:]:
            if count[1] == 9:
                comp += "9" + count[0]
                count = [c, 1]
            elif count[0] == c:
                count[1] = count[1] + 1
            else:
                comp += str(count[1]) + count[0]
                count = [c, 1]

        comp += str(count[1]) + count[0]

        return comp
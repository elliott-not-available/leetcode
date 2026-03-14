# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=daily-question&envId=2026-03-14

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        current_string = ""
        happy_strings = []
        self.generate_happy_strings(n, current_string, happy_strings)

        if len(happy_strings) < k:
            return ""
        
        return happy_strings[k-1]
    
    def generate_happy_strings(self, n, current_string, happy_strings):
        if len(current_string) == n:
            happy_strings.append(current_string)
            return
        
        for c in ["a", "b", "c"]:
            if len(current_string) > 0 and current_string[-1] == c:
                continue

            self.generate_happy_strings(n, current_string + c, happy_strings)
# split_string_into_max_number_of_unique_substrings_1593
# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/?envType=daily-question&envId=2024-10-21

class Solution_og_no_work:
    def maxUniqueSplit(self, s: str) -> int:

        i = 0
        j = 1
        current = []
        print(s)
        while j <= len(s):
            
            if s[i:j] not in current:
                current.append(s[i:j])
                print(i, j, s[i:j], len(current))
                i += len(s[i:j])
                j = i + 1
            else:
                j += 1

        return len(current)
    
class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def dfs(i, current_set):
            if i == len(s):
                return 0
            
            result = 0
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr in current_set:
                    continue
                current_set.add(substr)
                result = max(result, 1 + dfs(j+1, current_set))
                current_set.remove(substr)
            return result
        
        return dfs(0, set())
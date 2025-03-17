# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description/?envType=daily-question&envId=2025-02-16

class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        # brute force is 0(n**2) -> can greedy for sure
        # suggests heurist? algorith
        N = 2*n -1
        res = [0] * N

        # hm  for used? min heap?
        used = set()

        def backtrack(i):
            if i == len(res):
                return True
            
            for num in reversed(range(1,n+1)):
                # validate
                if num in used:
                    continue
                if num > 1 and (i+num >= N or res[i+num]):
                    continue

                # try
                used.add(num)
                res[i] = num
                if num > 1:
                    res[i+num] = num

                j = i+1
                while j < len(res) and res[j]:
                    j += 1

                if backtrack(j):
                    return True
                
                # backtrack
                used.remove(num)
                res[i] = 0
                if num > 1:
                    res[i+num] = 0

            return False

        backtrack(0)
        return res

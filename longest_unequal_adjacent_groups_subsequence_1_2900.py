# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/?envType=daily-question&envId=2025-05-15

class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        # # brute force: O(n**2) - only just passes
        # N = len(words)
        # i = 0
        # j = 1
        # cur = [i]
        # max_s = [i]

        # while i < N:
        #     if i == N-1:
        #         break

        #     if j == N:
        #         if len(cur) > len(max_s):
        #             max_s = cur
        #         i += 1
        #         j = i + 1
        #         cur = [i]
        #         continue
        #     print(f"{i}, {j}")

        #     if groups[cur[-1]] != groups[j]:
        #         cur.append(j)
        #         if len(cur) > len(max_s):
        #             max_s = cur
        #         print(f"update: {max_s}")
        #     j += 1

        # return [words[i] for i in max_s]
        #########################################################
        # greedy approach

        # chose first item which is alternate to current:
        N = len(words)
        if N == 1:
            return words

        res = [words[0]] + [words[i] for i in range(1,N) if groups[i] != groups[i-1]]
        return res
        #########################################################
        # # memo
        # N = len(words)

        # if N == 1:
        #     return words
        
        # dm = {
        #     0: (groups[0], [words[0]])
        # }
        # for i in range(1, N):
        #     g, l = dm[i-1]
        #     if groups[i] != g:
        #         dm[i] = (groups[i], l + [words[i]])
        #     else:
        #         dm[i] = (g, l)

        # return dm[N-1][1]
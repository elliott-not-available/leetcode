from longest_square_streak_in_array_2501 import Solution
from _testing_functions import print_first_row, print_row
inp1 = [4,3,6,16,8,2]
exp1 = 3

inp2 = [2,3,5,6,7]
exp2 = -1

inps = [inp1,inp2]
exps = [exp1,exp2]
outs = []

for inp in inps:
    out = Solution().longestSquareStreak(inp)
    outs.append(out)

print_first_row(["input", "output", "expected"], 20)
for i, o, e in zip(inps, outs, exps):
    print_row([i, o, e], 20)
# print_row([inps, outs, exps], 20)
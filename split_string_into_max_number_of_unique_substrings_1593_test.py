from split_string_into_max_number_of_unique_substrings_1593 import Solution
from _testing_functions import print_row, print_first_row


inp1 = "ababccc"
inp2 = "aba"
inp3 = "aa"
inp4 = "hq"
inp5 = "wwwzfvedwfvhsww"

# out = Solution().maxUniqueSplit(inp5)

inps = [inp1,inp2,inp3, inp4, inp5]
exp = [5,2,1,2,11]

print_first_row(["input", "output", "expected"])

for i, e in zip(inps, exp):
    out = Solution().maxUniqueSplit(i)
    print_row([i, out, e])
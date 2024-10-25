from _testing_functions import print_first_row, print_row
from remove_sub_folders_from_the_filesystem_1233 import Solution

inp1 = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
inp2 = ["/a","/a/b/c","/a/b/d"]
inp3 = ["/a/b/c","/a/b/ca","/a/b/d"]
inp4 = ["/ah/al/am","/ah/al"]

exp1 = ["/a","/c/d","/c/f"]
exp2 = ["/a"]
exp3 = ["/a/b/c","/a/b/ca","/a/b/d"]
exp4 = ['/ah/al']

exps = [exp1,exp2,exp3,exp4]
inps = [inp1,inp2,inp3,inp4]

outs = []

# o = Solution().removeSubfolders(inp4)
# print(o)

for inp in inps:
    out = Solution().removeSubfolders(inp)
    outs.append(out)

print_first_row(["input", "output", "expected"], 40)
for i, o, e in zip(inps, outs, exps):
    print_row([i, o, e],40)
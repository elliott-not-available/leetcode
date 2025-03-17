from height_of_binary_tree_after_subtree_removal_queries_2458 import Solution
from _testing_functions import build_tree_from_list, print_first_row, print_row

null = None

inp1_tree = [1,3,4,2,null,6,5,null,null,null,null,null,7]
inp1_query = [4]
inp2_tree = [5,8,9,2,1,3,7,4,6]
inp2_query = [3,2,4,8]

inps_tree = [inp1_tree, inp2_tree]
inps_query = [inp1_query, inp2_query]

exp1 = [2]
exp2 = [3,2,4,2]

expected = [exp1, exp2]

outs = []


for tree, query in zip(inps_tree, inps_query):
    root = build_tree_from_list(tree)
    out = Solution().treeQueries(root, query)
    outs.append(out)

print_first_row(["input", "output", "expected", "PASS"], 40)
for i, o, e in zip(inps_query, outs, expected):
    p = (o == e)
    print_row([i, o, e, p], 40)

from minimum_number_of_swaps_to_make_the_string_balanced_1963 import Solution

inp1 = "][]["
inp2 = "]]][[["
inp3 = "[]"

exp1 = 1
exp2 = 2
exp3 = 0

out1 = Solution().minSwaps(inp1)
out2 = Solution().minSwaps(inp2)
out3 = Solution().minSwaps(inp3)


inps = [inp1,inp2,inp3]
exps = [exp1,exp2,exp3]

# this can be expanded to take any number of inputs dynamically
def print_columns(col1, col2, col3, col4) -> None:
    col_width = 20
    print(f"{col1:<{col_width}}| {col2:^{col_width}}| {col3:^{col_width}}| {col4:{col_width}}")
    print(f"{'':-<{col_width*4}}")

def print_test_results(col1, col2, col3, col4) -> None:
    col_width = 20
    print(f"{col1:<{col_width}}| {col2:^{col_width}}| {col3:^{col_width}}| {col4:^{col_width}}")

print_test_results("Input", "Output", "Expected", "Passed")
print(f"{'':-<80}")

for i in range(len(inps)):

    out = Solution().minSwaps(inps[i])
    print_test_results(inps[i], out, exps[i], out==exps[i])



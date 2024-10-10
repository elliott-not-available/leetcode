from maximum_width_ramp_962 import Solution

inp1 = [6,0,8,2,1,5]
inp2 = [9,8,1,0,1,9,4,0,4,1]
inp3 = [10, 9, 10 , 0, 1, 1, 1, 1, 1, 1, 2, 3]

exp1 = 4
exp2 = 7
exp3 = 8

print(inp1)
out1 = Solution().maxWidthRamp(inp1)
print(inp2)
out2 = Solution().maxWidthRamp(inp2)
print(inp3)
out3 = Solution().maxWidthRamp(inp3)

print(f"output: {out1} expected: {exp1}")
print(f"output: {out2} expected: {exp2}")
print(f"output: {out3} expected: {exp3}")
from make_sum_divisible_by_p_1590 import Solution

def result_message(inp: list[int], p: int,  outp: int, exp: int):
    return f"{inp}, [{p}]", f"{outp} it should be {exp}", outp==exp

def print_message(msg: list) -> None:
    print(f"{msg[0]:<80} {msg[1]:^20} {msg[2]:>20}")

print(f"{"input":^80} {"output":^20} {"pass":>20}")

inp1 = [1,2,3]
p1 = 6
exp1 = 0
output1 = Solution().minSubarray(inp1, p1)
msg = result_message(inp1,p1,output1,exp1)
print_message(msg)

inp2 = inp1
p2 = 3
exp2 = 0
output2 = Solution().minSubarray(inp2, p2)
msg = result_message(inp2,p2,output2,exp2)
print_message(msg)

inp3 = [6,3,5,2]
p3 = 9
exp3 = 2
output3 = Solution().minSubarray(inp3, p3)
msg = result_message(inp3,p3,output3,exp3)
print_message(msg)

inp4 = [3,1,4,2]
p4 = 6
exp4 = 1
output4 = Solution().minSubarray(inp4, p4)
msg = result_message(inp4,p4,output4,exp4)
print_message(msg)

inp5 = [4,4,2]
p5 = 7
exp5 = -1
output5 = Solution().minSubarray(inp5, p5)
msg = result_message(inp5,p5,output5,exp5)
print_message(msg)

inp6 = [26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3]
p6 = 26
exp6 = 3
output6 = Solution().minSubarray(inp6, p6)
msg = result_message(inp6,p6,output6,exp6)
print_message(msg)

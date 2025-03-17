from parsing_a_boolean_expression_1106 import Solution
from _testing_functions import print_first_row, print_row

inp1 = "&(|(f))"
inp2 = "|(f,f,f,t)"
inp3 = "!(&(f,t))"
inp4 = "&(t,|(f,f,t),!(f))"

inps = [inp1,inp2,inp3,inp4]
outs = []

for i in inps:
    outs.append(Solution().parseBoolExpr(i))

print_first_row(["input", "output"])
for inp, out in zip(inps, outs):
    print_row([inp, out])

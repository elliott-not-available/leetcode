from maximum_swap_670 import Solution
from typing import Any

inp1 = 2736
out1 = Solution().maximumSwap(num=inp1)

inp2 = 98368
out2 = Solution().maximumSwap(num=inp2)


def print_columns(cols: list[Any], width: int = 20) -> None:
    # center aligned
    col_width = width
    out_str = ""

    for col in cols:
        out_str += f"{col:^{col_width}} | "

    print(out_str[:-3])


print_columns(["input", "output"], 10)
print("-"*25)
print_columns([inp1, out1], 10)
print_columns([inp2, out2], 10)
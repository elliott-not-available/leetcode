from typing import Any

def print_column(cols: list[Any], width: int = 20) -> None:
    # center aligned
    col_width = width
    out_str = ""

    for col in cols:
        col = str(col)
        out_str += f"{col:^{col_width}} | "

    print(out_str[:-3])

def print_first_row(cols: list[Any], width: int = 20) -> None:
    # center aligned
    col_width = width
    out_str = ""

    for col in cols:
        col = str(col)
        out_str += f"{col:^{col_width}} | "

    print(out_str[:-3])
    print("-"*(width*len(cols)))
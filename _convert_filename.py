#! python
import sys

input_list = sys.argv
number, title = "_".join(input_list[1:]).lower().split(".")
title = title[1:]
print(title.strip() + "_" + number)
# print("_".join(input_list[1:]).lower().split("."))
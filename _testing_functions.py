from typing import Any

def print_row(cols: list[Any], width: int = 20) -> None:
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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(vals: list[int]):
    invalid_terms = [None, "null"]
    root = TreeNode(vals[0])
    tree = [root]
    
    for i, v in enumerate(vals):
        if i == 0:
            continue

        j = (i - 1) // 2 # parent index
        # print(i, j, v)
        if (i % 2 == 1) & (v not in invalid_terms): # left child
            tree[j].left = TreeNode(val=v)
            tree.append(tree[j].left)
        elif (i % 2 == 0) & (v not in invalid_terms): # right child
            tree[j].right = TreeNode(val=v)
            tree.append(tree[j].right)

    # for n in tree:
    #     print(n.val)

    return root

test = [5,8,9,2,1,3,7,4,6]

root = build_tree_from_list(test)

print(root.val, root.left.val, root.right.val)


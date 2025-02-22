# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/?envType=daily-question&envId=2025-02-22
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution_og:
    # wrong output
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # list of layers
        # traverse string and fill in layers

        lol = []
        lol.append([1])
        depth = 0
        cur = ""
        layer_index = {} # layer, current ind


        for c in traversal[1:]:
            if c == "-":
                if cur:
                    lol[depth][layer_index[depth]] = int(cur)
                    layer_index[depth] += 1
                    cur = ""
                    depth = 0
                    
                    
                depth +=1
                if len(lol) < depth + 1:
                        lol.append([None]*(2**depth))
                        layer_index[depth] = 0
            else:
                cur += c

        lol[depth][layer_index[depth]] = int(cur)

        res = []
        for l in lol:
            for v in l:
                res.append(v)

        # ah i missunderstood question, it wants a tree

        # this would probably be better with something recursive

        # def build_tree_from_list(vals: list[int]):
        #     invalid_terms = [None, "null"]
        #     root = TreeNode(vals[0])
        #     tree = [root]
            
        #     for i, v in enumerate(vals):
        #         if i == 0:
        #             continue

        #         j = (i - 1) // 2 # parent index
        #         # print(i, j, v)
        #         if (i % 2 == 1) & (v not in invalid_terms): # left child
        #             tree[j].left = TreeNode(val=v)
        #             tree.append(tree[j].left)
        #         elif (i % 2 == 0) & (v not in invalid_terms): # right child
        #             tree[j].right = TreeNode(val=v)
        #             tree.append(tree[j].right)

        #     # for n in tree:
        #     #     print(n.val)

        #     return root

        # the indexing is a bit off, my logic is flawed in layer_index = {} # layer, current ind
        # return build_tree_from_list(vals=res)
        return res
    

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:


        # if more dashes than current go deeper, same = same level, less = back to start
        stack = []
        dashes = 0
        i = 0

        def add_to_node(parent: TreeNode, child: TreeNode):
            if parent.left:
                parent.right = child
            else:
                parent.left = child

        while i < len(traversal):
            if traversal[i] == "-":
                dashes += 1
                i += 1
            else:
                j = i
                while j < len(traversal) and traversal[j] != "-":
                    j += 1
                val = int(traversal[i:j])

                node = TreeNode(val=val)

                while len(stack) > dashes:
                    stack.pop()
                    
                if stack:
                    add_to_node(stack[-1], node)

                stack.append(node)
                i = j
                dashes = 0
        return stack[0]





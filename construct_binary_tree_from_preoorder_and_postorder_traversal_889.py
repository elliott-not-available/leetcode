# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/?envType=daily-question&envId=2025-02-23

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# did not work atall, idk why. apparently typeerror treenode not treenode
# TypeError: <__main__.TreeNode object at 0x7fed07b65610> is not valid value for the expected return type TreeNode
# class Solution:
#     def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:

#         def build_tree_from_list(vals: list[int]) -> TreeNode:
#             invalid_terms = [None, "null"]
#             root = TreeNode(val=vals[0])
#             tree = [root]
            
#             for i, v in enumerate(vals):
#                 if i == 0:
#                     continue

#                 j = (i - 1) // 2 # parent index
#                 # print(i, j, v)
#                 if (i % 2 == 1) & (v not in invalid_terms): # left child
#                     tree[j].left = TreeNode(val=v)
#                     tree.append(tree[j].left)
#                 elif (i % 2 == 0) & (v not in invalid_terms): # right child
#                     tree[j].right = TreeNode(val=v)
#                     tree.append(tree[j].right)

#             # for n in tree:
#             #     print(n.val)

#             return root

#         root = build_tree_from_list(preorder)

#         print(root)
#         return root


class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        N = len(postorder)
        post_val_to_idx = {} # val -> ind

        for i, n in enumerate(postorder):
            post_val_to_idx[n] = i

        def build(i1, i2, j1):

            if i1 > i2:
                return None
            
            root = TreeNode(preorder[i])

            if i1 != i2:
                left_val = preorder[i1+1]

                mid = post_val_to_idx[left_val]

                left_size = mid - j1 + 1

                root.left = build(i1+1, i1 + left_size, j1)
                root.right = build(i1 + left_size + 1, i2, mid + 1)


            return root

        return build(0, N - 1, 0)
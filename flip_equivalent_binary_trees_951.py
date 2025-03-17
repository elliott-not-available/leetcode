# flip_equivalent_binary_trees_951
# https://leetcode.com/problems/flip-equivalent-binary-trees/
from typing import Optional
from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # check contents match for each layer
        # def get_layer_contents(node: TreeNode, layer_contents: dict[int, list[int]], layer: int):

        #     if node.left:
        #         if layer not in layer_contents:
        #             layer_contents[layer] = [node.left.val]
        #         else:
        #             layer_contents[layer].append(node.left.val)
        #         get_layer_contents(node.left, layer_contents, layer+1)
        #     if node.right:
        #         if layer not in layer_contents:
        #             layer_contents[layer] = [node.right.val]
        #         else:
        #             layer_contents[layer].append(node.right.val)
        #         get_layer_contents(node.right, layer_contents, layer+1)

        # get_layer_contents(root1, layer_contents_1, 1)
        # get_layer_contents(root2, layer_contents_2, 1)
        # root1_layers = layer_contents_1.keys()
        # root2_layers = layer_contents_2.keys()

        # if Counter(root1_layers) != Counter(root2_layers):
        #     return False

        # for layer in root1_layers:
        #     if Counter(layer_contents_1[layer]) != Counter(layer_contents_2[layer]):
        #         return False

        keep_track = True
        def check_child_contents(node1: TreeNode, node2: TreeNode):
            nonlocal keep_track

            if not node1 and not node2:
                return True
            if not node1 or not node2:
                keep_track = False
                return False
            
            node1_children = [node1.left.val if node1.left else None, node1.right.val if node1.right else None]
            node2_children = [node2.left.val if node2.left else None, node2.right.val if node2.right else None]
            
            print(Counter(node1_children), Counter(node2_children))
            if Counter(node1_children) != Counter(node2_children):
                print("returning false: counter no match")
                keep_track = False
                return False
            
            # can assume children match
            if (node1.left.val if node1.left else None) == (node2.left.val if node2.left else None):
                check_child_contents(node1.left, node2.left)
            if (node1.right.val if node1.right else None) == (node2.right.val if node2.right else None):
                check_child_contents(node1.right, node2.right)
            if (node1.left.val if node1.left else None) == (node2.right.val if node2.right else None):
                check_child_contents(node1.left, node2.right)
            if (node1.right.val if node1.right else None) == (node2.left.val if node2.left else None):
                check_child_contents(node1.right, node2.left)

            return True
        
        if not root1 and not root2:
            return keep_track
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        
        check_child_contents(root1, root2)

        return keep_track
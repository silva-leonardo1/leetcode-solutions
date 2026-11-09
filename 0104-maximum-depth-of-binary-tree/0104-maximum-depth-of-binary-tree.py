# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: TreeNode | None) -> int:
        return self.height(root)

    def height(self, node: TreeNode | None) -> int:
        if node is None:
            return 0

        height_left = self.height(node.left)
        height_right = self.height(node.right)
        return 1 + max(height_left, height_right)

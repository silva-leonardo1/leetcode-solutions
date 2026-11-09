# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        if root is None:
            return []

        dq = deque([root])
        res = []
        zigzag = True

        while dq:
            temp = []
            for _ in range(len(dq)):
                node = dq.popleft()
                temp.append(node.val)
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            if zigzag:
                res.append(temp)
            else:
                temp.reverse()
                res.append(temp)
            zigzag = not zigzag
        return res

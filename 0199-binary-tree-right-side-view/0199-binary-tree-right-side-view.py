# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        from collections import deque
        if root is None:
            return []
        dq = deque([root])
        ans = [root.val]
        temp = root

        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left is not None:
                    dq.append(node.left)
                    temp = node.left
                if node.right is not None:
                    dq.append(node.right)
                    temp = node.right
            ans.append(temp.val)
        ans.pop()
        return ans



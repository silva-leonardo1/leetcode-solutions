# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}

        curr = head
        indx = 0
        while curr is not None:
            seen[curr] = indx
            curr = curr.next
            if curr in seen:
                return True
            indx += 1
        return False
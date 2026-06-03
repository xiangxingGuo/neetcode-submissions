# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            # 1. save the next
            nxt = curr.next

            # 2. reverse the current node's next
            curr.next = prev
            # 3. move previous node
            prev = curr

            # 4. move current node
            curr = nxt

        return prev
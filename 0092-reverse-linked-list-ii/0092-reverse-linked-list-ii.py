# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        dummy = pre = ListNode(0)
        dummy.next = head
        for i in range(left - 1):
            pre = pre.next
        
        cur = pre.next
        nxt = cur.next
        
        for i in range(right - left):
            tmp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = tmp
        
        pre.next.next = nxt
        pre.next = cur
        return dummy.next
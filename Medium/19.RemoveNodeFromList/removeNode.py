# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    index=0

    def removeNthFromEndHelper(self, head: ListNode) -> ListNode:
        if head.next:
            self.removeNthFromEndHelper(head.next)
            self.index-=1
        if self.index==0:
            head.next = head.next.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        self.index=n
        Originalhead= head
        self.removeNthFromEndHelper(head)
        if self.index>0:
            return Originalhead.next
        return Originalhead





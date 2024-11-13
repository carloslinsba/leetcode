# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def hasCycleHelper(self, head: Optional[ListNode], fast: Optional[ListNode]) -> bool:
        if head == fast:
            return True
        if not head.next:
            return False
        if fast and fast.next and fast.next.next:
            return self.hasCycleHelper(head.next, fast.next.next )
        return self.hasCycleHelper(head.next, None)
        

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head.next and head.next.next:
            return self.hasCycleHelper(head, head.next.next)
        return self.hasCycleHelper(head, None)
        

        #done
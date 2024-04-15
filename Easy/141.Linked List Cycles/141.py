# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:

    dic = {}

    def hasCycleHelper(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        while (not head.next is None):
            if head.val in self.dic:
                return True
            self.dic[head.val] = 1
            self.hasCycleHelper(head.next)
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        self.dic = {}
        return self.hasCycleHelper(head)
        
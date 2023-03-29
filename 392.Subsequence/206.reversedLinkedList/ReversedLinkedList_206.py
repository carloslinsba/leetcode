# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:        
    new_head = ListNode()
    def reverseList2(self, current, prior):
        if current.next:
            self.reverseList2(current.next, current)
        if current.next is None:
            self.new_head = current
        current.next = prior
        return
    
    def reverseList(self, head:ListNode) -> ListNode:
        if head is None:
            return None
        if head.next:
            self.reverseList2(head.next, head)
            head.next = None
        else:
            return head
        return self.new_head

    def printing(self, ln:ListNode()):
        print(ln.val)
        if ln.next:
            self.printing(ln.next)


s= Solution()
#s.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
s.reverseList(ListNode(1))
print("value:")
s.printing(s.new_head)



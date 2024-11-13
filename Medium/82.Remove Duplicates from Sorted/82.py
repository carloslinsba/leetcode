# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    previousNonDuplicate = None

    def deleteDuplicatesHelper(self, head: Optional[ListNode], next1:  Optional[ListNode], previous:Optional[ListNode], duplicate:Optional[bool] ) -> Optional[ListNode]:
        if not next1:
            if duplicate:
                previous.next = None 
            return
        if head.val != next1.val:
            if duplicate:
                previous.next = next1
                return self.deleteDuplicatesHelper(head= previous.next, next1= next1.next,duplicate= False, previous = previous)
            head.next = next1
            return self.deleteDuplicatesHelper(head.next, next1.next, head, False)
        else:
            return self.deleteDuplicatesHelper(head, next1.next, previous, True)
            
        
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if not head or not head.next:
            return head
        if head.val != head.next.val:
            self.deleteDuplicatesHelper(previous = head, head = head.next, next1 = head.next.next, duplicate= False)
        else:
            while head.val == head.next.val:
                head= head.next
                if not head.next:
                    return None
            return self.deleteDuplicates(head.next)
        return head


#done
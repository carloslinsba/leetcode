# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    head = ListNode()
    def mergeTwoListsHelper(self,list1, list2, head):
        if not list1:
            head.next = list2
            return
        if not list2:
            head.next = list1
            return
        
        if list1.val <= list2.val:
            head.next = list1
            self.mergeTwoListsHelper(list1.next, list2, head.next)
        else:
            head.next = list2
            self.mergeTwoListsHelper(list1, list2.next, head.next)



    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            self.head =list1
            self.mergeTwoListsHelper(list1.next, list2, self.head)
        else:
            self.head = list2
            self.mergeTwoListsHelper(list2.next, list1, self.head)

        return self.head
        
            
            
#done
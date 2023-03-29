# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
        
    def checkAndUpdate(self, list1:ListNode = None, list2:ListNode = None,newlist: ListNode = None):
        if (list1 is None):
            newlist.val= list2.val
            newlist.next= list2.next
            return
        if (list2 is None):
            newlist.val = list1.val
            newlist.next= list1.next
            return

        if (list1.val <= list2.val):
            newlist.val = list1.val
            list1 = list1.next
            newlist.next = ListNode()
        else:
            newlist.val = list2.val
            list2 = list2.next
            newlist.next = ListNode()
        self.checkAndUpdate(list1, list2, newlist.next)
    
    def mergeTwoLists(self, list1: ListNode, list2:ListNode) -> ListNode:
        if (list1 is None and list2 is None):
            return None
        newlist = ListNode()
        self.newlistHeader = newlist
        self.checkAndUpdate(list1, list2, newlist)
        return self.newlistHeader

s= Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
s.mergeTwoLists(list1, list2)


        
        

        

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoListsHelper2(self, list1: ListNode, list2: ListNode, currentList: ListNode):

        if not list1 or not list2:
            if not list1 and not list2:
                return None
            if not list1 :
                currentList.val = list2.val
                currentList.next = list2.next
                return
            else:
                currentList.val = list1.val
                currentList.next = list1.next
                return

        if list1.val <= list2.val:
            currentList.val = list1.val
            list1 = list1.next
        else:
            currentList.val = list2.val
            list2 = list2.next
        currentList.next = ListNode()
        self.mergeTwoListsHelper(list1, list2, currentList.next)

def mergeTwoLists2(self, list1: ListNode, list2: ListNode)-> ListNode:
    newList= ListNode()
    if not list1 and not list2:
                return None
    self.mergeTwoListsHelper(list1, list2, newList)
    return newList

        
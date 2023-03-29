# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoListsHelper(self, list1: ListNode, list2: ListNode, currentList: ListNode):

        while (list1 or list2):

            if not list1 or not list2:
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
            currentList= currentList.next
            

    def mergeTwoLists(self, list1: ListNode, list2: ListNode)-> ListNode:
        newList= ListNode()
        if not list1 and not list2:
                    return None
        self.mergeTwoListsHelper(list1, list2, newList)
        return newList

    def mergeKLists(self, lists: list[ListNode]) -> Optional[ListNode]:
        lsts_to_merge= []

        if len(lists)==1:
            return lists[0]
        if not lists:
            return None
        
        while(len(lists) > 1):
            for i in range(len(lists)-1,0,-2):
                lsts_to_merge.append(self.mergeTwoLists(lists[i], lists[i-1]))
            if len(lists)%2==1:
                lsts_to_merge.append(lists[0])
            lists = lsts_to_merge
            lsts_to_merge=[]
            
        return lists[0]
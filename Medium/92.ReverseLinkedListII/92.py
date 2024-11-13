# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    nextNode = ListNode()
    def reverseBetweenHelper(self,head, previous, count):
        if count <=0:
            self.nextNode = head.next
            head.next = None
            return
        if head.next:
            self.reverseBetweenHelper(head.next, head, count-1)
        head.next = previous
        return head

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left ==right:
            return head
        self.nextNode = None
        count=1
        current = head
        previous = None
        before = None
        while count <left:
            count+=1
            before = previous
            previous=current
            current=current.next
            
        previous.next = self.reverseBetweenHelper(current,previous, right-count ) #3

        count = right-left
        while count>0:
            current =current.next
            count -=1
        current.next = self.nextNode
        return head


        #verify edge case - left = starting pos
        #verify edge case right = ending pos - probably ok.

        


    # def reverseBetweenHelper(previous, right):
    #     count =0 
    #     while count< right:
    #         count+=1

    #         #getting the nodes
    #         current = previous.next
    #         next1 = current.next
    #         #reversing it
    #         next1.next = current
    #         current.next = previous
    #     pass

    

# not done.
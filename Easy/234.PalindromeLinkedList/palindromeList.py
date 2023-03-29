# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    count = 0
    def isPalindromeHelper(self, head:ListNode):
        self.count+=1
        if head.next:
            if not self.isPalindromeHelper(head.next):
                return False
        if head.val != self.originalHead.val:
            return False
        self.originalHead = self.originalHead.next
        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.count=0
        self.originalHead = head
        if self.isPalindromeHelper(head):
            return True
        return False


s = Solution()


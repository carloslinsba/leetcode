class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        current = head
        node_list = []
        if head is None:
            return None
        if not head.next:
            return None
        while current.next:
            node_list.append(current)
            if current.next in node_list:
                return current.next
            current= current.next
        return None

s = Solution()
print(s.detectCycle(None))
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = []
        q2 = []
        def connectHelper(root, depth):
            if not root:
                return
            if depth in q:
                i = q.index(depth)
                q2[i].next = root
                q.pop(i)
                q2.pop(i)
                q.append(depth)
                q2.append(root)
            else:
                q.append(depth)
                q2.append(root)
            connectHelper(root.left, depth+1)
            connectHelper(root.right, depth+1)
        connectHelper(root,0)
        return root


#time complexity: O(n)
#space complexity: O(n)



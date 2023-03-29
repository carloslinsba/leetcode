# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    lstNumber1=list()
    lstNumber2=list()

    def getNumber(self,head: ListNode, lstNumber):
        lstNumber.insert(0, head.val)
        if head.next:
            self.getNumber(head.next, lstNumber)
    
    
    
    def storeNumber(self, s:str)->ListNode: #807
        
        head = ListNode(s[len(s)-1], None)
        originalHead = head
        
        for i in range(len(s)-2, -1, -1):
            head.next = ListNode(s[i], None)
            head = head.next
        return originalHead



    def addTwoNumbers(self, l1: ListNode, l2:ListNode) -> ListNode:
        self.lstNumber1 =[]
        self.lstNumber2=[]
        if l1 is None:
            self.lstNumber1=[0]
        if l2 is None:
            self.lstNumber2=[0]
        
        self.getNumber(l1, self.lstNumber1)
        self.getNumber(l2, self.lstNumber2)

        s1 = str()
        s2 = str()
        for item in self.lstNumber1:
            s1+= str(item)
        
        for item in self.lstNumber2:
            s2+= str(item)

        sum= int (s1) + int(s2)
        
        return self.storeNumber(str(sum))


        
    


        
    
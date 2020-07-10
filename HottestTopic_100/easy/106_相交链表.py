# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha=headA
        hb=headB

        while ha!=hb:
            ha=ha.next if ha else headB
            hb=hb.next if hb else headA
        return ha
    def printf(self,head):
        while head:
            print(head.val,end=' ')
            head=head.next
        print()
    def generate(self,lis):
        p=head=ListNode(-1)
        for x in lis:
            p.next=ListNode(x)
            p=p.next
        return head.next
sol=Solution()
x1=sol.generate([4,1,8,4,5])
x2=sol.generate([5,0,1,8,4,5])
sol.printf(x1)
sol.printf(x2)
sol.printf(sol.getIntersectionNode(x1,x2))

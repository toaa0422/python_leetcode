class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
def generateList(lis):
    last=pre=ListNode(-1)
    for x in lis:
        last.next=ListNode(x)
        last=last.next
    return pre.next
def printList(l):
    while l:
        print(l.val,end=' ')
        l=l.next
    print(' ')

#recursion
class Solution():
    def mergeTwoLists(self,l1,l2):
        if not l1:return l2
        elif not l2:return l1
        elif l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2
#iteration
class Solution_():
    def mergeTwoLists(self,l1,l2):
        pre=head=ListNode(-1)
        while l1 and l2:
            if l1.val<l2.val:
                pre.next=l1
                l1=l1.next
            else:
                pre.next=l2
                l2=l2.next
            pre=pre.next

        pre.next=l1 if l1 else l2
        return head.next

sol=Solution_()
l1=[1,2,3]
l2=[1,3,4]
l1=generateList(l1)
l2=generateList(l2)
printList(l1)
printList(l2)
print(printList(sol.mergeTwoLists(l1,l2)))

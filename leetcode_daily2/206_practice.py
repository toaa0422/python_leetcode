class ListNode():
    def __init__(self,x):
        self.val=x
        self.next=None
def reverse(head):
    pre=None
    cur=head
    while cur:
        nxt=cur.next
        cur.next=pre
        pre=cur
        cur=nxt
    return pre
def reverse_(head):
    if not head or not head.next:return head
    p=reverse_(head.next)
    head.next.next=head
    head.next=None
    return p
def generateList(lis):
    p=head=ListNode(-1)
    for val in lis:
        head.next=ListNode(val)
        head=head.next
    return p.next
def printList(head):
    while head:
        print(head.val,end=' ')
        head=head.next
    print('')
x=generateList([1,2,2,3,4])
printList(x)
printList(reverse_(x))


class ListNode():
    def __init__(self,x):
        self.val=x
        self.next=None
def generateList(l: list) -> ListNode:
    prenode = ListNode(None)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next
def printList(l: ListNode):
    while l:
        print(l.val, end=' ')
        l = l.next
    print('')

def swapPairs(head):
    if not head or not head.next:
        return head
    nxt=head.next
    head.next=swapPairs(head.next.next)  #区分 nxt.head  与 head.next.next
    nxt.next=head
    return nxt

def swapPairs_(head):
    if not (head or head.next):
        return head
    pre=ListNode(-1)
    pre.next=head
    cur=pre
    while cur.next and cur.next.next:
        first,second=cur.next,cur.next.next
        cur.next = second
        first.next=second.next
        second.next=first
        cur=cur.next.next
    return pre.next

if __name__ == "__main__":
    #l1 = generateList([1, 5, 8])
    #l2 = generateList([9, 1, 2, 9])
    l1 = generateList([3,4])
    printList(l1)
    #x=swapPairs(l1)
    #printList(x)
    printList(swapPairs_(l1))



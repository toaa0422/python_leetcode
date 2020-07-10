def middleNode(head):
    cur=head
    count=0
    while cur:
        count+=1
        cur=cur.next
    i=0
    cur=head
    while i<count//2:
        i+=1
        cur=cur.next

    return cur
#快慢指针
#数组   append
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


if __name__ == "__main__":
    #l1 = generateList([1, 5, 8])
    #l2 = generateList([9, 1, 2, 9])
    l1 = generateList([3,4,2])
    printList(l1)
    printList(middleNode(l1))



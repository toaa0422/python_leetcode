# rotate 旋转,使循环 v
def rotateRight(head,k):
    if not head:
        return head
    p=head
    count=0
    while p:
        count+=1
        p=p.next
    k = k % count  #####取模技巧
    if k==0:
        return head
    pre,post=head,head
    for i in range(k):
        post=post.next
    while post.next:
        pre=pre.next
        post=post.next
    tmp=pre.next
    pre.next=None
    post.next=head
    return tmp
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
    l1 = generateList([1,2,3,4,5])
    printList(l1)
    printList(rotateRight(l1,2))
    printList(rotateRight(generateList([0,1,2]),4))








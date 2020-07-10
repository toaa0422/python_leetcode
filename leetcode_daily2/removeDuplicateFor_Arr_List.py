#双指针去重技巧
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
def removeDuplicateForList(arr):
    if not arr:
        return 0
    slow=0
    fast=1
    while fast<len(arr):
        if arr[fast]!=arr[slow]:
            slow+=1
            arr[slow]=arr[fast]
        fast+=1
    return slow+1
def removeDuplicateForLinkedList(head):
    #待后续回归改进  20200323
    if not head:
        return head
    slow=head
    fast=head.next
    while fast:
        if fast!=slow:
            slow.next=fast
            slow=slow.next
        fast=fast.next
    slow.next=None
    return slow



print(removeDuplicateForList([0,0,1,2,3]))
head=generateList([0,0,1,2,3])
printList(head)
s=removeDuplicateForLinkedList(head)
printList(s)
"""
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
def removeDuplicate(head):
    if not head:return head
    cur=head
    while cur.next:    #不能是while cur  待回归加强 2020/03/23
        if cur.val==cur.next.val:
            cur.next=cur.next.next
        else:
            cur=cur.next
    return head

head=generateList([0,0,1,2,3])
printList(head)
s=removeDuplicate(head)
printList(s)
"""
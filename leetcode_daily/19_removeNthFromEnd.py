#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def generatelist(lis):
    pnode=ListNode(None)
    phead=pnode
    for i in lis:
        phead.next=ListNode(i)
        phead=phead.next
    return pnode.next
def travel(linklis):
    while linklis:
        print(linklis.val,end=" ")
        linklis=linklis.next
    print("")

def removeNthFromEnd(head,n):
    node=head
    node_no=0
    while node:
        node_no+=1
        node=node.next
    node_no-=n+1
    node= head
    if node_no==-1:
        head=head.next
    else:

        while node_no:
            node = node.next
            node_no -= 1
        node.next = node.next.next
    return head




lis=[x for x in range(1,6)]
lis=generatelist(lis)
print(travel(lis))
l2=removeNthFromEnd(lis,3)
print(travel(l2))

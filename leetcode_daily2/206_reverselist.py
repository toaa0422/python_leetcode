#206 reverselist
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

def reverseList1(head):
    if not head:
        return None
    pre, cur = head, head.next
    while cur:
        # temp 为临时变量 用于保存下一个cur需要更新的节点
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    head.next = None
    return pre
def reverseList2(head):
    if head is None:
        return None
    cur = head
    pre = None
    nxt = cur.next
    while nxt:
        cur.next = pre
        pre = cur
        cur = nxt
        nxt = nxt.next
    cur.next = pre
    head = cur
    return head

#头插法本身就是翻转链表
def reverseList(head: ListNode) -> ListNode:
    pre, cur = None, head
    while cur:
        tmp = cur
        cur  = cur.next
        tmp.next = pre
        pre = tmp
    return pre

#递归解
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nextNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return nextNode
if __name__ == "__main__":
    #l1 = generateList([1, 5, 8])
    #l2 = generateList([9, 1, 2, 9])
    l1 = generateList([3,4,2,8,9])
    printList(l1)
    #printList(reverseList1(l1))
    #printList(reverseList2(l1))
    x=reverseList(l1)
    printList(x)



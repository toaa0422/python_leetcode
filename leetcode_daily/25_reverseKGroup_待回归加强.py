class ListNode():
    def __init__(self,x):
        self.val=x
        self.next=None

def reverseKGroup( head, k: int):
    prehead = ListNode(-1)
    prehead.next = head
    p = prehead

    p_list = [None for _ in range(k)]
    while True:
        # 构建前驱节点
        prenode = p
        # 构建交换节点
        for i in range(k):
            if p == None:
                break
            p = p.next
            p_list[i] = p
        if p == None:
            break
        # 翻转
        prenode.next = p_list[k - 1]
        p_list[0].next = p_list[k - 1].next
        for i in range(k - 1, 0, -1):
            p_list[i].next = p_list[i - 1]
        p = p_list[0]
    return prehead.next


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
    printList(reverseKGroup(l1,2))
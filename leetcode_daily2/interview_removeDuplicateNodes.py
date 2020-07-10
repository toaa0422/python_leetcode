class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicationNodes(self, head):
        if not head: return head
        occurred = {head.val}
        pos = head
        while pos.next:
            cur = pos.next
            if cur.val not in occurred:
                occurred.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next
        return head


class Solution_:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        my_set = {head.val}
        ret = head
        while head.next:
            if head.next.val in my_set:
                head.next = head.next.next
            else:
                my_set.add(head.next.val)
                head = head.next
        return ret


def GenerateList(list):
    head = p = ListNode(-1)
    for x in list:
        head.next = ListNode(x)
        head = head.next
    return p.next


def printf(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print('')


head = GenerateList([1, 2, 3, 3, 2, 1])
printf(head)
sol = Solution()
sol.removeDuplicationNodes(head)
printf(head)

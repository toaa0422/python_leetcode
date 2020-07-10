# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        return node
    def printf(self,head):
        while head:
            print(head.val,end=' ')
            head=head.next
        print(' ')

head=ListNode('a')
head.next=ListNode('b')
head.next.next=ListNode('c')
head.next.next.next=ListNode('d')
head.next.next.next.next=ListNode('e')
head.next.next.next.next.next=ListNode('f')
sol=Solution()
sol.printf(head)
sol.deleteNode(head)
sol.printf(head)

"""
没看懂
"""
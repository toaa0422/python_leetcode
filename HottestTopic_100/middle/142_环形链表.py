# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # hashtable
    def generateList(self,lis):
        head=p=ListNode(-1)
        for x in lis:
            head.next=ListNode(x)
            head=head.next
        return p.next

    def detectCycle(self, head: ListNode) -> ListNode:
        visited=set()
        node=head
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node=node.next
        return None

    # Floyd算法  龟兔赛跑  be  neglected
    def detectCycle_(self, head: ListNode) -> ListNode:
        pass
def printf(self,root):
    print(root.val)
sol=Solution()
head1=[3,2,0,-4]
head2=[1,2]
head3=[1]
print(sol.detectCycle(sol.generateList(head1)))
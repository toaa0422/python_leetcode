class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
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
# 由于链表中从高位到低位存放了数字的二进制表示
# simulate
class Solution_1290:
    def getDecimalValue(self,head):
        cur=head
        ans=0
        while cur:
            ans=ans*2+cur.val
            cur=cur.next
        return ans

head = GenerateList([1,0,1])
printf(head)
sol = Solution_1290()

print(sol.getDecimalValue(head))

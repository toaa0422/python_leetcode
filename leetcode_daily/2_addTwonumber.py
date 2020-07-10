# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# x,y=divmod(12,10)  #返回商和余数  返回除法的结果和余数 返回商和余数
# print(x,y)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prenode = ListNode(None)
        lastnode = prenode
        val = 0
        while val or l1 or l2:
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next
#超出时间限制
class Solution_():
    def addTwoNumbers(self, l1, l2):
        pNode = ListNode(0)
        pHead = pNode
        val = 0
        while l1 or l2 or val:
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            pNode.next = ListNode(val % 10)
            val /= 10
            pNode = pNode.next
        return pHead.next
class Solution__():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pnode = ListNode(0)
        phead=pnode
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            phead.next=ListNode(s%10)
            phead=phead.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            phead.next=ListNode(1)
        return pnode.next


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
    l2 = generateList([4,6,5])
    printList(l1)
    printList(l2)

    #s = Solution()
    #sum = s.addTwoNumbers(l1, l2)
    #printList(sum)

    ss=Solution__()
    x=ss.addTwoNumbers(l1,l2)
    printList(x)




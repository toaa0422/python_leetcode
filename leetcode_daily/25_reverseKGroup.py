class ListNode():
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def reverse(self,head,tail):
        prev=tail.next
        p=head
        while prev!=tail:
            nxt=p.next
            p.next=prev
            prev=p
            p=nxt
        return tail,head
    def reverseKGroup(self,head,k):
        hair=ListNode(0)
        hair.next=head
        pre=hair
        while head:
            tail=pre
            for i in range(k):
                tail=tail.next
                if not tail:
                    return hair.next
            nxt=tail.next
            head,tail=self.reverse(head,tail)
            pre.next=head
            tail.next=nxt
            pre=tail
            head=tail.next
        return hair.next
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

# 方法一：栈（只需要两个指针实现局部翻转）
class Solution_:
    def reverseKGroup(self,head,k):

        self.stack=[]
        p=ListNode(-1)
        result=p
        flag=True
        # temp_head=head
        while head:
            for i in range(k):
                # printList(head)
                if not head:

                    # print('not head')
                    flag=False
                    break
                self.stack.append(head)
                head=head.next
            # print(self.stack)
            if not flag:break
            else:
                temp_head=head
                print(temp_head)
            for i in range(k):
                cur=self.stack.pop()
                p.next=cur
                p=cur
            p.next=temp_head
        return result.next
# 方法二：利用三个指针实现局部翻转
class Solution__:
    def reverseKGroup(self,head,k):
        sentry=ListNode(-1)
        pre=sentry
        start=head
        flag=True
        while head:
            for i in range(k):
                if not head:
                    flag=False
                    break
                head=head.next
            if not flag:break
            pre.next=self.reverse(start,head)    #此处pre  与下面的pre赋值不明白  待回归
            printList(pre)
            start.next=head
            pre=start
            # printList(pre)
            start=head
            # printList(sentry)
        print('-----------------------------------')
        return sentry.next
    def reverse(self,start,end):
        pre, cur, nexts = None, start, start
        # detail:pre,cur,nexts=None,start,end

        # 三个指针进行局部翻转
        while cur != end:
            nexts = nexts.next
            # 箭头反指
            cur.next = pre
            # 更新pre位置
            pre = cur
            # 更新cur位置
            cur = nexts
        # return pre
        return pre



sol=Solution__()
x=generateList([1,2,3,4,5])
printList(x)
print("-----------------------")
printList(sol.reverseKGroup(x,2))

# note
# reverseList: head = 1
# reverseList: head = 2
# reverseList: head = 3
# reverseList: head = 4
# reverseList: head = 5
# 终止返回
# cur = 5
# 4.
# next.next->4，即5->4
# cur = 5
# 3.
# next.next->3，即4->3
# cur = 5
# 2.
# next.next->2，即3->2
# cur = 5
# 1.
# next.next->1，即2->1
#
# 最后返回cur
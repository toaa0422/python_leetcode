import queue
que=queue.PriorityQueue()

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
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
#2020/04/26  再次出现
class Solution_():
    def mergeKLists(self,lists):
        self.node=[]
        head=point=ListNode(0)
        for l in lists:
            while l:    #此处细节
                self.node.append(l.val)
                l=l.next
        for x in sorted(self.node):
            point.next=ListNode(x)
            point=point.next
        return head.next
# 方法二：堆排序/优先队列
# 利用python的heapq模块进行堆排序
class Solution__():
    def mergeKLists(self,lists):
        import heapq
        head=point=ListNode(0)
        heap=[]
        for l in lists:
            while l:
                heapq.heappush(heap,l.val)
                l=l.next
        while heap:
            val=heapq.heappop(heap)
            point.next=ListNode(val)
            point=point.next
        # point.next=None
        return head.next
# 分而治之   ****
class Solution1:
    def mergeKLists(self, lists) :
        if not lists:return
        n = len(lists)
        return self.merge(lists, 0, n-1)
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    def mergeTwoLists(self,l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":
    #l1 = generateList([1, 5, 8])
    #l2 = generateList([9, 1, 2, 9])
    l1 = generateList([3,4,2])
    l2 = generateList([4,6,5])
    printList(l1)
    printList(l2)
    lists=l1,l2
    s=Solution1()
    x=s.mergeKLists(lists)
    printList(x)


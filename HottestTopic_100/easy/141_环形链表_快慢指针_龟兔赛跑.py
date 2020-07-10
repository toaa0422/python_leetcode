# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (head == None or head.next == None): return False

        slow = head
        fast = head.next

        while (slow != fast):
            if (fast == None or fast.next == None):
                return False

            slow = slow.next
            fast = fast.next.next
        return True
#
#
# 作者：linuzb
# 链接：https: // leetcode - cn.com / problems / linked - list - cycle / solution / 141 - huan - xing - lian - biao - kuai - man - zhi - zhen - c - by - lin /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
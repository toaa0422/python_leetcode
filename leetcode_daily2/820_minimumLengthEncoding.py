
# minium Length Encoding  最小长度编码
#预备知识 tire
class Solution:
    def miniumLengthEncoding(self,words):
        class Node():
            def __init__(self,l):
                self.l=l
                self.children={}
        root=Node(0)
        def build(t, w):
            if not w:return
            if w[-1] not in t.children:
                t.children[w[-1]]=Node(t.l + 1)
            build(t.children[w[-1]], w[:-1])
        for w in words:
            build(root,w)
        ans=[0]
        def vis(t):
            if len(t.children)==0:
                if t.l>0:
                    ans[0]+=t.l+1
            for c in t.children.values():
                vis(c)
        vis(root)
        return ans[0]
s=Solution()
print(s.miniumLengthEncoding(["time",'me','bell']))

s={1:2}
print(len(s))
# s="haha"
# print(s[:-1])    从位置0到位置-1之前的数




"""
#官方题解 python
class Solution:
    def minimumLengthEncoding(self, words) -> int:
        import collections
        from functools import reduce
        words = list(set(words))
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]
        print(dict.__getattribute__)


        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)
s=Solution()
print(s.minimumLengthEncoding((["time",'me','bell'])))


words=["time",'me','bell']
words = sorted(words, key=lambda i: len(i), reverse=True)
print(words)
"""

#clooection.defaultdict 作用
#import collections
#d1 = dict()
#d2 = collections.defaultdict(list)
#dict subclass that calls a factory function to supply missing values   有key无value值   value缺失  不需要键对值
#print(d1['a'])
#print(d2['a'])




"""
#方法1  集合去重
class Solution:
    def minimumLengthEncoding(self, words) -> int:
        good = set(words)
        for word in words:
            print(f'word={word}')
            for k in range(1, len(word)):
                #print(f'k={k}')
                good.discard(word[k:])
                #print(word[k:])
                print(f'final={good}')
        return sum(len(word) + 1 for word in good)


#discard() 方法用于移除指定的集合元素。
#
#该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会
#
#set.discard(value)  val:要移除的元素
#discard  n. 抛弃；被丢弃的东西或人 vt. 抛弃；放弃；丢弃

s=Solution()

words=["time",'me','bell']
print(s.minimumLengthEncoding(words))


"""
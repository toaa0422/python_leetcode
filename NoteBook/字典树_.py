import collections
class TrieNode():
    def __init__(self):
        self.children=collections.defaultdict(TrieNode)
        self.isend=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for w in word:
            node=node.children[w]
        node.isend=True
    def search(self,word):
        node=self.root
        for w in word:
            node=node.children.get(w)
            if not node:
                return False
        return node.isend


sol=Trie()
print(sol.insert('hello'))
# print(sol.insert('he22llo'))
# print(sol.insert('he11llo'))
print(sol.search('hello'))

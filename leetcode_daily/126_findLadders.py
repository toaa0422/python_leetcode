from collections import defaultdict,deque
class Solution_:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordList.append(beginWord)
        ### 构建具有邻接关系的桶
        buckets = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                match = word[:i] + '_' + word[i+1:]
                buckets[match].append(word)
        ##### BFS遍历
        preWords = defaultdict(list)#前溯词列表
        toSeen = deque([(beginWord, 1)])#待遍历词及深度列表
        beFound = {beginWord:1}#已探测词词列表
        while toSeen:
            curWord, level = toSeen.popleft()
            for i in range(len(beginWord)):
                match = curWord[:i] + '_' + curWord[i+1:]
                for word in buckets[match]:
                    if word not in beFound:
                        beFound[word] = level+1
                        toSeen.append((word, level+1))
                    if beFound[word] == level+1:#当前深度等于该词首次遍历深度，则仍应加入前溯词列表
                        preWords[word].append(curWord)
            if endWord in beFound and level+1 > beFound[endWord]:#已搜索到目标词，且完成当前层遍历
                break
        #### 列表推导式输出结果
        if endWord in beFound:
            res = [[endWord]]
            while res[0][0] != beginWord:
                res = [[word] + r for r in res for word in preWords[r[0]]]
            return res
        else:
            return []
import collections

class Solution__:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordList = set(wordList)
        dic = collections.defaultdict(list)
        n = len(beginWord)
        for w in wordList:
            for i in range(n):
                dic[w[:i] + '*' + w[i+1:]].append(w)
        q, s = collections.deque([(beginWord, [beginWord])]), collections.deque()
        seen = set()
        res = []
        while q:
            while q:
                w, path = q.popleft()
                if w == endWord: res.append(path)
                seen.add(w)
                for i in range(n):
                    for v in dic[w[:i] + '*' + w[i+1:]]:
                        if v not in seen:
                            s.append((v, path + [v]))
            if res: return res
            q, s = s, q
        return []

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


sol=Solution_()
print(sol.findLadders(beginWord,endWord,wordList))

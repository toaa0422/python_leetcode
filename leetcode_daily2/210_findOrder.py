from collections import defaultdict
from collections import deque
#dfs
class Solution:
    def findOrder(self,numCourses,prerequisitites):
        edges=defaultdict(list)
        # edges[5].append(2)
        # print(edges)
        visited=[0]*numCourses
        # print(not visited[0])
        result=list()
        invalid=False
        for info in prerequisitites:
            edges[info[1]].append(info[0])
            # print(edges)
        # print(edges)
        def dfs(u):
            nonlocal invalid
            visited[u]=1
            for v in edges[u]:
                if visited[v]==0:
                    dfs(v)
                    if invalid:return
                    elif visited[v]==1:
                        invalid=True
                        return
            visited[u]=2
            result.append(u)
        for i in range(numCourses):
            if not invalid and not visited[i]:
                dfs(i)
        if invalid:
            return list()
        return result[::-1]
#bfs
class Solution_:
    def findOrder(self, numCourses: int, prerequisites):
        edges=defaultdict(list)
        indeg=[0]*numCourses
        result=list()
        # for info in prerequisites:
        #     edges[info[1]].append(info[0])
        #     indeg[info[0]]+=1


        # # 存储有向图
        # edges = defaultdict(list)
        # # 存储每个节点的入度
        # indeg = [0] * numCourses
        # # 存储答案
        # result = list()
        #
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1
        # 将所有入度为 0 的节点放入队列中

        q = deque([u for u in range(numCourses) if indeg[u] == 0])
        # error:  q = deque([u for u in range(numCourses) if indeg == 0])   X indeg V indeg[u]

        while q:
            # 从队首取出一个节点
            u = q.popleft()
            # 放入答案中
            result.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
                if indeg[v] == 0:
                    q.append(v)

        if len(result) != numCourses:
            result = list()
        return result

#入度拓扑排序，虽然垃圾但感觉很容易懂

class Solution_other:
    def findOrder(self,numCourses,prerequisites):
        res=[]
        if numCourses==1:return [0]
        next_node=defaultdict(list)
        rudu_num=defaultdict(int)
        for node in prerequisites:
            next_node[node[0]].append(node[1])
            rudu_num[node[1]]+=1
        start=0
        finish=0
        while start<numCourses:
            # print(rudu_num[start]==0)
            if rudu_num[start]==0:
                for node in next_node[start]:
                    rudu_num[node]-=1
                res.append(start)
                rudu_num[start]=-1
                start=0
                finish+=1
                continue
            if finish==numCourses:
                res.reverse()
                return res
            start+=1
        return []



sol=Solution()
x=[[1,0],[2,0],[3,1],[3,2]]
y=[[1,0]]
print(sol.findOrder(4,x))
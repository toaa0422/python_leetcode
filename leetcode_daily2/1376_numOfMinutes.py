from queue import Queue
from collections import defaultdict
# DFS自底向上  超出时间限制
class Solution:
    def numOfMinutes(self,n,headID,manager,informTime):
        visited=[False]*n
        test=[]
        res=0
        for i in range(n):
            if visited[i]:
                continue
            total=0
            while manager[i]!=-1:
                visited[i]=True
                i=manager[i]
                total+=informTime[i]
            test.append(total)
            res=max(total,res)
        print(test)
        return res
# DFS自顶向下
class Solution_:
    total=0
    def numOfMinutes(self,n,headID,manager,informTime):
        tmp=defaultdict(list)
        for i in range(len(manager)):
            tmp[manager[i]].append(i)
        self.dfs(tmp,informTime,headID,0)
        return self.total
    def dfs(self,tmp,informTime,head_id,total):
        if not tmp[head_id]:
            self.total=max(total,self.total)
        for id_ in tmp[head_id]:
            self.dfs(tmp,informTime,id_,total+informTime[head_id])
# bfs
class Solution__:
    def numOfMinutes(self,n,headID,manager,informTime):
        q=Queue()
        tmp=defaultdict(list)
        for i in range(len(manager)):
            if manager[i]==-1:
                continue
            tmp[manager[i]].append(i)
        q.put((headID,0))
        res=0
        while not q.empty():
            this_id,val=q.get()
            for id_ in tmp[this_id]:
                print(id_)
                print(val+informTime[this_id])
                q.put((id_,val+informTime[this_id]))
                res=max(res,val+informTime[this_id])
        return res


sol=Solution__()
# print(sol.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]))
# print(sol.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))
# print(sol.numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]))
# print(sol.numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
print(sol.numOfMinutes(n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]))







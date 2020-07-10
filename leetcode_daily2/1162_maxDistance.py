class solution:
    def maxDistance(self,grid):
        N=len(grid)
        que=[]
        for i in range(N):
            for j in range(N):
                if grid[i][j]==1:
                    que.append((i,j))
        if len(que)==0 or len(que)==N**2:
            return -1
        distacne=-1
        while len(que)>0:
            distacne+=1
            n = len(que)
            for i in range(n):
                r, c = que.pop(0)
                if r - 1 >= 0 and grid[r - 1][c] == 0:
                    grid[r - 1][c] = 2
                    que.append((r - 1, c))
                if r + 1 <N and grid[r + 1][c] == 0:
                    grid[r - 1][c] = 2
                    que.append((r + 1, c))
                if c - 1 >= 0 and grid[r][c - 1] == 0:
                    grid[r][c-1] = 2
                    que.append((r, c - 1))
                if c + 1 <N and grid[r][c + 1] == 0:
                    grid[r][c+1] = 2
                    que.append((r, c + 1))
        return distacne
class Solution:
    def maxDistance(self, grid) -> int:
        N=len(grid)
        que=[]
        for i in range(N):
            for j in range(N):
                if grid[i][j]==1:
                    que.append((i,j))
        if not que or len(que)>=N**2:return -1
        dsistance=-1
        while len(que)>0:
            dsistance+=1
            n=len(que)
            for i in range(n):
                r,c=que.pop(0)
                if r-1>=0 and grid[r-1][c]==0:
                    grid[r-1][c]=2
                    que.append((r-1,c))
                if r+1<N and grid[r+1][c]==0:
                    grid[r+1][c]=2
                    que.append((r+1,c))
                if c-1>=0 and grid[r][c-1]==0:
                    grid[r][c-1]=2
                    que.append((r,c-1))
                if c+1<N and grid[r][c+1]==0:
                    grid[r][c+1]=2
                    que.append((r,c+1))
        return dsistance
class solution_:
    def maxDistance(self,grid):
        q=[]
        res=0
        vector=[[0,1],[0,-1],[1,0],[-1,0]]
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    q.append([i,j])
        if not q or len(q)==row*col:return -1
        while q:
            l=len(q)
            for i in range(l):
                for v in vector:
                    r=v[0]+q[i][0]
                    c=v[1]+q[i][1]
                    if r>=0 and r<row and c>=0 and c<row:
                        if grid[r][c]==0:
                            grid[r][c]=1
                            q.append([r,c])
            #res即为层数
            res+=1
            q=q[l:]    #注意  不是 1  是L小写
        return res-1


s=solution_()
print(s.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
print(s.__str__())




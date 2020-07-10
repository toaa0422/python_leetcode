import numpy as np
import heapq
class Solution:
    #直接排序  yes
    def kthSmallest(self, matrix, k: int) -> int:
        # print(np.array(sum(matrix,[])))
        rec=sorted(sum(matrix,[]))
        print(np.array(rec))
        return rec[k-1]
    #归并排序  待后续
    def kthSmallest_(self, matrix, k: int):
        n=len(matrix)
        pq=[(matrix[i][0],i,0) for i in range(n)]
        # print(np.array(pq))
        heapq.heapify(pq)
        print(np.array(pq))
        ret=0
        heap_append=[]
        heap_pop=[]
        print("-------------------------------------------------------")
        for i in range(k-1):
            num,x,y=heapq.heappop(pq)
            heap_pop.append([num,x,y])
            if y!=n-1:
                heapq.heappush(pq,(matrix[x][y+1],x,y+1))
                heap_append.append([(matrix[x][y+1],x,y+1)])
        print(np.array(pq))
        print("-------------------------------------------------------")
        print(heap_pop)
        print(heap_append)
        return heapq.heappop(pq)[0]
    #二分查找   界点问题 带后续
    def kthSmallest__(self, matrix, k: int):
        n=len(matrix)
        def check(mid):
            i,j=n-1,0
            num=0
            while i>=0 and j<n:
                if matrix[i][j]<=mid:
                    num+=i+1
                    j+=1
                else:i-=1
            return num>=k
        left,right=matrix[0][0],matrix[-1][-1]
        while left<right:
            mid=(left+right)//2
            if check(mid):
                right=mid
            else:
                left=mid+1
        return left

sol=Solution()
matrix = [
   [ 3,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(sol.kthSmallest_(matrix,k))
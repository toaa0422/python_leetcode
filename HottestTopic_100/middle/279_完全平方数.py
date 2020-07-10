class Solution:
    # brute force
    def numSquares(self, n: int) -> int:
        import math
        square_nums=[i**2 for i in range(1,int(math.sqrt(n))+1)]
        # print(square_nums)
        def minNumSquares(k):
            if k in square_nums:
                return 1
            min_num=float('inf')
            for square in square_nums:
                if k<square:
                    break
                # print(k)
                new_num=minNumSquares(k-square)+1
                min_num=min(min_num,new_num)
            return min_num
        return minNumSquares(n)
    # dynamic planning
    def numSquares_(self, n: int) -> int:
        import math
        square_nums=[i**2 for i in range(0,int(math.sqrt(n)+1))]
        dp=[float('inf')]*(n+1)
        dp[0]=0
        print(dp)
        for i in range(1,n+1):
            for square in square_nums:
                if i<square:
                    break
                dp[i]=min(dp[i],dp[i-square]+1)
        print(dp)
        return dp[-1]

    # 贪心枚举
    def numSquares__(self, n: int) -> int:
        def is_divided_by(n,count):
            if count==1:
                return n in square_nums
            for k in square_nums:
                if is_divided_by(n-k,count-1):
                    return True
            return False
        square_nums=set([i*i for i in range(1,int(n**0.5)+1)])
        for count in range(1,n+1):
            if is_divided_by(n,count):
                return count
    # 贪心 + BFS
    def numSquares___(self, n: int) -> int:
        square_nums=[i*i for i in range(1,int(n**0.5)+1)]
        level=0
        queue={n}
        while queue:
            level+=1
            next_queue=set()
            for remainder in queue:
                for square_num in square_nums:
                    if remainder==square_num:
                        return level
                    elif remainder<square_num:
                        break
                    else:
                        next_queue.add(remainder-square_num)
            queue=next_queue
        return level
    # mathematical operation
    # 四平方和定理，也称为Bachet猜想
    def isSquare(self,n)->bool:
        import math
        sq=int(math.sqrt(n))
        return sq**2==n

    def numSquares_math(self, n: int) -> int:
        while (n&3)==0:
            n>>=2
        if (n&7)==7:
            return 4
        if self.isSquare(n):
            return 1
        for i in range(1,int(n**(0.5))+1):
            if self.isSquare(n-i**2):
                return 2
        return 3

    # 最后一个简直降维打击，动态规划是50ms
    # 贪心是14ms，最后一个1ms


sol=Solution()
print(sol.numSquares_math(12))
print(sol.numSquares_math(13))
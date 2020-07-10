class Solution:
    # 题意 没看懂 待后续
    def leastInterval(self, tasks, n: int) -> int:
        length=len(tasks)
        if length<=1:return 1
        task_map=dict()
        for task in tasks:
            task_map[task]=task_map.get(task,0)+1
        task_sort=sorted(task_map.items(),key=lambda x:x[1],reverse=True)
        max_task_count=task_sort[0][1]
        res=(max_task_count-1)*(n+1)
        for sort in task_sort:
            if sort[1]==max_task_count:
                res+=1
        return res if res>=length else length
sol=Solution()
print(sol.leastInterval(tasks = ["A","A","A","B","B","B"],n=2))

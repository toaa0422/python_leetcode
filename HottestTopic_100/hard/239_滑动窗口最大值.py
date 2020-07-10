class Solution:
    # brute force   yes  超时  略
    def maxSlidingWindow(self, nums, k: int):
        n=len(nums)
        if n*k==0:
            return []
        return [max(nums[i:i+k]) for i in range(n-k+1)]
    # dequeue   double queue
    def maxSlidingWindow1(self, nums, k: int):
        from collections import deque
        n = len(nums)
        if n * k == 0:return []
        if k==1:return nums
        def clean_deque(i):
            if deq and deq[0]==i-k:
                deq.popleft()
            while deq and nums[i]>nums[deq[-1]]:
                deq.pop()

        deq=deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output
    # dynamic planning
    def maxSlidingWindow11(self, nums, k: int):
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))

        return output


nums = [1,3,-1,-3,5,3,6,7]
k = 3
sol=Solution()
print(sol.maxSlidingWindow(nums,k))
print(sol.maxSlidingWindow1(nums,k))
print(sol.maxSlidingWindow11(nums,k))
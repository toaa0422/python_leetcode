#method :归并排序     2020/04/24
class Solution():
    def mergeSort(self,nums,tmp,l,r):
        if l>=r:return 0
        mid=(l+r)//2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        # inv_count=self.mergeSort(nums,tmp,l,mid)+self.mergeSort(nums,tmp,l,r)  #细节
        i,j,pos=l,mid+1,l
        while i <= mid and j <= r:
            print(f"{tmp}")
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1

            #     pos-=1    #细节
        for k in range(i,mid+1):
            tmp[pos]=nums[k]
            inv_count+=(j-(mid+1))
            pos+=1
        for k in range(j,r+1):
            tmp[pos]=nums[k]
            pos+=1
        nums[l:r+1]=tmp[l:r+1]
        return inv_count
    def reversePairs(self,nums):
        n=len(nums)
        tmp=[0]*n
        return self.mergeSort(nums,tmp,0,n-1)

#离散化树状数组    预备知识   离散化 树状数组
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.tree[x]
            x -= BIT.lowbit(x)
        return ret

    def update(self, x):
        while x <= self.n:
            self.tree[x] += 1
            x += BIT.lowbit(x)

import bisect
class Solution_:
    def reversePairs(self, nums) -> int:
        n = len(nums)
        # 离散化
        tmp = sorted(nums)
        for i in range(n):
            nums[i] = bisect.bisect_left(tmp, nums[i]) + 1
        # 树状数组统计逆序对
        bit = BIT(n)
        ans = 0
        for i in range(n - 1, -1, -1):
            ans += bit.query(nums[i] - 1)
            bit.update(nums[i])
        return ans



s=Solution_()
print(s.reversePairs([7,5,6,4]))
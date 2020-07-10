
class Solution():
    def singleNumbers(self,nums):
        import functools
        ret=functools.reduce(lambda x,y:x^y,nums)   #按位异或逻辑运算符
        div=1
        while div & ret==0:
            # print(f"{div}={bin(div)},{ret}={bin(ret)}")
            div<<=1
            # print(f"{bin(div)}={div}")
        a,b=0,0
        # for n in nums:
        #     print(n&div)
        for n in nums:
            # print(bin(n&div))
            if n &div:
                a^=n
                print(n&div,a^n)
            else:
                b^=n
                # print(bin(b))
        return [a,b]

# print(bin(1^2^2^3))
class Solution_:
    def singleNumbers(self, nums):
        res = 0
        for i in nums:
            res = res ^ i

        idx = 1
        while idx & res == 0:
            idx = idx << 1
        print(f'idx={idx}')

        a, b = 0, 0
        for i in nums:
            if i & idx == 0:
                a = a ^ i
            else:
                b = b ^ i
        return ([a, b])

class Solution__:
    def singleNumbers(self, nums):
        a,n = 0,len(nums)
        for i in range (0,n):
            a^=nums[i]
        b,c = 0,0
        mask = a & (-a)
        print(f'mask={mask}')
        for i in range(len(nums)):
            if(nums[i] & mask == 0):
                b^=nums[i]
            else:
                c^=nums[i]
        return b,c
# 假设全员异或后的值ret，答案为a,b，有ret=a^b
# 只需要在ret的二进制里面，找到一个为1的位p(使用lowbit)
# 显然a和b在p位不同(a!=b则ab至少有一位不同，则一定存在p位)
# 只需要再次遍历，按照p位01把整体分成两组
# 可以证明：
# ①相同的数字一定在一组
# ②a和b在不同的分组
# 组内异或即可找出a和b(其实只要找出a或b
#
# 作者：liu-xian-qing-chi-yan
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/6xing-de-pyshi-jian-o1kong-jian-onsi-lu-jian-duan-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution___:
    def singleNumbers(self, nums):
        import functools
        ans = [0, 0]
        xor = functools.reduce(lambda x, y: x ^ y, nums)
        low = xor & -xor
        for num in nums: ans[not num & low] ^= num
        # for num in nums:ans[bool(num&low)]^=num #同理
        return ans





s=Solution_()
print(s.singleNumbers([1,2,2,3]))
# print(bin(1^1))
# s=Solution()
# print(s.singleNumbers([1,2,2,3,3,5]))


# ^是按位异或逻辑运算符，比如5^6，其实是101^110，结果是011，所以5^6的答案是3
# print(1^2)   >>>3
# print(3^3)   >>>0


# the finnal solution by myself
class Solution_max:
    def singleNumbers(self, nums):
        import functools
        xor=functools.reduce(lambda x,y:x^y,nums)
        mask=xor&(-xor)
        a=0
        b=0
        for x in nums:
            if x&mask==0:
                a^=x
            else:
                b^=x
        return [a,b]
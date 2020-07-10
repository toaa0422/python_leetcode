# 哈希表 + 逐一统计
class   Solution:
    def subarraysDivByK(self,A,K):
        record={0:1}
        total,ans=0,0
        for elem in A:
            total+=elem
            modulus=total%K    #n. 系数；模数
            # print(f'{modulus}')
            same=record.get(modulus,0)
            print(f'{same}')
            ans+=same
            record[modulus]=same+1
        return ans
# 哈希表 + 单次统计
class Solution_():
    def subarraysDivByK(self,A,K):
        record={0:1}
        total=0
        for elem in A:
            total+=elem
            modulus=total%K
            record[modulus]=record.get(modulus,0)+1
        print(record)
        ans=0
        for x,cx in record.items():

            ans+=cx*(cx-1)//2
            print(cx*(cx-1)//2)
        return ans


A = [4,5,0,-2,-3,1]
K = 5
sol=Solution_()
print(sol.subarraysDivByK(A,K))

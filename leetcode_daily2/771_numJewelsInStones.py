# Brute Force
class Solution:
    def numJewelInStones(self,J,S):
        # return list(s in J for s in S)   #[True, True, True, True, True, True, True]
        return sum(s in J for s in S)
#哈希集合  相比上面 优化点
class Solution_:
    def numJewelInStones(self,J,S):
        Jset=set(J)
        return sum(s in Jset for s in S)
sol=Solution_()
print(sol.numJewelInStones('aA','aaaaAAA'))
# print(sum([True]))   #>>1
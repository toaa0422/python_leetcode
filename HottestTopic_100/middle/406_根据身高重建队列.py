#此题 难的是读懂题意！！！！
class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x:(-x[0],x[1]))
        print(people)
        output=[]
        for p in people:
            print(p[1],p)
            output.insert(p[1],p)
            print(output)
        print('————————————————————————————')
        return output
sol=Solution()
print(sol.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
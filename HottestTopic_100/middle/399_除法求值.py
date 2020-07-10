class Solution:
    # 并查集   待后续
    def calcEquation(self, equations, values, queries) :
        word = set()
        for i in equations:
            word.add(i[0])
            word.add(i[1])
        word = list(word)
        parent = {i: i for i in word}
        rank = {i: 0 for i in word}

        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])

        def union(x, y):
            xroot = find(x)
            yroot = find(y)
            if xroot != yroot:
                if rank[xroot] > rank[yroot]:
                    parent[y] = x
                elif rank[yroot] > rank[xroot]:
                    parent[x] = y
                else:
                    parent[x] = y
                    rank[yroot] += 1

        def union_find():
            for pair in equations:
                union(pair[0], pair[1])

            equ_dic = {}
            for i in range(len(equations)):
                equ_dic[equations[i][0] + '#' + equations[i][1]] = values[i]
                equations[i].reverse()
                equ_dic[equations[i][0] + '#' + equations[i][1]] = 1 / values[i]

            res = []

            def find2(x, d):
                if parent[x] == x:
                    return x, d
                try:
                    return find2(parent[x], d * equ_dic[x + '#' + parent[x]])
                except KeyError as e:
                    return find2(parent[x], d * equ_dic[parent[x] + '#' + x])

            for q in queries:
                if q[0] not in word or q[1] not in word:
                    res.append(-1)
                    continue
                aroot, d1 = find2(q[0], 1)
                broot, d2 = find2(q[1], 1)
                if aroot != broot:
                    res.append(-1)
                    continue
                res.append(d1 / d2)
            return res

        return union_find()

sol=Solution()
x=[ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(sol.calcEquation([ ["a", "b"], ["b", "c"] ],[2.0, 3.0],x))


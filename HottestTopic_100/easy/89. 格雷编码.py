class Solution:
    def grayCode(self, n: int):
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res

    def grayCode1(self, n: int) :
        res = [0]
        for i in range(1, (1 << n)):
            res.append(res[-1] ^ (i & -i))
        return res


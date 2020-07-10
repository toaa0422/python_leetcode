class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.sums = [0] * self.n

    def update(self, i, delta):
        while i < self.n:
            self.sums[i] += delta
            i += i & (-i) # = i & (~i + 1) 用于追踪最低位的1

    def prefixSum(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res

    def rangeSum(self, s, e):
        return self.prefixSum(e) - self.prefixSum(s - 1)
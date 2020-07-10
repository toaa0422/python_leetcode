class FenwickTree:

    def __init__(self, arrayA):  # 传入初始数组，构建树状数组
        self.size = len(arrayA)  # 保存数组大小
        self.arrayA = [0 for i in range(self.size)] #保存初始数组以及变更
        #树状数组初始设置为0
        self.arrayC = [0 for i in range(self.size)]
        for i in range(1,self.size+1):
            """
            构建类的初始数组A和树状数组B
            这里有一个注意事项，我们对于求前缀和与单点更新时，树状数组C是拿来直接使用的，
            那么问题来了，树什么时候建立好的，我怎么不知道？?
            事实上，对于一个输入的数组A，我们一次读取的过程，就可以想成是一个不断更新值的过程
            （把A1~An从0更新成我们输入的A[i]），所以一边读入A[i]，一边将C[i]涉及到的祖先节点值更新，
             完成输入后树状数组C也就建立成功了
            """
            self.update(i,arrayA[i-1]) #【注意】数组从0下标开始，update方法从1开始

    def lowbit(self,m):
        """
        求出m的二进制表示的末尾1的位置
        :return:
        """
        return m & (-m)

    def update(self, i, val):  # 【注意】数组从0下标开始，update方法从1开始
        self.arrayA[i-1] += val  # 更新初始数组
        while i <= self.size:
            self.arrayC[i-1] += val #注意数组下标从0开始
            i += self.lowbit(i)


    def sum(self, i):  # 求前缀和，sum方法从1开始
        ans = 0
        while i > 0:
            ans += self.arrayC[i-1] #数组下标从1开始
            i -= self.lowbit(i)
        return ans



if __name__ == "__main__":
    fenwickTree = FenwickTree([1,2,3,4,5,6,7,8])
    print(fenwickTree.arrayA) #打印初始数组
    print(fenwickTree.arrayC) #打印树状数组
    print(fenwickTree.sum(4))#求arrayA前4项的和
    fenwickTree.update(1,3) #arrayA第1个元素+3
    print(fenwickTree.arrayA)  # 打印更新数组[4,2,3,4,5,6,7,8]
    print(fenwickTree.arrayC)  # 打印树状数组
    print(fenwickTree.sum(4))#求arrayA前4项的和
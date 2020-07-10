class Solution:
    # 方法一：Trie + 动态规划
    # 方法二：字符串哈希

    # 回溯加备份
    def respace(self, dictionary, sentence: str) -> int:
        import functools
        lens=list({len(w) for w in dictionary})
        print(lens)
        lens.sort(reverse=True)
        print(lens)
        N=len(sentence)
        print(N)
        # N,res,i=len(sentence),0,0
        @functools.lru_cache(maxsize=1000)
        def sol(i):
            if i >= N: return 0     #if i>N:return 0
            # tails = []
            tails = [sol(i + l) for l in lens if i + l <= N and sentence[i:i + l] in dictionary]
            tails += [1 + sol(i + 1)]
            return (min(tails) if tails else 0)
        return sol(0)
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
sol=Solution()
print(sol.respace(dictionary,sentence))



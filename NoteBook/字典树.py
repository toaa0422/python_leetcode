# words = ['cat','category','tree','trace','top']
words=['cat']
trie = {}
for word in words:
    t = trie # 请把这个t理解为指针，这个指针除了用来移动外，也用来建立新的字典。
    for c in word:
        if c not in t:
            t[c] = {} # 若没有，为下一个字母建立一个新的字典
        t = t[c] # 进入下一层
    t['#'] = '#' # 句尾结束符
print(trie)
import collections
class Solution:
    def countCharacters(self, words, chars: str) -> int:
        """
        :param words: words = ["cat","bt","hat","tree"]
        :param chars: "atach"
        :return:
        """
        chars_cnt = collections.Counter(chars)
        """Counter({'a': 2, 't': 1, 'c': 1, 'h': 1})"""
        ans = 0
        for word in words:
            word_cnt = collections.Counter(word)
            for c in word_cnt:
                if chars_cnt[c] < word_cnt[c]:
                    break
            else:
                ans += len(word)
            '''在for循环完整完成后才执行else；如果中途从break跳出，则连else一起跳出(不执行else内的语句)'''
        return ans


chars='atach'
chars_cnt = collections.Counter(chars)
print(chars_cnt)
s=Solution()
print(s.countCharacters(["cat","bt","hat","tree"],"atach"))
print(s.countCharacters(["hello","world","leetcode"],'welldonehoneyr'))


"""
对于一个单词 word，只要其中的每个字母的数量都不大于 chars 中对应的字母的数量，那么就可以用 chars 中的字母拼写出 word。
"""
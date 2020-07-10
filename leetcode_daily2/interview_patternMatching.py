#类似于二元一次方程 求解
class Solution_official:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = sum(1 for ch in pattern if ch == 'a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)
        if not value:
            return count_b == 0
        if not pattern:
            return False
        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - count_a * len_a
            if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):
                len_b = 0 if count_b == 0 else rest // count_b
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos + len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos + len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    # print(len_a,len_b)
                    return True

        return False



#解整数二元一次方程计算a，b可能的长度，获得对应字符串，以此从pattern获得字符串与value对比
class Solution_:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = pattern.count('a')
        count_b = pattern.count('b')
        length = len(value)
        # 处理只有一种字符和二者均为空的情况
        if count_a == 0:
            if count_b == 0:
                return value == ''
            str_b = value[0:length//count_b]
            return value == str_b*count_b
        if count_b == 0:
            str_a = value[0:length//count_a]
            return value == str_a*count_a
        # 处理ab都有的情况，i和j分别遍历a和b可能的长度
        for i in range(length//count_a+1):
            if (length - count_a*i)%count_b == 0:
                j = (length - count_a*i)//count_b
                index_a = pattern.find('a')
                index_b = pattern.find('b')
                # 确定a，b分别代表的字符串
                str_a = value[index_a*j:index_a*j+i]
                str_b = value[index_b*i:index_b*i+j]
                # 相同的时候不合题意，跳过
                if str_a == str_b:
                    continue
                #判断pattern构成字符串是否等于value
                str_check = ''
                for char in pattern:
                    if char =='a':
                        str_check += str_a
                    else:
                        str_check += str_b
                if str_check == value:
                    return True
        return False

sol=Solution_official()
print(sol.patternMatching(pattern = "abba", value = "dogcatcatdog"))         #  True

# print(sol.patternMatching(pattern = "abba", value = "dogcatcatdog"))         #  True
# print(sol.patternMatching(pattern = "abba", value = "dogcatcatfish"))        #  false
# print(sol.patternMatching(pattern = "aaaa", value = "dogcatcatdog"))         #  false
# print(sol.patternMatching(pattern = "abba", value = "dogdogdogdog"))         #  true
# print(sol.patternMatching(pattern = "", value = ""))         #  true

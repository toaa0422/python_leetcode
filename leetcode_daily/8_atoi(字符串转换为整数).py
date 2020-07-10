# 方法一：自动机
#   automaton  n. 自动机；机器人；自动机器
#   automation  n. 自动化；自动操作
#  准确地说，这是确定有限状态机（deterministic finite automaton, DFA）   编译原理
INT_MAX=2**31-1
INT_MIN=-2**31
# print(f'{INT_MIN},{INT_MAX}')
class Automaton():

    def __init__(self):
        self.state='start'
        self.sign=1
        self.ans=0
        self.table={
            'start':['start','signed','in_number','end'],
            'signed':['end','end','in_number','end'],
            'in_number':['end','end','in_number','end'],
            'end':['end','end','end','end'],
        }
    def __str__(self):
        return self.sign
    def get_col(self,c):
        if c.isspace():
            return 0
        if c=='+'or c=='-':
            return 1
        if c.isdigit():
            return 2
        return 3



    def get(self,c):
        self.state=self.table[self.state][self.get_col(c)]
        print(f'{self.state},{self.__str__()}')
        if self.state=='in_number':
            #print(f'{self.ans},{self.ans*10}')

            self.ans=self.ans*10+int(c)
            self.ans=min(self.ans,INT_MAX) if self.sign==1 else min(self.ans,-INT_MIN)

        elif self.state=='signed':  #细节     self.state  error:self.stable
            self.sign=1 if c=='+'else -1
class Solution():
    def myAtoi(self,str):
        automaton=Automaton()
        for c in str :
            automaton.get(c)
        return automaton.sign*automaton.ans


from enum import Enum
class State(Enum):
    START=1
    POSITIVE=2
    NEGATIVE=3


# 枚举用法
class Solution_:
    def myAtoi(self, string: str) -> int:
        string=string.lstrip()
        INT_MAX=(1<<31)-1
        INT_MIN=-(1<<31)
        now=State.START
        number=0
        for s in string:
            if now is State.START:
                if s=='+':
                    now=State.POSITIVE
                elif s=='-':
                    now=State.NEGATIVE
                elif s.isdigit():
                    number+=int(s)
                    now=State.POSITIVE
                else:
                    return 0
            elif now is State.POSITIVE:
                if s.isdigit():
                    number*=10
                    number+=int(s)
                    if number>=INT_MAX:
                        return INT_MAX
                else:
                    break
            elif now is State.NEGATIVE:
                if s.isdigit():
                    number*=10
                    number-=int(s)
                    if number<=INT_MIN:
                        return INT_MIN
                else:
                    break
        return number

class Solution__:
    def myAtoi(self, str_: str) -> int:
        flag, ans = None, []
        for c in str_:
            if c == ' ' and not ans and not flag:
                continue
            elif c in '+-' and not flag and not ans:
                flag = (1 if c=='+' else -1)
            elif c in '0123456789':
                ans.append(c)
            else:
                break
            print(f'{ans}')
        if not ans:
            return 0
        ans = (flag if flag else 1)*int(''.join(ans))
        return ans if -2**31<=ans<=2**31-1 else (2**31-1 if ans>0 else -2**31)
s=Solution__()
print(s.myAtoi("-4193 with words"))



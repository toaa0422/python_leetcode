class ListNode:
    def __init__(self,value):
        self.value=value
        self.exp=None
        self.next=None


class Solution:
    @staticmethod
    def multiply_best(num1, num2):
        """
        采用数组存储
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        res=[0]*(len(num1)+len(num2))
        len_num1 = len(num1)
        len_num2 = len(num2)
        for i in range(len_num1-1,-1,-1):
            num_1 = int(num1[i])
            exp_1= len_num1-i-1
            for j in range(len_num2 - 1, -1, -1):
                num_2 = int(num2[j])
                exp_2 = len_num2 - j - 1
                exp=exp_1+exp_2
                res[exp]+=num_1*num_2
                c=res[exp]//10
                res[exp]=res[exp] % 10
                exp+=1
                while c>0:
                    res[exp] += c
                    c = res[exp] // 10
                    res[exp] = res[exp] % 10
                    exp = exp + 1
        flag = False
        if res[-1]==0:
            flag = True


        res_str=""
        for i in range(len(res)-1,-1,-1):
            if res[i]==0 and flag:
                flag=False
                continue
            else:
                res_str+=str(res[i])
        return res_str




    @staticmethod
    def multiply_worse(num1, num2):
        """
        采用链表存储
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return 0



        p_head_num1=ListNode(-1)
        p_head_num2 = ListNode(-1)
        res_head=ListNode(-1)


        len_num1=len(num1)
        len_num2=len(num2)

        for index,num in enumerate(num1):
            p = ListNode(int(num))
            p.exp = len_num1-index-1
            p.next=p_head_num1.next
            p_head_num1.next=p

        for index,num in enumerate(num2):
            p = ListNode(int(num))
            p.exp = len_num2-index-1
            p.next=p_head_num2.next
            p_head_num2.next=p


        p2=p_head_num2.next
        while p2 is not None:
            p1 = p_head_num1.next
            while p1 is not None:
                tmp = p2.value*p1.value
                c = tmp // 10
                value = tmp % 10
                exp = p2.exp+p1.exp
                p = res_head.next
                q=res_head
                flag_1 = True
                flag_2 = True
                while p is not None:
                    if p.exp==exp:
                        c += (p.value + value)//10
                        p.value=(p.value+value)%10
                        flag_1=False
                        q = p
                        p = p.next
                        if c == 0:
                            flag_2=False
                        break
                    q=p
                    p=p.next
                if flag_1:
                    p_new=ListNode(value)
                    p_new.exp=exp
                    q.next=p_new
                    q=q.next
                if c >0 and flag_2 :
                    while c != 0 and p is not None:
                        y=p.value + c
                        p.value = y % 10
                        c = y//10
                        exp=exp+1
                        q=p
                        p=p.next
                    if c>0:
                        p_new = ListNode(c)
                        p_new.exp = exp + 1
                        q.next = p_new


                p1=p1.next
            p2=p2.next
        p=res_head.next
        res=""
        while p is not None:
            res=str(p.value)+res
            p=p.next
        return res





if __name__=="__main__":
    num1="999"
    num2="999"
    print(Solution.multiply_best(num1,num2))

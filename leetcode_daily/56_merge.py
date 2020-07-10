class Solution:
    def merge(self, intervals):
        # intervals.sort(key=lambda x: x[0])
        intervals.sort()
        print(intervals)


        merged = []
        for interval in intervals:
            print(merged)

            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:

                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


s=Solution()
x=[(1, 9), (2, 5), (19, 20), (10, 11), (12, 20), (0, 3), (0, 1), (0, 2)]
xx=[]
for i in x:
    xx.append(list(i))
# print(xx)
# print(xx[-1][1])
print(s.merge(xx))
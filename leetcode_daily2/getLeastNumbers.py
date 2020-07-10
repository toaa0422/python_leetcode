def gerLeastNumbers(arr,k):
    return sorted(arr)[:k]


def getLeastNumbers_(arr,k):
    if not arr or not k:
        return []
    sort_list=sorted(arr)
    res=[]
    for val in sort_list:
        res.append(val)
        k-=1
        if k==0:
            break
    return res
"""
if not arr or not k:
            return []
        sorted_lis=sorted(list)   ###arr  be attention to the detail
        res=[]
        for val in sorted_lis:
            res.append(val)
            k-=1
            if k==0:
                break
        return res
"""



arr = [3,2,1]
k = 2
print(gerLeastNumbers(arr,k))
print(getLeastNumbers_(arr,k))

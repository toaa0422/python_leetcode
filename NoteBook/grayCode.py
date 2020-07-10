def grayCode(n):
    res = [0]
    i = 0
    while i < n:  # 从2的0次方开始，
        next_base = 1 << i
        res_inv = [x + next_base for x in reversed(res)]
        res.extend(res_inv)
        i += 1
    return sorted(res)

print(grayCode(4))
res=[]
for x in grayCode(4):
    res.append(''.join(bin(x)[2:].zfill(4)))
print(res)





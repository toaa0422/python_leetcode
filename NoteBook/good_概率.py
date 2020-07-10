import itertools
# s=list(itertools.product(('A','B'),('A','B')))
# d=list(itertools.product(('A','B'),repeat=2))
a=list(itertools.permutations('good',r=4))

# print(s)
# print(d)
res=[]
for s in a:
    res.append(''.join(s))
for i in range(len(res)):
    if i%10==0:
        print('')
    print(res[i],end=' ')
print('')
print(len(res))
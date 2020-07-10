import random  # 导入随机函数包
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] # 10个老师的姓名，这里最简化代替
offices = [[], [], [], []] # 四个办公室，每一个办公室算一个数组

'''这是一个for循环，循环次数是names里名字数量的次数'''
for name in names:  # 遍历names里的名字
    index = random.randint(0, 3) # 在0-3之间获取随机值，offices中三个数组的索引
    offices[index].append(name) # 将其中一个名字添加到刚刚获取的随机索引所在的列表

i = 1 # i的初始值
for office in offices: # 对offices列表进行循环遍历，执行次数为4次，因为offices里有4个数组
    num = len(office) # 对遍历出来的四个数组进行长度判断，即人数
    print('第%d个办公室有%d人' % (i, num)) # 占位符打印，i和num都是纯数字，所以用%d
    for name in office: # 对每个办公室进行循环，以找出每个办公室的内老师的名字
        print(name, end='\t') # 横向打印这个办公室老师的名字
    print() # 换行
    i += 1 # 每执行一次遍历i就加1，从第一个办公室开始，所以i的初始值为1
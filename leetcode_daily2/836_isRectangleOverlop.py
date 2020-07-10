def isRectangleOverlap(rec1,rec2):
    return not(rec1[2]<=rec2[0] or
               rec1[0]>=rec2[0] or
               rec1[1]>=rec2[3] or
               rec1[3]<=rec2[1])

print(isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]))


"""
轴投射
"""
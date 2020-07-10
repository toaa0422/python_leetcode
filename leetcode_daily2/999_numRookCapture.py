#rook  车 bishop 象 pawn 卒
class Solution:
    def numRookCaptures(self, board) -> int:
        if not board:
            return 0
        Rx,Ry=0,0
        for i in range(8):
            for j in range(8):
                if board[i][j]=="R":  #注意细节 board=="R"
                    Rx,Ry=i,j
        dx,dy=[0,1,0,-1],[1, 0, -1, 0]#[1,0,-1,0],[0,-1,0,1]
        cnt=0
        for i in range(4):
            step=0
            while True:
                x=Rx+dx[i]*step
                y=Ry+dy[i]*step
                #if x<0 or x>8 or y<0 or y>8 or board[x][y]=="B":
                if x < 0 or x >= 8 or y < 0 or y >= 8 or board[x][y]=='B': #if x>=8 细节问题
                    break
                #else:pass
                if board[x][y]=='p':
                    cnt += 1
                    break


                step+=1
        return cnt


class Solution_:
    def numRookCaptures(self, board) -> int:

        x, y = -1, -1  # 若无此, x,y 算局部变量， 后续无法使用
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x, y = i, j  # 不要直接用 i,j 局部变量
                    break
        dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

        count = 0
        for i in range(4):  # 大杀四方：朝四个方向都走一次，算一次移动
            nx, ny = x + dx[i], y + dy[i]
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] == 'B':
                    break
                if board[nx][ny] == 'p':
                    count += 1
                    break
                nx += dx[i]
                ny += dy[i]

        return count


lis=[[".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","."],
     [".",".",".","R",".",".",".","p"],
     [".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","."]]

s=Solution_()
ss=Solution()
print(s.numRookCaptures(lis))
print(ss.numRookCaptures(lis))

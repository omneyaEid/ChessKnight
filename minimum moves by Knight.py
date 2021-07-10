class Cell:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist
 
# block[] = board[x][y]
def isInside(x, y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    return False
 
 
# isBlock(z.x , z.y , x , y)
def isBlock(zx , zy , x , y , board):
    # 0 0 >> 2 0 >> 2 1
 
    flg = False
    if(x == 1 and y == -2 and isInside(zx + x , zy + y)):
        if(board[zx + 1][zy] == '*' or board[zx + 1][zy - 1] == '*' or board[zx + 1][zy - 2] == '*'):
            flg = True
 
    if(x == 2 and y == -1 and isInside(zx + x , zy + y)):
        if(board[zx + 1][zy] == '*' or board[zx + 2][zy] == '*' or board[zx + 2][zy - 1] == '*'):
            flg = True
 
    if(x == 2 and y == 1 and isInside(zx + x , zy + y)):
        if(board[zx + 1][zy] == '*' or board[zx + 1][zy] == '*' or board[zx + 2][zy + 1] == '*'):
            flg = True
 
    if(x == 1 and y == 2 and isInside(zx + x , zy + y)):
        if(board[zx + 1][zy] == '*' or board[zx + 1][zy + 1] == '*' or board[zx + 1][zy + 2] == '*'):
            flg = True
 
    if(x == -1 and y == 2 and isInside(zx + x , zy + y)):
        if(board[zx - 1][zy] == '*' or board[zx - 1][zy + 1] == '*' or board[zx - 1][zy + 2] == '*'):
            flg = True
 
    if(x == -2 and y == 1 and isInside(zx + x , zy + y)):
        if(board[zx - 1][zy] == '*' or board[zx - 2][zy] == '*' or board[zx - 2][zy + 1] == '*'):
            flg = True
 
    if(x == -2 and y == -1 and isInside(zx + x , zy + y)):
        if(board[zx - 1][zy] == '*' or board[zx - 2][zy] == '*' or board[zx - 2][zy - 1] == '*'):
            flg = True
 
 
    if(x == -1 and y == -2 and isInside(zx + x , zy + y)):
        if(board[zx - 1][zy] == '*' or board[zx - 1][zy - 1] == '*' or board[zx - 1][zy - 2] == '*'):
            flg = True
    return flg
 
 
def play():
 
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    queue = []
    board = [[0, 1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20, 21, 22, 23],
            [24, 25, 26, 27, 28, 29, 30, 31],
            [32, 33, 34, 35, 36, 37, 38, 39],
            [40, 41, 42, 43, 44, 45, 46, 47],
            [48, 49, 50, 51, 52, 53, 54, 55],
            [56, 57, 58, 59, 60, 61, 62, 63]]
 
    # to initail visited
    visited = [[False for i in range(0, 8)] for j in range(0, 8)]
 
    # to get src
    x_axes = -1
    y_axes = -1
 
    print("Enter X-axes for src :- ")
    x_src = int(input())
    print("Enter Y-axes for src :- ")
    y_src = int(input())
    queue.append(Cell(x_src, y_src))
 
    print("Enter X-axes for goal :- ")
    x_goal = int(input())
    print("Enter Y-axes for goal :- ")
    y_goal = int(input())
    dst = Cell(x_goal, y_goal)
 
    N = 0
    print("Enter Number Of Obstacles :- ")
    N = int(input())
 
    for i in range(0 , N):
        print("Enter X-axes for dest :- ")
        x_axes = int(input())
        print("Enter Y-axes for dest :- ")
        y_axes = int(input())
        board[x_axes][y_axes] = '*'
 
 
    if board[x_src][y_src] == board[x_goal][y_goal]:
        return 0
 
    while len(queue) > 0:
        z = queue[0]
        queue.pop(0)
        if z.x == dst.x and z.y == dst.y:
            return z.dist
        for i in range(8):
            x = z.x + dx[i]
            y = z.y + dy[i]
 
            if isInside(x, y) and not isBlock(z.x , z.y , dx[i] , dy[i] , board) and not visited[x][y]:
                print("Start point (" + str(z.x) + " , "+ str(z.y)+ 
                " )    Next point (" + str(x) + " , "+ str(y)+ " )"       )
 
              #  print(z.x , z.y , x , y)
                visited[x][y] = True
                queue.append(Cell(x, y, z.dist + 1))
 
print("\nthe minimum number of steps from start to goal is  " + str(play()))
# '.', '#', 'O', 'R', 'B' 
# . : 빈칸, # : 벽, O : 구멍, R : 빨간공, B : 파란공
import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
path = [[[[[0, 0, 0, 0, 0] for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
command = ['U', 'R', 'D', 'L']
ans = list()

def move(x, y, dir):
    cnt = 0

    while board[x + dx[dir]][y + dy[dir]] != "#" and board[x][y] != "O":
        x += dx[dir]
        y += dy[dir]
        cnt += 1
    return x, y, cnt

def BFS(x1, y1, x2, y2):
    Q = deque([[x1, y1, x2, y2, 1]])

    while Q:
        rx, ry, bx, by, cnt = Q.popleft()
        visited[rx][ry][bx][by] = True

        if cnt > 10:
            print(-1)
            exit(0)

        for i in range(4):
            rnx, rny, rcnt = move(rx, ry, i)
            bnx, bny, bcnt = move(bx, by, i)

            if board[bnx][bny] != "O":
                if board[rnx][rny] == "O":
                    ans.append(command[i])
                    rmx, rmy, bmx, bmy = rx, ry, bx, by
                    while rmx:
                        rmx, rmy, bmx, bmy, k = path[rmx][rmy][bmx][bmy]
                        ans.append(command[k])
                    ans.pop()
                    ans.reverse()
                    print(cnt)
                    print(''.join(ans))
                    exit(0)

                if rnx == bnx and rny == bny:
                    if rcnt > bcnt:
                        rnx -= dx[i]
                        rny -= dy[i]
                    else:
                        bnx -= dx[i]
                        bny -= dy[i]

                if not visited[rnx][rny][bnx][bny]:
                    visited[rnx][rny][bnx][bny] = True
                    Q.append([rnx, rny, bnx, bny, cnt+1])
                    path[rnx][rny][bnx][bny] = (rx, ry, bx, by, i)


    print(-1)
    return


rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

BFS(rx, ry, bx, by)

# pprint(board)
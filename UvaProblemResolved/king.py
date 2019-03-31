from sys import stdin
from collections import deque
#11352 - Crazy King
source,dest = None,None
grid,rows,cols = None,None,None

delta = [ (0,-1), (0,1), (1,0), (-1,0),(1,-1),(1,1),(-1,1),(-1,-1)]
deltab = [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]


def predictHorse():
    global visited,rows,cols,grid
    for i in range(rows):
        for j in range(cols):
            if(grid[i][j] == 'Z'):
                for dr,dc in deltab:
                    nr,nc = i+dr,j+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == '.':
                        grid[nr][nc] = 'L'
def bfs():
  global grid,rows,cols,source,dest, visited
  ans = None
  queue = deque()
  queue.append((source[0],source[1],0)) ; visited[source[0]][source[1]] = 1
  while ans==None and len(queue)!=0:
    row,col,d = queue.popleft()
    if row==dest[0] and col==dest[1]: ans = d
    else:
      for dr,dc in delta:
        nr,nc = row+dr,col+dc
        if 0<=nr<rows and 0<=nc<cols and visited[nr][nc]==0:
            if grid[nr][nc] == '.' or grid[nr][nc] == 'B':
              queue.append((nr,nc,d+1)) ; visited[nr][nc] = 1

    visited[row][col] = 2
  return ans


def solve():
  global visited, source, dest, grid
  visited = [ [ 0 for c in range(cols) ] for r in range(rows) ]
  c = cols-1
  r = 0
  band = 0
  ans = 0
  predictHorse()
  ans = bfs()
  return ans

def main():
    global grid, cols,rows,dest,source
    line = stdin.readline().split()
    Cp = int(line[0])
    while Cp != 0:
        line = stdin.readline().split()
        rows,cols = int(line[0]),int(line[1])
        grid =  [ [] for i in range(rows)]
        for i in range(rows):
            line = stdin.readline().strip()
            for j in range(len(line)):
                if(line[j] == 'A'):
                    source= (i,j)
                if(line[j] == 'B'):
                    dest = (i,j)
                grid[i].append(line[j])
        ans = solve()
        if(ans!= None):
            print("Minimal possible length of a trip is {0}".format(ans))
        else:
            print("King Peter, you can't go now!")
        Cp-=1

main()

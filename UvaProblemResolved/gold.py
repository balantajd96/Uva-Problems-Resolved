#11561 - Getting Gold
from sys import stdin

grid,rows,cols = None,None,None
delta = [ (0,-1), (0,1), (1,0), (-1,0) ]

def dfs(visited, row, col):
  global grid,rows,cols,delta
  stack = [ (row, col) ] ; visited[row][col] = 1
  ans = 0
  while len(stack)!=0:
    r,c = stack.pop()
    #Verificar Caminos Validos Cercanos
    trap = 0
    for dr,dc in delta:
      if(grid[r+dr][c+dc] == 'T'):
          visited[r+dr][c+dc] = 1
          trap = 1
     #Si detecto una trampa en los lados, no puede seguir
    if(trap != 1):
        for dr,dc in delta:
            if(grid[r+dr][c+dc] == '.' and visited[r+dr][c+dc]==0):
                stack.append((r+dr,c+dc))
            elif(grid[r+dr][c+dc] == 'G' and visited[r+dr][c+dc]==0):
                visited[r+dr][c+dc] = 1
                ans +=1
                stack.append((r+dr,c+dc))
    visited[r][c] = 2
  return ans
def solve():
  visited = [ [ 0 for c in range(cols) ] for r in range(rows) ]
  c = cols-1
  r = 0
  while r<rows and c == cols-1:
      for c in range(cols):
          if(visited[r][c] == 0 and grid[r][c] == 'P'):
              ans = dfs(visited,r,c)
              break
      r=r+1
  return ans

def main():
  global grid,rows,cols
  line = stdin.readline().split()
  cols,rows = int(line[0]), int(line[1])
  while True:
    grid = [ None for r in range(rows) ]
    for r in range(rows): grid[r] = stdin.readline().strip()
    print(solve())

    line = stdin.readline().split()
    if(len(line) == 0):
        break
    cols,rows = int(line[0]), int(line[1])

main()

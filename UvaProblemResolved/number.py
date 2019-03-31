from sys import stdin

from heapq import heappop,heappush

#problem 929 - Number Maze

delta = [(0,1),(-1,0),(1,0),(0,-1)]


INF = float('inf')

def sssp(G,source,a):
  global col, fil
  dist = [ INF for i in range(col*fil) ];    dist[source] = 0
  visited = [ False for i in range(col*fil) ]
  heap = [ (a,source) ]
  while len(heap)!=0:
    d,u = heappop(heap)
    if not(visited[u]):
      visited[u] = True
      for v,w in G[u]:
        if dist[v]>d+w:
          dist[v] = d+w
          heappush(heap,(dist[v],v))
  return dist


def main():
    global fil, col
    nLab = int(stdin.readline().strip(""))
    while nLab >0:
          g = {}; n= 0; G= {}
          fil = int(stdin.readline().strip(""))
          col = int(stdin.readline().strip(""))
          for i in range(fil):
              c = [int(x) for x in stdin.readline().split()]
              for j in range(len(c)):
                  vertice = (i,j)
                  g[vertice] = (n,c[j])
                  G[n] = []
                  n+=1
          for v,w in g:
              for i in range(4):
                  f = v+delta[i][0]
                  t = w+delta[i][1]
                  if(f>= 0 and f<fil and t>= 0 and t< col):
                      G[g[(v,w)][0]].append(g[(f,t)])

          nLab-=1
          minway = sssp(G,0,g[(0,0)][1])
          print(minway[len(minway)-1])

main()

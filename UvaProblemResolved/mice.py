from sys import stdin
from heapq import heappop,heappush

#problem 1112 - Mice and Maze
INF = float('inf')

def sssp(G,source):
  global INF
  dist = [ INF for i in range(len(G)) ] ; dist[source] = 0
  visited = [ False for i in range(len(G)) ]
  heap = [ (0,source) ]
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
    global Nc, n, e, t ,m
    Nc = int(stdin.readline())
    line = stdin.readline()
    while(Nc!=0):
        n = int(stdin.readline().strip(""))
        e = int(stdin.readline().strip(""))-1
        t = int(stdin.readline().strip(""))
        m = int(stdin.readline().strip(""))
        g = dict()
        for i in range(n):
            g[i] = []
        while(m>0):
            t1  = stdin.readline().strip("\n").split(" ")
            t2 = [int(x) for x in t1]
            t2[0]-=1
            t2[1]-=1
            pair = (t2[0],t2[2])
            g[t2[1]].append(pair)
            m-=1
        res  = sssp(g,e)
        ans = 0
        for i in range(len(res)):
            if(res[i] <= t ):
                ans+=1
        print(ans)
        line = stdin.readline()
        Nc-=1
        if(Nc!=0):
            print("")


main()

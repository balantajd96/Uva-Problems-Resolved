from sys import stdin
from collections import deque
#problem 1148 - The mysterious X network
source,dest = None,None
grid = None

def bfs():
    global grid,dest,source,nCam
    ans= None
    visited = [ 0 for i in range(nCam)]
    queue = deque()
    queue.append((source,0)); visited[source] = 1
    while ans == None and len(queue)!=0:
        now,d = queue.popleft()
        if(now == dest):
            ans = d-1
            return ans
        else:
            i = 0
            while i< len(grid[now]):
                v = grid[now][i]
                if(visited[v] == 0):
                    queue.append((v,d+1)); visited[v] = 1
                i += 1
    return ans-1


def main():
    global grid,dest,source,nCam
    N = int(stdin.readline().strip())
    SpaceBlank = stdin.readline()
    while N!=0:
        nCam = int(stdin.readline().strip())
        grid = [[]for i in range(nCam)]
        for i in range(nCam):
            line = stdin.readline().split()
            p = int(line[0])
            line = [int(line[x]) for x in range(2,len(line))]
            grid[p] = line
        line = stdin.readline().split()
        source,dest = int(line[0]),int(line[1])
        SpaceBlank = stdin.readline()
        print("{0} {1} {2}".format(source,dest,bfs()))
        N-=1
        if(N!=0):
            print("")
main()

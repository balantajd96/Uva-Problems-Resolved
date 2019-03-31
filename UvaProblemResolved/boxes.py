from sys import stdin
#Problem 11003 - Boxes
def phi(W,L,M):
  N = len(W)
  n, m = 1,0
  tab = [[0 for _ in range(M+1)] for _ in range(N+1)]
  while n!= N+1:
    if(m == M+1):n,m = n+1,0
    else:
      tab[n][m] = tab[n-1][m]
      if(W[n-1] <= m):
        tab[n][m] = max(tab[n-1][m],1+tab[n-1][min(m-W[n-1],L[n-1])])
      m= m+1
  return tab[N][M]

def main():
    global tab
    while True:
        W = []
        L = []
        line = stdin.readline().split()
        numCajas = int(line[0])
        if(numCajas == 0):break
        M = 0
        for i in range(numCajas):
            line = stdin.readline().split()
            w = int(line[0])
            l = int(line[1])
            M = max(w+l,M)
            W.append(w)
            L.append(l)
        W.reverse()
        L.reverse()
        print(phi(W,L,M))

main()

#Problem 166 - Making Change
from sys import stdin
import math
D = [5,10,20,50,100,200]
INF = 9999999

def phi_tab(X):
  """Coin change for denominations in D with tabulation and memory
     optimization"""
  N = len(D)
  tab = [ INF for x in range(X+1) ] ; tab[0] = 0
  n,x = 1,0
  while n!=N+1:
    if x==X+1: n,x = n+1,0
    else:
      if D[n-1]<=x: tab[x] = min(tab[x],1+tab[x-D[n-1]])
      x += 1
  return tab[X]

def limiteCoinChange(x, d, l):
    ans = 0
    for i in reversed(range(6)):
        operator = min(x//d[i],l[i])
        if(d[i]<= x and operator != 0):
            x -= d[i]*operator
            ans += operator
    if(x !=0  ): return INF
    else:
        return ans


def main():
    global ha, dp
    tab = {}
    for i in range(5,205,5):
        tab[i] = phi_tab(i)
    while True:
        line = stdin.readline().split()
        ha = [ int(line[i]) for i in range(len(line)-1)]
        x = int(round(100*(float(line[len(line)-1]))))
        if(sum(ha)  == 0):break
        ans = limiteCoinChange(x,D,ha)
        for i in range(5,205,5):
            ans = min(ans,limiteCoinChange(x+i,D,ha)+tab[i])
        print('%3d' % ans)


main()

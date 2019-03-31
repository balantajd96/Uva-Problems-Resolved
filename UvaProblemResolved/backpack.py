#Problem 907 - Winterim Backpacking Trip
from sys import stdin
MAX = 610
sites = [ None for i in range(MAX) ]
sums,omin,omax,n,k = None,None,None,None,None

def check(res):
  global n,k,sites
  add = cont = i = 0
  while (i < n):
    if (sites[i] > res):
      return 0
    if (sites[i] + add > res):
      add = sites[i]
      cont += 1
    else:
      cont += sites[i]
    i += 1
  if (add):
    cont += 1
  return k

def solve():
  global sites,sums,omin,omax,n,k

  l = omin
  r = omax
  while (l <= r):
    mid = (l+r)/2
    if (check(mid)):
      r = mid-1
    else:
      l = mid+1

  return r

def main():
  global sites,n,k,omin,omax
  inp = stdin
  l = stdin.readline().strip()
  while len(l)>0:
    n,k = [ int(x) for x in l.split() ]
    n += 1
    omin,omax,sums = float('inf'),float('-inf'),0
    for i in range(n):
      sites[i] = int(inp.readline().strip())
      if sites[i]>omax: omax = sites[i]
      if sites[i]<omin: omin = sites[i]
      sums += sites[i]
    if sums== 0:
      print(0)
    else:
      print(solve())
    l = stdin.readline().strip()

main()

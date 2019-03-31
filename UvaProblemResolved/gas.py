#Problem 12321 - Gas Stations
from sys import stdin

def gas():
  global station, g , l
  inter = list()
  for i in range(len(station)):
      pair = (station[i][0]-station[i][1],station[i][0]+station[i][1])
      inter.append(pair)
  inter.sort()
  ans,low,n,ok,N = len(inter),0,0,True,len(inter)
  while ok and low<l and n!=N:
    ok = inter[n][0]<=low
    best,n = n,n+1
    while ok and n!=N and inter[n][0]<=low:
      if inter[n][1]>inter[best][1]:
        best = n
      n += 1
    ans-=1
    low = inter[best][1]
  ok = ok and low>=l
  if ok==False:
    ans = -1
  if(ans == []): return -1
  else:return ans


def main():
    global g, l, station , xi, ri
    pair  = stdin.readline().strip()
    j = pair.split(" ")
    l, g = int(j[0]), int(j[1])
    while(l != 0 and g != 0):

        station = list()
        for i in range(int(g)):
            pair  = stdin.readline().strip()
            j = pair.split(" ")
            xi, ri = int(j[0]), int(j[1])
            station.append((xi,ri))
        ans  = gas()
        print(ans)
        pair  = stdin.readline().strip()
        j = pair.split(" ")
        l, g = int(j[0]), int(j[1])




main()

from sys import stdin
import math
#Problem 10245 - The Closest Pair Problem
EPS,points = 1e-9,None

def distance(x1 , y1 ,x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def merge_sort(low, hi):
 if low+1 != hi:
    mid = low+((hi-low)//2)
    merge_sort(low, mid)
    merge_sort(mid, hi)
    merge(low, mid, hi)

def merge(p, q, r):

  global points
  a1 = list()
  for i in range(p, q):
    a1.append(points[i])

  a2 = list()
  for i in range(q, r):
    a2.append(points[i])
  n1,n2 = q-p,r-q
  i1,i2,n = 0,0,r-p
  for j in range(p, r):

    if i1<n1 and i2<n2:

      if a1[i1][1] < a2[i2][1]:
        points[j] = a1[i1]
        i1 += 1
      else:
        points[j] = a2[i2]
        i2 += 1
    elif i1<n1:
      points[j] = a1[i1]
      i1 += 1
    else:
      points[j] = a2[i2]
      i2 += 1

def divide(l,r):
    global pointy
    alt = []
    if((r-l) == 3):
        d1 = distance(points[l][0],points[l][1],points[l+1][0],points[l+1][1])
        d2 = distance(points[l+1][0],points[l+1][1],points[l+2][0],points[l+2][1])
        d3 = distance(points[l][0],points[l][1],points[l+2][0],points[l+2][1])
        return min(d1,d2,d3)
    elif((r-l) == 2):
       return distance(points[l][0],points[l][1],points[r-1][0],points[r-1][1])

    elif(r-l == 1):
        return   1e99

    else:
        mid = l+(r-l)//2
        L = divide(l,mid)
        R = divide(mid,r)
        ans = min(L,R)
        for i in range(l,r):
            if abs(points[mid][0]-points[i][0])< ans:
                alt.append(points[i])
        for j in range(len(alt)):
            for w in range(j+1,len(alt)):
                d =  distance(alt[j][0],alt[j][1],alt[w][0],alt[w][1])
                ans = min(d,ans)
    return ans






def solve():
  global points
  global men
  global pointy
  pointy = list()
  pointy = sorted(points, key = lambda element : element[1])
  points.sort()
  dx = divide(0,len(points))
  return dx

def main():
  global points
  n = int(stdin.readline())
  while n!=0:
    points = list()
    for i in range(n):
      tok = stdin.readline().split()
      points.append((float(tok[0]),float(tok[1])))
    ans = solve()
    if(ans < 10000):
         print('{:.4f}'.format(ans))
    else:
          print("INFINITY")
    n = int(stdin.readline())

main()

##https://www.cs.mcgill.ca/~cs251/ClosestPair/ClosestPairDQ.html#

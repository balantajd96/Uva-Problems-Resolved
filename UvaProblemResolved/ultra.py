#Problem 10810 - Ultra-QuickSort
from sys import stdin
MAX=50010
num=[None for i in range(MAX)]
aux=[None for i in range(MAX)]

def solve(low,hi):
	global num
	cuent=0
	if low+1 < hi:
		mid=low+((hi-low)>>1)
		cuent=cuent+solve(low,mid)
		cuent=cuent+solve(mid,hi)
		cuent=cuent+merge(low,mid,hi)
	return cuent

def merge(low, mid, hi):
	global aux, num
	cont=0
	for i in range(low,hi):
		aux[i]=num[i]
	l,r,i=low,mid,low
	while i!= hi:
		if l!=mid and r!=hi:
			if aux[l]<=aux[r]:
				num[i]=aux[l]
				l+=1
			else:
				num[i]=aux[r]
				r+=1
				cont=cont+(r-(i+1))
		elif r==hi:
			num[i]=aux[l]
			l+=1
		else:
			num[i]=aux[r]
			r+=1
		i+=1
	return cont

def main():
  global num
  inp = stdin
  n = int(stdin.readline().strip())
  while n>0:
    for i in range(n):
      num[i] = int(stdin.readline())
      #solve(0,n)
    print(solve(0, n))
    n = int(stdin.readline().strip())

main()

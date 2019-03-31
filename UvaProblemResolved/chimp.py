from sys import stdin

#Problem 10611 - The Playboy Chimp


def bSearchMax(Array, x):
	N = len(Array)
	ans = False
	if N >= 1:
		low, hi = 0, N
		while Array[low]!= x and low + 1 != hi:
			mid = low + ((hi-low)>>1)
			if Array[mid] < x:
				low = mid
			else:
				hi = mid
		ans = Array[low]
	return ans

def binSearchMin(Array,x):
	N = len(Array)
	ans = False
	if N >= 1 :
		low, hi = 0, N
		while low + 1 != hi:
			mid = low + ((hi-low)>>1)
			if Array[mid] > x:
				hi = mid
			else:
				low = mid
		ans = Array[hi]
	return ans

def solve(ladies, x):
	ansMax, ansMin = 'X', 'X'
	if  ladies[0]<x  and ladies[len(ladies)-1] > x:
		ansMax = bSearchMax(ladies,x)
		ansMin = binSearchMin(ladies,x)
	elif ladies[0]<x:
		ansMax = bSearchMax(ladies,x)
	elif ladies[len(ladies)-1] > x:
		ansMin = binSearchMin(ladies,x)
	print(ansMax,ansMin)



def main():
  inp = stdin
  inp.readline()
  ladies = [ int(x) for x in inp.readline().split() ]
  inp.readline()
  queries = [ int(x) for x in inp.readline().split() ]
  for x in queries:
    solve(ladies, x)

main()

from sys import stdin
import operator
#Problem 437 - The Tower of Babylon

block = []

def PermutacionesBase(x,y,z):
	global block
	block.append([x,z,y])
	block.append([x,y,z])
	block.append([y,z,x])
	block.append([y,x,z])
	block.append([z,x,y])
	block.append([z,y,x])

def aux_memoization(block,n,memo):
  ans = memo[n]
  if ans==None:
    ans = 0
    for i in range(n):
      if block[i][0]>block[n][0] and block[i][1]>block[n][1] :
        ans = max(ans,aux_memoization(block,i,memo))
    ans += block[n][2]
    memo[n] = ans
  return ans

def lis_memoization(block):
  N = len(block)
  ans = 0
  if N!=0:
    memo = [ None for i in range(N) ]
    for n in range(N):
      ans = max(ans,aux_memoization(block,n,memo))
  return ans


def main():
	global block,x,y,z
	line = 1
	case = 1
	while int(line) != 0:
		contador = 0
		line = int(stdin.readline().strip())
		while contador < line:
			j = stdin.readline().strip().split()
			x,y,z = [int(k) for k in j]
			PermutacionesBase(x,y,z)
			contador = contador + 1
		block.sort(key = operator.itemgetter(0, 1))
		block.reverse()
		if int(line) != 0:
			case=str(case)
			print("Case "+case+":","maximum height =",lis_memoization(block))
			case = int(case) + 1
			block = []


main()

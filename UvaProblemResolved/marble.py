from sys import stdin
#Problem 10474 - Where is the Marble?
marble,lenm = None,None

def divide(l,r,x):
    mid = l+(r-l)//2
    if(l+1 != r):
        if(marble[mid]== x):
            firstOcu = mid
            later_ocur = divide(l,mid,x)
            if(later_ocur != -1):
                return later_ocur
            else:
                return firstOcu

        elif (x < marble[mid] ):
            return divide(l,mid,x)
        else:
            return divide(mid,r,x)

    elif(l+1 == r):
        if marble[mid] == x:
            return mid
        else:
            return -1

def solve(x):
  global marble,lenm
  return divide(0,lenm,x)
def main():
  global marble,lenm
  inp = stdin
  cas = 1
  lenm,lenq = [ int(x) for x in inp.readline().split() ]
  while lenm+lenq!=0:
    marble = [ int(inp.readline()) for i in range(lenm) ]
    marble.sort()
    print('CASE# {0}:'.format(cas))
    for q in range(lenq):
      x = int(inp.readline())
      ans = solve(x)
      if ans==-1 or marble[ans]!=x:
          print('{0} not found'.format(x))
      else:
          print('{0} found at {1}'.format(x,ans+1))
    lenm,lenq = [ int(x) for x in inp.readline().split() ]
    cas += 1

main()

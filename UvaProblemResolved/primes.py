#Problem 3619 - Sum of Different Primes
from sys import stdin
import math
global prims, ans

def initAns():
    global ans, prims
    ans = []
    for i in range(1121):
        ans.append([])
        for j in range(15):
            ans[i].append([])
            for k in range(len(prims)+1):
                ans[i][j].append(-1)

def createAns(n,k,i):
    global prims,ans
    if(n == 0 and k == 0):return 1
    elif(n<0 or i>=len(prims) or k==0):return 0
    elif(ans[n][k][i]!=-1):return ans[n][k][i]
    else:
        ans[n][k][i] = createAns(n,k,i+1)+createAns(n-prims[i],k-1,i+1);
        return ans[n][k][i]

def createPrim():
    global prims
    prims = []
    prims.append(2)
    cont = 3
    while cont < 1120:
        band = 0
        for k in range(2,cont):
            if(cont%k==0):
                band  = 1
                break
        if(band != 1):
            prims.append(cont)
        cont += 2

def main():
    global prims, ans
    createPrim()
    initAns()
    while (True):
         n = stdin.readline()
         num = n.split(" ")
         n , k = int(num[0]), int(num[1])
         if(n == 0 and k == 0):
             break
         print(createAns(n,k,0))

main()

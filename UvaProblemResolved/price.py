#Problem 10313 - Pay the Price
from sys import stdin

def query0(n): return query2(n,0,n)
def query1(n,l0): return query2(n,0,l0)
def query2(n,l0,l1):
    ans,l1 = 0, min(l1,n)
    for l in range(l0,l1+1):
         ans += N[l][n]
    return ans

def main():
    global N
    N = list()
    for i in range(0,301):
        N.append([])
        for k in range(0,301):
            N[i].append(0)
    N[0][0]=1
    m,n,l = 1,0,1
    while m!= 301:
        if l == 301:
            m,n,l = m+1,0,1
        elif n == 301:
            n,l = 0, l+1
        else:
            if m<= n:
                N[l][n] += N[l-1][n-m]
            n+=1

    while (True):
         n = stdin.readline()
         num = n.split(" ")

         if(num[0 ]== ''):
             break
         if(len(num)==1):
             n, l1,l2 = int(num[0].strip(" ")), 0, 0
             print(query0(n))
         elif(len(num)==2):
             n, l1,l2 = int(num[0]), int(num[1].strip(" ")), 0
             print(query1(n,l1))
         else:
             n, l1,l2 = int(num[0]), int(num[1]), int(num[2].strip(" "))
             print(query2(n,l1,l2))

main()

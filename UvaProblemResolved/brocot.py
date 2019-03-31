from sys import stdin
#Problem 11350 - Stern-Brocot Tree

def solve(n1,d1,n2,d2):

    while True:
        if(n<d1+d2):break
        if(n1+n2 == m and d1+d2 == n):break
        if((d1+d2)*m < n*(n1+n2)):
            trazo.append("L")
            n2,d2 = n2+n1,d2+d1
        else:
            trazo.append("R")
            n1,d1 = n1+n2,d1+d2

def main():
    global m,n,trazo
    while True:
        line = stdin.readline().split()
        m,n = int(line[0]),int(line[1])
        trazo = []
        if(m == 1 and n==1 ):break
        solve(0,1,1,0)
        print("".join(trazo))

main()

from sys import stdin
INF = 999999999

#Problem 10401 - Injured Queen Problem
def solve(n,j):
    if n==N:return 1

    if mem[n][j] != INF:return mem[n][j]
    ans = 0
    if(T[n+1] == 0):
        for i in range(1,N+1):
            if(i!= j+1 and i!=j and i!= j-1):ans+= solve(n+1,i)
    elif(T[n+1]!=j+1 and T[n+1]!= j and T[n+1]!= j-1): ans+=solve(n+1,T[n+1])
    mem[n][j] = ans
    return mem[n][j]


def main():
    while True:
        global  T, N, mem
        line = stdin.readline()
        if(len(line) ==0):break
        T = ['x']
        for i in range(len(line)-1):
            T.append(line[i])
        for i in range(1,len(T)):
            if(T[i]== '?'):
                T[i] = 0
            elif(T[i].isdigit()== True):
                T[i] = int(T[i])
            else:
                T[i] = ord(T[i])+5-60
        N = len(T)-1
        mem = [[INF for i in range(16) ]for i in range(16)]
        ans = 0
        if(T[1] == 0):
            for i in range(1,N+1):ans += solve(1,i)
        else: ans+=solve(1,T[1])
        print("%d" % ans)

main()

from sys import stdin
#Problem 10718 - Bitmask

def ans():
    global N,L,U
    ans = 0
    for i in reversed(range(32)):
        p = ans|(1<<i)
        ll = (L>>i)
        uu = (U>>i)
        if((N>>i)&1):
            x = (ans>>i)
            if(x >= ll and x <=uu):continue
        else:
            x =(p>>i)
            if(x<ll or x> uu):continue
        ans = p

    return ans;


def main():
    global N,L,U
    line = stdin.readline().strip()
    while(line != ""):
        op = line.split(" ")
        N,L,U = int(op[0]), int(op[1]), int(op[2])
        print(ans())
        line = stdin.readline().strip()

main()

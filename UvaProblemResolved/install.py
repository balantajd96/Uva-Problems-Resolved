from sys import stdin
#Problem 1193 - radar installation

def distance(coord,coord2,d):
    return (((coord2[0]-coord[0])**(2)+(coord2[1]-coord[1])**(2))**(0.5)) <= d


def nradar():
    global N, d , coord
    inter = []
    for i in range(len(coord)):
        #print(coord[i][1],d)
        if(coord[i][1])> d:
            return -1
        else:
            resu =  ((d*d-coord[i][1]*coord[i][1])**(0.5))
            a = coord[i][0] - resu
            b = coord[i][0] + resu
            inter.append((a,b))

    inter.sort()
    r = -(1e+60)
    nradar = 0
    for i in range(len(coord)):
        if(inter[i][0] <= r):
            r = min(r,inter[i][1])
            continue
        nradar +=1
        r = inter[i][1]
    return nradar


def main():
    global N, d, coord
    arch = stdin
    cont = 1
    while(True):
        m = arch.readline().strip()
        num = m.split(" ")
        N , d = int(num[0]) , int(num[1])
        if(N == 0 and d == 0):
            break
        coord = list()
        for i in range(N):
            m = arch.readline().strip()
            pair = tuple()
            num =  m.split(" ")
            pair = (int(num[0]),int(num[1]))
            coord.append(pair)
        m = arch.readline().strip()
        #print(coord)
        ans = nradar()
        print("Case {0}: {1}".format(cont,ans))
        cont+=1

main()

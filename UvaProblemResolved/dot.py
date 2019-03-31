from sys import stdin
from operator import itemgetter
#Problem 10819 - Trouble of 13-Dots

MAX = 10000
cost = []
itemFavor =[]

def main():
    while True:
        line = stdin.readline().split()
        if(len(line) == 0):
            break
        money,nItem = int(line[0]),int(line[1])
        cost, itemFavor = [],[]
        cost.append('0')
        itemFavor.append('0')
        for i in range(nItem):
            line = stdin.readline().split()
            cost.append(int(line[0]))
            itemFavor.append(int(line[1]))
        tab = [-1 for i in range(MAX+1)]
        tab[0] = 0
        for i in range(1,nItem+1):
            for k in reversed(range(1,MAX+1)):
                if(k<cost[i]):
                    break
                tab[k]= max(tab[k],tab[k-cost[i]]+itemFavor[i])
        ans = 0
        for i in range(MAX+201):
            if((i>2000 and money+200>=i) or i<= money):
                ans = max(ans,tab[i])
        print(ans)


main()

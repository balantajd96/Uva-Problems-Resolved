from sys import stdin
import random
global d
d = [120,210,1540,7140,11628,24310,3003]

def choose2(x):
    return int((x*(x-1))>>1)
def choose3(x):
    return int(((x*(x-1)*(x-2))/6)+0.5)

high =  [44721360,181713] #Max 2 y 3

def combination(mid,x,k):
    if(k ==2):
        ans = choose2(mid)
    elif(k == 3):
        ans = choose3(mid)
    return ans

def binarySearch(x):            #Busqueda de coeficiente 2 y 3
    coefi = {}
    coefi[x] = [(x,1),(x,x-1)]
    for i in range(2,4):
        l,r = 0,high[i-2]
        while(l+1<=r):
            mid = (l+r)>>1
            val = combination(mid,x,i)
            if(val<=x):
                if(val == x):
                    coefi[x].append((mid,i))
                    coefi[x].append((mid,mid-i))
                    return coefi[x]
                l = mid+1
            else:
                r = mid
    return coefi[x]

def solve(x):
    global parent, cota
    if(x in parent):
        if(x in d):
            return parent[x]
        if(len(parent[x])>2):
            return parent[x]
        elif(len(parent[x]) <= 2 and len(parent[x]) >=1  and parent[x][0][0] != x):
            parent[x].append((x,1))
            parent[x].append((x,x-1))
            return parent[x]

        else:
            parent[x] = binarySearch(x)
            return parent[x]
    else:
        parent[x] = binarySearch(x)
        return parent[x]

def comb(n,k):
    res = int(((n*(n-1)*(n-2))/6)+0.5)
    for i in range(4,k+1):
        res =int((res * ((n-(i-1))/i))+0.5)
    return res

def main():
    global parent
    parent = {1:[()],2:[(2,1)], 3:[(3,1),(3,2)], 4:[(4,1),(4,3)],
                6:[(4,2),(6,1),(6,5)],
                10:[(5,2),(5,3),(10,1),(10,9)],
              120:[(10,3),(10,7),(16,2),(16,14),(120,1),(120,119)],
              210:[(10,4),(10,6),(21,2),(21,19),(210,1),(210,209)],
              1540:[(22,3),(22,19),(56,2),(56,54),(1540,1),(1540,1539)],
              7140:[(36,3),(36,33),(120,2),(120,118),(7140,1),(7140,7139)],
              11628:[(19,5),(19,14),(153,2),(153,151),(11628,1),(11628,11627)],
              24310:[(17,8),(17,9),(221,2),(221,219),(24310,1),(24310,24309)],
              3003:[(14,6),(14,8),(15,5),(15,10),(78,2),(78,76),(3003,1),(3003,3002)]}
    #Precalculo 4-30
    for l in range(4,31):
        i = 2
        while(True):
            ans = comb(i,l)
            if(ans>9999999999999999):
            #    print("({0},{1}),({2},{3}),{4}".format(i,l,i,i-l,ans))
                break
            else:
                if(ans>1):
                    if ans not in d:
                        if(ans not in parent):
                            parent[ans] = [(i,l),(i,i-l)]

                        else:
                            if((i,l) not in parent[ans]):
                                parent[ans].append((i,l))
                                parent[ans].append((i,i-l))
                    if i not in d:
                        if i not in parent:
                           parent[i] = [(i,1),(i,i-1)]
                        elif(parent[i][0][0] != i and len(parent[i])<4):
                           parent[i].append((i,1))
                           parent[i].append((i,i-1))

            i+=1
    nCases = int(stdin.readline().strip())
    for i in range(nCases):
        x = int(stdin.readline().strip())
        ans = solve(x)
        ans = sorted(ans, key=lambda x: x[:])
        cont = 0
        anterior = (0,0)
        string = ""
        for i in range(len(ans)):
            if(ans[i][0] == anterior[0] and ans[i][1] == anterior[1]):
                continue
            string +=  "({0},{1})".format(ans[i][0],ans[i][1]) + " "
            anterior = ans[i]
            cont+=1
        string = string[:len(string)-1]
        print(cont)
        print(string)
main()

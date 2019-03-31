from sys import stdin
#Problem 11413 - Fill the Containers

def busquedabin():
    global lista, m, n
    left = lista[0]
    right = 0
    med = 0
    for i in lista:
        right += i
    maximo = max(lista)
    while (left<=right):
            cont = 0
            add = 0
            add2 = 0
            med=left+((right-left)>>1)
            while cont < n:
                if(med < maximo):
                    add2 = m+1
                    cont = n
                elif(add + lista[cont] > med):
                    add2 += 1
                    add = lista[cont]
                else:
                    add +=  lista[cont]
                cont += 1
            if(add2 < m):
                right =  med-1
            else:
                left  = med +1
    return right+1

def main():
    global lista, m, n
    inp = stdin
    while True:
        lenm = inp.readline().strip()
        if(lenm == ''):
            break
        n,m = [int(x) for x in lenm.split()]
        lenm = inp.readline().strip()
        lista = [int(x) for x in lenm.split()]
        ans = busquedabin()
        print(ans)
main()

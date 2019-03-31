#Problem 10446 - The Marriage Interview :-)
from sys import stdin
def trib(n, back):
    global lista
    i = 1
    if(n<= 1): return 1
    if(lista[n][back]!=0 ): return lista[n][back]
    lista[n][back] = 1
    while(i<= back):
        lista[n][back]+=trib(n-i,back)
        i+=1
    return lista[n][back]

def main():
 global count,lista
 lista = []
 for i in range(61):
     lista.append([])
     for k in range(61):
         lista[i].append(0)
 casos = 1
 while True :
     n = stdin.readline()
     num = n.split(" ")
     num1,num2 = int(num[0]),int(num[1])
     if(num1>60 or num2 >60):
         break
     count = trib(num1,num2);
     print("Case {0}: {1}".format(casos,count))
     casos+=1

main()

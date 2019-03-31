from sys import stdin
#Problem 11584 - Partitioning by Palindromes

def esPalindrome(l):
    return l[::-1] == l


def palindrome(palabra):
    tab = [101 for i in range(len(palabra)+1)]
    tab[0] = 0
    cont = 0
    while cont<= len(palabra) :
        for i in range(cont):
            if(esPalindrome(palabra[i:cont]) == True):
                    tab[cont] = min(tab[cont],tab[i]+1)
        cont+=1
    return tab[len(palabra)]


def main():
    global tab
    inp = stdin
    lenm = inp.readline()
    for i in range(int(lenm)):
        palabra  =list(inp.readline().strip('\n'))
        if(esPalindrome(palabra)== True):
                print(1)
        else:
            print(palindrome(palabra))

main()

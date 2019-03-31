
#Juan Miguel Cardona- equidivsion

from sys import stdin



def main():
    global Nmatriz,colum
    line = int(stdin.readline().strip(""))
    while(line != 0):
        colum = []
        for i in range(line-2):
            line = stdin.readline().strip("")
            fil = line.split(" ")
            colum.append(fil)
        print(colum)
        line = int(stdin.readline().strip("")
        print(line)

main()

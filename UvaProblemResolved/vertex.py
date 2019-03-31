from sys import stdin
from collections import deque
#problem 280 - Vertex
graph,visited = None,None

def search(b):
    global graph,n
    cont = 0
    queue = deque()
    visited = [0 for _ in range(n+1)]
    queue.append(b)
    while len(queue)!=0:
        v = queue.popleft()
        for i in range(len(graph[v])):
            if(visited[graph[v][i]] == 0):
                visited[graph[v][i]] = 1
                queue.append(graph[v][i])
    text = ''
    for i in range(1,len(visited)):
        if(visited[i] == 0):cont+=1
    text+=str(cont)+ ' '
    for i in range(1,len(visited)):
        if(visited[i] ==0): text+=str(i)+' '
    print(text[:len(text)-1])

def main():
    global graph,n
    n = int(stdin.readline().strip())
    while n != 0:
        graph= [[]for i in range(n+1)]
        line = stdin.readline().strip().split()
        while (len(line)>1):
            nv = int(line[0])
            for j in range(1,len(line)-1):
                graph[nv].append(int(line[j]))
            line = stdin.readline().strip().split()
        case = stdin.readline().split()
        case = case[1:]
        for i in range(len(case)):case[i] =int(case[i])
        for t in case:
            search(t)
        n = int(stdin.readline().strip())

main()

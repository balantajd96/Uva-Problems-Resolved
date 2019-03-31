#11747 - Heavy Cycle Edges
from sys import stdin

class dforest(object):

  def __init__(self,size=100):
    """create an emtpy forest"""
    self.__parent = [ i for i in range(size) ]
    self.__size = [ 1 for i in range(size) ]
    self.__rank = [ 0 for i in range(size) ]

  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return len(self.__parent)

  def __contains__(self,x):
    """return if x is an element of the forest"""
    return 0 <= x < len(self)

  def find(self,x):
    """return the representative of the tree of x"""
    assert x in self
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self,x,y):
    """make the union of the trees of x and y"""
    assert x in self and y in self
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      nx,ny = self.__rank[rx],self.__rank[ry]
      if nx<=ny:
        self.__parent[rx] = ry
        self.__size[ry] += self.__size[rx]
        if nx==ny: self.__rank[ry]+=1
      else:
        self.__parent[ry] = rx
        self.__size[rx] += self.__size[ry]

  def size(self,x):
    """return the size of the tree of x"""
    assert x in self
    return self.__size[self.find(x)]

def kruskal(G):
  """G is a connected graph in adjacency list representation. For each
  vertex u in G, G[u] is the list of pairs (v0,w0),...(vn,wn) such that
  there is an edge between u and vi with weight wi (0 <= i <= n)"""
  edges = list()
  for i in range(len(G)):               # collect the edges in G
    for v,w in G[i]:
      edges.append((i,v,w))
  # sort the edges in ascending order w.r.t weights in the edges
  edges.sort(key=lambda x: x[2])
  df = dforest(len(G))
  i = 0
  while i!=len(edges):
    u,v,w = edges[i]
    if df.find(u)!=df.find(v):
      df.union(u,v)
    else:
        cost.append(edges[i][2])
    i += 1




def main():
    line = stdin.readline().split()
    global cost
    while True:
        cost = []
        N = int(line[0])
        M = int(line[1])
        G =  [[] for i in range(N)]
        if(N == 0 and M == 0):
            break
        for i in range(M):
            line = stdin.readline().split()
            u,v,w = int(line[0]),int(line[1]),int(line[2])
            G[u].append((v,w))
        kruskal(G)
        if(len(cost)== 0):
            print("forest")
        else:
            letra =""
            cost.sort()
            for i in range(len(cost)):
                letra+=str(cost[i])
                letra+= " "
            print(letra[:len(letra)-1])
        line = stdin.readline().split()


main()

from enum import Enum
import string
from typing import Any, Tuple
from typing import Optional
from typing import Dict, List
from typing import Callable
from collections import defaultdict
import networkx as network
import matplotlib.pyplot as plt

class EdgeType(Enum):
    directed = 1
    undirected = 2
class Vertex:
    data: Any
    index: int
    def __init__(self,data: None):
        self.data=data
        self.index=magazyn.t
        magazyn.t+=1
class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]
class Graph:
    adjacencies: Dict[Vertex, List[Edge]]
    def __init__(self,adjacencies= None):
        if(adjacencies == None):
            adjacencies={}
        self.adjacencies = adjacencies
    def create_vertex(self, data: Any) -> Vertex:
        vertex = Vertex(data)
        self.adjacencies[vertex.data,vertex.index]=[]
    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        xd=destination.data,destination.index
        self.adjacencies[source,source.index].append(xd)
    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        xd=(destination.data,destination.index)
        xd1=(source.data,source.index)
        self.adjacencies[source.data,source.index].append(xd)
        self.adjacencies[destination.data,destination.index].append(xd1)
    def __str__(self):
        edges = []
        for vertex in self.adjacencies:
            for neighbour in self.adjacencies[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append((vertex, neighbour))
        ##print(edges)
        d = defaultdict(list)
        d2 = defaultdict(list)
        for k, v in edges:
            d[k].append(v)
        for key,value in d.items():
            d2[key].append(value)
        t=''
        for key, value in d2.items():
            for x in key:
                t=t+str(x)+":"
            t+="---->"
            for y in value:
                t+=str(y)
            t+="\n"
        return t

    def addedgetype(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if(edge==1):
            self.add_directed_edge(source,destination,weight)
        elif(edge==2):
            self.add_undirected_edge(source,destination,weight)
    def show(self):
        G = network.Graph(self.adjacencies)
        network.draw(G, pos=network.circular_layout(G),  with_labels=True,arrows=False)
        plt.show()
def DF(graph, currentVertex, visiteds,destiny):
    visiteds.append(currentVertex)
    for vertex in graph.adjacencies[currentVertex]:
        if vertex not in visiteds:
            DF(graph, vertex, visiteds.copy(),destiny)
        if(visiteds[len(visiteds)-1]==destiny)and(len(visiteds[len(visiteds)-1])<=magazyn.dlugosc):
            magazyn.visited.append(visiteds)
            magazyn.dlugosc=len(visiteds[len(visiteds)-1])
def findminimalroads():
    min=1000
    new_k = []
    for elem in magazyn.visited:
        if elem not in new_k:
            new_k.append(elem)
    t=[]
    for x in new_k:
        t.append(len(x))
    for y in t:
        if(y<min and y!=0):
            min=y
    u=[]
    for h in new_k:
        if(min==len(h)):
            u.append(h)
    return u
def friend_path(graph,a,b)->List[Any]:
    DF(graph,a,[],b) 
    lista=findminimalroads()
    return lista
class magazyn:
    t=0
    visited=[[]]
    dlugosc=9999
graph = Graph()
def testbeta():
    a=Vertex("VI")
    b=Vertex("RU")
    c=Vertex("PA")
    d=Vertex("CO")
    e=Vertex("CH")
    f=Vertex("SU")
    g=Vertex("KE")
    magazyn.t=0
    graph.create_vertex("VI")
    graph.create_vertex("RU")
    graph.create_vertex("PA")
    graph.create_vertex("CO")
    graph.create_vertex("CH")
    graph.create_vertex("SU")
    graph.create_vertex("KE")
    graph.addedgetype(2,(a),(e))
    graph.addedgetype(2,(a),(b))
    graph.addedgetype(2,(a),(c))
    graph.addedgetype(2,(b),(c))
    graph.addedgetype(2,(b),(d))
    graph.addedgetype(2,(d),(e))
    graph.addedgetype(2,(e),(g))
    graph.addedgetype(2,(f),(g))
    ##lita=friend_path(graph,a,b)
    lita=friend_path(graph,(g.data,g.index),(b.data,b.index))
    ##depthFirst(graph,(g.data,g.index),[],(b.data,b.index))
    ##print(magazyn.visited)
    print(lita)
def testprojekt():
    a=Vertex("1")
    b=Vertex("2")
    c=Vertex("3")
    d=Vertex("4")
    e=Vertex("5")
    f=Vertex("6")
    g=Vertex("7")
    magazyn.t=0
    graph.create_vertex("1")
    graph.create_vertex("2")
    graph.create_vertex("3")
    graph.create_vertex("4")
    graph.create_vertex("5")
    graph.create_vertex("6")
    graph.create_vertex("7")
    graph.addedgetype(2,(a),(f))
    graph.addedgetype(2,(a),(b))
    graph.addedgetype(2,(b),(c))
    graph.addedgetype(2,(f),(e))
    graph.addedgetype(2,(d),(e))
    graph.addedgetype(2,(g),(c))
    graph.addedgetype(2,(g),(d))
    graph.addedgetype(2,(f),(a))
    ##graph.addedgetype(2,(f),(g))
    lita=friend_path(graph,(a.data,a.index),(g.data,g.index))
    ##depthFirst(graph,(g.data,g.index),[],(b.data,b.index))
    ##print(magazyn.visited)
    print(lita)
def testomega():
    a=Vertex("Olsztyn")
    b=Vertex("Radom")
    c=Vertex("Rzym")
    d=Vertex("Warszawa")
    e=Vertex("Helsinki")
    f=Vertex("SUwalki")
    g=Vertex("Moskwa")
    magazyn.t=0
    graph.create_vertex("Olsztyn")
    graph.create_vertex("Radom")
    graph.create_vertex("Rzym")
    graph.create_vertex("Warszawa")
    graph.create_vertex("Helsinki")
    graph.create_vertex("SUwalki")
    graph.create_vertex("Moskwa")
    graph.addedgetype(2,(a),(f))
    graph.addedgetype(2,(a),(b))
    graph.addedgetype(2,(a),(c))
    graph.addedgetype(2,(e),(f))
    graph.addedgetype(2,(f),(d))
    graph.addedgetype(2,(d),(g))
    graph.addedgetype(2,(e),(g))
    graph.addedgetype(2,(f),(g))
    lita=friend_path(graph,(a.data,a.index),(g.data,g.index))
    ##depthFirst(graph,(g.data,g.index),[],(b.data,b.index))
    ##print(magazyn.visited)
    print(lita)
##testomega()
##testbeta()
testprojekt()
print(graph)
graph.show()
'''
def test1():
    graph.addedgetype(1,("v0"),("v1"))
    graph.addedgetype(1,("v0"),("v5"))
    graph.addedgetype(1,("v1"),("v3"))
    graph.addedgetype(1,("v2"),("v1"))
    graph.addedgetype(1,("v3"),("v4"))
    graph.addedgetype(1,("v4"),("v1"))
    graph.addedgetype(1,("v4"),("v5"))
    graph.addedgetype(1,("v5"),("v1"))
    graph.addedgetype(1,("v5"),("v0"))
def test2():
    graph.addedgetype(1,("v0"),("v1"),6)
    graph.addedgetype(1,("v0"),("v5"),4)
    graph.addedgetype(1,("v5"),("v2"),3)
    graph.addedgetype(1,("v2"),("v3"),1)
    graph.addedgetype(1,("v1"),("v4"),1)
    graph.addedgetype(1,("v4"),("v2"),1)
def test3():
    graph.addedgetype(2,("v0"),("v1"))
    graph.addedgetype(2,("v0"),("v5"))
    graph.addedgetype(2,("v1"),("v3"))
    graph.addedgetype(2,("v2"),("v1"))
    graph.addedgetype(2,("v3"),("v4"))
    graph.addedgetype(2,("v4"),("v1"))
    graph.addedgetype(2,("v4"),("v5"))
def test4():
    graph.addedgetype(2,("v0"),("v1"),2)
    graph.addedgetype(2,("v1"),("v5"),3)
    graph.addedgetype(2,("v1"),("v3"),4)
    graph.addedgetype(2,("v2"),("v1"),5)
    graph.addedgetype(2,("v3"),("v4"),6)
    graph.addedgetype(2,("v4"),("v1"),5)
    graph.addedgetype(2,("v4"),("v5"),3)
'''
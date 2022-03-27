from typing import Any, List, Callable, Union, Optional
import treelib as tr
from itertools import groupby
import numpy as NP
import itertools as it
from copy import copy,deepcopy
class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'
    def __init__(self,value):
        self.value=value
        self.right_child = None
        self.left_child = None
    def is_leaf(self) -> bool:
        if (self.right_child is None and self.left_child is None):
            return True
        else:
            return False
    def add_left_child(self, value: Any):
        self.left_child=BinaryNode(value)
    def add_right_child(self, value: Any):
        self.right_child=BinaryNode(value)
    def traverse_in_order(self, visit: Callable[[Any], None])->None:
        if (self.left_child is not None):
            self.traverse_in_order(visit)
        visit(self)
        if (self.right_child is not None):
            self.traverse_in_order(visit)
    def traverse_pre_order(self, visit: Callable[['BinaryNode'], None]) -> None:
        visit(self)
        if (self.left_child is not None):
            self.traverse_pre_order(visit)
        if (self.right_child is not None):
            self.traverse_pre_order(visit)
    def traverse_post_order(self, visit: Callable[['BinaryNode'], None]) -> None:
        if (self.left_child is not None):
            self.traverse_pre_order(visit)
        if (self.right_child is not None):
            self.traverse_pre_order(visit)
        visit(self)
    def __str__(self):
        return str(self.value)
    def print(tre: 'BinaryNode'):
        print(tre.value)
    def Print_Tree(self,s:tr.Tree):
        if self.left_child is not None:
            s.create_node(str(self.left_child),str(self.left_child),parent=str(self.value)) 
            self.left_child.Print_Tree(s)
        if self.right_child is not None:
            s.create_node(str(self.right_child),str(self.right_child),parent=str(self.value))
            self.right_child.Print_Tree(s)
class BinaryTree:
    root: BinaryNode
    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.traverse_in_order(visit)
    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.traverse_post_order(visit)
    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.traverse_pre_order(visit)
    def __init__(self, root: BinaryNode = None) -> None:
        if root is None:
            self.root = BinaryNode()
        else:
            self.root = root
    def showt(self):
        s=tr.Tree()
        s.create_node(str(self.root.value),str(self.root.value))
        self.root.Print_Tree(s)
        s.show()
class E:
    b=0
    t=[]
    liscie=[]
def isleaf(x):
    if(x.left_child is None and  x.right_child is None):
        return True
    return False
def wywal(root):
    if root is not None:
        return None
def ilesciezek(drzewo: BinaryNode):
    E.b+=1
    if (drzewo.left_child is not None):
        ilesciezek(drzewo.left_child)
    if (drzewo.right_child is not None):
        ilesciezek(drzewo.right_child)
    if(isleaf(drzewo)==True):
        E.liscie.append(drzewo.value)
def znajdzsciezke(drzewo: BinaryNode):
    E.t.append(str(0))
    E.t.append(str(drzewo.value))
    while 1:
        if drzewo.left_child is not None:
            E.t.append(str(drzewo.left_child.value))
            if isleaf(drzewo.left_child)==True:
                drzewo.left_child=wywal(drzewo.left_child)    
                return drzewo
            drzewo=drzewo.left_child 
        if drzewo.right_child is not None:
            E.t.append((str(drzewo.right_child)))
            if(isleaf(drzewo.right_child )==True):    
                drzewo.right_child=wywal(drzewo.right_child)    
                return drzewo
            drzewo=drzewo.right_child 
def findallways(drzewo: BinaryNode):
            ilesciezek(drzewo)
            x=E.b
            for d in range(E.b-1):
                znajdzsciezke(drzewo)
            x=[list(x[1]) for x in it.groupby(E.t, lambda x: x=='0')] 
            b=0
            for a in range(len(x)):
                if a%2==0:
                    x.pop(a-b)
                    b+=1
            b=0
            c=0
            wynika=[[],[]]
            for t in x:
                for u in t:
                    b+=E.liscie.count(int(u))
                if(b!=0):
                    wynika.append(t)
                    b=0
                else:
                    b=0
            return wynika
def all_equal_paths1(tree: BinaryTree, suma: Any) ->List[List[BinaryNode]]:
    drzewo=deepcopy(tree.root)
    lista=findallways(drzewo)
    sumy=0
    print("wszystkie sciezki :" ,lista)
    wynik=[[],[]]
    for t in lista:
        for o in t:
            sumy+=int(o)
        if(sumy==suma):
            wynik.append(t)
            sumy=0
        sumy=0
    return wynik
tree: BinaryNode = BinaryNode(1)
tree.add_left_child(2)
tree.add_right_child(5)
tree.left_child.add_left_child(9)
tree.left_child.add_right_child(3)
tree.left_child.right_child.add_right_child(17)
tree.left_child.left_child.add_left_child(11)
tree.right_child.add_left_child(4)
tree.right_child.add_right_child(7)
tree.right_child.right_child.add_right_child(10)
treee: BinaryTree = BinaryTree(root=tree)
treee.showt()
lista=all_equal_paths1(treee,23)
treee.showt()
print(*lista)


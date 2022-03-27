from typing import Any

class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None
    def push(self, data = any)-> None:
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    def append(self,data=any)->None:
        new_node=Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node;
    def node(self, at: int) -> Node:
        a=0
        if self.start_node is None:
            print("lista pusta")
            return
        else:
            n = self.start_node
            while n is not None:
                if a==at:
                    return n.item
                a+=1
                n = n.ref
            print("wskazana pozycja poza lista")
    def insert(self, value: Any, after: Node) ->None:
        new_node = Node(value)
        if self.start_node is None:
            return 0
        elif self.start_node==after:
            new_node = Node(value)
            new_node.ref = self.start_node
            self.start_node= new_node
            return
        n = self.start_node
        while n.ref is not None and n.item!=after:
            n=n.ref
        new_node = Node(value)
        new_node.ref = n.ref
        n.ref = new_node
    def remove_last(self) -> Any:
        if self.start_node is None:
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        temp=n.ref.item
        n.ref = None
        return temp
    def remove(self,after: Node) ->None:
        n = self.start_node
        if n is None:
            print("pusta lista")
            return
        if n.item == after:
            n.ref=n.ref.ref
            return
        while n.ref is not None:
            if n.item == after:
                break
            n = n.ref
        if n.ref is None:
            return
        else:
             n.ref=n.ref.ref
             return
    def pop(self) -> Any:
        temp=self.start_node.item
        if self.start_node is None:
            print("pusta lista")
            return
        self.start_node =self.start_node.ref
        return temp



            
def printlist(self):
    a=0
    if self.start_node is None:
        print("Brak elementów")
        return
    else:
        n = self.start_node
        while n is not None:
            print(n.item , "-> " ,end = '')
            a+=1
            n = n.ref
            if(a==lenlist(lista)-1):
                print(n.item)
                break
        print(" ")
def lenlist(self):
    a=0
    if self.start_node is None:
        return 0
    else:
        n = self.start_node
        while n is not None:
            a+=1
            n = n.ref
    return a

lista=LinkedList()
lista.push(4)
lista.push(5)
lista.push(9)
lista.append(7)
lista.insert(6,7)
print("lista pierwotna")
printlist(lista)
print("3 element listy ")
print(lista.node(2)) ## jak  w  tablicach zaczynamy od 0 
print("aktualna dlugosc listy",lenlist(lista))
print("usun ostatni element ")
print(lista.remove_last())
printlist(lista)
print("dlugosc listy po usuwaniu ost ")
print("aktualna dlugosc listy",lenlist(lista))
print("usun element po 5 ")
lista.remove(5)
print("lista po ")
printlist(lista)
print("aktualna dlugosc listy",lenlist(lista))
print("usuwanie pierwszego elementu i zwracanie ")
print(lista.pop())
print(lenlist(lista))
printlist(lista)
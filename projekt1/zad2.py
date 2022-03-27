import copy
class Node():
    def __init__(self, data):
        self.item = data
        self.ref = None

class Stack():
    def __init__(self):
        self.top = Node("item")
        self.size = 0
    def push(self, element: any) -> None:
        n=Node(element)
        if n is None:
            return
        n.item=element
        n.ref=self.top
        self.top=n
        self.size+=1
    def pop(self) -> any:
        if self.top is None:
            print("pusty stos")
            return  
        temp=self.top.item
        self.top=self.top.ref
        self.size=self.size-1
        return temp 
def len(self):
    return self.size

def printa(self):
    selfa = copy.deepcopy(self) 
    if selfa.top is None:
        return  
    while selfa.top.ref is not None:
        print(selfa.top.item)
        selfa.top=selfa.top.ref
    return



    
s = Stack()
a = 22
b = 33
c = 34
t = Stack()

t.push( a)
t.push( b)
t.push( c)

print("wypisywane elementy to  :")
printa(t)
print("ilosc elementów to :",len(t))
print("usuwam i wyswietlam  1 raz ", t.pop())
print("ilosc elementów to :",len(t))
print("usuwam i wyswietlam  2 raz ", t.pop())
print("ilosc elementów to :",len(t))
print("usuwam i wyswietlam  3 raz ", t.pop())
print("ilosc elementów to :",len(t))

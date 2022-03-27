class Node():
    def __init__(self, item):
        self.item = item
        self.ref = None

class Queue():
    def __init__(self):
        self.top = self.bot = None
        self.size = 0
    def peek(self) -> any:
        return self.top.item 
    def enqueue(self, element:any) -> None:
        temp = Node(element)
        if self.bot == None:
            self.top = self.bot = temp
            self.size+=1
            return
        self.bot.ref = temp
        self.bot = temp
        self.size+=1
    def dequeue(self):
        if self.size==0:
            return
        temp = self.top.item
        self.top = self.top.ref
        self.size-=1
        return temp

def printq(self):
    a=0
    temp=self.top
    while temp is not None:
        if  lenq(self)-1==a:
            print(temp.item,end="")
            return
        print(temp.item,end="->")
        a+=1
        temp=temp.ref    
def lenq(self):
    return self.size
print("SPIS TRESCI  \n ")
print("klient obslugiwany = KOMENDA dequeque \n ")
print("nastepny w kolejce  = KOMENDA peek \n ")
print("ile osob w kolejce:  = FUNKCJA  len \n ")
print("kolejka wyglada nastepujaca : = FUNKCJA PRINT  ")
print("\n ")
que=Queue()
que.enqueue("klient 1 ")
que.enqueue("klient 2 ")
que.enqueue("klient 3 ")
que.enqueue("klient 4 ")
que.enqueue("klient 5 ")
que.enqueue("klient 6 ")
print("kolejka wyglada nastepujaca : ")
printq(que)
print("\n")
print("klient obslugiwany: " ,que.dequeue())
print("nastepny w kolejce : " ,que.peek())
print("ile osob w kolejce: " ,lenq(que))
print("kolejka wyglada nastepujaca : ")
print("\n")
printq(que)
print("\n")
print("do kolejki dochodzi 2: ")
que.enqueue("klient 7 ")
que.enqueue("klient 8 ")
print("klient obslugiwany: " ,que.dequeue())
print("nastepny w kolejce : " ,que.peek())
print("ile osob w kolejce: " ,lenq(que))
print("kolejka wyglada nastepujaca : ")
print("\n")
printq(que)
print("\n")
print("klient obslugiwany: " ,que.dequeue())
print("nastepny w kolejce : " ,que.peek())
print("ile osob w kolejce: " ,lenq(que))
print("kolejka wyglada nastepujaca : ")
print("\n")
printq(que)
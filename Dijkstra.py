from abc import ABC, abstractmethod

class INode(ABC):
    @abstractmethod
    def get_id(self)-> int:pass

    @abstractmethod
    def get_neighbours(self)-> list:pass

class Node(INode):
    def __init__(self,id:int):
        self._neighbours = []
        self._id = id
        
    def get_id(self): return self._id

    def get_neighbours(self): return self._neighbours
    
    def set_neighbours(self, *neighbours:dict):
        for args in neighbours:
            self._neighbours.append(args)

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
#{"next": , "distance": }
node0.set_neighbours({"next":node1,"distance":3},{"next":node4, "distance":3})
node1.set_neighbours({"next":node2, "distance":1})
node2.set_neighbours({"next":node3, "distance":3},{"next":node5 , "distance":1})
node3.set_neighbours({"next":node1, "distance":3})
node4.set_neighbours({"next":node5 , "distance": 2})
node5.set_neighbours({"next":node0 , "distance": 6},{"next": node3, "distance":1})
S = []
Q = [node0,node1,node2,node3,node4,node5]
d = []
p = []

for element in Q:
    d.append(100000)#przyjmuję za nieskończoność taką liczbę z braku pomysłów
    p.append(-1)
    
d[0] = 0#element startowy
while Q:
    i = 0
    counter = 0
    mn = int(d[Q[0].get_id()])
    for node in Q:
        ind = node.get_id()
        #print(d)
        if d[node.get_id()] < mn:
            print("tutaaaaj")
            mn = d[node.get_id()]
            i = counter
        counter+=1
    
    print(str(mn)+"###########")
    print(str(i)+"###########")
    print(Q[i].get_id())
    
    S.append(Q.pop(i))#przeniesienie wierzchołka z Q do S o najmniejszym koszcie dojścia

    w:list = S[-1].get_neighbours()

    for element in w:#iteruj przez wierzchołki
        if element["next"] in Q:# jeśli wierzchołek jest w Q
            if d[element["next"].get_id()] > d[S[-1].get_id()] + element["distance"]:
                d[element["next"].get_id()] = d[S[-1].get_id()] + element["distance"]
                p[element["next"].get_id()] = S[-1].get_id()
                
        else:
            continue
    print("-----------------------------")
    print(Q)
    print("-----------------------------")
    print(S)
    print("-----------------------------")
    print("[0, 1, 2, 3, 4, 5]")
    print(d)
    print(p)
    print("-----------------------------")


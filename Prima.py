from abc import ABC, abstractmethod
class INode(ABC):
    @abstractmethod
    def get_id(self)-> int:pass

    @abstractmethod
    def get_neighbours(self)-> list:pass

class Node(INode):
    def __init__(self,id:int):
        """konstruktor klasy Node
        
        Arguments:
            INode {[klasa abstrakcyjna]} -- [potrzebny do lepszej realizacji zasad OOP]
            id {int} -- [identyfikator wierzchołka]
        """
        self._neighbours = []
        self._id = id
        
    def get_id(self): return self._id

    def get_neighbours(self): return self._neighbours

    def set_neighbours(self, *neighbours:dict):
        for args in neighbours:
            self._neighbours.append(args)
def main():
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    #{"next": , "distance": }
    node0.set_neighbours({"next":node1,"distance":5},{"next": node3 , "distance":9 },{"next": node6 , "distance":3})
    node1.set_neighbours({"next":node0, "distance":5},{"next":node2 , "distance":9 },{"next": node5, "distance":6 },{"next": node4 , "distance":8 },{"next": node7, "distance": 7})
    node2.set_neighbours({"next":node1 , "distance":9 }, {"next": node3, "distance":9 },{"next":node4, "distance": 4},{"next": node6, "distance":5 },{"next": node7, "distance": 3})
    node3.set_neighbours({"next":node0 , "distance": 9},{"next": node2, "distance": 9},{"next": node6, "distance": 8})
    node4.set_neighbours({"next":node1, "distance": 8},{"next":node5 , "distance": 2},{"next":node2 , "distance": 4},{"next": node6, "distance": 1},)
    node5.set_neighbours({"next":node1 , "distance": 6},{"next":node4 , "distance": 2},{"next": node6 , "distance": 6})
    node6.set_neighbours({"next":node5, "distance": 6},{"next": node3, "distance": 8 },{"next": node0 , "distance": 3},{"next":node4 , "distance":1 },{"next": node2 , "distance": 5},{"next": node7, "distance":9 })
    node7.set_neighbours({"next":node6, "distance": 9},{"next": node1, "distance":7 },{"next":node2, "distance": 3})
    Graf = [node0,node1,node2,node3,node4,node5,node6,node7]#wierzchołki grafu
    n:int = len(Graf)    
    Q = []
    visited = []
    for element in Graf: visited.append(False)
    T = []
    v = 0
    visited[v] = True
    suma_wag = 0
    for x in range(n-1):
        #print("############################")
        #print(f"JESTEM W {v}")
        neighbours:list = Graf[v].get_neighbours()
        neighbour:dict = {"next":INode,"distance":int}
        for neighbour in neighbours:
            if visited[neighbour["next"].get_id()] == False:
                Q.append((neighbour["next"], neighbour["distance"],Graf[v].get_id(),(neighbour["next"].get_id())))
                #print("tutaj")
            #print("!!!!------!!!!")

        #print(f"to jest nie sortowane Q: {Q}")
        esc = False
        while not esc:
            Q.sort(key = lambda x: x[1])
            #print(f"------to jest Q: {Q}")
            u = Q.pop(0)
            #print(u)
            if visited[u[0].get_id()] == True:
                continue
            else:
                T.append(f"{u[2]}-->{u[0].get_id()}: {u[1]} ")
                visited[u[0].get_id()] = True
                v = u[0].get_id()
                suma_wag+=u[1]
                esc = True
            print(T)
            print(f"Suma wag: {suma_wag}")
            
            #print(visited)
    
    print(T)
    
                
if __name__ == "__main__":
    main()
    
    


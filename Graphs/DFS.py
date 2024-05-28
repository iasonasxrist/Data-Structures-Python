from collections import defaultdict
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    
    def BFS(self, startFromVertex):
        color = [False ] * len(self.graph)
        distance = [0] * len(self.graph)
        predecessor = [-1] * len(self.graph)
        queue=[startFromVertex]
        color[startFromVertex] = True

        while queue:
            s = queue.pop(0)
            print((s, distance[s]), predecessor[s])

            for adj in self.graph[s]:
                
                if color[adj] == False:
                    predecessor[adj] = s
                    distance[adj] = distance[s] + 1
                    queue.append(adj)
                    color[adj] = True
        return predecessor

    def doesPathExistsRec(self, u, v, pred):
        if u == v :
            print("yes")
            return True
        if pred[v] == -1:
            print("nit")
            return False   

    def doesPathExists(self, u, v):
        pred =  self.BFS(u)
        return self.doesPathExistsRec(u, pred[v], pred)



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.doesPathExists(0, 2)
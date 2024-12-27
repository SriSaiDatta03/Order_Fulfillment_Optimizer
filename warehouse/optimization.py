import networkx as nx

class WarehouseGraph:
    def __init__(self):
        self.graph=nx.Graph()
    
    def add_path(self,node1,node2,distance):
        self.graph.add_edge(node1,node2,weight=distance)

    def shortest_path(self,start,end):
        return nx.shortest_path(self.graph,source=start,target=end,weight="weight")
    
import numpy as np
from abc import ABC, abstractmethod

class Vertex:
    def __init__(self):
        pass


class Edge:
    def __init__(self):
        pass
    

class Graph(ABC):
    @abstractmethod
    def add_edge(self, e : Edge) -> Graph:
        assert isinstance(e, Edge)
    
    @abstractmethod
    def add_vertex(self, v : Vertex) -> Graph:
        assert isinstance(v, Vertex)
        
class UndirectedGraph(Graph):
    pass
class DirectedGraph(Graph):
    pass
class WeightedDirectedGraph(Graph):
    pass
class WeightedUndirectedGraph(Graph):
    pass
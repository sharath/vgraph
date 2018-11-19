from .graph import Graph
from .vertex import Vertex

def generate_K(x):
    g = Graph()
    for i in range(5):
        g.add_vertex(Vertex(name=i))
        for j in range(i):
            g.add_edge(a=i, b=j)
    return g
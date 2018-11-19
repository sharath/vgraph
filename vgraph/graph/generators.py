from .graph import Graph
from .vertex import Vertex
import numpy as np

def generate_K(x):
    spacing = 2*np.pi/(x)
    g = Graph(monitor=False, figsize=(x, x))
    for i in range(x):
        g.add_vertex(Vertex(name=i, position=((x+3)*np.cos(spacing*i), (x+3)*np.sin(spacing*i)), radius=1))
        for j in range(i):
            g.add_edge(a=i, b=j)
    return g
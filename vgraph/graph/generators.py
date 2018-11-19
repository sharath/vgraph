from .graph import Graph
from .vertex import Vertex
import numpy as np

def generate_K(x):
    spacing = 2*np.pi/(x)
    g = Graph(monitor=False)
    for i in range(x):
        g.add_vertex(Vertex(name=i, position=(40*np.cos(spacing*i), 40*np.sin(spacing*i))))
        for j in range(i):
            g.add_edge(a=i, b=j)
    return g
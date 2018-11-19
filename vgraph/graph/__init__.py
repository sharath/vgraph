import numpy as np
from abc import ABC, abstractmethod

from ..viz import Monitor


__vradius = 10
__vcolor = (255, 255, 255)
__rcolor = (0, 0, 0)
__ecolor = (0, 0, 0)


def set_vradius(value):
    __vradius = value
    

def set_vcolor(value):
    __vcolor = value
    
    
def set_rcolor(value):
    __rcolor = value
    
    
def set_ecolor(value):
    __ecolor = value

    
class Vertex:
    def __init__(self, name, value, **kwargs):
        self.name = name
        self.value = value
        self.radius = kwargs['radius'] if 'radius' in kwargs else __vradius
        self.color = kwargs['color'] if 'color' in kwargs else __vcolor
        self.rcolor = kwargs['rcolor'] if 'rcolor' in kwargs else __rcolor
        self.position = kwargs['position'] if 'position' in kwargs else (None, None)


class Edge:
    def __init__(self, a : Vertex, b : Vertex, **kwargs):
        assert isinstance(a, Vertex)
        assert isinstance(b, Vertex)
        self.a = a
        self.b = b
        self.loop = True a is b else False
        self.weight = kwargs['weight'] if 'weight' in kwargs else None
        self.color = kwargs['color'] if 'color' in kwargs else __ecolor
    

class Graph:
    def __init__(self, directed=False, weighted=False):
        self._directed = directed
        self._weighted = weighted
        self._alist = {}
        self._vertices = {}

        
    def add_edge(self, a, b, **kwargs):
        assert a in self._vertices
        assert b in self._vertices
        e = Edge(self._vertices[a], self._vertices[b])
        
        self._alist[a].append(e)
        if not directed:
            self._alist[b].append(e)
        
        
    def add_vertex(self, v : Vertex):
        assert isinstance(v, Vertex)
        assert v.name not in self._vertices
        
        self._alist[v.name] = []
        self._vertices[v.name] = v
        

class GraphMonitor(Monitor):
    pass
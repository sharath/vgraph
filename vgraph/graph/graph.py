from collections import deque, namedtuple
from ..viz import Monitor
from .vertex import Vertex
from .edge import Edge


class Graph:
    def __init__(self, directed=False, weighted=False, monitor=True):
        self._directed = directed
        self._weighted = weighted
        self._alist = {}
        self._vertices = {}
        self._monitor = monitor
        self._gmonitor = GraphMonitor(self) if monitor else None
    
    def show(self):
        pass
    
    def render(self):
        assert self._monitor
        return self._gmonitor.render()

        
    def add_edge(self, a, b, **kwargs):
        assert a in self._vertices
        assert b in self._vertices
        e = Edge(self._vertices[a], self._vertices[b])
        
        self._alist[a].append(e)
        if not self._directed:
            self._alist[b].append(e)
        
        if self._monitor:
            self._gmonitor.record()
        
        
    def add_vertex(self, v):
        assert v.name not in self._vertices
        
        self._alist[v.name] = []
        self._vertices[v.name] = v
        
        if self._monitor:
            self._gmonitor.record()

            
    def save(self):
        pass

    
class GraphMonitor(Monitor):
    def __init__(self, g):
        super(GraphMonitor, self).__init__()
        self._g = g
        self._frame = namedtuple('frame', ('step', 'alist', 'vertices'))

    def record(self):
        self._it += 1
        self._recording.append(self._frame(self._it, dict(self._g._alist), dict(self._g._vertices)))
        


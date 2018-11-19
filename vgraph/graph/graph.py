from collections import deque, namedtuple
from tempfile import TemporaryFile as tf

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Circle, ConnectionPatch

from ..viz import Monitor
from .vertex import Vertex
from .edge import Edge


class Graph:
    def __init__(self, directed=False, weighted=False, monitor=True, **kwargs):
        self._directed = directed
        self._weighted = weighted
        self._alist = {}
        self._vertices = {}
        self._monitor = monitor
        self._gmonitor = GraphMonitor(self) if monitor else None
        self.figsize = (10, 10)
        self.xmin, self.xmax = -1, 1
        self.ymin, self.ymax = -1, 1
        
    
    def show(self, filename=None, **kwargs):
        tsx, tsy = kwargs.get('tsx', 0), kwargs.get('tsy', 0)
        fig, ax = plt.subplots(figsize=self.figsize)
        
        ax.axis('equal')
        ax.set_xticks([]), ax.set_yticks([])
        sns.despine(left=True, bottom=True, right=True, top=True)
        
        ax.set_xlim((min(self.ymin, self.xmin), max(self.ymax, self.xmax)))
        ax.set_ylim((min(self.ymin, self.xmin), max(self.ymax, self.xmax)))
        
        for name, v in self._vertices.items():
            vx, vy = v.position
            c = Circle((vx, vy), v.radius, zorder=20)
            c.set_edgecolor(v.rcolor)
            c.set_facecolor(v.color)
            ax.annotate(name, xy=(vx, vy), fontsize=v.tsize, ha='center', xytext=(vx+tsx, vy+tsy), color=v.tcolor, zorder=21)
            ax.add_artist(c)
            
            for e in self._alist[name]:
                l = ConnectionPatch(e.a.position, e.b.position, 'data')
                ax.add_artist(l)

        plt.close()
        return fig
    
    
    def render(self, filename):
        assert self._monitor
        return self._gmonitor.render(filename)

        
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
        
        vx, vy = v.position
        vr = v.radius
        self.xmin, self.xmax = min(self.xmin, vx - 3*vr), max(self.xmax, vx + 3*vr)
        self.ymin, self.ymax = min(self.ymin, vy - 3*vr), max(self.ymax, vy + 3*vr)
        
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
        
    

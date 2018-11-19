_vradius = 3
_vcolor = (1, 1, 1)
_vrcolor = (0, 0, 0)
_vtcolor = (0, 0, 0)
_vtsize = 10


def set_vradius(value):
    global _vradius
    _vradius = value
    
def set_vcolor(value):
    global _vcolor
    _vcolor = value
    
def set_vrcolor(value):
    global _vrcolor
    _vrcolor = value
    
def set_vtcolor(value):
    global _vtcolor
    _vtcolor = value    

def set_vtsize(value):
    global _vtsize
    _vtsize = 10

    
class Vertex:
    def __init__(self, name, value=None, **kwargs):
        global _vradius
        global _vcolor
        global _rcolor
        self.name = name
        self.value = value
        self.radius = kwargs.get('radius', _vradius)
        self.color = kwargs.get('color', _vcolor)
        self.rcolor = kwargs.get('vrcolor', _vrcolor)
        self.tcolor = kwargs.get('vtcolor', _vtcolor)
        self.tsize = kwargs.get('vtsize', _vtsize)
        self.position = kwargs.get('position', (None, None))

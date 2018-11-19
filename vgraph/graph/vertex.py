_vradius = 10
_vcolor = (255, 255, 255)
_vrcolor = (0, 0, 0)


def set_vradius(value):
    _vradius = value
    

def set_vcolor(value):
    _vcolor = value

    
def set_vrcolor(value):
    _vrcolor = value
    
    
class Vertex:
    def __init__(self, name, value=None, **kwargs):
        global _vradius
        global _vcolor
        global _rcolor
        self.name = name
        self.value = value
        self.radius = kwargs['radius'] if 'radius' in kwargs else _vradius
        self.color = kwargs['color'] if 'color' in kwargs else _vcolor
        self.rcolor = kwargs['rcolor'] if 'rcolor' in kwargs else _vrcolor
        self.position = kwargs['position'] if 'position' in kwargs else (None, None)

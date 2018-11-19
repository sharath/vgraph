_ecolor = (0, 0, 0)

def set_ecolor(value):
    _ecolor = value


class Edge:
    def __init__(self, a, b, **kwargs):
        global _ecolor
        self.a = a
        self.b = b
        self.loop = True if a is b else False
        self.weight = kwargs['weight'] if 'weight' in kwargs else None
        self.color = kwargs['color'] if 'color' in kwargs else _ecolor

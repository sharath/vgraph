from abc import ABC, abstractmethod
from collections import deque

class Monitor(ABC):
    def __init__(self):
        self._it = 0
        self._recording = deque()

    @abstractmethod
    def render(self):
        raise UnimplementedError
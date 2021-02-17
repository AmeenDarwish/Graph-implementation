
import collections
import warnings
from Edge import Edge
#todo WHAT IS THE DEAL WITH IMPORTS ?






'''
object:type
should take any data type since python allows it
'''
class Vertex:

    def __init__(self, key=None, neighbors=None, labels=None):
        self.__neighbors = {} if neighbors is None else neighbors
        self.__labels = {} if labels is None else labels
        self.__key = key
        self.__level = None
        self.__is_source = None
        self.__is_sink = None
        self.__degree = len(self.__neighbors.values())

    def __str__(self):
        return "Verix:value:{},level:{},neighbors:{}".format(self.__key, self.__level, self.get_neighbors())

    def __copy__(self):
        new_vertex = Vertex(self.__key)
        new_vertex.__neighbors.update(self.__neighbors)
        return new_vertex

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__key == other.__key
        else:
            warnings.warn("Warning: no equal operator implementation for other data type")
            return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        if isinstance(self.__key, collections.Hashable):
            return hash(self.__key)

        warnings.warn("Warning: Un-hashable value data type")
        return NotImplemented

    def __iter__(self):
        return iter(self.__neighbors.values())

    def set_key(self, key):
        self.__key = key

    def get_key(self):
        val = self.__key
        return val

    def set_level(self, level):
        if level < 0:
            raise Exception("Level can't be negative, you cookin' ?")
        if isinstance(level, int):
            raise Exception(TypeError)

        self.__level = level

    def get_level(self) -> int:
        level = self.__level
        return level

    def add_neighbor(self, vertex, weight=None) -> None:
        self.__neighbors[vertex] = weight

    def remove_neighbor(self, vertex) -> None:
        if vertex in self.__neighbors:
            del self.__neighbors[vertex]
        return

    def get_neighbors(self) -> dict:
        return dict(self.__neighbors)

    def get_weight(self, neighbor):
        if neighbor in self.__neighbors:
            return self.__neighbors[neighbor]

    def is_isolated(self):
        return self.__degree == 0

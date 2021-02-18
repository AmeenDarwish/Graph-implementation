from Vertex import Vertex
import warnings

'''
object:type
should take any data type since python allows it
'''
import collections


class Edge(object):

    def __init__(self, source: Vertex, target: Vertex, weight=None):

        self.__target = target
        self.__weight = weight
        self.__source = source

    def __str__(self):
        return "edge({},{})".format(
            self.__source.get_key(),
            self.__target.get_key())

    def __repr__(self):
        return self.__str__()

    def __copy__(self):
        edge = Edge(self.__target, self.__source, self.__weight())
        return edge

    def __eq__(self, other):
        if isinstance(other, self.__class__):

            same_target = self.__target == other.get_target()
            same_source = self.__source == other.get_source()
            same_weight = self.__weight == other.get_weight()
            return same_target and same_source and same_weight

        else:
            warnings.warn("Warning: no equal operator implementation for other data type")
            return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        """
        hash function assumes our weight value is hashable type
        :return: hash of weight
        """
        # if isinstance(self.__weight, collections.Hashable):
        return hash(self.__weight)
        # warnings.warn("Warning: Un-hashable value data type")
        # return NotImplemented

    def get_weight(self):
        """

        :return: NONE IF USER DIDNT DEFINE VALUE FOR WEIGHT
        """
        return self.__weight

    def get_source(self):
        return self.__source

    def get_target(self):
        return self.__target

    def __cmp__(self, other):
        return 1 if self.__weight > other.get_weight() else -1

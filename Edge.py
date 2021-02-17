from Vertex import Vertex
import warnings

# todo WHAT IS THE DEAL WITH IMPORTS ?

'''
object:type
should take any data type since python allows it
'''


class Edge(object):
    def __init__(self):
        # todo implement me!
        return

    def __str__(self):
        # todo implement me!
        return

    def __copy__(self):
        # todo implement me!
        return

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            # todo implement me!
            pass
        else:
            warnings.warn("Warning: no equal operator implementation for other data type")
            return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # if isinstance(weight????):
        #     return hash(weight)
        # todo implement me!
        warnings.warn("Warning: Un-hashable value data type")
        return NotImplemented

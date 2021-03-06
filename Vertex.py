import collections
import warnings

'''
object:type
should take any data type since python allows it
'''


class Vertex(object):
    """
        A class used to represent an Animal

        ...

        Attributes
        ----------

        key : primitive
            the name of the animal
        sound : str
            the sound that the animal makes
        num_legs : int
            the number of legs the animal has (default 4)

        Methods
        -------
        says(sound=None)
            Prints the animals name and what sound it makes
        """

    def __init__(self, key=None, labels=None):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """
        self.__key = key
        self.__level = 0  # LEVELS! https://youtu.be/aQyXeLSL0II?t=10
        self.__is_source = None
        self.__is_sink = None
        self.__degree = 0
        self.__labels = None

    def __str__(self):
        return f"{self.__key}"

    def __copy__(self):
        new_vertex = Vertex(self.__key)
        new_vertex.__is_source = self.__is_source
        new_vertex.__is_sink = self.__is_sink
        return new_vertex

    def __eq__(self, other):
        return self.get_key() == other

    def __repr__(self):
        return self.__str__()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __cmp__(self, other):
        # i don't know , maybe , you do like levels so here you go

        return 1 if self.__level > other.__level else -1

    def __hash__(self):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.

        Returns
        -------


        """
        # if isinstance(self.__key, collections.Hashable):
        return hash(self.__key)

        # warnings.warn("Warning: Un-hashable value data type")
        # return NotImplemented

    def set_key(self, key):
        self.__key = key

    def get_key(self):
        val = self.__key
        return val

    def set_level(self, level):
        if level < 0:
            raise Exception("Level can't be negative, you cookin' ?")
        if not isinstance(level, int):
            raise Exception(TypeError)

        self.__level = level

    def get_level(self) -> int:
        level = self.__level
        return level

    def is_isolated(self):
        return self.__degree == 0

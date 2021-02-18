from Vertex import Vertex
from Edge import Edge

import warnings



class Graph(object):

    def __init__(self, graph_dict=None, __in_graph_dict=None, adjList=None):

        self.__graph_dict = {} if graph_dict is None else graph_dict
        self.__in_graph_dict = {} if __in_graph_dict is None else __in_graph_dict
        self.__in_edges = []
        self.__out_edges = []
        self.__source = None
        self.__max_level = 0
        self.changed = False  # absolutley FILTHY flag

    def __len__(self):
        return len(self.__graph_dict)

    def __copy__(self):
        new_graph = Graph(graph_dict=dict(self.__graph_dict), __in_graph_dict=dict(self.__in_graph_dict))
        new_graph.__in_edges = list(self.__in_edges)
        new_graph.__out_edges = list(self.__out_edges)
        return new_graph

    def __delitem__(self, vertex: Vertex):

        self.remove_vertex(vertex.get_key())

    def __xor__(self, other):
        # define xor operator , interesting
        return

    def get_vertices(self):
        """
        :return: list of vertices within DAG
        """
        return list(self.__graph_dict.keys())

    def get_out_edges(self) -> list:
        """
        :return: list of edges within DAG
        """
        return self.__out_edges

    def get_in_edges(self) -> list:
        """
        :return: list of edges within bi-directional DAG
        """

        return self.__in_edges

    def add_vertex(self, key) -> None:
        """
        This is probably redundunt by now , too tired to upgrade old implementation
        :param key:
        :return:
        """
        newvertex = Vertex(key)
        if key not in self.__graph_dict:
            self.__graph_dict[newvertex] = []
        if key not in self.__in_graph_dict:
            self.__in_graph_dict[newvertex] = []

    def __add_vertex(self, vertex: Vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
        if vertex not in self.__in_graph_dict:
            self.__in_graph_dict[vertex] = []

    def remove_vertex(self, key):
        """

        :param key: key of vertex to remove
        :return: None
        """
        # fixme , think of the case where you remove vertex in the middle
        #  resulting in two graphs or one graph without vertex?
        #  currently two graphs, since if a link is missing between the nodes , the other half is irrelevant ?
        self.__graph_dict.pop(key)

    def add_edge(self, edge, weight=0):
        """
        Adds edge to graph , edge is expected to be an iterable of two values
        :param edge:
        :param weight:
        :return:
        """
        v1 = Vertex(edge[0])
        v2 = Vertex(edge[1])

        if (v1 == v2):
            return  # to avoid a self cycle
        if v1 in self.__graph_dict:
            if v2 in self.__graph_dict[v1]:
                # to avoid multiples of edges
                # there could be more efficient way, no time
                return
        self.__add_vertex(v1)
        self.__add_vertex(v2)

        # added to adj list

        self.__graph_dict[v1].append(v2)

        # print("\033[1;30;41m Only thing going in circles around this code is your brain not this graph mister!")
        # do i raise exception , do i print error , do i assert ?

        if v1 in self.__graph_dict[v2]:
            raise Exception("Cyclic vertices!")

        out_edge = Edge(v1, v2, weight)
        v1.add_neighbor(v2)
        # add to edges
        in_edge = Edge(v2, v1, weight)

        # this is probably uselsess since i have all in edges
        self.__in_graph_dict[v2].append(v1)
        self.__out_edges.append(out_edge)
        self.__in_edges.append(in_edge)
        self.changed = True

    def __contains__(self, v: Vertex) -> bool:
        return True if v in self.__graph_dict else False

    @staticmethod
    def __get_edges(target_graph: dict) -> list:
        """
        old implementation , deprecated darling
        :param target_graph:
        :return:
        """
        edges = []
        for vertex in target_graph:
            for neighbor in target_graph[vertex]:
                edges.append([vertex, neighbor])

        return edges

    def get_vertice_degree_out(self, key):
        if key in self.__graph_dict:
            return len(self.__graph_dict[key])

    def get_vertice_degree_in(self, key):
        if key in self.__in_graph_dict:
            return len(self.__graph_dict[key])

    def find_path(self, start_vertex: Vertex, target_vertex: Vertex, path: list = None) -> list or None:
        if path is None:
            path = []

        path = path + [start_vertex]

        if start_vertex == target_vertex:
            return path
        if start_vertex not in self.__graph_dict:
            return None

        for vertix in self.__graph_dict[start_vertex]:

            if vertix not in path:

                extended_path = self.find_path(vertix, target_vertex, path)

                if extended_path:
                    return extended_path

        return None

    def find_all_paths(self, key1, key2, path: list = None) -> list:

        if (path is None):  # init list
            path = []

        all_paths = []
        start_vertex = self.__graph_dict[key1]
        target_vertex = self.__graph_dict[key2]

        # path to unconnected vertex is itself
        if start_vertex not in self.__graph_dict:
            return [start_vertex]

        # add current vertex to path
        path.append(start_vertex)

        # arrived to target
        if start_vertex == target_vertex:
            all_paths.append(path)
            return all_paths

        for vertex in self.__graph_dict[start_vertex]:
            if vertex not in path:

                # get all sub paths
                sub_paths = self.find_all_paths(vertex, target_vertex, path)

                # append found sub_paths to all_paths
                for valid_path in sub_paths:
                    all_paths.append(valid_path)

        return all_paths

    def __eq__(self, other):
        # not sure this really works but hey i can always test it if it matters
        same_adj_list = self.__graph_dict == other.__graph_dict

        same_in_edges = self.__in_edges == self.__in_edges

        same_out_edges = self.__out_edges == self.__out_edges

        return same_in_edges and same_out_edges and same_adj_list

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):

        # optional
        return 0

    def __iter__(self):
        return iter(self.__graph_dict)

    def get_density(self):
        """
        method to calculate the density of a graph
        :returns ratio of the number of edges |E| with respect to the maximum possible edges.
        """
        vertices = len(self.__graph_dict.keys())
        edges = len(self.__in_edges)
        return 2 * edges / (vertices * (vertices - 1))

    def get_diameter(self):
        """
        if diameter is longest VALID path between two nodes
        UNLESS IT'S A BI-DIRECTIONAL , THEN IT'S A WHOLE OTHER THING!
        :return: maximum level in graph
        """
        return self.__max_level  # i think am not sure

    def is_cyclic(self):
        """

        :return: True if graph has cycle , false otherwise
        """
        # TODO implement me!

        return

    def find_shortest_path(self, key1, key2):
        """
        :return:  shortest path between two vertices v1,v2 for key1,key2
        """
        # TODO implement me!
        #   USE BFS HERE !!!!!!
        #   i can use levels if i had time , it would almost be the same, almost
        if key1 == key2:
            return 0
        source_level = self.__graph_dict[key1].get_level()
        target_level = self.__graph_dict[key1].get_level()
        if target_level > source_level:
            # if i am looking for shortest possible path, then that should be
            # at least less then longest path right, of course , am joking
            # no VALID path from V1 to V2
            return -1

        # i dont have much time , my deepest apologies for this monstrosity
        shortest_path = min(self.find_all_paths(key1, key2), key=lambda path: len(path))
        return shortest_path

    def get_vertex_level(self, key):
        """

        :param key:
        :return: level of vertex in graph ; constant time
        """
        if (self.changed):
            self.__set_levels()
            self.changed = False

        for vertex in self.__graph_dict:
            if (vertex.get_key() == key):
                return vertex.get_level()

    def get_vertices_at_level(self, level):
        """
        i have considered
        :param level:
        :return: all vertices at given level in graph
        """
        res = []
        for vertex in self.__graph_dict:
            if vertex == level:
                res.append(vertex.get_key())
        return res

    def __set_levels(self):
        """

        This method is really what introduces levels into our graphs
        it looks like a double for loop with complexity V^2 , but it's really O(V).

        Only really needs to be called once and then we can keep updating the levels on input of indices
        but for that we need to assume that indices would be input in order
        and that our connections are correctly assigned, Not realistic , maybe

        for simplicity , and validity sake , we can run after each add

        :return: None
        """
        # only really needs to be called after all adding is done
        # max complexity is number of vertices

        i = 0
        for vertex in self.__graph_dict:

            if len(self.__in_graph_dict[vertex]) == 0:
                vertex.set_level(level=0)
            if vertex.get_level() == i:
                for neighbor in self.__graph_dict[vertex]:
                    if i + 1 > neighbor.get_level():
                        neighbor.set_level(i + 1)
                        if i + 1 > self.__max_level:
                            self.__max_level = i + 1

                if self.__max_level == len(self.__graph_dict.keys()) - 1:
                    break
                i += 1

    def get_sources(self):
        """
        # source would be Vertice with in degree = 0
        # sink would be Vertice with out degree = 0
        if you wanted just one and only source , get sources would be always a list of size == 1
        :return: a list of keys , that have level = 0 aka sources
        """
        res = []
        for vertex in self.__graph_dict:
            # dont know if this isolated really helps here , not sure
            if len(self.__in_graph_dict[vertex]) == 0 and not vertex.is_isolated():
                res.append(vertex)

    def get_sinks(self):
        """
        # source would be Vertice with in degree = 0
        # sink would be Vertice with out degree = 0
        if you wanted just one and only sink , get sinks would be always a list of size == 1
        :return: a list of keys , that have level = 0 aka sources
        """
        res = []
        for vertex in self.__graph_dict:
            # dont know if this isolated really helps here , not sure
            if len(self.__graph_dict[vertex]) == 0 and not vertex.is_isolated():
                res.append(vertex)
        return res

    def is_connected(self, vertices_encountered=None, start_vertex=None):
        """

        :param vertices_encountered:
        :param start_vertex:
        :return: True if all vertices in graph are connected (no isolated vertices)
        """
        if vertices_encountered is None:
            vertices_encountered = set()
            print(self.__graph_dict)
        out_dict = self.__graph_dict
        in_dict = self.__in_graph_dict

        vertices = (list(in_dict.keys()))

        if not start_vertex:
            start_vertex = vertices[0]

        vertices_encountered.add(start_vertex)

        if len(vertices_encountered) != len(vertices):
            mix = set(list(in_dict[start_vertex]) + list(out_dict[start_vertex]))
            for vertex in mix:

                if vertex not in vertices_encountered:

                    if self.is_connected(vertices_encountered, vertex):
                        return True

        else:
            return True

        return False


if __name__ == '__main__':
    my_correct_graph = Graph()
    my_correct_graph.add_edge(("A", "B"))
    my_correct_graph.add_edge(("B", "C"))
    my_correct_graph.add_edge(("X", "C"))
    my_correct_graph.add_vertex("Y")

    for v in my_correct_graph:
        print(v, " ", my_correct_graph.get_vertex_level(v))

    out_edges = my_correct_graph.get_out_edges()
    in_edges = my_correct_graph.get_in_edges()
    print(my_correct_graph.is_connected())

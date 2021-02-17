from Vertex import Vertex
from Edge import Edge


# todo WHAT IS THE DEAL WITH IMPORTS ?

class Graph(object):

    def __init__(self, graph_dict=None, __in_graph_dict=None):
        self.__graph_dict = {} if graph_dict is None else graph_dict
        self._in_graph_dict = {} if __in_graph_dict is None else __in_graph_dict

        self.__in_edges = None
        self.__out_edges = None

        self.changed = None

    def __copy__(self):
        new_graph = Graph(graph_dict=dict(self.__graph_dict), __in_graph_dict=dict(self._in_graph_dict))
        new_graph.__in_edges = dict(self.__in_edges)
        new_graph.__out_edges = dict(self.__out_edges)
        return new_graph

    def __delitem__(self, vertex: Vertex):
        self.remove_vertex(vertex.get_key())

    def __sizeof__(self):
        return self.__graph_dict.__sizeof__()

    def __xor__(self, other):
        # TODO implement me!
        # define xor operator , interesting
        return

    def get_vertices(self):
        return list(self.__graph_dict.keys())

    def get_out_edges(self) -> list:
        if self.__out_edges is None:
            self.__out_edges = self.__get_edges(self.__graph_dict)

        return self.__out_edges

    def get_in_edges(self):
        if self.__in_edges is None:
            self.__in_edges = self.__get_edges(self._in_graph_dict)

        return self.__in_edges

    def add_vertex(self, key) -> None:
        new_vertex = Vertex(key=key)
        if new_vertex not in self.__graph_dict:
            self.__graph_dict[new_vertex] = []
        if new_vertex not in self._in_graph_dict:
            self._in_graph_dict[new_vertex] = []

    def remove_vertex(self, key):
        del self.__graph_dict[key]

    def merge_vertices(self, vertex1: Vertex, vertex2: Vertex):
        # TODO implement me!
        return

    def add_edge(self, edge: tuple):
        v1 = edge[0]
        v2 = edge[1]
        self.add_vertex(v1)
        self.add_vertex(v2)

        # added
        self.__graph_dict[v1].append(v2)

        # synth
        self._in_graph_dict[v2].append(v1)

    def __contains__(self, v: Vertex) -> bool:
        return True if v in self.__graph_dict else False

    def __get_edges(self, target_graph: dict) -> list:
        edges = []
        for vertex in target_graph:
            for neighbor in target_graph[vertex]:
                edges.append([vertex, neighbor])

        return edges

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

    def find_all_paths(self, start_vertex: Vertex, target_vertex: Vertex, path: list = None) -> list:

        if (path is None):  # init list
            path = []

        all_paths = []

        # path to unconnected vertex is itself
        if (start_vertex not in self.__graph_dict):
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

    def is_connected(self, vertices_encountered: set = None, start_vertex: Vertex = None):
        if vertices_encountered is None:
            vertices_encountered = set()

        out_dict = self.__graph_dict
        in_dict = self._in_graph_dict

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

    def source_function(self, edge) -> Vertex:
        # TODO implement me!
        return

    def target_function(self, edge) -> Vertex:
        # TODO implement me!
        return

    def __eq__(self, other):
        # TODO implement me!
        return

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):

        # optional
        return 0

    def __iter__(self):
        return iter(self.__graph_dict)

    def get_density(self):
        """ method to calculate the density of a graph """
        vertices = len(self.__graph_dict.keys())
        edges = len(self.__in_edges())
        return 2 * edges / (vertices * (vertices - 1))

    def get_diameter(self):
        # TODO implement me!
        return

    def is_cyclic(self):
        # TODO implement me!
        return

    def find_shortest_path(self):
        # TODO implement me!
        #   USE BFS HERE !!!!!!
        return

    def get_level(self, v: Vertex):
        # todo implement me!
        #   USE BFS HERE !!!!!!
        #   Use in_graphs ?
        #   what if a vertex has two connections ; one to next neighbor(level+1) and one to sink(max(level)
        return


# done implement find all paths

# done class for vertex

# todo class for edge

# todo edge class for source , dest(from to kind of gig){explicit definitions}

# todo create a graph function called level that finds the VALUE for each vertix that represents the level of each node

# TODO LEVELING ,NODE SHOULD have level higher than pre-decessors and lower than successors

# for a complicated graph ,you need efficient leveling!

# TODO make validation of leveling and seperate it from implementation

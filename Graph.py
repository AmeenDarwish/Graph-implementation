from Vertex import Vertex
from Edge import Edge


# todo WHAT IS THE DEAL WITH IMPORTS ?

class Graph(object):

    def __init__(self, graph_dict=None, __in_graph_dict=None, adjList=None):

        self.__graph_dict = {} if graph_dict is None else graph_dict
        self.__in_graph_dict = {} if __in_graph_dict is None else __in_graph_dict
        self.lst_key = {"a"}
        self.__in_edges = []
        self.__out_edges = []
        self.__source = None
        self.__max_level = 0

    def __copy__(self):
        new_graph = Graph(graph_dict=dict(self.__graph_dict), __in_graph_dict=dict(self.__in_graph_dict))
        new_graph.__in_edges = list(self.__in_edges)
        new_graph.__out_edges = list(self.__out_edges)
        return new_graph

    def __delitem__(self, vertex: Vertex):
        self.remove_vertex(vertex.get_key())

    # def __sizeof__(self):
    #     return self.__graph_dict.__sizeof__()

    def __xor__(self, other):
        # TODO implement me!
        # define xor operator , interesting
        return

    def get_vertices(self):
        return list(self.__graph_dict.keys())

    def get_out_edges(self) -> list:

        return self.__out_edges

    def get_in_edges(self) -> list:

        return self.__in_edges

    def add_vertex(self, key) -> None:

        new_vertex = Vertex(key)
        if new_vertex not in self.__graph_dict:
            self.__graph_dict[new_vertex] = []
        if new_vertex not in self.__in_graph_dict:
            self.__in_graph_dict[new_vertex] = []

    def remove_vertex(self, key):
        # fixme , think of the case where you remove vertex in the middle
        #  resulting in two graphs or one graph without vertex?
        #  currently two graphs, since if a link is missing between the nodes , the other half is irrelevant ?
        del self.__graph_dict[key]

    def add_edge(self, edge: tuple, weight=0):

        v1 = Vertex(edge[0])
        v2 = Vertex(edge[1])

        self.add_vertex(v1)
        self.add_vertex(v2)

        # added to adj list
        self.__graph_dict[v1].append(v2)

        v1.add_neighbor(v2)

        # add to edges
        out_edge = Edge(v1, v2, weight)
        in_edge = Edge(v2, v1, weight)

        self.__out_edges.append(out_edge)
        self.__in_edges.append(in_edge)

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

    def source_function(self, edge: Edge) -> Vertex:
        return edge.get_source()

    def target_function(self, edge) -> Vertex:

        return edge.get_target()

    def __eq__(self, other):
        # TODO implement me!
        # same_adj_list = self.__graph_dict == other.__graph_dict
        # same_edges = self.__graph_dict == other.__graph_dict
        # same_adj_list = self.__graph_dict == other.__graph_dict
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
        edges = len(self.__in_edges)
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

    def get_vertex_level(self, key):
        # why not constant when you can constant

        return self.__graph_dict[key].get_level()

    def get_vertices_at_level(self, level):
        res = []
        for vertex in self.__graph_dict:
            if vertex == level:
                res.append(vertex.get_key())
        return res

    def __set_levels(self):
        # max range is number of vertices

        i = 0
        for vertex in self.__graph_dict:
            if len(self.__in_graph_dict[vertex]) == 0:
                vertex.set_level(level=0)
            if (vertex.get_level() == i):
                for neigbor in vertex.get_neighbors():

                    if (i + 1 > neigbor.get_level()):
                        neigbor.set_level(i + 1)
                        if (i + 1 > self.__max_level):
                            self.__max_level = i + 1

                i += 1
                if (self.__max_level == len(self.__graph_dict.keys()) - 1):
                    break


# done implement find all paths

# done class for vertex

# done class for edge

# done edge class for source , dest(from to kind of gig){explicit definitions} ?

# done create a graph function called level that finds the VALUE for each vertix that represents the level of each node

# done LEVELING ,NODE SHOULD have level higher than pre-decessors and lower than successors

# for a complicated graph ,you need efficient leveling!

# TODO make validation of leveling and seperate it from implementation


if __name__ == '__main__':
    my_correct_graph = Graph()
    my_correct_graph.add_edge(("A", "B"))
    my_correct_graph.add_edge(("B", "C"))
    my_correct_graph.add_edge(("X", "C"))
    my_correct_graph.add_vertex("Y")
    # graph not connected
    # in degree is number of in edges going into this node
    # out degree is number of out edges leaving this node
    # source would be Vertice.in_degree = 0
    # sink would be Vertice.out_degree = 0

    # connected? ->

    out_edges = my_correct_graph.get_out_edges()
    in_edges = my_correct_graph.get_in_edges()

    print(my_correct_graph.is_connected())
    # print(out_edges)
    # print(in_edges)

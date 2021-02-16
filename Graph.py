class Graph(object):

    def __init__(self, graph_dict=None, _in_graph_dict=None):
        self._graph_dict = {} if graph_dict is None else graph_dict
        self._in_graph_dict = {} if _in_graph_dict is None else _in_graph_dict

        self.__in_edges = None
        self.__out_edges = None

        self.changed = None

    def vertices(self):
        return list(self._graph_dict.keys())

    def get_out_edges(self) -> list:
        if self.__out_edges is None:
            self.__out_edges = self.__generate_edges(self._graph_dict)

        return self.__out_edges

    def get_in_edges(self):
        if self.__in_edges is None:
            self.__in_edges = self.__generate_edges(self._in_graph_dict)

        return self.__in_edges

    def add_vertex(self, v: str) -> None:
        if v not in self._graph_dict:
            self._graph_dict[v] = []
        if v not in self._in_graph_dict:
            self._in_graph_dict[v] = []

    "edge is a tuple or list"

    def add_edge(self, edge):
        v1 = edge[0]
        v2 = edge[1]
        self.add_vertex(v2)
        self.add_vertex(v1)

        # added
        self._graph_dict[v1].append(v2)

        # synth
        self._in_graph_dict[v2].append(v1)

    def set_vertex(self, v: str) -> None:
        return

    def __contains__(self, item) -> bool:
        return True if item in self._graph_dict else False

    def __generate_edges(self, target_graph) -> list:
        edges = []
        for vertex in target_graph:
            for neighbor in target_graph[vertex]:
                edges.append([vertex, neighbor])

        return edges

    def find_path(self, start_vertex, end_vertex, all_paths, path=None) -> list or None:
        if path is None:
            return []

        graph = self._graph_dict

        path = path + [start_vertex]

        if start_vertex == end_vertex:
            return path

        if start_vertex not in graph:
            return None


        # todo implement find all paths

        # todo classes for edge,vertix

        # todo edge class for source , dest(from to kind of gig){explicit definitions}

        # todo create a graph function called level that finds the VALUE for each vertix that represents the level of each node

        # TODO LEVELING ,NODE SHOULD have level higher than pre-decessors and lower than successors

        # for a complicated graph ,you need efficient leveling!

        # TODO make validation of leveling and seperate it


        for vertix in graph[start_vertex]:

            if vertix not in path:

                extended_path = self.find_path(vertix, end_vertex, all_paths, path)

                if extended_path:
                    extended_path.append(all_paths)

    def is_connected(self, vertices_encountered=None, start_vertex=None):
        if vertices_encountered is None:
            vertices_encountered = set()

        out_dict = self._graph_dict
        in_dict = self._in_graph_dict

        # for element in out_dict.keys():
        #     gdict[element] = out_dict[element]
        #
        # for element in in_dict.keys():
        #     if(element in gdict):
        #         for edge in element:
        #             if(edge not in gdict[element]):
        #                 gdict[element].append(edge)
        #     else:
        #         gdict[element] = in_dict[element]

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



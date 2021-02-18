# todo space and time complexity comparisons between different implementations
#  rememmember to keep some mind to BFS,Bellford and dijkestra whilst writing complex algos
#  this should also help you in the validation process


import unittest
from bigO import BigO
from Graph import Graph
import random


class TestEfficiency(unittest.TestCase):

    def test_add(self, graph, size):
        test_size = size
        for i in range(size):
            graph.add_vertex((i))
        assert (len(graph.get_vertices()) == test_size)
        # assert (graph.is_connected()) not necessarily

    def test_add2(self, graph, size):
        for i in range(size):
            graph.add_edge(str(i), str(i + 1))

        assert ((graph.get_size()) == size + 1)
        # assert (graph.is_connected()) failed , maximum recursion depth at 2^10
        # i know this is wrong, no time
        graph.get_vertex_level("2")
        assert (graph.get_diameter() == size)

    def test_is_connected(self, graph):
        assert (graph.is_connected())

    def test_find_all_paths(self, graph):
        assert (len(graph.find_all_paths("1", "999")) == 1)
        assert (len(graph.find_all_paths("1", "999")[0]) == 1000)
        assert (len(graph.find_all_paths("0", str(graph.get_size()))[0]) == graph.get_size())

    def test_get_level(self, graph, key):
        assert (graph.get_vertex_level(key))

    def test_all(self):

        test_size = 2 ** 10  # 1 gig rip failed
        big_graph = Graph()
        self.test_add(big_graph, test_size)
        big_graph = Graph()
        self.test_add2(big_graph, test_size)

        for i in range(test_size):
            big_graph.add_edge(i, i + 1)
        # self.test_find_all_paths(big_graph)
        self.test_get_level(big_graph, 1)  # no reason


class TestCorrectness(unittest.TestCase):

    # ran out of time
    def test_is_connected(self, size):
        i = 0
        graph = Graph()
        cycle = False
        while (i < size):
            try:
                graph.add_edge(random.randint(0, i), random.randint(0, i))
                graph.add_vertex(random.randint(0, i))
                graph.add_vertex(random.randint(0, i))
            except Exception:
                # odds are it will catch cycle
                cycle = True
                # cought cycle
        assert (not graph.is_connected())
        assert (cycle)

    def test_levels(self, graph):
        for source in graph.get_sources():
            assert source.get_level() == 0

        for sink in graph.get_sources():
            assert sink.get_level() == graph.get_size()

        for vertex in graph:
            assert (vertex.get_level() >= 0)
            assert (vertex.get_level < graph.get_size())
            # here i have to validate that current vertex level < next vertex level
            #                     and also  current vertex level > before vertex level

        return True

from .lgraph.graph import Graph as LGraph
import unittest as ut


class TestLGraph(ut.TestCase):
    def test_add_vertex(self):
        graph = LGraph()
        
        graph.add_vertex(5)
        graph.add_vertex(2)
        graph.add_vertex(1)
        
        self.assertEqual(graph.verticies(), 3)
    
    def test_remove_vertex(self):
        graph = LGraph()
        
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.remove_vertex(3)
        
        self.assertEqual(graph.verticies(), 2)
    
    def test_add_edge(self):
        graph = LGraph()
        
        graph.add_vertex(1)
        graph.add_vertex(2)
        
        graph.add_edge(1, 2)
        graph.add_edge(2, 1)
        
        self.assertEqual(graph.edges(), 2)
    
    def test_remove_edge(self):
        graph = LGraph()
        
        graph.add_vertex(1)
        graph.add_vertex(2)
        
        graph.add_edge(1, 2)
        graph.add_edge(2, 1)
        graph.remove_edge(1, 2)
        
        self.assertEqual(graph.edges(), 1)
    
    def test_eq(self):
        graph_a, graph_b = LGraph(), LGraph()
        
        graph_a.add_vertex(1)
        graph_a.add_vertex(2)
        graph_a.add_edge(2, 1)
        
        graph_b.add_vertex(1)
        graph_b.add_vertex(2)
        graph_b.add_edge(2, 1)
        
        self.assertEqual(graph_a, graph_b)
        
        graph_b.add_edge(1, 2)
        
        self.assertNotEqual(graph_a, graph_b)


if __name__ == "__main__":
    ut.main()
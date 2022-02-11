from typing import TypeVar, Generic, Dict, Set


T = TypeVar("T")


class Graph(Generic[T]):
    _adjacency_list: Dict[T, Set[T]]
    
    __slots__ = "_adjacency_list"
    
    def __init__(self) -> None:
        self._adjacency_list = dict()
    
    def add_vertex(self, vertex: T) -> None:
        if vertex not in self._adjacency_list:
            self._adjacency_list[vertex] = set()
    
    def remove_vertex(self, vertex: T) -> None:
        if vertex in self._adjacency_list:
            del self._adjacency_list[vertex]
    
    def add_edge(self, vertex_a: T, vertex_b) -> None:
        if vertex_a in self._adjacency_list:
            self._adjacency_list[vertex_a].add(vertex_b)
    
    def remove_edge(self, vertex_a: T, vertex_b) -> None:
        if vertex_a in self._adjacency_list:
            self._adjacency_list[vertex_a].remove(vertex_b)
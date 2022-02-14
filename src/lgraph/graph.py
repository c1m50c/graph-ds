from typing import TypeVar, Generic, Dict, Set


T = TypeVar("T")


class Graph(Generic[T]):
    """
        An adjacency list based `Graph`.
    """
    
    _adjacency_list: Dict[T, Set[T]]
    
    __slots__ = "_adjacency_list"
    
    def __init__(self) -> None:
        self._adjacency_list = dict()
        super().__init__()
    
    def add_vertex(self, vertex: T) -> bool:
        """
            Adds a new `vertex` into the `Graph`,
            returns `True` if the `vertex` was not present within the `Graph` before addition.
            Time complexity is `O(1)`.
        """
        
        if vertex not in self._adjacency_list:
            self._adjacency_list[vertex] = set()
            return True
        return False

    def remove_vertex(self, vertex: T) -> bool:
        """
            Removes a `vertex` from the `Graph`.
            returns `True` if the `vertex` was found within the `Graph` and removed.
            Time complexity is `O(1)`.
        """
        
        if vertex in self._adjacency_list:
            del self._adjacency_list[vertex]
            return True
        return False

    def add_edge(self, vertex_from: T, vertex_to: T) -> None:
        """
            Adds an edge between two verticies, `vertex_from` and `vertex_to`.
            An edge in this example is a one-directional link between two verticies.
            Time complexity is `O(1)`.
        """
        
        self._adjacency_list[vertex_from].add(vertex_to)
    
    def remove_edge(self, vertex_from: T, vertex_to: T) -> None:
        """
            Removes an edge between two verticies, `vertex_from` and `vertex_to`.
            Time complexity is `O(1)`.
        """
        
        if vertex_to in self._adjacency_list[vertex_from]:
            self._adjacency_list[vertex_from].remove(vertex_to)
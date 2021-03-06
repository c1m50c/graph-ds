from __future__ import annotations
from typing import TypeVar, Generic, Union, Dict, Set


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
    
    def __eq__(self, other: Graph) -> bool:
        if len(self._adjacency_list) != len(other._adjacency_list):
            return False
        
        for vertex, edges in self._adjacency_list.items():
            if vertex not in other._adjacency_list:
                return False
            elif edges != other._adjacency_list[vertex]:
                return False
        
        return True

    def __bool__(self) -> bool:
        return self.verticies() != 0

    def __len__(self) -> int:
        return self.verticies()
    
    def is_adjacent(self, center: T, checking: T) -> bool:
        """
            Returns a `bool` determining if `checking` is adjacent to `center`,
            adjacent in this context meaning that there is an edge connecting from `center` to `checking`.
            Time complexity is `O(1)`.
        """
        
        return checking in self._adjacency_list[center]

    def neighbors(self, vertex: T) -> Set[T]:
        """
            Returns a set containing all the neighboring verticies of `vertex`,
            neighboring in this context meaning that there is an edge connecting from `vertex` to the neighbor.
            Time complexity is `O(1)`.
        """
        
        return self._adjacency_list[vertex].copy()
    
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
    
    def get_vertex(self, vertex: T) -> Union[T, None]:
        """
            Returns the `vertex` within the `Graph`, if the `vertex` does not exist this will return `None`.
            Time complexity is `O(1)`.
        """
        
        return self._adjacency_list[vertex] if vertex in self._adjacency_list else None

    def verticies(self) -> int:
        """
            Returns the number of verticies within the `Graph`.
        """
        
        return len(self._adjacency_list.keys())
    
    def edges(self) -> int:
        """
            Returns the number of edges within the `Graph`.
        """
        
        result: int = 0
        
        for _, edges in self._adjacency_list.items():
            result += len(edges)
        
        return result
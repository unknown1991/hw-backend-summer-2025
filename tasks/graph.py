from typing import TypeVar, Generic

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        #raise NotImplementedError
        visited = []

        self._dfs(self._root, visited)

        return visited

    def bfs(self) -> list[Node]:
        #raise NotImplementedError
        visited = []  # Посещена ли вершина?
        Q = []  # Очередь
        BFS = []

        self._bfs(self._root, Q, BFS, visited)

        return visited

    def _dfs(self, v, visited):

        if v in visited:
            return
        visited.append(v)
        for i in v.outbound:
            if not i in visited:
                self._dfs(i, visited)

    def _bfs(self, v, Q, BFS, visited):

        if v in visited:
            return
        visited.append(v)
        BFS.append(v)
        for i in v.outbound:
            if not i in visited:
                Q.append(i)
        while Q:
            self._bfs(Q.pop(0), Q, BFS, visited)

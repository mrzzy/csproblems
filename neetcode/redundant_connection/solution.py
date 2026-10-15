#
# CSProblems
# Neetcode
# NC90. Redundant Connection
#


from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    node_id: int
    depth: int = 1
    parent: Optional["Node"] = None

    def root(self):
        path = [self] # type: list[Node]
        while path[-1].parent is not None:
            path.append(path[-1].parent)

        # path compression: assign all child nodes to root component
        root = path[-1]
        for node in path[:-1]:
            node.parent = root

        return root

    def component(self):
        return self.root().node_id

    def union(self, other: "Node"):
        self_subtree, other_subtree = self.root(), other.root()
        # weighted quick union: always union with the larger tree as parent
        # so that component search depth is at most log(n0
        if self_subtree.depth > other_subtree.depth:
            parent, child = self_subtree, other_subtree
        else:
            parent, child = other_subtree, self_subtree

        child.parent = parent
        parent.depth += 1


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # init nodes
        N = len(edges)
        nodes = [Node(node_id=i) for i in range(N)]

        redundant = []
        for src_id, dest_id in edges:
            src, dest = nodes[src_id - 1], nodes[dest_id - 1]
            # check if edge is redundant: ie. forms a cycle
            if src.component() == dest.component():
                redundant = [src_id, dest_id]
                continue

            # edge connects src to dest in 1 connected component
            src.union(dest)

        return redundant

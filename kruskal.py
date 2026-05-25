from typing import List, Tuple
from union_find import UnionFind

# Kruskal's algorithm finds the minimum spanning tree (MST) of a weighted,
# undirected graph by greedily adding the cheapest edge that does not form
# a cycle. Cycle detection is handled in near-constant time using UnionFind.
# Time complexity: O(|E| log |E|)
# Space complexity: O(|V| + |E|)
def kruskal(num_nodes: int, edges: List[Tuple[int, int, float]]) -> List[Tuple[int, int, float]]:
    uf = UnionFind(num_nodes)
    mst = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if uf.union(u, v):
            mst.append((u, v, w))
    return mst

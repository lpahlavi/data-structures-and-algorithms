# Dijkstra's algorithm finds the shortest path between two nodes
# in a weighted directed graph with positive weights. The algorithm
# relies on the observation that the first time a node is visited
# will always be through the shortest path through it.
# Time complexity: O((|E|+|V|)log|V|)
# Space complexity: O(|V|+|E|)
def dijkstra (start: int, end: int, adjacency_list: dict) -> int:
    heap = [(0.0, start)]
    visited = set()
    while heap:
        node, dist = heapq.heappop(heap)
        if node == end:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in adjacency_list(node):
            heapq.heappush((dist + weight, neighbor))

    return float('inf')
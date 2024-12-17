# The Floyd-Warshall algorithm finds the shortest distance between all pairs
# of nodes in a weighted, directed graph with possibly negative weights but
# without negative cycles.
# Time complexity: O(n^3)
# Space complexity: O(n^2)
def floyd_warshall (n: int, edges: List[List[int]]) -> int:
    d = [[float('inf') for _ in range(n)] for _ in range(n)]

    for (u, v, w) in edges:
        d[u][v] = w
    for u in range(n):
        d[u][u] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    return d
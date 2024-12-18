# Disjoint-set data structure, also known as union-find data structure.
# Keeps track of `n` disjoint sets and allows merging any two sets by refering
# to any one of their respective elements.
# The use of path compression and union-by rank gives a worst case runtime of α(n)
# for both the `find` and `union` methods, where α is the inverse Ackermann function.
class UnionFind:
    def __init__(self, num_nodes: int):
        self.parents = [i for i in range(num_nodes)]
        self.sizes = [0 for _ in range(num_nodes)]

    # Find the index of the parent of `node`
    def find(self, node: int) -> int:
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    # Merge the sets containing nodes `node1` and `node2`. Returns `True` is a merge
    # occurred, and `False` if the two nodes were already in the same set.
    def union(self, node1: int, node2: int) -> bool:
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False

        if self.sizes[parent1] > self.sizes[parent2]:
            self.parents[parent2] = parent1
            self.sizes[parent1] += self.sizes[parent2]
        else:
            self.parents[parent1] = parent2
            self.sizes[parent2] += self.sizes[parent1]
        return True

from typing import List

# Prefix sum array for efficient range sum queries.
# After O(n) preprocessing, any contiguous subarray sum can be answered in O(1).
class PrefixSums:
    def __init__(self, array: List[int]):
        self._prefix = [0] * (len(array) + 1)
        for i, x in enumerate(array):
            self._prefix[i + 1] = self._prefix[i] + x

    # Return the sum of elements in array[l..r] (inclusive, 0-indexed)
    # O(1) time | O(1) space
    def query(self, l: int, r: int) -> int:
        return self._prefix[r + 1] - self._prefix[l]

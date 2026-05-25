from typing import List, Optional

# Find the majority element (leader) in an array — the element that appears
# strictly more than n/2 times — using the Boyer-Moore Voting Algorithm.
# Returns None if no majority element exists.
# Time complexity: O(n)
# Space complexity: O(1)
def find_leader(array: List[int]) -> Optional[int]:
    candidate, count = None, 0
    for x in array:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1

    # Verify the candidate is actually a majority element
    if array.count(candidate) > len(array) // 2:
        return candidate
    return None

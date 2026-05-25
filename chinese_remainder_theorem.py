from math import prod
from typing import List

# Solve the system of congruences x ≡ remainders[i] (mod moduli[i]) for all i
# using the Chinese Remainder Theorem. Requires all moduli to be pairwise coprime.
# Returns the unique solution x in [0, N) where N = product of all moduli.
# Time complexity: O(n * log(max(moduli)))
# Space complexity: O(1)
def chinese_remainder_theorem(remainders: List[int], moduli: List[int]) -> int:
    N = prod(moduli)

    x = 0
    for r, m in zip(remainders, moduli):
        Ni = N // m
        x += r * Ni * pow(Ni, -1, m)

    return x % N

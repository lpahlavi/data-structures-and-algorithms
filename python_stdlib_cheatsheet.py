import heapq
from bisect import bisect_left, bisect_right, insort
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import accumulate, combinations, permutations, product
from math import comb, factorial, gcd, isqrt, lcm, perm


# -----------------------------------------------------------
# Counter
# -----------------------------------------------------------

# Build from an iterable — counts occurrences of each element
c = Counter("abracadabra")        # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
c = Counter([1, 1, 2, 3, 3, 3])   # Counter({3: 3, 1: 2, 2: 1})

# Access counts — missing keys return 0, not KeyError
c["a"]   # 4
c["z"]   # 0

# Most / least common elements
c.most_common(2)         # [('a', 5), ('b', 2)]  (top 2)
c.most_common()[:-3:-1]  # two least common

# Arithmetic — add / subtract / intersect / union counters
a = Counter({"x": 3, "y": 2})
b = Counter({"x": 1, "y": 4})
a + b    # Counter({'y': 6, 'x': 4})   element-wise sum
a - b    # Counter({'x': 2})            drops zero / negative
a & b    # Counter({'x': 1, 'y': 2})   element-wise min
a | b    # Counter({'y': 4, 'x': 3})   element-wise max

# Update (add) and subtract in-place
c.update("aab")    # adds counts
c.subtract("aab")  # subtracts counts (can go negative)

# Total count and element iteration
sum(c.values())    # total; or c.total() in Python 3.10+
list(c.elements()) # ['a', 'a', 'a', ..., 'b', 'b', ...]


# -----------------------------------------------------------
# defaultdict
# -----------------------------------------------------------

# Values are auto-initialised on missing key access using the factory
d: defaultdict[str, list] = defaultdict(list)
d["key"].append(1)   # no KeyError — creates [] then appends

# Common factories
defaultdict(int)    # missing key → 0    (frequency counts)
defaultdict(set)    # missing key → set()
defaultdict(list)   # missing key → []
defaultdict(dict)   # missing key → {}

# Adjacency list example
graph: defaultdict[int, list] = defaultdict(list)
graph[0].append((1, 5.0))   # (neighbour, weight)

# Note: .get() does NOT trigger the default factory
d.get("missing")    # returns None


# -----------------------------------------------------------
# deque  (double-ended queue)
# -----------------------------------------------------------

q = deque([1, 2, 3])

q.append(4)       # add to right  — O(1)
q.appendleft(0)   # add to left   — O(1)
q.pop()           # remove right  — O(1)
q.popleft()       # remove left   — O(1)   (list.pop(0) is O(n)!)

q.rotate(2)       # rotate right by 2 steps
q.rotate(-1)      # rotate left  by 1 step

# Useful as a BFS queue and sliding-window monotone deque
deque(maxlen=3)   # fixed-size window; oldest element is dropped automatically


# -----------------------------------------------------------
# heapq  (min-heap on a plain list)
# -----------------------------------------------------------

h: list[int] = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappush(h, 2)

heapq.heappop(h)      # 1  (smallest)
h[0]                  # peek without popping

heapq.heapify(h)      # turn arbitrary list into heap in O(n)

# Push then pop (or pop then push) in one efficient step
heapq.heappushpop(h, 0)   # push 0, then pop and return the smallest
heapq.heapreplace(h, 0)   # pop smallest, then push 0 (faster if new item ≥ popped)

# n largest / smallest without sorting the whole list
heapq.nlargest(3, h)
heapq.nsmallest(3, h)

# Max-heap: negate values on entry and exit
heapq.heappush(h, -value)
-heapq.heappop(h)


# -----------------------------------------------------------
# bisect  (binary search on sorted lists)
# -----------------------------------------------------------

a = [1, 3, 3, 5, 7]

bisect_left(a, 3)    # 1  — first index where 3 can be inserted (leftmost 3)
bisect_right(a, 3)   # 3  — index after all existing 3s
bisect_left(a, 4)    # 3  — insertion point to keep list sorted

# Count occurrences of x in sorted list
bisect_right(a, 3) - bisect_left(a, 3)  # 2

# Insert while maintaining sort order — O(n) due to list shift
insort(a, 4)    # a becomes [1, 3, 3, 4, 5, 7]


# -----------------------------------------------------------
# @cache  (functools — memoisation)
# -----------------------------------------------------------

# Caches the return value for each unique argument tuple (unbounded).
# Equivalent to @lru_cache(maxsize=None) but slightly faster.
@cache
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

fib(100)            # O(n) first call, O(1) on repeats
fib.cache_clear()   # discard all cached results
fib.cache_info()    # CacheInfo(hits=..., misses=..., maxsize=None, currsize=...)

# Arguments must be hashable; use tuples to pack multiple parameters
@cache
def dp(i: int, j: int) -> int:
    ...


# -----------------------------------------------------------
# itertools
# -----------------------------------------------------------

# Combinations and permutations
list(combinations([1, 2, 3], 2))    # [(1,2), (1,3), (2,3)]       — no repeats, order irrelevant
list(permutations([1, 2, 3], 2))    # [(1,2),(1,3),(2,1),(2,3),…] — no repeats, order matters
list(product([0, 1], repeat=3))     # all 3-bit binary strings     — with repeats

# Prefix sums via accumulate (default operator is addition)
list(accumulate([1, 2, 3, 4]))                      # [1, 3, 6, 10]
list(accumulate([1, 2, 3, 4], max))                 # [1, 2, 3, 4]  (running max)
list(accumulate([1, 2, 3, 4], lambda a, b: a * b))  # [1, 2, 6, 24]  (factorial)


# -----------------------------------------------------------
# math
# -----------------------------------------------------------

gcd(12, 8)          # 4
lcm(4, 6)           # 12
isqrt(17)           # 4  (integer square root, floor)
factorial(5)        # 120
comb(10, 3)         # 120  (n choose k, no repetition)
perm(10, 3)         # 720  (n permute k)


# -----------------------------------------------------------
# Bitwise operations
# -----------------------------------------------------------

n = 0b1011  # 11

# Operators
n & 0b1100   # 0b1000  — AND:  bits set in both
n | 0b1100   # 0b1111  — OR:   bits set in either
n ^ 0b1100   # 0b0111  — XOR:  bits set in exactly one
~n           # -(n+1)  — NOT:  flip all bits (two's complement)
n << 2       # n * 4   — left shift  (multiply by 2^k)
n >> 1       # n // 2  — right shift (divide by 2^k, floor)

# Read bit i  (0 = LSB)
i = 2
(n >> i) & 1        # 0 or 1

# Set bit i
n | (1 << i)

# Clear bit i
n & ~(1 << i)

# Toggle bit i
n ^ (1 << i)

# Isolate the lowest set bit
n & (-n)            # e.g. 0b1100 → 0b0100

# Clear the lowest set bit
n & (n - 1)         # e.g. 0b1100 → 0b1000

# Count set bits
bin(n).count('1')   # works everywhere
n.bit_count()       # Python 3.10+

# Bit length (position of highest set bit + 1)
n.bit_length()      # 4 for n=0b1011

# Power-of-two checks
n & (n - 1) == 0            # True if n is a power of 2 (also True for n=0)
n > 0 and n & (n - 1) == 0  # strict power-of-two check

# XOR identities — useful for "find the unique element" problems
# a ^ a == 0  and  a ^ 0 == a,  so XOR-ing a list cancels duplicates:
nums = [2, 3, 2, 4, 3]
result = 0
for x in nums:
    result ^= x
# result == 4  (the only element that appears an odd number of times)

# Enumerate all non-empty subsets of a bitmask
mask = 0b1011
sub = mask
while sub:
    # process sub …
    sub = (sub - 1) & mask  # walk to the next smaller subset

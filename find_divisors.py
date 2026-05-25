# Find all divisors of `n` by iterating up to sqrt(n) and collecting
# both elements of each divisor pair (i, n // i).
# Time complexity: O(sqrt(n))
# Space complexity: O(d(n)), where d(n) is the number of divisors of n
def find_divisors(n: int) -> list[int]:
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return sorted(divisors)

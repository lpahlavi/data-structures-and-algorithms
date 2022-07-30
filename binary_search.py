
# Find the index of `target` in the sorted list `array`
def binary_search(array: List[float], target: float) -> int:
    l, r = 0, len(array) - 1
    while l <= r:
        m = (l + r) // 2
        if array[m] == target:
            return m
        if array[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

# Find the index of the last element less than or equal to `target`
# in the sorted list `array`, i.e. the greatest lower bound.
def greatest_lower_bound(array: List[float], target: float) -> int:
    if array[0] > target:
        return -1

    l, r = 0, len(array)-1
    while l < r:
        m = (l + r + 1) // 2
        if array[m] == target:
            return m
        if array[m] > target:
            r = m - 1
        else:
            l = m
    return l

# Find the index of the first element greater than or equal to `target`
# in the sorted list `array`, i.e. the least upper bound.
def least_upper_bound(array: List[float], target: float) -> int:
    if array[-1] < target:
        return -1

    l, r = 0, len(array)-1
    while l < r:
        m = (l + r) // 2
        if array[m] == target:
            return m
        if array[m] < target:
            l = m + 1
        else:
            r = m
    return r
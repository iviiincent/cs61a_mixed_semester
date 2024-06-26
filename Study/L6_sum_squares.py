# tail recurison
def sum_squares_tail_recursion(n):
    """sum of k**2 for 1 <= k <= n

    >>> sum_squares_tail_recursion(-1)
    0
    >>> sum_squares_tail_recursion(0)
    0
    >>> sum_squares_tail_recursion(4)
    30
    """

    def part_sum_tail_recursion(accum, k):
        if k <= n:
            return part_sum_tail_recursion(accum + k**2, k + 1)
        else:
            return accum

    return part_sum_tail_recursion(0, 1)

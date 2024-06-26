def tree(tree, children=[]):
    """
    >>> tree(20,
    ...     [tree(12,
    ...         [tree(9,
    ...             [tree(7),
    ...             tree(2)]),
    ...         tree(3)]),
    ...     tree(8,
    ...         [tree(4),
    ...         tree(4)])])
    (20, [(12, [(9, [(7, []), (2, [])]), (3, [])]), (8, [(4, []), (4, [])])])
    """
    return (tree, children)


def label(tree):
    return tree[0]


def children(tree):
    return tree[1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

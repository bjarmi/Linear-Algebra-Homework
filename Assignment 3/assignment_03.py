from vec import Vec
from GF2 import one


# 1: (Problem 3.8.1) Vector Comprehension and Sum
def vec_select(veclist, k):
    """
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    """
    sublist = []
    for vec in veclist:
        if vec[k] == 0:
            sublist.append(vec)
    return sublist


def vec_sum(veclist, D):
    """
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    """
    out = Vec(D, {})
    for vec in veclist:
        out = out + vec
    return out


def vec_select_sum(veclist, k, D):
    """
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    """
    return vec_sum(vec_select(veclist, k), D)


# 2: (Problem 3.8.2) Vector Dictionary
def scale_vecs(vecdict):
    """
    >>> v1 = Vec({1,2,4}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> result = scale_vecs({3: v1, 5: v2})
    >>> len(result)
    2
    >>> [v in [Vec({1,2,4},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})] 
        >>> for v in result]
    [True, True]
    """
    return [(a / 10) * vec for a, vec in vecdict.items()]


# 3: (Problem 3.8.3) Constructing a Span over GF(2)
def GF2_span(D, L):
    """
    >>> D = {'a', 'b', 'c'}
    >>> result = GF2_span(
    >>>     D, [Vec(D, {'a': one, 'c': one}), Vec(D, {'c': one})]
    >>> )
    >>> len(result)
    4
    >>> [v in result for v in [
    >>>     Vec(D, {}),Vec(D, {'a': one, 'c': one}),Vec(D,
    >>>     {'c': one}),Vec(D, {'a':one})
    >>> ]]
    [True, True, True, True]
    """
    pass

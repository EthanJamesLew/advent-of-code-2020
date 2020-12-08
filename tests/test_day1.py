import pytest

from day1 import iterate_prod


def test_online_example():
    example_list = [1721,
                    979,
                    366,
                    299,
                    675,
                    1456]
    out = tuple(iterate_prod(example_list))
    p = 1
    for i in out[0]:
        p *= i
    assert (p,) == (514579,)

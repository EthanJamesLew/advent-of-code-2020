import pytest

from day10 import jolt_diff, valid_combos


t1 = [16,
10,
15,
5,
1,
11,
7,
19,
6,
12,
4]


t2 = [28,
33,
18,
42,
31,
14,
46,
20,
48,
47,
24,
23,
49,
45,
19,
38,
39,
11,
1,
32,
25,
35,
8,
17,
7,
9,
4,
2,
34,
10,
3]


def test_online_example():
    res = jolt_diff(t1 + [0,])
    assert len(res[1]) == 7
    assert len(res[3]) == 5
    res = jolt_diff(t2 + [0,])
    print(res)
    assert len(res[1]) == 22
    assert len(res[3]) == 10
    assert valid_combos(t1 + [0, max(t1) + 3]) == 8
    assert valid_combos(t2 + [0, max(t2) + 3]) == 19208

import pytest

from day9 import XmasStream


out_ls = [35,
20,
15,
25,
47,
40,
62,
55,
65,
95,
102,
117,
150,
182,
127,
219,
299,
277,
309,
576]


def test_online_example():
    xms = XmasStream(out_ls[:5])
    with pytest.raises(ValueError) as excinfo:
        for i in out_ls[5:]:
            xms.push(i)
            if i == 127:
                break
    assert xms.find_contiguous_range(127) == (15, 25, 47, 40)

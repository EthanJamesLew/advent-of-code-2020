import pytest

from day5 import decode_str, get_seat_id


def test_online_example():
    strs = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
    codes = [(44, 5), (70, 7), (14, 7), (102, 4)]
    sids = [357, 567, 119, 820]

    for test_str, (code, sid) in zip(strs, zip(codes, sids)):
        assert get_seat_id(test_str) == sid
        assert decode_str(test_str) == code

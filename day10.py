"""
Advent of Code Day 10 Puzzle

author: Ethan Lew

--- Day 10: Adapter Array ---
"""
import typing as typ
import re
from functools import reduce, lru_cache

from day1 import iterate_prod


def jolt_diff(
    jolt_arr: typ.Sequence[int],
    diffs: typ.Sequence[int] = (1, 3)) -> typ.Dict:
    jolt_arr.append(max(jolt_arr) + 3)
    jolt_arr.sort()
    list(diffs).sort()
    jdict = {d: [] for d in diffs}
    for ji, jj in zip(jolt_arr[:-1], jolt_arr[1:]):
        diff = abs(ji - jj)
        jdict[diff].append((ji, jj))
    return jdict


@lru_cache(maxsize = 128)
def trib(n):
    """calculate the tribonacci sequence starting with (0, 1, 1)"""
    if n == 0:
        return 0
    if n < 3:
        return 1
    return trib(n-1) + trib(n-2) + trib(n-3)


def valid_combos(jolt_arr):
    """find number of valid jolt supply configurations"""
    jolt_arr.sort()
    diff_arr = [jj - ji for ji, jj in zip(jolt_arr[:-1], jolt_arr[1:])]
    jstr = ''.join([str(i) for i in diff_arr])

    # find sequences of 1s greater than order 1
    mtch = [
        i for i in re.split(r"(1+)", jstr) if not (len(i) <= 1 or '3' in i)
    ]

    # take the product
    return reduce(lambda x, y: x * y, [trib(len(l) + 1) for l in mtch], 1)


def main():
    with open("./inputs/day10.txt", "r") as fp:
        in_str = fp.read()
    in_data = [int(i.strip()) for i in in_str.splitlines(False)]
    res = jolt_diff(in_data + [
        0,
    ])
    print(
        f"The Answer to the Day 10 Adapter Array Puzzle is {len(res[1]) * len(res[3])}"
    )
    print(
        f"The Answer to the Day 10 Part 2 Adapter Array Puzzle is {valid_combos(in_data + [0, max(in_data) + 3])}"
    )


if __name__ == '__main__':
    main()

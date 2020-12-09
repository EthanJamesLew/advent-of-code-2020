"""
Advent of Code Day 9 Puzzle

author: Ethan Lew

--- Day 9: Encoding Error ---
"""
import typing as typ
from collections import deque

from day1 import iterate_prod


class XmasStream:
    def __init__(self, preamble: typ.Sequence[int]):
        self._norder = len(preamble)
        self._preamble = deque(preamble, self._norder)
        self._history = list(preamble.copy())

    def push(self, val: int) -> None:
        sum_prob = tuple(iterate_prod(self._preamble, sum_target = val))
        if len(sum_prob) > 0:
            self._preamble.append(val)
            self._history.append(val)
        else:
            raise ValueError(f"{val} not a valid next integer for Xmas sequence {self._preamble}")

    def find_contiguous_range(self, target_val: int):
        for idx, v in enumerate(self._history):
            target_sum = v
            idxi = idx + 1
            while target_sum < target_val or idxi == len(self._history):
                target_sum += self._history[idxi]
                idxi += 1
            if target_sum == target_val:
                return tuple(self._history[idx:idxi])


def main():
    with open("./inputs/day9.txt") as fp:
        in_dat = fp.read()
    in_vals = [int(i) for i in in_dat.splitlines(False)]
    xms = XmasStream(in_vals[:25])
    try:
        for i in in_vals[25:]:
            xms.push(i)
    except:
        print(
            f"The Answer to the Day 9 XMAS Puzzle is {i}"
        )
    r = xms.find_contiguous_range(i)
    print(
        f"The Answer to the Day 9 Part 2 XMAS Puzzle is {min(r) + max(r)}"
    )


if __name__ == '__main__':
    main()

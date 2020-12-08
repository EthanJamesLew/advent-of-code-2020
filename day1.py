"""
Advent of Code Day 1 Puzzle

author: Ethan Lew

--- Day 1: Report Repair ---
"""
import csv
from functools import reduce
import typing as typ


def iterate_prod(nums: typ.Sequence[int],
                 sum_target: int = 2020,
                 nvals: int = 2) -> typ.Iterator[int]:
    """given a list of nums, yield products of values in nums that sum to sum_target"""

    # save scanned numbers
    ret = set()
    for num in nums:

        # don't look at same number twice
        if num in ret:
            continue

        # register current number
        ret.add(num)

        # find sum of other terms
        complement = sum_target - num

        # apply same problem to other terms
        if nvals > 2:
            nums_p = list(nums).copy()
            nums_p.remove(num)
            citer = iterate_prod(nums_p,
                                 sum_target=complement,
                                 nvals=nvals - 1)
            complement = tuple(citer)
            if len(complement) > 0:
                complement = complement[0]
            else:
                continue
        else:
            complement = (complement, )

        # find if complement satisfies cache conditions
        if all([i in nums for i in complement
                ]) and not all([i in ret for i in complement]):
            for i in complement:
                ret.add(i)
            yield (*complement, num)


def main():
    """apply the iterate_prod solver to the puzzle input"""
    with open("./inputs/day1.csv", "r") as fp:
        reader = csv.reader(fp, delimiter='\n')
        input_data = [int(r[0]) for r in list(reader)]
    out = tuple(iterate_prod(input_data))
    assert len(out) == 1
    print(f"The Answer to the Day 1 Sum / Product Puzzle is {reduce(lambda x, y: x * y, out[0], 1)}")
    out = tuple(iterate_prod(input_data, nvals=3))
    print(f"The Answer to the Day 1 Sum / Product Puzzle is {reduce(lambda x, y: x * y, out[0], 1)}")


if __name__ == '__main__':
    main()

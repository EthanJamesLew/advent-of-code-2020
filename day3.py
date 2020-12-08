"""
Advent of Code Day 2 Puzzle

author: Ethan Lew

--- Day 3: Toboggan Trajectory ---
"""
from functools import reduce
import typing as typ


class Trees:
    """Model a forest of trees, for the toboggan ride
    """
    valid_chars = {'#', '.'}

    @classmethod
    def from_str(cls, in_str: str):
        return cls([line for line in in_str.splitlines(False)])

    @staticmethod
    def is_valid_str(tstr: str) -> bool:
        return set(tstr).issubset(Trees.valid_chars)

    def __init__(self, trees: typ.Sequence['str']):
        for tree in trees:
            assert self.is_valid_str(tree), f"row {tree} is invalid!"
        self._trees = trees

    def get_collisions(self, right_move: int, down_move: int = 1):
        """ for a given move of right_moves per down move, count the number of collisions"""
        ncollisions = 0
        for i in range(1, self.nrows):
            yidx, xidx = i * down_move, (right_move * i) % self.ncols
            if yidx >= self.nrows:
                break
            if self._trees[yidx][xidx] == '#':
                ncollisions += 1
        return ncollisions

    @property
    def nrows(self):
        return len(self._trees)

    @property
    def ncols(self):
        if self.nrows > 0:
            return len(self._trees[0])
        else:
            return 0


def main():
    with open("./inputs/day3.txt", "r") as fp:
        in_str = fp.read()
    trees = Trees.from_str(in_str)
    ncollisions = trees.get_collisions(3, down_move = 1)
    print(f"The Answer to the Day 3 Trees Puzzle is {ncollisions}")
    moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    collisions = [trees.get_collisions(m[0], down_move = m[1]) for m in moves]
    print(f"The Answer to the Day 3 Part 2 Trees Puzzle is {reduce(lambda x, y: x * y, collisions, 1)}")



if __name__ == '__main__':
    main()

#  LocalWords:  toboggan

import pytest

from day3 import Trees


in_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def test_online_example():
    trees: Trees = Trees.from_str(in_data)
    assert trees.get_collisions(1, 1) == 2
    assert trees.get_collisions(3, 1) == 7
    assert trees.get_collisions(5, 1) == 3
    assert trees.get_collisions(7, 1) == 4
    assert trees.get_collisions(1, 2) == 2

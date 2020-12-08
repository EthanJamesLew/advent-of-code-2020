import pytest

from day2 import PasswordPolicy


def test_online_example():
    example_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    for idx, example in enumerate(example_input):
        es, policy = PasswordPolicy.from_advent_format(example)
        if idx in [0, 2]:
            assert policy.is_password_valid(es)
        else:
            assert not policy.is_password_valid(es)


def test_online_example_part2():
    example_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    for idx, example in enumerate(example_input):
        es, policy = PasswordPolicy.from_advent_format(example)
        if idx in [0,]:
            assert policy.is_password_valid_part2(es)
        else:
            assert not policy.is_password_valid_part2(es)

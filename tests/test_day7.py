import pytest

from day7 import BagRules


in_str = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


def test_online_example():
    rules = BagRules.from_str(in_str)
    assert len(rules._rules) == 9
    assert rules._rules["dotted black"] == {}
    assert rules._rules["dark olive"] != {}
    assert len(rules.get_outermost_bags("shiny gold")) == 4
    assert rules.get_bag_count("shiny gold") == 32

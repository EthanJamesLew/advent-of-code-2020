"""
Advent of Code Day 7 Puzzle

author: Ethan Lew

--- Day 7: Handy Haversacks ---
"""
import typing as typ

import re


class BagRules:
    # lexing regexs
    rule_outer_match = r"(.*)\s+contain\s+(.*)."
    rule_inner_match = r"([0-9])(.*)"
    color_match = r"(.*)bags?"

    @staticmethod
    def get_color(cstr: str) -> str:
        sp = [i for i in re.split(BagRules.color_match, cstr) if len(i) > 0]
        assert len(sp) == 1
        return sp[0].strip()

    @staticmethod
    def parse_rules_str(in_str: str) -> typ.Dict:
        rules = {}
        for line in in_str.strip().splitlines(False):
            spl = [
                i for i in re.split(BagRules.rule_outer_match, line)
                if len(i) > 0
            ]
            k, v = spl[0], spl[1].strip().split(",")
            v = [[
                BagRules.get_color(i.strip())
                for i in re.split(BagRules.rule_inner_match, s.strip())
                if len(i) > 0
            ] for s in v]
            v = {s[1]: int(s[0]) for s in v if s[0] != 'no other'}
            rules[BagRules.get_color(k)] = v
        return rules

    @classmethod
    def from_str(cls, in_str: str):
        return cls(cls.parse_rules_str(in_str))

    @classmethod
    def from_filename(cls, fname: str):
        with open(fname, "r") as fp:
            in_str = fp.read()
        return cls.from_str(in_str)

    def __init__(self, rules: typ.Dict):
        self._rules = rules

    def _outermost_bags_iterator(self, color_name: str):
        for k, v in self._rules.items():
            for c in v.keys():
                if c == color_name:
                    yield k
                    yield from self._outermost_bags_iterator(k)

    def get_outermost_bags(self, color_name: str):
        return set([i for i in self._outermost_bags_iterator(color_name)])

    def get_bag_count(self, color_name: str):
        v = self._rules[color_name]
        if v != {}:
            total = sum([s for ki, s in v.items()])
            for k in v.keys():
                total += v[k] * self.get_bag_count(k)
            return total
        else:
            return 0


def main():
    rules = BagRules.from_filename("./inputs/day7.txt")
    print(
        f"The Answer to the Day 7 Bag Puzzle is {len(rules.get_outermost_bags('shiny gold'))}"
    )
    print(
        f"The Answer to the Day 7 Part 2 Bag Puzzle is {rules.get_bag_count('shiny gold')}"
    )


if __name__ == '__main__':
    main()

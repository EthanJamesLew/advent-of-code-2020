"""
Advent of Code Day 2 Puzzle

author: Ethan Lew

--- Day 2: Password Philosophy ---
"""
import csv
import re
import typing as typ


class PasswordPolicy:
    @classmethod
    def from_advent_format(cls, fmt_str: str) -> typ.Tuple[str, None]:
        re_match_str = r'\A(.*)-(.*)\s(.*):\s(.*)'
        match = re.match(re_match_str, fmt_str)
        assert match is not None, f"{fmt_str} fails to match with advent format"
        return match.group(4), cls(match.group(3),
                                   (int(match.group(1)), int(match.group(2))))

    def __init__(self, char: str, bound: typ.Tuple[int, int]):
        assert len(
            char) == 1, f"char argument {char} must be exactly one character"
        assert len(bound) == 2, f"bound {bound} must be exactly two values"
        assert bound[1] >= bound[
            0], f"second bound argument must be greater or equal to the first {bound}"

        self.rule_character = char
        self.bound = bound

    def is_password_valid(self, password: str) -> bool:
        """whether password adheres to the password policy"""
        count = sum([(1 if c == self.rule_character else 0) for c in password])
        return count >= self.bound[0] and count <= self.bound[1]

    def is_password_valid_part2(self, password: str) -> bool:
        return (self.rule_character == password[self.bound[0] - 1]) ^ \
            (self.rule_character == password[self.bound[1] - 1])


def main(is_part2: bool = False):
    with open("./inputs/day2.csv", "r") as fp:
        reader = csv.reader(fp, delimiter='\n')
        input_data = [r[0] for r in list(reader)]
    valid_count = 0
    for fmt_str in input_data:
        password, policy = PasswordPolicy.from_advent_format(fmt_str)
        if (policy.is_password_valid(password)
                if not is_part2 else policy.is_password_valid_part2(password)):
            valid_count += 1
    print(
        f"The Answer to the Day 2 {'Part 2 ' if is_part2 else ''}Password Puzzle is: {valid_count} -- {valid_count}/{len(input_data)}"
    )


if __name__ == '__main__':
    main()
    main(is_part2=True)

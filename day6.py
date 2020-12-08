"""
Advent of Code Day 6 Puzzle

author: Ethan Lew

--- Day 6: Custom Customs ---
"""
import typing as typ
import re
import string


class GroupAnswers:
    @classmethod
    def from_file(cls, fname: str) -> typ.Sequence:
        ret_answers = []
        with open(fname, "r") as fp:
            in_str = fp.read()
        pass_match = re.compile(r"^(.*)^\s*$", re.MULTILINE)
        ganswers: typ.Sequence[str] = [
            r for r in re.split(pass_match, in_str) if len(r) > 0
        ]
        for group_answer in ganswers:
            rga: GroupAnswers = cls()
            for answer in group_answer.strip().splitlines(False):
                rga.submit_answer(answer)
            ret_answers.append(rga)
        return tuple(ret_answers)

    acceptable_answers = set(string.ascii_lowercase)

    def __init__(self):
        self._answers: typ.List[set] = []

    def submit_answer(self, ans_str: typ.Union[str, typ.Set[str]]):
        if isinstance(ans_str, str):
            ans_str = set(ans_str)
        assert ans_str.issubset(self.acceptable_answers)
        self._answers.append(ans_str)

    @property
    def everyone_answer(self):
        a = set()
        for ai in self._answers:
            a |= ai
        return a

    @property
    def agree_answer(self):
        if len(self._answers) > 1:
            return self._answers[0].intersection(*self._answers[1:])
        elif len(self._answers) == 1:
            return self._answers[0]
        else:
            return set()

    @property
    def nanswers(self):
        return len(self.everyone_answer)

    @property
    def nanswers_agree(self):
        return len(self.agree_answer)


def main():
    answers: typ.Sequence[GroupAnswers] = GroupAnswers.from_file(
        "./inputs/day6.txt")
    count = [a.nanswers for a in answers]
    print(f"The Answer to the Day 6 Group Answer Puzzle is {sum(count)}")
    count2 = [a.nanswers_agree for a in answers]
    print(
        f"The Answer to the Day 6 Part 2 Group Answer Puzzle is {sum(count2)}")


if __name__ == '__main__':
    main()

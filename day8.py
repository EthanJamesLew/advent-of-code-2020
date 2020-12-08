"""
Advent of Code Day 8 Puzzle

author: Ethan Lew

--- Day 8: Handheld Halting ---
"""
import copy
import re
import typing as typ


class Instruction:
    instructions = {"NOP", "ACC", "JMP"}

    def __init__(self, name: str, args: tuple):
        assert name in self.instructions
        self._name = name
        assert isinstance(args[0], int)
        self._args = args

    def __eq__(self, other):
        if isinstance(other, Instruction):
            return self._name == other._name
        else:
            return self._name == other

    @property
    def args(self):
        return self._args

    def __repr__(self):
        return f"<{self._name}{self._args}>"


class Program:
    instruction_match = r"(\w+)+\s([+|-]\w+)"

    @classmethod
    def from_file(cls, fname: str):
        with open(fname, "r") as fp:
            in_str = fp.read()
        return cls.from_str(in_str)

    @classmethod
    def from_str(cls, in_str: str):
        instructions = []
        for line in in_str.strip().splitlines(False):
            instr = [
                i for i in re.split(cls.instruction_match, line) if len(i) > 0
            ]
            assert len(instr) == 2
            instructions.append(
                Instruction(instr[0].upper(), (int(instr[1]), )))
        return cls(instructions)

    def __init__(self, instructions: typ.Sequence[Instruction]):
        self._instr: typ.Sequence[Instruction] = instructions
        self._acc: int = 0
        self._line_registry: typ.Set[int] = set()

    def execute(self, lno, only_once=True):
        if lno in self._line_registry and only_once:
            return False
        self._line_registry.add(lno)
        if lno >= len(self._instr):
            return True
        line: Instruction = self._instr[lno]
        if line == "ACC":
            self._acc += line.args[0]
            return self.execute(lno + 1)
        elif line == "NOP":
            return self.execute(lno + 1)
        elif line == "JMP":
            return self.execute(lno + line.args[0])
        else:
            raise RuntimeError

    def fix(self):
        for idx, instr_f in enumerate(self._instr):
            instrs = self._instr.copy()
            instr = copy.deepcopy(instr_f)
            if instr == "JMP":
                instr._name = "NOP"
            elif instr == "NOP":
                instr._name = "JMP"
            else:
                pass
            instrs[idx] = instr
            prog_test = Program(instrs)
            ret = prog_test.execute(0)
            if ret:
                return prog_test


def main():
    prog = Program.from_file("./inputs/day8.txt")
    prog.execute(0)
    print(
        f"The Answer to the Day 8 Instructions Puzzle is {prog._acc}"
    )
    prog_fix = prog.fix()
    print(
        f"The Answer to the Day 8 Part 2 Instructions Puzzle is {prog_fix._acc}"
    )


if __name__ == '__main__':
    main()

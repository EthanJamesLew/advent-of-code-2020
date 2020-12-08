import pytest

from day8 import Instruction, Program


in_str = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def test_online_example():
    prog = Program.from_str(in_str)
    prog.execute(0)
    assert prog._acc == 5
    prog_fix = prog.fix()
    assert prog_fix._acc == 8

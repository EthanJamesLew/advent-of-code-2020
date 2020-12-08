import pytest

from day6 import GroupAnswers

answers = [('abc', ), ("a", "c", "b"), ("ab", "ac"), ("a", "a", "a", "a"),
           ("b", )]

sols = (3, 3, 3, 1, 1)
sols2 = (3, 0, 1, 1, 1)


def test_online_example():
    for a, (sol0, sol1) in zip(answers, zip(sols, sols2)):
        ga = GroupAnswers()
        for ai in a:
            ga.submit_answer(ai)
        assert ga.nanswers == sol0, f"answers {a} no satisfying solution {sol0}"
        assert ga.nanswers_agree == sol1, f"answers {a} no satisfying solution {sol1}"

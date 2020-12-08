"""
Advent of Code Day 4 Puzzle

author: Ethan Lew

--- Day 4: Passport Processing ---
"""
import re
import typing as typ


class Passport:
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    @classmethod
    def from_str(cls, in_str: str, **kwargs) -> typ.Sequence:
        passports = []
        pass_match = re.compile(r"^(.*)^\s*$", re.MULTILINE)
        field_match = re.compile(r"\s*(\w+):([^\s]*)\s*", re.MULTILINE)
        m = [r for r in re.split(pass_match, in_str) if len(r) > 0]
        for s in m:
            spls = [r for r in re.split(field_match, s) if len(r) > 0]
            pdict = {k: v for k, v in zip(spls[::2], spls[1::2])}
            try:
                passports.append(cls(pdict, **kwargs))
            except AssertionError:
                passports.append(None)

        return tuple(passports)

    @staticmethod
    def height_from_str(hstr: str) -> typ.Tuple[int, str]:
        assert len(hstr) > 2
        unit = hstr[-2:]
        assert unit in {"in", "cm"}
        val = int(hstr[:-2])
        return val, unit

    def __init__(self, passport: dict, do_cast=False):
        assert self.required_fields.issubset(set(passport.keys())), \
            f"passport dict {passport} doesn't have the required fields!"
        self._passport = passport
        if do_cast:
            self._cast_values()
            assert self.validate_values()

    def _cast_values(self):
        try:
            self._passport['byr'] = int(self._passport['byr'])
            self._passport['iyr'] = int(self._passport['iyr'])
            self._passport['eyr'] = int(self._passport['eyr'])
            self._passport['hgt'] = self.height_from_str(self._passport['hgt'])
        except Exception:
            return

    def validate_values(self, fault_detect=False) -> bool:
        self._cast_values()
        byear_good = self._passport['byr'] <= 2002 and self._passport[
            'byr'] >= 1920
        iyear_good = self._passport['iyr'] <= 2020 and self._passport[
            'iyr'] >= 2010
        eyear_good = self._passport['eyr'] <= 2030 and self._passport[
            'eyr'] >= 2020
        if isinstance(self._passport['hgt'], str):
            height_good = False
        else:
            hval, vunit = self._passport['hgt']
            if vunit == "cm":
                height_good = hval <= 193 and hval >= 150
            else:
                height_good = hval <= 76 and hval >= 59
        hair_good = re.match(r"(^#[0-9a-f]{6}\Z)",
                             self._passport['hcl']) is not None
        eye_good = self._passport['ecl'] in {
            "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
        }
        pid_good = re.match(r"(^[0-9]{9}\Z)",
                            self._passport["pid"]) is not None
        if fault_detect:
            return {
                "birth_year": byear_good,
                "issue_year": iyear_good,
                "expire_good": eyear_good,
                "height_good": height_good,
                "hair_good": hair_good,
                "eye_good": eye_good,
                "pid_good": pid_good
            }
        else:
            return byear_good and iyear_good and eyear_good and height_good and hair_good and eye_good and pid_good


def main():
    with open("inputs/day4.txt", "r") as fp:
        in_data = fp.read()

    passports = Passport.from_str(in_data)
    counts = [(1 if p is not None else 0) for p in passports]
    print(f"The Answer to the Day 4 Passport Puzzle is {sum(counts)}")

    passports = Passport.from_str(in_data, do_cast=True)
    counts = [(1 if p is not None else 0) for p in passports]
    print(f"The Answer to the Day 4 Part 2 Passport Puzzle is {sum(counts)}")


if __name__ == '__main__':
    main()

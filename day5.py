"""
Advent of Code Day 5 Puzzle

author: Ethan Lew

--- Day 5: Binary Boarding ---
"""
import csv
import typing as typ


def decode_str(code_str: str) -> typ.Tuple[int, int]:
    row = int(code_str[:7].replace('F', '0').replace('B', '1'), base = 2)
    seat = int(code_str[-3:].replace('L', '0').replace('R', '1'), base = 2)
    return (row, seat)


def get_seat_id(code: typ.Union[str, typ.Tuple[int]]) -> int:
    if isinstance(code, str):
        return get_seat_id(decode_str(code))
    else:
        return code[0] * 8 + code[1]


def main():
    with open("./inputs/day5.csv", "r") as fp:
        reader = csv.reader(fp, delimiter='\n')
        input_data = [str(r[0]) for r in list(reader)]
    sids = [get_seat_id(r) for r in input_data]
    print(f"The Answer to the Day 5 Seat ID Puzzle is {max(sids)}")
    for idx in range(min(sids), max(sids)):
        if idx not in sids:
            print(f"The Answer to the Day 5 Part2 Seat ID Puzzle is {idx}")


if __name__ == '__main__':
    main()

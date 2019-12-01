from aoc import file_reader

def fuel_req(m):
    return m // 3 - 2 


def solve():
    text_input = file_reader("day1part1")
    masses = [int(x) for x in text_input]
    return sum([fuel_req(m) for m in masses])

print(solve())
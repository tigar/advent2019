from aoc import file_reader

def solve(noun: int, verb: int) -> int:
    code = file_reader("day2")
    list_code = code[0].split(",")
    intcode = [int(x) for x in list_code]
    i = 0
    intcode[1] = noun
    intcode[2] = verb
    while intcode[i] != 99:
        if intcode[i] == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        if intcode[i] == 2:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
        i += 4
        cur = intcode[i]


    return intcode[0]

def part2(target):
    for i in range(100):
        for j in range(100):
            if solve(i, j) == target:
                return 100 * i + j

print(solve(12, 2))
print(part2(19690720))
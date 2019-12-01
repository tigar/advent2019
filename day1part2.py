from aoc import file_reader

def fuel_req(m):
    return m // 3 - 2 

def solve():
    text_input = file_reader("day1part1")
    masses = [int(x) for x in text_input]

    res = 0
    
    for m in masses:
        temp = m
        while fuel_req(temp) > 0:
            temp = fuel_req(temp)
            res += temp

    return res

print(solve())
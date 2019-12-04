from aoc import file_reader

def solve():
    count = 0
    ranges = file_reader('day4')
    A = int(ranges[0])
    B = int(ranges[1])
    for i in range(A, B):
        if adjacent(str(i)) and increase(i):
            count += 1

    return count

def adjacent(n):
    counter = 0
    seen_double = 0

    for i in range(5):
        if n[i] == n[i+1]:
            seen_double += 1
        else:
            # ***  part 1 ****
            # if seen_double > 0:
            #     counter+=1

            # ***  part 2 ****
            if seen_double == 1:
                counter+=1
            seen_double = 0

    # ***  part 1 ****
    # if seen_double > 0:
    #     counter += 1

    # ***  part 2 ****
    if seen_double == 1:
        counter += 1
    return counter > 0

    

def increase(n):
    n = str(n)
    cur = n[0]
    for i in range(1,6):
        if n[i] < cur:
            return False
        else:
            cur = n[i]
    return True

print(increase('122222'))
print(solve())
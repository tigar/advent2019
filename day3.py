from aoc import file_reader

code = file_reader("day3")
A = code[0].split(",")
B = code[1].split(",")

directions = {'R': (1, 0), 'D': (0, 1), 'L':(-1, 0), 'U': (0, -1)}

def solve(K):
    x = 0
    y = 0
    dist = 0
    res = {}

    for i in K:
        d = i[0]
        length = int(i[1:])

        for j in range(length):
            x += directions[d][0]
            y += directions[d][1]
            dist+=1
            if (x, y) not in res:
                res[(x,y)] = dist
    return res

solvedA = solve(A)
solvedB = solve(B)

union = set(solvedA.keys())&set(solvedB.keys())

ans1 = min([abs(x) + abs(y) for (x,y) in union])
ans2 = min([solvedA[i] + solvedB[i] for i in union])
print(ans1, ans2)
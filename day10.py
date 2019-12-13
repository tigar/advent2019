import math
from aoc import file_reader

with open("day10.in") as f:
    content = f.readlines()

allAsteroids = file_reader("day10")

def countAsteroids(loc, asteroids):
    found = set()
    for asteroid in asteroids:
        if asteroid != loc:
            dx, dy = asteroid[0] - loc[0], asteroid[1] - loc[1]
            gcdenom = abs(math.gcd(dx, dy))
            reduced_gcd = (dx//gcdenom, dy//gcdenom)
            found.add(reduced_gcd)

    return found

asteroids = set()

for x in range(len(allAsteroids)):
    for y in range(len(allAsteroids[0])):
        if allAsteroids[x][y] == "#":
            asteroids.add((x,y))

station_locs = []

for loc in asteroids:
    num = countAsteroids(loc, asteroids)
    station_locs.append((len(num), loc, num))
    
station_locs.sort()
ans, loc, found = station_locs[-1]
print("Part 1: {}".format(ans))





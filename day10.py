import math
from aoc import file_reader

with open("day10.in") as f:
    content = f.readlines()
allAsteroids = file_reader("day10")

def countAsteroids(loc, asteroids):
    '''
    take the slope of location and the asteroid, 
    return a set of the gcd-reduced slopes
    '''
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

'''
Go through each asteroid and total the number of asteroids
in the line of sight
'''
station_locs = []
for loc in asteroids:
    num = countAsteroids(loc, asteroids)
    station_locs.append((len(num), loc, num))
    
station_locs.sort()
ans, loc, seen_from_station = station_locs[-1]
print("Part 1: {}".format(ans))

# Atan2 is cool, I wish I knew about it sooner!
destroyed = [(math.atan2(dy, dx), (dx, dy)) for dx, dy in seen_from_station]
destroyed.sort(reverse=True)
dx, dy = destroyed[199][1]

x, y = loc[0]+dx, loc[1]+dy
while (x,y) not in asteroids:
    x, y = x+dx, y+dy

print("Part 2: {}".format(y*100+x))


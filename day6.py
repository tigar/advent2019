from collections import defaultdict

# use the defaultdict to create sets for new keys
planets = defaultdict(lambda: set())

with open('day6.in') as f:
    text = f.readlines()

for line in text:
    i, j = line.strip().split(")")
    planets[i].add(j)
    planets[j].add(i)

def solve(start, tree):
    # Create a queue with the node and its depth from the start
    queue = [(start,0)]
    visited = set()
    total = 0
    for planet, d in queue:
        visited.add(planet)
        new_planets = planets.get(planet, [])
        queue += [(new_planet, d+1) for new_planet in new_planets if new_planet not in visited]
        yield planet, d

# print(solve('COM', planets))
ans1 = sum(d for planet, d in solve('COM', planets))
print("Part 1: " + str(ans1))

ans2 = next(d - 2 for planet, d in solve('YOU', planets) if planet == 'SAN')
print("part 2: " + str(ans2))
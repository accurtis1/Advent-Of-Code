def get_asteroids(oFile):
    orbits = {}
    objects = set()

    mapList = []
    currentRow = []

    for line in _file:
        ## NOT FINISHED BECAUSE FUCK THIS PROBLEM
        to_orbit, orbiter = line.rstrip().split(")")
        orbits[orbiter] = to_orbit
        objects.add(to_orbit)
        objects.add(orbiter)

    return empty, asteroids

def get_asteroid_map(empty, asteroids):
    

with open("testMap1.txt") as oFile:
    empty, asteroids = get_asteroids(oFile)

print(f"{get_asteroid_map(empty, asteroids)}")  

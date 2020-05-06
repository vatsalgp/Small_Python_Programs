toCheck = []


def arrayToDict(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            map[y][x] = {"isWall": map[y][x], "distance": float("inf")}
    return map


def neighbour(map, y, x, nextY, nextX):
    global toCheck
    if not map[nextY][nextX]["isWall"]:
        old = map[nextY][nextX]["distance"]
        new = map[y][x]["distance"] + 1
        if new < old:
            map[nextY][nextX]["distance"] = new
            toCheck.append([nextY, nextX])


def neighbours(map, y, x, height, length):
    if x+1 < length:
        neighbour(map, y, x, y, x+1)
    if x-1 >= 0:
        neighbour(map, y, x, y, x-1)
    if y+1 < height:
        neighbour(map, y, x, y+1, x)
    if y-1 >= 0:
        neighbour(map, y, x, y-1, x)


def shortestPath(map):
    global toCheck
    height = len(map)
    length = len(map[0])

    toCheck.append([0, 0])
    map[0][0]["distance"] = 1

    while len(toCheck):
        [y, x] = toCheck.pop(0)
        if not map[y][x]["isWall"]:
            neighbours(map, y, x, height, length)

    minLength = map[-1][-1]["distance"]

    for y in range(height):
        for x in range(length):
            map[y][x]["distance"] = float("inf")

    return minLength


def solution(map):
    global toCheck
    map = arrayToDict(map)
    minLength = min(shortestPath(map), float("inf"))

    height = len(map)
    length = len(map[0])

    for y in range(height):
        for x in range(length):
            if map[y][x]["isWall"]:
                map[y][x]["isWall"] = 0
                minLength = min(shortestPath(map), minLength)
                map[y][x]["isWall"] = 1
    return minLength


# map = [
#     [0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0]
# ]

# print(solution(map))

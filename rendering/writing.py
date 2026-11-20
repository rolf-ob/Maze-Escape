from core.spatial import world_to_screen
from constants import COLORS

def draw_line(game: object, point1: tuple, point2: tuple):
    dx = (point1[0] - point2[0])
    dy = (point1[1] - point2[1])
    step = abs(dx) if abs(dx) >= abs(dy) else abs(dy)

    if step != 0:
        dx /= step
        dy /= step
        new_x = point2[0]
        new_y = point2[1]

        for _ in range(step):
            game.world[int(new_x), int(new_y)] = "1"
            new_x += dx
            new_y += dy

def connect_corners(game, corner1, corner2):
    point1 = world_to_screen(game, game.camera, corner1[0], corner1[1], corner1[2])
    point2 = world_to_screen(game, game.camera, corner2[0], corner2[1], corner2[2])
    
    if point1 and point2:
        draw_line(game, point1, point2)

def draw_cubes(game):
    for cube in game.cubes:
        for i in range(4):
            connect_corners(game, cube.corners[i], cube.corners[[1, 2, 3, 0][i]])

        for i in range(4, 8):
            connect_corners(game, cube.corners[i], cube.corners[[5, 6, 7, 4][i-4]])

        for i, j in zip(range(4), range(4, 8)):
            connect_corners(game, cube.corners[i], cube.corners[j])

def write(game):
    draw_cubes(game)

    ls = [
        [
            f"{game.world.get((x, y), "0")}"
            for x in range(game.size.columns)
        ]
        for y in range(game.size.lines)
    ]

    output = ""
    for i, y in enumerate(ls):
        for x in y:
            output += x
        if i != len(ls)-1:
            output += "\n"

    return output
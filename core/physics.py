def update(game):
    for cube in game.cubes:
        cube.yaw += 1
        cube.recompute()
import shutil, sys, math, mouse

from core.input import handle_input
from core.physics import update
from rendering.writing import write
from entities.cube import Cube
from entities.camera import Camera
from constants import FOV

class Game:
    def __init__(self):
        print("\033[H\033[J", end="")
        mouse.move(500, 500)
        self.running = True

        self.camera = Camera(0, 40, -50, -35, 0)
        self.fov_rad = math.radians(FOV)
        self.locked = True

        self.cubes = [
            Cube(0, 0, 0, 10, 10, 10),
            Cube(0, 0, 0, 10, 10, 10, yaw=90),
            Cube(0, 0, 0, 10, 10, 10, yaw=180),
            Cube(0, 0, 0, 10, 10, 10, yaw=270),
            Cube(0, 10, 0, 5, 5, 5),
            Cube(0, 10, 0, 5, 5, 5, yaw=90),
            Cube(0, 10, 0, 5, 5, 5, yaw=180),
            Cube(0, 10, 0, 5, 5, 5, yaw=270),
        ]

    def run(self):
        while self.running:
            self.world = {}
            self.size = shutil.get_terminal_size()
            self.fov_scale = self.size.columns / (2 * math.tan(self.fov_rad / 2))

            handle_input(self)
            update(self)
            screen = write(self)

            print("\033[H\033[J\033[32m", end="")
            sys.stdout.write(screen)
            sys.stdout.flush()
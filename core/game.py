import shutil, sys, math, mouse

from core.input import handle_input
from rendering.writing import write
from entities.cube import Cube
from entities.camera import Camera
from constants import FOV

class Game:
    def __init__(self):
        print("\033[H\033[J", end="")
        mouse.move(500, 500)
        self.running = True

        self.camera = Camera()
        self.fov_rad = math.radians(FOV)

        self.cubes = [
            Cube(0, 0, 0, 10, 10, 10)
        ]

    def run(self):
        while self.running:
            self.world = {}
            self.size = shutil.get_terminal_size()
            self.fov_scale = self.size.columns / (2 * math.tan(self.fov_rad / 2))

            handle_input(self)
            screen = write(self)
            
            sys.stdout.write(screen)
            sys.stdout.flush()
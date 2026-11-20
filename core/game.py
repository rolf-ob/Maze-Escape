import shutil, sys

from core.input import handle_input
from rendering.writing import write

class Game:
    def __init__(self):
        print("\033[H\033[J", end="")

        self.running = True

    def run(self):
        while self.running:
            self.size = shutil.get_terminal_size()

            handle_input(self)
            screen = write(self)

            
            sys.stdout.write(screen)
            sys.stdout.flush()
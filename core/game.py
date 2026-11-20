from core.input import handle_input

class Game:
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            handle_input(self)
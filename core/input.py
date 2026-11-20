import keyboard as k

def handle_input(game):
    if k.is_pressed("esc"):
        game.running = False
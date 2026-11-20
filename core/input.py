import keyboard as kb

def handle_input(game):
    if kb.is_pressed("esc"):
        game.running = False
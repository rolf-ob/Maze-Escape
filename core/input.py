import keyboard as kb
import math, mouse

from constants import CAMERA_MOVEMENT_SPEED, MOUSE_SENSITIVITY

def handle_input(game):
    yaw = math.radians(game.camera.yaw)
    cos_y, sin_y = math.cos(yaw), math.sin(yaw)

    if kb.is_pressed("esc"):
        game.running = False

    if kb.is_pressed("u"):
        game.locked = not game.locked

    if kb.is_pressed("w"):
        game.camera.z += cos_y * CAMERA_MOVEMENT_SPEED
        game.camera.x += sin_y * CAMERA_MOVEMENT_SPEED
    if kb.is_pressed("a"):
        game.camera.x -= cos_y * CAMERA_MOVEMENT_SPEED
        game.camera.z += sin_y * CAMERA_MOVEMENT_SPEED
    if kb.is_pressed("s"):
        game.camera.z -= cos_y * CAMERA_MOVEMENT_SPEED
        game.camera.x -= sin_y * CAMERA_MOVEMENT_SPEED
    if kb.is_pressed("d"):
        game.camera.x += cos_y * CAMERA_MOVEMENT_SPEED
        game.camera.z -= sin_y * CAMERA_MOVEMENT_SPEED
    
    if kb.is_pressed("left shift"):
        game.camera.y -= CAMERA_MOVEMENT_SPEED
    if kb.is_pressed("spacebar"):
        game.camera.y += CAMERA_MOVEMENT_SPEED

    if game.locked:
        mouse_x, mouse_y = mouse.get_position()
        yaw_movement, pitch_movement = mouse_x - 500, mouse_y - 500
        mouse.move(500, 500)

        game.camera.pitch -= pitch_movement * MOUSE_SENSITIVITY
        game.camera.yaw += yaw_movement * MOUSE_SENSITIVITY

        game.camera.pitch = max(-90, min(90, game.camera.pitch))
        game.camera.yaw %= 360
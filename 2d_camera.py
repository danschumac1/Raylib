'''
Camera has 4 main properties:
1. offset: the offset of the camera in the world
3. zoom: the zoom level of the camera
2. rotation: the angle of the camera in the world
4. target: the point in the world where the camera is looking
'''

import pyray as p

ball_x = 40
ball_y = 40

p.init_window(800, 600, "Ball Game")

cam = p.Camera2D((400, 300), (0,0), 45, 1)

while not p.window_should_close():
    p.begin_drawing()
    # this would be where UI elements are drawn
    p.begin_mode_2d(cam)                                            # starts 2D mode with the camera
    # everything drawn here will be affected by the camera
    p.clear_background(p.RAYWHITE)                                  # clears the background each frame
    
    # we need int to cast the float to an int
    p.draw_rectangle(int(ball_x), int(ball_y), 40, 30, p.RED)     # casts coordinates to int for drawing

    # Movement
    if p.is_key_down(p.KeyboardKey.KEY_RIGHT):                      # moves the ball to the right
        ball_x += 0.1                                               # keeps ball_x as a float for smooth movement
    if p.is_key_down(p.KeyboardKey.KEY_LEFT):                       # moves the ball to the left
        ball_x -= 0.1                                               # keeps ball_x as a float for smooth movement
    if p.is_key_down(p.KeyboardKey.KEY_UP):                         # moves the ball up
        ball_y -= 0.1                                               # keeps ball_y as a float for smooth movement
    if p.is_key_down(p.KeyboardKey.KEY_DOWN):                       # moves the ball down
        ball_y += 0.1                                               # keeps ball_y as a float for smooth movement

    # Camera Controls
    # Zoom
    if p.is_key_down(p.KeyboardKey.KEY_A):                          # zooms in
        cam.zoom -= 0.0001
    if p.is_key_down(p.KeyboardKey.KEY_S):                          # zooms out
        cam.zoom += 0.0001
    # Rotation
    if p.is_key_down(p.KeyboardKey.KEY_D):                          # rotates the camera clockwise
        cam.rotation -= 0.01
    if p.is_key_down(p.KeyboardKey.KEY_F):                          # rotates the camera counter-clockwise
        cam.rotation += 0.01


    p.end_mode_2d()                                                 # ends 2D mode
    p.end_drawing()
p.close_window()

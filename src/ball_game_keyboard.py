import pyray as p

ball_x = 40
ball_y = 40
BALL_RADIUS = 30

p.init_window(800, 600, "Ball Game")
while not p.window_should_close():
    p.begin_drawing()
    p.clear_background(p.RAYWHITE)                                  # clears the background each frame
    
    # we need int to cast the float to an int
    p.draw_circle(int(ball_x), int(ball_y), BALL_RADIUS, p.RED)     # casts coordinates to int for drawing

    if p.is_key_down(p.KeyboardKey.KEY_RIGHT):                      # moves the ball to the right
        ball_x += 0.1                                               # keeps ball_x as a float for smooth movement
    if p.is_key_down(p.KeyboardKey.KEY_LEFT):                       # moves the ball to the left
        ball_x -= 0.1                                               # keeps ball_x as a float for smooth movement
    if p.is_key_down(p.KeyboardKey.KEY_UP):                         # moves the ball up
        ball_y -= 0.1                                               # keeps ball_y as a float for smooth movement
    if p.is_key_down(p.KeyboardKey.KEY_DOWN):                       # moves the ball down
        ball_y += 0.1                                               # keeps ball_y as a float for smooth movement

    p.end_drawing()
p.close_window()

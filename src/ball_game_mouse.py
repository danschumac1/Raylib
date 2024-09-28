import pyray as p

ball_x = 40
ball_y = 40
BALL_RADIUS = 30
ball_color = p.RED

p.init_window(800, 600, "Ball Game")
while not p.window_should_close():
    p.begin_drawing()
    p.clear_background(p.RAYWHITE)                                  # clears the background each frame
    
    # we need int to cast the float to an int
    p.draw_circle(int(ball_x), int(ball_y), BALL_RADIUS, ball_color)     # casts coordinates to int for drawing

    mouse_pos = p.get_mouse_position()                              # keeps ball_y as a float for smooth movement
    ball_x = mouse_pos.x
    ball_y = mouse_pos.y

    if(p.is_mouse_button_down(p.MouseButton.MOUSE_BUTTON_LEFT)):
        ball_color = p.BLUE
    if(p.is_mouse_button_down(p.MouseButton.MOUSE_BUTTON_RIGHT)):
        ball_color = p.RED
    if(p.is_mouse_button_down(p.MouseButton.MOUSE_BUTTON_MIDDLE)):
        ball_color = p.GREEN

    p.end_drawing()
p.close_window()

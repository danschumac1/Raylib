import pyray as p

# width, height, title
p.init_window(                                           # initializes the window
    800,
    600,
    "Welcome to PyRay"
)

while not p.window_should_close():                      # keeps the window open
    p.begin_drawing()                                   # starts drawing
    # drawing code here

    # x-cord, y-cord, font-size, color
    p.draw_text("Hellow world!", 10, 14, 50, p.BLUE)    # draws text
    p.end_drawing()                                     # ends drawing

p.close_window()                                        # closes the window
import pyglet

x_pressed = False
y_pressed = False
x_released = False
y_released = False

def on_joybutton_press(joystick, button):
    print("button pressed...")
    print(f"button: {button}")

def on_joyaxis_motion(joystick, axis, value):
    #print(f"axis: {axis} | value: {value}")
    print(f"x: {joystick.x} | axis: {axis} | value: {value}")
    print(f"y: {joystick.y} | axis: {axis} | value: {value}")
    #if axis == "x":
    #    if value == 1.0 or value == -1.0:
    #        print("x pressed...")
    #        x_pressed = True
    #        x_released = False
    #    elif x_pressed:
    #        print("x released...")
    #        x_released = True
    #        x_pressed = False

joysticks = pyglet.input.get_joysticks()

if joysticks: 
    joystick = joysticks[0]

joystick.on_joybutton_press = on_joybutton_press
joystick.on_joyaxis_motion = on_joyaxis_motion

#win = pyglet.window.Window()
#joystick.open(window=win)
joystick.open()
pyglet.app.run()

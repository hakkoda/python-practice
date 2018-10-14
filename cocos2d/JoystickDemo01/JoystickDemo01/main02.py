import pyglet
import cocos
from cocos.actions import *

class HelloJoystick(cocos.layer.ColorLayer):
    def __init__(self):
        super(HelloJoystick, self).__init__(64, 64, 224, 255)
        joysticks = pyglet.input.get_joysticks()
        if joysticks: 
            self.joystick = joysticks[0]
        self.joystick.on_joybutton_press = self.on_joybutton_press
        self.joystick.on_joyaxis_motion = self.on_joyaxis_motion
        self.joystick.open()

        self.x_pressed = False
        self.y_pressed = False
        self.x_released = False
        self.y_released = False

    def on_joybutton_press(self, joystick, button):
        print("button pressed...")
        print(f"button: {button}")

    def on_joyaxis_motion(self, joystick, axis, value):
        print(f"x: {joystick.x} | axis: {axis} | value: {value}")
        print(f"y: {joystick.y} | axis: {axis} | value: {value}")
        if axis == "x":
            if value == 1.0 or value == -1.0:
                print("x pressed...")
                self.x_pressed = True
                self.x_released = False
            elif self.x_pressed:
                print("x released...")
                self.x_released = True
                self.x_pressed = False
        elif axis == "y":
            if value == 1.0 or value == -1.0:
                print("y pressed...")
                self.y_pressed = True
                self.y_released = False
            elif self.y_pressed:
                print("y released...")
                self.y_released = True
                self.y_pressed = False



# Init the director
cocos.director.director.init()

# Create the layer
hello_layer = HelloJoystick()

# Create a scene with our layer
main_scene = cocos.scene.Scene(hello_layer)

# Have the director run the scene
cocos.director.director.run(main_scene)

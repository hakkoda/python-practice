import pyglet
import cocos
from cocos.actions import *

class PlayerSprite(cocos.sprite.Sprite):
    def __init__(self):
        pyglet.resource.path = ["img"]
        pyglet.resource.reindex()
        invader = pyglet.resource.image("animated_invaders.png")
        self.invader_seq = pyglet.image.ImageGrid(invader, 1, 2)
        self.animated_img = pyglet.image.Animation.from_image_sequence(self.invader_seq[0:], 0.1, loop=True)
        super(PlayerSprite, self).__init__(self.invader_seq[0])
        #self.sprite2 = cocos.sprite.Sprite(self.animated_img)  # during movement
        #self.sprite2 = cocos.sprite.Sprite(self.invader_seq[0]) # during rest
        self.position = 32,24 
        self.scale = 1
        self.speed = 150
        self.velocity = 0, 0

    def rest(self):
        self.velocity = 0,0
        self.image = self.invader_seq[0]

    def move_x(self, value):
        current_y_velocity = self.velocity[1]
        self.velocity = value * self.speed, current_y_velocity
        self.image = self.animated_img

    def move_y(self, value):
        current_x_velocity = self.velocity[0]
        self.velocity = current_x_velocity, -value * self.speed
        self.image = self.animated_img


class SpriteDemo01(cocos.layer.ColorLayer):
    def __init__(self):
        super(SpriteDemo01, self).__init__(0,0,0,0)
        sprite1 = cocos.sprite.Sprite("img/invaders.png")
        sprite1.position = 320, 240
        #sprite.position = 16, 12
        sprite1.scale = 4
        sprite1.do(Repeat(RotateBy(360, duration=2)))
        self.add(sprite1)

        ## trying out animated sprite
        #pyglet.resource.path = ["img"]
        #pyglet.resource.reindex()

        ## animate with gif -- useful, but I don't feel like I have good control
        ## on the timing of the animation.
        ##invader = pyglet.resource.animation("invaders.gif")
        ##self.sprite2 = cocos.sprite.Sprite(invader)

        self.sprite2 = PlayerSprite()
        self.add(self.sprite2)

        # setup joysticks
        joysticks = pyglet.input.get_joysticks()
        if joysticks: 
            self.joystick = joysticks[0]
        self.joystick.on_joybutton_press = self.on_joybutton_press
        self.joystick.on_joybutton_release = self.on_joybutton_release
        self.joystick.on_joyaxis_motion = self.on_joyaxis_motion
        self.joystick.open()

        self.x_button_status = "RELEASED"
        self.y_button_status = "RELEASED"

        self.sprite2.do(Move())

    def on_joyaxis_motion(self, joystick, axis, value):
        if axis == "x":
            if value == 1.0 or value == -1.0:
                self.x_button_status = "PRESSED"
                self.sprite2.move_x(value)
            elif self.x_button_status == "PRESSED":
                self.x_button_status = "RELEASED"
                self.sprite2.rest()
        elif axis == "y":
            if value == 1.0 or value == -1.0:
                self.y_button_status = "PRESSED"
                self.sprite2.move_y(value)
            elif self.y_button_status == "PRESSED":
                self.y_button_status = "RELEASED"
                self.sprite2.rest()

    def on_joybutton_press(self, joystick, button):
        print("button pressed...")
        print(f"button: {button}")
        self.sprite2.speed = 300

    def on_joybutton_release(self, joystick, button):
        print("button released...")
        print(f"button: {button}")
        self.sprite2.speed = 150


if __name__ == "__main__":
    cocos.director.director.init()
    demo_layer = SpriteDemo01()
    main_scene = cocos.scene.Scene(demo_layer)
    cocos.director.director.run(main_scene)

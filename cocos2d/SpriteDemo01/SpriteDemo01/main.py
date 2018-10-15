import pyglet
import cocos
from cocos.actions import *

class SpriteDemo01(cocos.layer.ColorLayer):
    def __init__(self):
        super(SpriteDemo01, self).__init__(0,0,0,0)
        sprite1 = cocos.sprite.Sprite("img/invaders.png")
        sprite1.position = 320, 240
        #sprite.position = 16, 12
        sprite1.scale = 4
        sprite1.do(Repeat(RotateBy(360, duration=2)))
        self.add(sprite1)

        # static image sprite
        #self.sprite2 = cocos.sprite.Sprite("img/invaders.png")
        #self.sprite2.position = 32,24 
        #self.sprite2.scale = 2
        #self.sprite2.speed = 150
        #self.sprite2.velocity = 0, 0
        #self.add(self.sprite2)

        # trying out animated sprite
        pyglet.resource.path = ["img"]
        pyglet.resource.reindex()

        # animate with gif -- useful, but I don't feel like I have good control
        # on the timing of the animation.
        #invader = pyglet.resource.animation("invaders.gif")
        #self.sprite2 = cocos.sprite.Sprite(invader)

        # animate with sprite sheet
        invader = pyglet.resource.image("animated_invaders.png")
        self.invader_seq = pyglet.image.ImageGrid(invader, 1, 2)
        self.animated_img = pyglet.image.Animation.from_image_sequence(self.invader_seq[0:], 0.1, loop=True)
        #self.sprite2 = cocos.sprite.Sprite(self.animated_img)  # during movement
        self.sprite2 = cocos.sprite.Sprite(self.invader_seq[0]) # during rest

        self.sprite2.position = 32,24 
        self.sprite2.scale = 1
        self.sprite2.speed = 150
        self.sprite2.velocity = 0, 0
        self.add(self.sprite2)

        # setup joysticks
        joysticks = pyglet.input.get_joysticks()
        if joysticks: 
            self.joystick = joysticks[0]
        self.joystick.on_joybutton_press = self.on_joybutton_press
        self.joystick.on_joybutton_release = self.on_joybutton_release
        self.joystick.on_joyaxis_motion = self.on_joyaxis_motion
        self.joystick.open()

        self.x_pressed = False
        self.y_pressed = False
        self.x_released = False
        self.y_released = False

        self.sprite2.do(Move())

    def on_joybutton_press(self, joystick, button):
        print("button pressed...")
        print(f"button: {button}")
        self.sprite2.speed = 300

    def on_joybutton_release(self, joystick, button):
        print("button released...")
        print(f"button: {button}")
        self.sprite2.speed = 150

    def on_joyaxis_motion(self, joystick, axis, value):
        if axis == "x":
            if value == 1.0 or value == -1.0:
                self.x_pressed = True
                self.x_released = False
                self.sprite2.velocity = value * self.sprite2.speed, 0
                self.sprite2.image = self.animated_img
            elif self.x_pressed:
                self.x_released = True
                self.x_pressed = False
                self.sprite2.velocity = 0,0
                self.sprite2.image = self.invader_seq[0]
        elif axis == "y":
            if value == 1.0 or value == -1.0:
                self.y_pressed = True
                self.y_released = False
                self.sprite2.velocity = 0, -value * self.sprite2.speed
                self.sprite2.image = self.animated_img
            elif self.y_pressed:
                self.y_released = True
                self.y_pressed = False
                self.sprite2.velocity = 0,0
                self.sprite2.image = self.invader_seq[0]

if __name__ == "__main__":
    cocos.director.director.init()
    demo_layer = SpriteDemo01()
    main_scene = cocos.scene.Scene(demo_layer)
    cocos.director.director.run(main_scene)

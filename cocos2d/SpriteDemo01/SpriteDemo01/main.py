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

        sprite2 = cocos.sprite.Sprite("img/invaders.png")
        sprite2.position = 32,24 
        sprite2.scale = 2
        self.add(sprite2)

if __name__ == "__main__":
    cocos.director.director.init()
    demo_layer = SpriteDemo01()
    main_scene = cocos.scene.Scene(demo_layer)
    cocos.director.director.run(main_scene)

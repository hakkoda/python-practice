from random import *

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return "finished"

class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print("central_corridor")
        return "laser_weapon_armory"

class LaserWeaponArmory(Scene):
    def enter(self):
        print("laser_weapon_armory")
        return "the_bridge"

class TheBridge(Scene):
    def enter(self):
        print("the_bridge")
        return "escape_pod"

class EscapePod(Scene):
    def enter(self):
        print("escape_pod")
        return "finished"

class Map(object):
    def __init__(self, start_scene):
        self.scenes = { 
            "death": Death(),
            "central_corridor": CentralCorridor(),
            "laser_weapon_armory": LaserWeaponArmory(),
            "the_bridge": TheBridge(),
            "escape_pod": EscapePod(),
            "finished": Finished()
        }
        self.start_scene = self.scenes[start_scene]

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)

    def opening_scene(self):
        return self.start_scene

a_map = Map("central_corridor")
a_game  = Engine(a_map)
a_game.play()

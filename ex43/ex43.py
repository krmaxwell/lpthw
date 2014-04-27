from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "Play's first scene", current_scene

        while True:
            print "\n-----"
            next_scene_name = current_scene.enter()
            print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "map returns new scene", current_scene


class Death(Scene):

    def enter(self):
        print "Wipe yourself off - you dead."
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "ERMAGERD aliens out to getcha. Whatcha gon' do?"
        action = raw_input("> ")

        if "shoot" in action:
            print "You shoot, you score. Then the rest blast you."
            return 'death'
        elif "dodge" in action:
            print "You can't dodge a laser, silly."
            return 'death'
        elif "joke" in action:
            print "The aliens laugh so hard you get away."
            return 'laser_weapon_armory'
        else:
            print "lolwut."
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You need to unlock the code. 3 digits, 10 tries, go."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input('[keypad]> ')
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZT wrong!"
            guesses += 1
            guess = raw_input('[keypad]> ')

        if guess == code:
            print "You set you up the bomb and head to the bridge."
            return 'the_bridge'
        else:
            print "Too bad. You will die now."
            return 'death' 


class TheBridge(Scene):

    def enter(self):
        print "How do you want to handle this?"
        action = raw_input('> ')

        if 'throw' in action:
            print "It'll go off, sure, but as soon as it hits the deck. At least they'll die too."
            return 'death'
        elif 'place' in action:
            print "Good job. Now let's blow this joint and go home."
            return 'escape_pod'
        else:
            print "lolwut."
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print "5 pods here - which one?"
        good_pod = randint(1,5)
        guess = raw_input("[pod]> ")

        if int(guess) != good_pod:
            print "Space jelly"
            return 'death'
        else:
            print "You win!"
            return 'finished'


class Map(object):

    scenes = {
              'central_corridor': CentralCorridor(),
              'laser_weapon_armory': LaserWeaponArmory(),
              'the_bridge': TheBridge(),
              'escape_pod': EscapePod(),
              'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "start_scene in __init__", self.start_scene

    def next_scene(self, scene_name):
        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

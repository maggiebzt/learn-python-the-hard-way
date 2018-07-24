# Scene is-a object
class Scene(object):
	
	def enter(self):
		pass

# Engine is-a object
class Engine(object):
	
	def __init__(self, scene_map):
		pass
	
	def play(self):
		pass

# Death is-a Scene
class Death(Scene)
	
	def enter(self):
		pass
		
# CentralCorridor is-a Scene
class CentralCorridor(Scene):
	
	def enter(self):
		pass

# LaserWeaponArmory is-a Scene
class LaserWeaponArmory(Scene):
	
	def enter(self):
		pass

# TheBridge is-a Scene
class TheBridge(Scene):

	def enter(self):
		pass

# EscapePod is-a Scene
class EscapePod(Scene):
	
	def enter(self):
		pass

# Map is-a Object
class Map(object):

	def __init__(self, start_scene):
		pass
	
	def next_scene(self, scene_name):
		pass
		
	def opening_scene(self):
		pass
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
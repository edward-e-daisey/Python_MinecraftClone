# Name: Edward E. Daisey
# Date: January 5th, 2023
# Description: This is a Minecraft clone made in Python.
# Source: https://tinyurl.com/py-minecraft

# Purpose - Allows use of the Ursina Engine to create a GUI from a first person perspective.
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Purpose - Textures & Sounds.
app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
punch_sound   = Audio('assets/punch_sound.wav',loop = False, autoplay = False)
block_pick = 1

# Purpose - Allows user to pick block.
def update():
	global block_pick

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4

# Purpose - Ground cube parameters.
class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)
		
# Purpose - Allows placement and destruction of cubes.
	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				punch_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)

			if key == 'right mouse down':
				punch_sound.play()
				destroy(self)
# Purpose - Sky parameters.
class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)
		
# Purpose - Hand parameters.
class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)

# Purpose - Creates 25 x 25 Map.
for z in range(25):
	for x in range(25):
		voxel = Voxel(position = (x,0,z))

# Purpose - Calls FirstPersonController, Sky, and Hand.
player = FirstPersonController()
sky = Sky()
hand = Hand()

# Purpose - Run Application.
app.run()

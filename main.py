from ursina import *
from ursina import texture_importer
from random import choice, randint 
# Likely refers to a component or class used in game development to implement a first-person perspective and control scheme for the player.
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.fullscreen = True
window.borderless = False 

velocity: int = 0
max_speed: int = 50
acceleration: int = 5
deceleration: int = 8
speed_text = Text(text="Speed: 0", position=(-0.85, 0.45), origin=(0,0), scale=2)

# Grid parameters
grid_size = 10 # number of cells in one row/ column
cell_size = 20 # size of each cell 
road_width = 4 # width of roads between cells


EditorCamera()
sky = Sky(Texture='sky_sunset')
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1)) # point the light in a specific direction 



# add ground
ground = Entity(
    model="plane", 
    scale=(10000, 1, 10000), 
    texture="_assets/aerial_grass_rock_1k/aerial_grass_rock_diff_1k.jpg")
ground.texture_scale=(1000, 1000) # stretch the texture to fit the ground


road = Entity(
    model="cube", 
    scale=(10, 0.1, 100), # scale the ground to be large 
    texture="_assets/asphalt_02_1k/asphalt_02_diff_1k.jpg")
road.position=(0, 0.1, 0)
road.texture_scale = (10, 100)
road_width = 10

off_road = Entity(
    model="cube", 
    scale=(10, 0.1, 50), 
    texture="_assets/gravelly_sand_1k/gravelly_sand_diff_1k.jpg")
off_road.position=(15, 0.1, 0)
off_road.texture_scale = (10, 50)

terrain_from_heightmap_texture = Entity(model=Terrain('heightmap_1', skip=8), scale=(40,5,20), texture='heightmap_1')

'''
I'm just getting the height values from the previous terrain as an example, but you can provide your own.
It should be a list of lists, where each value is between 0 and 255.
'''
hv = terrain_from_heightmap_texture.model.height_values.tolist()
terrain_from_list = Entity(model=Terrain(height_values=hv), scale=(40,5,20), texture='heightmap_1', x=40)
terrain_bounds = Entity(model='wireframe_cube', origin_y=-.5, scale=(40,5,20), color=color.lime)




# # add buildings 
for i in range(10):
    distance_between_buildings = 30
    road_length = road.scale.z * 100 # use roads scale for aligment

    # left side of the road
    building_left  = Entity(model="cube")

# for x in range(-50, 50, 10):
#     for z in range(-50, 50, 10):
#         building = Entity(model="cube", scale=(5, 10, 5), texture='building_texture', position=(x, 5, z))

# # Add trees
# for x in range(-50, 50, 10):
#     for z in range(-50, 50, 10):
#         if x % 20 == 0 and z % 20 == 0:  # Place trees in a grid
#             tree = Entity(model='cube', scale=(1, 5, 1), texture='tree_texture', position=(x, 2.5, z))




# Add a player car
car = Entity(
    model='_assets/Truck/Constructiont/con_truck.gltf', 
    scale=(1, 1, 1), 
    position=(0, 1, 0))



# ai traffic

npc_car = Entity(model='cube', scale=(2, 1, 4), color=color.red, position=(0, 1, -50))


# Replace the static camera with a FirstPersonController
# player = FirstPersonController()
# player.position = (0, 10, 0)  # Start the player above the ground
# player.gravity = 0  # Disable gravity so the player can fly
# camera.position = (0, 10, -60) # position the camera above the ground


ground.collider = 'box'
road.collider = 'box'
car.collider = car.model

# camera modes 
camera_mode = "car" # start with car camera
free_camera = None 
def toggle_camera_mode():
    global camera_mode, free_camera
    if camera_mode == "car":
        camera_mode = "free"
        print("switched to free camera")
        if free_camera is None:
            free_camera = FirstPersonController()
            free_camera.gravity = 0
        else:
            free_camera.enabled = True
    else:
        camera_mode = "car"
        print("switched to car camera")
        if free_camera is not None:
            free_camera.enabled = False


# Basic driving mechanics
def update():
    # driving mechanics
    global velocity
    global deceleration
    if npc_car.position.z > 50: # reset npc position 
        npc_car.position.z = -50

    speed_text.text = f"Speed: {int(velocity)} km/h"
    if held_keys['w']:  # Move forward
        velocity = min(max_speed, velocity + acceleration * time.dt)
    elif velocity > 0:
        velocity = max(0, velocity - deceleration * time.dt)

    car.position += car.forward * velocity * time.dt

    if held_keys['s']:  # Move backward
        car.position -= car.forward * time.dt * 10
    if held_keys['a']:  # Turn left
        car.rotation_y -= 50 * time.dt
    if held_keys['d']:  # Turn right
        car.rotation_y += 50 * time.dt

    # update the camera modes
    if camera_mode == "car":
        # third person car camera
        camera.position = car.position + (0, 10, -20) # position the camera behind the car
        camera.rotation_c = 20
        camera.look_at(car.position) # make the camera look at the car
    elif camera_mode == "free":
       pass
   

def input(key):
    if key == "c":
        toggle_camera_mode()
    if key == "escape":
        quit()



app.run()
from ursina import *
from ursina import texture_importer

# Likely refers to a component or class used in game development to implement a first-person perspective and control scheme for the player.
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


# Add a sky box
EditorCamera()
sky = Sky(Texture='sky_sunset')


# Add lighting
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1)) # point the light in a specific direction 


# add ground
ground = Entity(
    model="plane", 
    scale=(10000, 1, 10000), 
    texture="_assets/terrain/grass/grass_texture.jpg")
ground.texture_scale=(1000, 1000) # stretch the texture to fit the ground


road = Entity(
    model="cube", 
    scale=(10, 0.1, 100), # scale the ground to be large 
    texture="_assets/roads/asphalt_02_1k/asphalt_02_diff_1k.jpg")
road.position=(0, 0.1, 0)
road.texture_scale = (10, 100)

off_road = Entity(
    model="cube", 
    scale=(10, 0.1, 50), 
    texture="_assets/roads/gravelly_sand_1k/gravelly_sand_diff_1k.jpg")
off_road.position=(15, 0.1, 0)
off_road.texture_scale = (10, 50)


# terrain = Entity(model=Terrain('heightmap'), scale=(100, 10, 100), texture = 'grass_texture')
# terrain.texture_scale = (100, 100)

# # add buildings 
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
    model='_assets/Car/Subaru-Loyale--OBJ/_Subaru-Loyale.obj', 
    scale=(1, 1, 1), 
    texture='car_texture', 
    position=(0, 1, 0))



# Replace the static camera with a FirstPersonController
# player = FirstPersonController()
# player.position = (0, 10, 0)  # Start the player above the ground
# player.gravity = 0  # Disable gravity so the player can fly
# camera.position = (0, 10, -60) # position the camera above the ground



# camera modes 
camera_mode = "car" # start with car camera

def toggle_camera_mode():
    global camera_mode
    if camera_mode == "car":
        camera_mode = "free"
        print("switched to free camera")
    else:
        camera_mode = "car"
        print("switched to car camera")


# Basic driving mechanics
def update():
    # driving mechanics

    if held_keys['w']:  # Move forward
        car.position += car.forward * time.dt * 10
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
        if not hasattr(app, "free_camera"):
            app.free_camera = FirstPersonController()
            app.free_camera.position = car.position + (0, 10, 0)
            app.free_camera.gravity = 0
            # app.free_camera.rotation_x = 0 # tilt the camera to look down at the scene 
            # app.free_camera.rotation_y = 0
    else:
        app.free_camera.enabled = True

def input(key):
    if key == "c":
        toggle_camera_mode()
    if key == "escape":
        quit()



app.run()
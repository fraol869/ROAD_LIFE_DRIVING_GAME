import os  
import sys 

from ursina import *
from ursina import texture_importer
from ursina.prefabs.first_person_controller import FirstPersonController

from dataclasses import dataclass, field
from random import choice, randint 
from typing import List, Dict, Tuple, Optional, Union, Any


from rl_log_utils import ScriptLogger
# from rl_enviroment import create_enviroment
# from rl_city import create_city


@dataclass
class GameData:
    """Configuration for the game"""
    logger = ScriptLogger("roadlife")
    # environment related constants 

    terrains = []
    roads = []

    num_terrains = 3
    grid_size: int = 5
    cell_size: int = 20
    road_width: int =  cell_size * 0.4
    
    # car related constants
    velocity: int = 0
    max_speed: int = 50
    acceleration: int = 5
    deceleration: int = 8

    building_models: list = None 
    terrain_texture: str = None
    road_texture: str = None
    sky_texture: str = None 
    free_camera: str = None 
    car_camera: str = None 
    camera_mode = "menu"

    # booleans 
    game_started = False 
    menu_buttons: List[Dict[str, Any]] = field(default_factory=lambda: [
        {"text": "Start Game", "color": color.orange},
        {"text": "Resume Game", "color": color.green},
        {"text": "Settings", "color": color.black90},
        {"text": "Quit", "color": color.red},
       
    ])

    # paths 
    script_dir: str = os.path.dirname(__file__) 
    asset_dir: str = os.path.join(script_dir, "_assets")

gd = GameData()
app = Ursina()


#-----------------------------------------------------------CORE METHODS ----------------------------------------------------------------
# create the enviroment 
def create_enviroment():
    """Create the terrain"""
    ground = Entity(
            model="plane",
            scale=(1000, 1, 1000),
            texture=("_assets/terrain/grass/grass_texture.jpg"),
            texture_scale=(100, 100))

    # create multiple terrains 
    # for i in range(gd.num_terrains):
    #     terrain = Entity(
    #         model=Terrain('heightmap_1', skip=8),
    #         scale=(gd.grid_size * gd.cell_size, 30, gd.grid_size * gd.cell_size),
    #         position=(
    #             i * gd.grid_size * gd.cell_size,  # offset terrains along the x-axis
    #             0, # slightly above the ground 
    #             0), # centered on the z axis
    #         texture=("_assets/terrain/grass/aerial_grass_rock_arm_1k.jpg"),
    #         texture_scale=(gd.grid_size, gd.grid_size),
    #         collider='mesh',
    #     )
    #     gd.terrains.append(terrain)
        # gd.logger.log("/ terrain created")

        # create roads on top of the terrains
    # road = Entity(
    #     model='cube',
    #     scale=(gd.grid_size * gd.road_width, 1, gd.road_width),
    #     textures="_assets/roads/asphalt_02_1k/asphalt_02_diff_1k.jpg",
    #     position=(0, 0.1, 0),
    #     texture_scale = (10, 100),
    #     colliders='box', )
    # gd.roads.append(road)



building_models = [
    ("_assets/homes/abandoned_house/scene.gltf"),
    ("_assets/homes/long_warehouse/scene.gltf"),
    ("_assets/homes/old_garage/scene.gltf"),
    ("_assets/homes/small_warehouse/scene.gltf"),
]


def create_city():   
    for i in range(10):
        distance_between_buildings = 20  
        road_lenght = 100   
        building_model = choice(building_models)
        building = Entity(
            model="_assets/homes/abandoned_house/scene.gltf",
            scale=(1, 1, 1),
            position=(-road_lenght/20, 0, i * distance_between_buildings),
            collider='box',
        )
    road = Entity(
        model='cube',
        scale=(10, 0.1, 1000),
        texture="_assets/roads/asphalt_02_1k/asphalt_02_diff_1k.jpg",
        texture_scale =(1,100),
        position=(20, 0, 0),
        colliders='box', )


#_--------------------------------------------------------GAME ENTRY METHODS--------------------------------------------------------

def RoadLifeGame():
    """Main game loop"""
    sky = Sky(Texture='sky_sunset')
    if sky:
        gd.logger.log("/ Sky loaded")

    sun = DirectionalLight()
    sun.look_at(Vec3(1, -1, -1))
    if sun:
        gd.logger.log("/ Sun Created succesfully")

    free_camera = FirstPersonController()
    free_camera.position = (0, 10, 0)
    free_camera.gravity = 0
    free_camera.speed = 20
    gd.logger.log("/ Game Started")






def input(key):
    if key == "c":
        toggle_camera_mode()
    if key == "escape":
        quit()

    if key == "m":
        mouse.locked = not mouse.locked
        print(mouse.velocity)

def main():
    RoadLifeGame()
    create_enviroment()
    create_city()
    Cursor()
    app.run()


if __name__ == "__main__":
    main()
import os  
import sys 

from ursina import *
from ursina import texture_importer
from ursina.prefabs.first_person_controller import FirstPersonController

from dataclasses import dataclass, field
from random import choice, randint 
from typing import List, Dict, Tuple, Optional, Union, Any
from log_utils import ScriptLogger


@dataclass
class GameData:
    """Configuration for the game"""
    logger = ScriptLogger("roadlife")
    # environment related constants 

    grid_size: int = 100
    cell_size: int = 20
    road_width: int = 4
    
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
    
class Enviroment:
    """ Handles terrain, roads, and building placement."""
    def __init__(self):
        self.gdata = GameData()
        self.ground_tiles = []

    def create_terrain(self):
        ground = Entity(
            model="plane",
            scale=(1000, 1, 1000),
            texture=("_assets/terrain/grass/grass_texture.jpg"),
            texture_scale=(1000, 1000)
        )
        
        self.gdata.logger.log("/ terrain created")
    
    def create_grid(self):
        self.gdata.logger.log("/ grid created")
    
    def place_building(self, x, z):
        Entity(
            model="cube", 
            position=(x, 1, z),
            scale=(1, 2, 1),
            color=color.red
        )
        self.gdata.logger.log("/ building placed at ({}, {})".format(x, z))
    

class RoadLifeGame:
    """ Main game class. """
    def __init__(self):
        self.app = Ursina()
        self.environment = Enviroment()    
        self.gdata = GameData()
        self.menu_panel = None

    def create_menu(self):
        self.menu_panel = Entity(
            parent=camera.ui,
            model='quad',
            scale=(0.8, 0.9),
            texture='white_cube',
            color=color.black66,
            position=(0,0))
        
        title = Text(
            "ROAD LIFE DRIVING GAME",
            parent=self.menu_panel,
            scale=2.5,
            y=0.4,
            x=-0.4,
            color=color.turquoise)
        
        for i, btn in enumerate(self.gdata.menu_buttons):
            Button(
                text=btn["text"],
                parent=self.menu_panel,
                y=0.2 - (i * 0.2),
                color=btn["color"],
                scale=(0.5, 0.1),
                on_click=self.start_game if i == 0 else self.quit_game
            )
        
        # start_button = Button(
        #     text="Start Game",
        #     parent=menu_panel,
        #     y=0.1,
        #     color=color.orange,
        #     scale=(0.5, 0.1), 
        #     on_click=self.start_game,)
        
        # quit_button = Button(
        #     text="Quit",
        #     parent=menu_panel,
        #     y=-0.3,
        #     color=color.red,
        #     scale=(0.5, 0.1),
        #     on_click=self.quit_game)

        # return menu_panel 

    def start_game(self):
        """ Starts the game."""
        self.gdata.game_started = True 
        if self.menu_panel:
            destroy(self.menu_panel)

        self.gdata.logger.log("/ Game started, welcome")
        self.setup_scene()

    
    def setup_scene(self):
        """ Sets up the game scene. """
        sky = Sky(Texture='sky_sunset')
        sun = DirectionalLight()
        sun.look_at(Vec3(1, -1, -1))
        self.environment.create_terrain()
        self.environment.create_grid()


    def _run_game(self):
        """ Runs the game. """
        window.fullscreen = True 
        window.borderless = False    
        self.create_menu()
        self.app.run()
    
    def quit_game(self):
        self.gdata.logger.log("/  Quitting game. Goodbye!")


gdata = GameData()


    

if __name__ == "__main__":
    try:
        def update():
            if not gdata.game_started:
                return
        road_life = RoadLifeGame()
        road_life._run_game()
    except KeyboardInterrupt:
        print("/ Game interrupted.")
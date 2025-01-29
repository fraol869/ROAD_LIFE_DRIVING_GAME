import os 
import sys 

from ursina import *
from ursina import texture_importer
from ursina.prefabs.first_person_controller import FirstPersonController

from random import choice, randint 
from pathlib import Path

app = Ursina()
sky = Sky(Texture='sky_sunset')
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1)) # point the light in a specific direction 

window.fullscreen = True
window.borderless = False 
game_started = False 


# menu UI 
def create_menu(): 
    menu_panel = Entity(
        parent=camera.ui,
        model='quad',
        scale=(0.8, 0.9),
        texture='white_cube',
        color=color.black66,
        position=(0,0)
    )
    title = Text(
        "ROAD LIFE DRIVING GAME", 
        parent=menu_panel, 
        scale=2.5,  
        y=0.4,
        x=-0.4, 
        color=color.turquoise)
   
    start_button = Button(
        text="start game",
        parent=menu_panel,
        y=0.1,
        color=color.orange,
        scale=(0.5, 0.1),
        on_click=start_game,
    )
    camera_mode_button = Button(
        text="switch camera mode",
        parent=menu_panel,
        y=-0.1,
        color=color.lime,
        scale=(0.5, 0.1),
        on_click=toggle_camera_mode
    )
    quit_button = Button(
        text="Quit",
        parent=menu_panel,
        y=-0.3,
        color=color.red,
        scale=(0.5, 0.1),
        on_click=quit_game
    )
    return menu_panel

# game setup
def start_game():
    global game_started, menu_panel
    game_started = True
    destroy(menu_panel)
    print("/ Game started")

def quit_game():
    print("/ Quitting game. Goodbye!")
    application.quit()


# toggle camera mode 
camera_mode = "menu"  # start with menu mode
free_camera = None
car_camera = None

def toggle_camera_mode():
    global camera_mode, free_camera
    if camera_mode == "car":
        camera_mode = "free"
        print("/ Switched to free camera")
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

# Display the menu 
menu_panel = create_menu()


# Basic driving mechanics
def update():
    if not game_started:
        return 
    pass 
   
app.run()

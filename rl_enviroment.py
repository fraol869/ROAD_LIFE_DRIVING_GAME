from ursina import *
from random import choice, randint 






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
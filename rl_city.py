from ursina import *
from random import choice, randint 


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

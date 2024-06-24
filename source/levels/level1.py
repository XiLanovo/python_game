# level1.py
from source.levels.level import BaseLevel


class Level1(BaseLevel):
    def __init__(self):
        super().__init__('source/assets/json/level1_wall_terrain.json', 'source/assets/json/level1_trap_terrain.json')

# level.py
from source.levels.trap_terrain import TrapTerrain
from source.levels.wall_terrain import WallTerrain


class BaseLevel:
    def __init__(self, wall_json_file, trap_json_file):
        self.wall_terrain = WallTerrain(wall_json_file)
        self.trap_terrain = TrapTerrain(trap_json_file)

    def draw(self, screen):
        self.trap_terrain.draw(screen)
        self.wall_terrain.draw(screen)

    def get_wall_tiles(self):
        return self.wall_terrain.tiles

    def get_trap_tiles(self):
        return self.trap_terrain.tiles


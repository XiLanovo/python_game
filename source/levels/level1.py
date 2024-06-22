# # Terrain.py
#
# import pygame
# import json
# from os.path import join, dirname
#
# class Terrain:
#     def __init__(self, layout_file, tile_image, tile_size):
#         self.tile_size = tile_size
#         self.tileset = pygame.image.load(join(dirname(__file__), tile_image))
#         self.tileset = pygame.transform.scale(self.tileset, (tile_size, tile_size))
#         self.load_layout(layout_file)
#         self.terrain_rects = []
#
#     def load_layout(self, layout_file):
#         with open(join(dirname(__file__), layout_file), 'r') as file:
#             self.layout = json.load(file)
#
#         # 根据布局创建碰撞矩形列表
#         for y, row in enumerate(self.layout):
#             for x, tile in enumerate(row):
#                 if tile:  # 假设地形布局中的1表示存在Tile
#                     self.terrain_rects.append(pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))
#
#     def draw(self, surface):
#         for rect in self.terrain_rects:
#             surface.blit(self.tileset, rect)
#
#     def check_collision(self, rect):
#         # 检测rect是否与地形中的任何矩形发生碰撞
#         for terrain_rect in self.terrain_rects:
#             if rect.colliderect(terrain_rect):
#                 return True
#         return False

# level1.py
from source.levels.Level import Level
import json
from source.levels.Terrain import Terrain


class Level1(Level):
    def __init__(self, screen):
        with open('source/assets/images/level1.json', 'r') as file:
            layout_data = json.load(file)['layout']
        tile_image_path = 'source/assets/images/Tile.png'
        terrain = Terrain(tile_image_path, 32, layout_data)
        super().__init__(screen, terrain)

    def handle_events(self, events):
        # Level1的事件处理逻辑
        pass

    def check_completion(self):
        # Level1的完成条件检查逻辑
        pass

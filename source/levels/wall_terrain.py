# wall_terrain.py
import pygame
import json
from pygame.sprite import Sprite, Group


class WallTerrain:
    def __init__(self, json_file):
        self.tiles = Group()
        self.tiles = self.load_wall_terrain(json_file)

    def load_wall_terrain(self, json_file):
        tiles = []
        with open(json_file, 'r') as file:
            data = json.load(file)
            layout = data['layout']

            for row in range(len(layout)):  # 使用布局的实际行数
                for col in range(len(layout[row])):  # 使用每行的实际列数
                    tile_type = layout[row][col]
                    if tile_type == 1:  # Tile
                        image_path = 'source/assets/images/tile.png'
                    # elif tile_type == 2:  # Spike
                    #     image_path = 'source/images/spike.png'
                    elif tile_type == 0:  # Empty space, skip
                        continue

                    tile_image = pygame.image.load(image_path).convert_alpha()
                    tile_rect = tile_image.get_rect(topleft=(col * 32, row * 32))
                    tile = Sprite()
                    tile.image = tile_image
                    tile.rect = tile_rect
                    tile.mask = pygame.mask.from_surface(tile_image)  # 创建遮罩
                    tiles.append(tile)
        return tiles

    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)

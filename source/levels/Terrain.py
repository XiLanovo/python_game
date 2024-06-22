# terrain.py
import pygame as pg
import json

class Terrain:
    def __init__(self, layout_file, tile_image_path, tile_size):
        self.tile_size = tile_size
        self.tile_image = pg.image.load(tile_image_path).convert_alpha()
        self.layout_data = self.load_layout(layout_file)
        self.terrain_rects = self.create_terrain_rects()

    def load_layout(self, layout_file):
        with open(layout_file, 'r') as file:
            layout_data = json.load(file)
        return layout_data['layout']

    def create_terrain_rects(self):
        rects = []
        for y, row in enumerate(self.layout_data):
            for x, tile in enumerate(row):
                if tile:  # 假设tile值为1表示存在地形
                    rect = pg.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                    rects.append(rect)
        return rects

    def draw(self, surface):
        for y, row in enumerate(self.layout_data):
            for x, tile in enumerate(row):
                if tile:  # 只绘制值为1的tile
                    surface.blit(self.tile_image, (x * self.tile_size, y * self.tile_size))
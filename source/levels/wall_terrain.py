# wall_terrain.py
import pygame
import json
from pygame.sprite import Sprite, Group


class WallTerrain:
    """
    墙壁地形类，用于加载和管理游戏中的墙壁地形。
    """

    def __init__(self, json_file):
        """
        初始化墙壁地形，从JSON文件中加载墙壁数据。

        :param json_file: 包含墙壁布局的JSON文件路径。
        """
        self.tiles = Group()  # 创建一个精灵组来存储墙壁瓦片
        self.tiles = self.load_wall_terrain(json_file)  # 加载墙壁地形

    def load_wall_terrain(self, json_file):
        """
        从JSON文件中加载墙壁地形。

        :param json_file: 包含墙壁布局的JSON文件路径。
        :return: 一个包含墙壁瓦片的Sprite列表。
        """
        tiles = []
        with open(json_file, 'r') as file:
            data = json.load(file)
            layout = data['layout']  # 获取布局数据

            # 遍历布局中的每个单元格
            for row in range(len(layout)):
                for col in range(len(layout[row])):
                    tile_type = layout[row][col]
                    if tile_type == 1:  # Tile类型，加载墙壁图像
                        image_path = 'source/assets/images/tile.png'
                    elif tile_type == 0:  # 空空间，跳过
                        continue

                    # 加载图像并创建墙壁瓦片
                    tile_image = pygame.image.load(image_path).convert_alpha()
                    tile_rect = tile_image.get_rect(topleft=(col * 32, row * 32))
                    tile = Sprite()
                    tile.image = tile_image
                    tile.rect = tile_rect
                    tile.mask = pygame.mask.from_surface(tile_image)  # 创建碰撞掩码
                    tiles.append(tile)
        return tiles

    def draw(self, screen):
        """
        将墙壁地形绘制到屏幕上。

        :param screen: Pygame的屏幕对象。
        """
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)  # 绘制每个墙壁瓦片
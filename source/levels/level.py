# level.py
from source.levels.trap_terrain import TrapTerrain
from source.levels.wall_terrain import WallTerrain


class BaseLevel:
    """
    基础关卡类，用于创建游戏中的关卡。
    """

    def __init__(self, wall_json_file, trap_json_file):
        """
        初始化关卡的墙壁和陷阱地形。

        :param wall_json_file: 墙壁地形的JSON配置文件路径。
        :param trap_json_file: 陷阱地形的JSON配置文件路径。
        """
        # 创建墙壁地形实例
        self.wall_terrain = WallTerrain(wall_json_file)
        # 创建陷阱地形实例
        self.trap_terrain = TrapTerrain(trap_json_file)

    def draw(self, screen):
        """
        绘制关卡中的陷阱和墙壁到屏幕上。

        :param screen: Pygame的屏幕对象。
        """
        # 绘制陷阱地形
        self.trap_terrain.draw(screen)
        # 绘制墙壁地形
        self.wall_terrain.draw(screen)

    def get_wall_tiles(self):
        """
        获取所有的墙壁瓦片。

        :return: 一个包含墙壁瓦片的列表。
        """
        # 返回墙壁地形中的瓦片列表
        return self.wall_terrain.tiles

    def get_trap_tiles(self):
        """
        获取所有的陷阱瓦片。

        :return: 一个包含陷阱瓦片的列表。
        """
        # 返回陷阱地形中的瓦片列表
        return self.trap_terrain.tiles
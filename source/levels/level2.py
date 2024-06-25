# level1.py
from source.levels.level import BaseLevel


class Level2(BaseLevel):
    """
    继承自BaseLevel的类，代表游戏的第二关。
    """

    def __init__(self):
        """
        初始化第二关的关卡，加载特定的墙壁和陷阱地形配置。

        在这个方法中，我们调用了基类(BaseLevel)的构造方法，传入了第二关的墙壁和陷阱地形的配置文件路径。
        """
        # 调用基类的构造方法，并传入第二关的墙壁和陷阱地形的JSON配置文件路径
        super().__init__(
            'source/assets/json/level2_wall_terrain.json',
            'source/assets/json/level2_trap_terrain.json'
        )
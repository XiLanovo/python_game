# init.py
import pygame as pg
import os
from source.sprites.player import Player
from source.levels.level1 import Level1
from source.levels.level2 import Level2

# 初始化Pygame
pg.init()

# 定义基础路径
BASE_IMAGE_PATH = os.path.join(os.getcwd(), 'source', 'assets', 'images')


# 定义图片路径函数
def get_image_path(image_name):
    return os.path.join(BASE_IMAGE_PATH, image_name)


# 设置窗口的尺寸
screen_width, screen_height = 800, 640
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('平台跳跃游戏')
clock = pg.time.Clock()
fps = 45
delta_time = clock.tick(24) / 1000.0  # 计算每秒流逝的时间

# 玩家初始位置
initial_player_position = (32, 608 - 32)

# 加载玩家图片
player_image_path = get_image_path('player_stand.png')
player_walk_image_path = get_image_path('player_walk.png')
player_jump_image_path = get_image_path('player_jump.png')

player = Player(*initial_player_position,
                player_image_path,
                player_walk_image_path,
                player_jump_image_path,
                screen_width,
                screen_height)  # 初始位置为第24行第2列

# 加载背景图片
background_path = get_image_path('background.png')
background_img = pg.image.load(background_path).convert()
background_img = pg.transform.scale(background_img, (screen_width, screen_height))


# 加载首页背景图片
start_menu_background_path = get_image_path('start_menu.png')
start_menu_background_img = pg.image.load(start_menu_background_path).convert().convert_alpha()
start_menu_background_img = pg.transform.scale(start_menu_background_img, (screen_width, screen_height))

# 加载结束背景图
passed_menu_background_path = get_image_path('passed_menu.png')
passed_menu_background_img = pg.image.load(passed_menu_background_path).convert().convert_alpha()
passed_menu_background_img = pg.transform.scale(passed_menu_background_img, (screen_width, screen_height))

# 加载游戏失败页面背景
died_menu_background_path = get_image_path('died_menu.png')
died_menu_background_img = pg.image.load(died_menu_background_path).convert().convert_alpha()
died_menu_background_img = pg.transform.scale(died_menu_background_img, (screen_width, screen_height))

# 加载按钮图片
start_button_path = get_image_path('start_button.png')
start_button_img = pg.image.load(start_button_path).convert_alpha()
end_button_path = get_image_path('quit_button.png')
end_button_img = pg.image.load(end_button_path).convert_alpha()
restart_button_path = get_image_path('restart_button.png')
restart_button_img = pg.image.load(restart_button_path).convert_alpha()
restart_game_button_path = get_image_path('restart_game_button.png')
restart_game_button_img = pg.image.load(restart_game_button_path).convert_alpha()
# 定义按钮位置

start_button_rect = start_button_img.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
end_button_rect = end_button_img.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
restart_button_rect = restart_button_img.get_rect(center=(screen_width // 2, screen_height//2+50))
restart_game_button_rect = restart_game_button_img.get_rect(center=(screen_width//2, screen_height//2-50))
# 初始化字体
# 死亡结算
fi = pg.font.Font('source/assets/fonts/Boxy-Bold.ttf', 50)
text = fi.render('You dead!', True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (400, 200)

# 通关结算
f2 = pg.font.Font('source/assets/fonts/Boxy-Bold.ttf', 50)
text2 = f2.render('Mission Accomplished!', True, (255, 255, 255))
text_rect2 = text2.get_rect()
text_rect2.center = (400, 100)

# 创建关卡实例
level1 = Level1()
level2 = Level2()
levels = [level1, level2]
current_level_index = 0
current_level = levels[current_level_index]

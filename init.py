# init.py
import pygame as pg
import os
from source.sprites.player import Player
from source.levels.level1 import Level1
from source.levels.level2 import Level2

# 初始化Pygame
pg.init()
pg.mixer.init()
# 设置基础路径
BASE_IMAGE_PATH = os.path.join(os.getcwd(), 'source', 'assets', 'images')
BASE_FONT_PATH = os.path.join(os.getcwd(), 'source', 'assets', 'fonts', 'Boxy-Bold.ttf')
BASE_SOUND_PATH = os.path.join(os.getcwd(), 'source', 'assets', 'sounds')


# 加载和缩放图片的函数
def load_and_scale_image(image_name, width, height):
    image_path = get_image_path(image_name)
    image = pg.image.load(image_path).convert()
    return pg.transform.scale(image, (width, height))


# 获取图片路径的函数
def get_image_path(image_name):
    return os.path.join(BASE_IMAGE_PATH, image_name)


# 加载图片的函数
def load_image(image_name):
    image_path = get_image_path(image_name)
    return pg.image.load(image_path).convert_alpha()


# 设置窗口尺寸
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

# 创建玩家对象
player = Player(*initial_player_position,
                player_image_path,
                player_walk_image_path,
                player_jump_image_path,
                screen_width,
                screen_height)

# 加载背景图片
background_img = load_and_scale_image('background.png', screen_width, screen_height)
start_menu_background_img = load_and_scale_image('start_menu.png', screen_width, screen_height)
passed_menu_background_img = load_and_scale_image('passed_menu.png', screen_width, screen_height)
died_menu_background_img = load_and_scale_image('died_menu.png', screen_width, screen_height)

# 加载按钮图片
start_button_img = load_image('start_button.png')
end_button_img = load_image('quit_button.png')
restart_button_img = load_image('restart_button.png')
restart_game_button_img = load_image('restart_game_button.png')

# 定义按钮位置
start_button_rect = start_button_img.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
end_button_rect = end_button_img.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
restart_button_rect = restart_button_img.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
restart_game_button_rect = restart_game_button_img.get_rect(center=(screen_width // 2, screen_height // 2 - 50))


# 渲染文本的函数
def render_text(text, size, color=(255, 255, 255)):
    font = pg.font.Font(BASE_FONT_PATH, size)
    return font.render(text, True, color)


# 渲染文本
text = render_text('You dead!', 50)
text_rect = text.get_rect(center=(400, 200))
text2 = render_text('Mission Accomplished!', 50)
text_rect2 = text2.get_rect(center=(400, 100))


def play_music(music_name, loops):
    # 构建音乐文件的完整路径
    music_path = os.path.join(BASE_SOUND_PATH, music_name)
    # 加载并播放音乐
    if pg.mixer.music.get_busy():  # 检查音乐是否已经在播放
        pg.mixer.music.stop()  # 如果是，停止当前音乐
    pg.mixer.music.load(music_path)  # 加载新的音乐文件
    pg.mixer.music.play(loops)  # 播放音乐，loops=-1 表示无限循环


# 创建关卡实例
levels = [Level1(), Level2()]
current_level_index = 0
current_level = levels[current_level_index]

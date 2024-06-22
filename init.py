# init.py
import pygame as pg
import os

# 初始化Pygame
pg.init()

# 设置窗口的尺寸
screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('平台跳跃游戏')

# 加载背景图片
background_path = os.path.join(os.getcwd(), 'source', 'assets', 'images', 'background.png')
background_img = pg.image.load(background_path).convert()
background_img = pg.transform.scale(background_img, (screen_width, screen_height))

# 加载首页背景图片
start_menu_background_path = os.path.join(os.getcwd(), 'source', 'assets', 'images', '1.png')
start_menu_background_img = pg.image.load(start_menu_background_path).convert().convert_alpha()
start_menu_background_img = pg.transform.scale(start_menu_background_img, (screen_width, screen_height))


# 加载按钮图片
start_button_path = os.path.join(os.getcwd(), 'source', 'assets', 'images', 'start_button.png')
start_button_img = pg.image.load(start_button_path).convert_alpha()
end_button_path = os.path.join(os.getcwd(), 'source', 'assets', 'images', 'quit_button.png')
end_button_img = pg.image.load(end_button_path).convert_alpha()

# 定义按钮位置
start_button_rect = start_button_img.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
end_button_rect = end_button_img.get_rect(center=(screen_width // 2, screen_height // 2 + 50))

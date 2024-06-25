#   Main.py
import source.states.start_menu as start_menu
import pygame as pg
import sys

if __name__ == '__main__':  # 程序主入口
    start_menu.start_menu()     # 加载到首页
    pg.quit()   # 退出游戏
    sys.exit()

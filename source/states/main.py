#   main.py
import pygame as pg
import init
from source.levels.level1 import Level1
# 假设其他关卡类（Level2, Level3, ...）也已导入


def main():
    # 创建关卡列表
    levels = [Level1(init.screen)]  # 所有关卡的实例
    current_level = levels[0]  # 从第一关开始
    running = True
    clock = init.pg.time.Clock()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                # 检测到鼠标点击事件，切换到下一关卡
                if current_level.handle_events(event):
                    current_level = levels[levels.index(current_level) + 1]
                    if current_level is None:
                        # 如果没有更多关卡，退出循环（游戏结束）
                        running = False

        init.screen.fill((0, 0, 0))  # 清屏
        current_level.draw()  # 绘制当前关卡
        init.screen.blit(init.background_img, (0, 0))   # 绘制背景图片
        pg.display.flip()  # 更新屏幕显示
        clock.tick(60)

    pg.quit()

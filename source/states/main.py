# main.py
import pygame as pg
import init
from source.states.passed_menu import passed_menu


def main():
    running = True
    while running:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                passed_menu()

        # 填充屏幕背景色
        init.screen.fill((0, 0, 0))
        # 绘制背景图片
        init.screen.blit(init.background_img, (0, 0))
        # 绘制关卡
        init.level.draw(init.screen)

        # 移动玩家
        init.player.move(keys, init.delta_time, init.level.get_wall_tiles())
        # 绘制玩家
        init.player.draw(init.screen)

        # 更新屏幕显示
        pg.display.flip()
        # 控制游戏帧率
        init.clock.tick(init.fps)

    pg.quit()

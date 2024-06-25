# main.py
import pygame as pg
import init
from source.states.passed_menu import passed_menu


def main():
    init.play_music('gaming.mp3', -1)
    running = True
    while running:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # 填充屏幕背景色
        init.screen.fill((0, 0, 0))
        # 绘制背景图片
        init.screen.blit(init.background_img, (0, 0))
        # 绘制关卡
        init.current_level.draw(init.screen)

        # 移动玩家
        init.player.move(keys,
                         init.delta_time,
                         init.current_level.get_wall_tiles(),
                         init.current_level.get_trap_tiles())
        # 绘制玩家
        init.player.draw(init.screen)

        # 检查是否需要切换关卡
        if init.player.rect.right >= init.screen_width:
            init.current_level_index += 1
            if init.current_level_index < len(init.levels):
                init.current_level = init.levels[init.current_level_index]
                init.player.reset_position()
            else:
                init.current_level_index = 0  # 重置关卡索引
                passed_menu()

        # 更新屏幕显示
        pg.display.flip()
        # 控制游戏帧率
        init.clock.tick(init.fps)

    pg.quit()

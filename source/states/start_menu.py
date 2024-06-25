# start_menu.py
import pygame as pg
import init
import source.states.main
import source.states.died_menu


def start_menu():
    """
    游戏开始菜单，显示游戏开始和退出选项。
    """
    pg.mixer.music.load("source/music/begin.mp3")
    pg.mixer.music.play()
    running = True
    while running:
        # 绘制开始菜单背景
        init.screen.blit(init.start_menu_background_img, (0, 0))

        # 处理事件
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # 如果点击关闭窗口，则退出循环，结束游戏
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                # 如果鼠标点击，检查是否点击了开始游戏按钮的区域
                if init.start_button_rect.collidepoint(pg.mouse.get_pos()):
                    pg.mixer.music.stop()
                    pg.mixer.music.unload()
                    # 重置玩家位置和状态
                    init.player.reset_position()
                    # 进入游戏主循环
                    source.states.main.main()
                # 检查是否点击了退出按钮的区域
                elif init.end_button_rect.collidepoint(pg.mouse.get_pos()):
                    # 如果点击退出，则退出循环，结束游戏
                    running = False

        # 将开始游戏按钮和退出按钮绘制到屏幕上
        init.screen.blit(init.start_button_img, init.start_button_rect)
        init.screen.blit(init.end_button_img, init.end_button_rect)
        # 更新屏幕显示
        pg.display.flip()

    # 如果玩家选择退出，关闭游戏
    pg.quit()
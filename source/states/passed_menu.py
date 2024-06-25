# passed_menu.py
import pygame as pg
import init
import source.states.start_menu


def passed_menu():
    """
    游戏通过菜单，显示游戏通过的信息，并提供重新开始游戏或退出的选项。
    """
    pg.mixer.music.load('source/music/end.mp3')
    pg.mixer.music.play()
    running = True
    while running:
        # 绘制游戏通过菜单背景和文本
        init.screen.blit(init.passed_menu_background_img, (0, 0))
        init.screen.blit(init.text2, init.text_rect2)

        # 处理事件
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # 如果点击关闭窗口，则退出循环，结束游戏
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                # 如果鼠标点击，检查是否点击了重新开始游戏按钮的区域
                if init.restart_game_button_rect.collidepoint(pg.mouse.get_pos()):
                    # 重置关卡索引和当前关卡
                    init.current_level_index = 0
                    init.current_level = init.levels[init.current_level_index]
                    # 重置玩家位置和状态
                    init.player.reset_position()
                    # 重新进入游戏开始菜单
                    source.states.start_menu.start_menu()
                # 检查是否点击了退出按钮的区域
                elif init.end_button_rect.collidepoint(pg.mouse.get_pos()):
                    # 如果点击退出，则退出循环，结束游戏
                    running = False

        # 将重新开始游戏按钮和退出按钮绘制到屏幕上
        init.screen.blit(init.restart_game_button_img, init.restart_game_button_rect)
        init.screen.blit(init.end_button_img, init.end_button_rect)
        # 更新屏幕显示
        pg.display.flip()

    # 如果玩家选择退出，关闭游戏
    pg.quit()

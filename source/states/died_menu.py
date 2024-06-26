# died_menu.py
import pygame as pg
import init
import source.states.main


def died_menu():
    """
    玩家死亡菜单，显示死亡信息并提供重新开始游戏的选项。
    """
    # 在进入死亡菜单时播放音乐
    init.play_music('died.mp3', 0)
    running = True
    while running:
        # 绘制死亡菜单背景和文本
        init.screen.blit(init.died_menu_background_img, (0, 0))
        init.screen.blit(init.text, init.text_rect)

        # 处理事件
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # 如果点击关闭窗口，则退出循环，结束游戏
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                # 如果鼠标点击，检查是否点击了重新开始按钮的区域
                if init.restart_button_rect.collidepoint(pg.mouse.get_pos()):
                    # 重置玩家位置和状态
                    init.player.reset_position()
                    # 重新进入游戏主循环
                    source.states.main.main()

        # 将重新开始按钮绘制到屏幕上
        init.screen.blit(init.restart_button_img, init.restart_button_rect)
        # 更新屏幕显示
        pg.display.flip()

    # 如果玩家选择退出，关闭游戏
    pg.quit()

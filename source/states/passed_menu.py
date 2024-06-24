import pygame as pg
import init
import source.states.start_menu


def passed_menu():
    running = True
    while running:
        init.screen.blit(init.passed_menu_background_img, (0, 0))
        init.screen.blit(init.text2, init.text_rect2)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if init.restart_game_button_rect.collidepoint(pg.mouse.get_pos()):
                    source.states.start_menu.start_menu()
                elif init.end_button_rect.collidepoint(pg.mouse.get_pos()):
                    running = False

        init.screen.blit(init.restart_game_button_img, init.restart_game_button_rect)
        init.screen.blit(init.end_button_img, init.end_button_rect)
        pg.display.flip()

    pg.quit()

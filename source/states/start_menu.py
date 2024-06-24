# start_menu.py
import pygame as pg
import init
import source.states.main
import source.states.died_menu


def start_menu():
    running = True
    while running:
        init.screen.blit(init.start_menu_background_img, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if init.start_button_rect.collidepoint(pg.mouse.get_pos()):
                    source.states.main.main()
                elif init.end_button_rect.collidepoint(pg.mouse.get_pos()):
                    source.states.died_menu.died_menu()

        init.screen.blit(init.start_button_img, init.start_button_rect)
        init.screen.blit(init.end_button_img, init.end_button_rect)
        pg.display.flip()

    pg.quit()

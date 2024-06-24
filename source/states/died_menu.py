import pygame as pg
import init
import source.states.main


def died_menu():
    running = True
    while running:
        init.screen.blit(init.died_menu_background_img, (0, 0))
        init.screen.blit(init.text, init.text_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if init.restart_button_rect.collidepoint(pg.mouse.get_pos()):
                    source.states.main.main()

        init.screen.blit(init.restart_button_img, init.restart_button_rect)
        pg.display.flip()

    pg.quit()

# level.py
import pygame as pg
from source.levels.Terrain import Terrain


class Level:
    def __init__(self, screen, terrain):
        self.screen = screen
        self.terrain = terrain

    def handle_events(self, events):
        raise NotImplementedError

    def draw(self):
        self.terrain.draw(self.screen)

    def check_completion(self):
        raise NotImplementedError

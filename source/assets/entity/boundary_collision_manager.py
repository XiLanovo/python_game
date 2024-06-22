# boundary_collision_manager.py

from source.assets.entity.abstract_collision_manager import AbstractCollisionManager


class BoundaryCollisionManager(AbstractCollisionManager):
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def collide(self, player):
        player.rect.x = max(0, min(player.rect.x, self.screen_width - player.rect.width))
        player.rect.y = max(0, min(player.rect.y, self.screen_height - player.rect.height))

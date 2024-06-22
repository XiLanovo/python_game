# trap_collision_manager.py
from abc import ABC

from abstract_collision_manager import AbstractCollisionManager


class TrapCollisionManager(AbstractCollisionManager, ABC):
    def __init__(self, traps, player_start_pos):
        self.traps = traps  # 陷阱列表
        self.player_start_pos = player_start_pos

    def check_collision(self, player):
        for trap in self.traps:
            if player.rect.colliderect(trap.rect.topleft):
                self.handle_collision(player)

    def handle_collision(self, player):
        # 碰撞处理逻辑：将玩家位置重置到初始位置
        player.rect.topleft = self.player_start_pos
        print("Player hit a trap and was reset to start position.")

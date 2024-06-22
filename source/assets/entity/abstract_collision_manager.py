# abstract_collision_manager.py

from abc import ABC, abstractmethod


class AbstractCollisionManager(ABC):
    @abstractmethod
    def collide(self, player):
        pass

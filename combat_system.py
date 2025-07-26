import pygame
import random

class CombatSystem:
    def __init__(self, f1, f2, ui):
        self.f1 = f1
        self.f2 = f2
        self.ui = ui
        self.round = 1
        self.is_game_over = False

    def update(self):
        if self.is_game_over:
            return

        if self.f1.is_attacking and self.f1.hit_cooldown <= 0:
            if self.f1.get_rect().colliderect(self.f2.get_rect()):
                damage = random.randint(10, 25)
                defeated = self.f2.take_damage(damage)
                if defeated:
                    self.ui.set_winner(self.f1.name)
                    self.is_game_over = True

        if self.f2.is_attacking and self.f2.hit_cooldown <= 0:
            if self.f2.get_rect().colliderect(self.f1.get_rect()):
                damage = random.randint(10, 25)
                defeated = self.f1.take_damage(damage)
                if defeated:
                    self.ui.set_winner(self.f2.name)
                    self.is_game_over = True

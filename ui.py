import pygame

class UI:
    def __init__(self, screen):
        self.font = pygame.font.SysFont('Courier New', 24)
        self.winner_text = None
        self.screen = screen

    def draw(self, f1, f2, round_number, state):
        # Health bars
        pygame.draw.rect(self.screen, (100, 100, 100), (50, 30, 300, 20))
        pygame.draw.rect(self.screen, (0, 255, 0), (50, 30, 3 * f1.health, 20))

        pygame.draw.rect(self.screen, (100, 100, 100), (self.screen.get_width() - 350, 30, 300, 20))
        pygame.draw.rect(self.screen, (0, 255, 0), (self.screen.get_width() - 350, 30, 3 * f2.health, 20))

        # Round
        text = self.font.render(f"ROUND {round_number}", True, (255, 255, 0))
        self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, 60))

        if state == 'gameover' and self.winner_text:
            gameover = self.font.render(self.winner_text, True, (255, 255, 0))
            restart = self.font.render("Press R to restart", True, (255, 255, 255))
            self.screen.blit(gameover, (self.screen.get_width() // 2 - gameover.get_width() // 2, 200))
            self.screen.blit(restart, (self.screen.get_width() // 2 - restart.get_width() // 2, 240))

    def set_winner(self, name):
        self.winner_text = f"{name} WINS!"

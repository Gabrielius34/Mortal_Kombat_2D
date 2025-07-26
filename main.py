import pygame
from arena import Arena
from fighter import Fighter
from combat_system import CombatSystem
from ui import UI

WIDTH, HEIGHT = 1280, 720

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Mortal Kombat Arena (Python)")
        self.clock = pygame.time.Clock()
        self.running = True

        self.ui = UI(self.screen)
        self.arena = Arena(self.screen)
        self.fighter1 = Fighter("PLAYER 1", 100, (100, HEIGHT - 200), pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_q, pygame.K_e)
        self.fighter2 = Fighter("PLAYER 2", 100, (WIDTH - 200, HEIGHT - 200), pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_o, pygame.K_p)
        self.combat = CombatSystem(self.fighter1, self.fighter2, self.ui)
        self.state = 'playing'

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000  # delta time in seconds
            self.handle_events()
            if self.state == 'playing':
                self.update(dt)
                self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.state == 'gameover' and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.__init__()

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.fighter1.update(dt, keys)
        self.fighter2.update(dt, keys)
        self.combat.update()

        if self.combat.is_game_over:
            self.state = 'gameover'

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.arena.draw()
        self.fighter1.draw(self.screen)
        self.fighter2.draw(self.screen)
        self.ui.draw(self.fighter1, self.fighter2, self.combat.round, self.state)
        pygame.display.flip()


if __name__ == "__main__":
    Game().run()
    pygame.quit()

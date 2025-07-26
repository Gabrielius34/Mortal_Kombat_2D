import pygame

class Fighter:
    def __init__(self, name, health, position, left, right, up, down, punch, block):
        self.name = name
        self.health = health
        self.max_health = health
        self.pos = list(position)
        self.speed = 200
        self.controls = {
            'left': left, 'right': right, 'up': up, 'down': down,
            'punch': punch, 'block': block
        }
        self.width, self.height = 60, 120
        self.is_blocking = False
        self.is_attacking = False
        self.hit_cooldown = 0

    def update(self, dt, keys):
        if self.hit_cooldown > 0:
            self.hit_cooldown -= dt

        dx = dy = 0
        if keys[self.controls['left']]:
            dx -= self.speed * dt
        if keys[self.controls['right']]:
            dx += self.speed * dt
        if keys[self.controls['up']]:
            dy -= self.speed * dt
        if keys[self.controls['down']]:
            dy += self.speed * dt

        self.pos[0] += dx
        self.pos[1] += dy

        self.is_attacking = keys[self.controls['punch']]
        self.is_blocking = keys[self.controls['block']]

    def draw(self, screen):
        color = (255, 0, 0) if self.is_attacking else (0, 0, 255)
        if self.is_blocking:
            color = (0, 255, 255)
        pygame.draw.rect(screen, color, (*self.pos, self.width, self.height))

    def take_damage(self, amount):
        if self.is_blocking:
            amount *= 0.3
        self.health -= amount
        self.health = max(0, self.health)
        self.hit_cooldown = 0.5
        return self.health <= 0

    def get_rect(self):
        return pygame.Rect(*self.pos, self.width, self.height)

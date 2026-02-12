import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT - 70))
        self.vel_y = 0
        self.jump_power = 10
        self.score = 0

    def update(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        self.handle_controls()
        if self.rect.y >= SCREEN_HEIGHT - 50:
            self.rect.y = SCREEN_HEIGHT - 50
            self.vel_y = 0

    def handle_controls(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_SPACE] and self.vel_y == 0:
            self.vel_y = -self.jump_power

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(random.randint(800, 1200), SCREEN_HEIGHT - 70))

    def update(self):
        self.rect.x -= 4
        if self.rect.x < -50:
            self.rect.x = random.randint(800, 1200)

# Initialize the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mario Bros Game')

# Group for sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Create enemies
enemies = pygame.sprite.Group()
for i in range(5):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions
    if pygame.sprite.spritecollideany(player, enemies):
        print('Game Over!')
        running = False

    # Draw
    screen.fill((135, 206, 235))  # Sky blue
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
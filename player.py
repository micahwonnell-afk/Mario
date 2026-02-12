class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_jumping = False
        self.gravity = 1

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            # Set initial jump velocity
            self.jump_velocity = -10

    def update(self):
        if self.is_jumping:
            self.y += self.jump_velocity
            self.jump_velocity += self.gravity  # Apply gravity
            if self.y >= 0:  # Assume ground level is y = 0
                self.y = 0
                self.is_jumping = False

    def collides_with(self, other):
        # Simple AABB collision detection
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y)

    def draw(self, screen):
        # Assuming sprite is loaded elsewhere
        screen.blit(player_sprite, (self.x, self.y))

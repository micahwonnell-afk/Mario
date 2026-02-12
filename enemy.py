class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f'{self.name} took {damage} damage! Remaining health: {self.health}')

class Goomba(Enemy):
    def __init__(self):
        super().__init__('Goomba', health=1)

class KoopaTroopa(Enemy):
    def __init__(self):
        super().__init__('Koopa Troopa', health=3)
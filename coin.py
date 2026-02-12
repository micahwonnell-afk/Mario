class Coin:
    def __init__(self, value):
        self.value = value
        self.collected = False

    def collect(self):
        if not self.collected:
            self.collected = True
            return self.value
        return 0

    def reset(self):
        self.collected = False

    def __str__(self):
        return f"Coin(value={self.value}, collected={self.collected})"
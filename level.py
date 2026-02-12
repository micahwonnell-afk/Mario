class Level:
    def __init__(self):
        self.platforms = []
        self.obstacles = []
        self.coins = []
        self.design = ""

    def add_platform(self, platform):
        self.platforms.append(platform)

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def add_coin(self, coin):
        self.coins.append(coin)

    def set_design(self, design):
        self.design = design

    def __str__(self):
        return f"Level Design: {self.design} \n Platforms: {self.platforms} \n Obstacles: {self.obstacles} \n Coins: {self.coins}"
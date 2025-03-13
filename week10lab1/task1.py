class Player:
    def __init__(self, name, age):
        self.name=name
        self.age=age


    def play(self):
        print(f"{self.name} plays the game.")

class FootballPlayer(Player):
    def __init__(self, name, age):
        super().__init__(name, age)

    def play(self):
        print(f"{self.name} kicks the ball.")

class BasketballPlayer(Player):
    def __init__(self, name, age):
        super().__init__(name, age)

    def play(self):
        print(f"{self.name} shoots the ball.")

def perform_play(player):
    player.play()

football_player = FootballPlayer("A", 25)
basketball_player = BasketballPlayer("B", 28)

perform_play(football_player)
perform_play(basketball_player)

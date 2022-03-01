
class Team:

    def __init__(self, name, players, coach):
        self.points = 0
        self.name = name
        self.players = players
        self.coach = coach
        
    
    def add_player(self, name):
        self.players.append(name)
    
    def has_player(self, name):
        for player in self.players:
            if player == name:
                return True 
        return False       

    def play_game(self, result):
        if result == True:
            self.points += 3
    


        
# Task A
    # I've created a class called Team, then added a method with the __init__ method and added name and coach to it - hint: could be bananas.
    # then added those three properties, but did not add players to the init method, because I am creating an empty list of players from the start.
    # Created then new method to add new player, which is then with its name added via append. to the empty list of players





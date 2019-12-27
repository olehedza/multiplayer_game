class Game:
    def __init__(self, id):
        self.player_1_went = False
        self.player_2_went = False
        self.ready = False
        self.session_id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, p):
        """

        :param p: [0, 1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.player_1_went = True
        else:
            self.player_2_went = True

    def connected(self):
        return self.ready

    def both_went(self):
        return self.player_1_went and self.player_2_went

    def winner(self):
        player1 = self.moves[0].upper()[0]
        player2 = self.moves[1].upper()[0]

        winner = -1
        if player1 == "R" and player2 == "S":
            winner = 0
        elif player1 == "S" and player2 == "R":
            winner = 1
        elif player1 == "P" and player2 == "R":
            winner = 0
        elif player1 == "R" and player2 == "P":
            winner = 1
        elif player1 == "S" and player2 == "P":
            winner = 0
        elif player1 == "P" and player2 == "S":
            winner = 1

        return winner

    def reset_went(self):
        self.player_1_went = False
        self.player_2_went = False

class Game():
    def __init__(
            self, turn = "X", tie = False, winner = None, board = 
                {
                    'a1': None, 'b1': None, 'c1': None,
                    'a2': None, 'b2': None, 'c2': None,
                    'a3': None, 'b3': None, 'c3': None,
                }
            ):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = board
    def play_game(self):
        print("Welcome to tic-tac-toe, let's play it")
        while not self.winner or self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
        
        if self.winner:
            print(f"the winner is {self.turn}")
        else:
            print(f"We got a is tie, start over")


    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game")
        else:
            print(f"It' player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()
    
    def get_move(self):
        while(True):
            move = input(f"Enter a valid move (Example: A1): ").lower()
            if move in self.board.keys() and self.board[move] == None:
                self.board[move] = self.turn
                break
            else:
                print("invalid input, please try it again")
    
    def check_for_winner(self):
        if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']):
            self.winner = True
            self.render()
        if self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']):
            self.winner = True
            self.render()
        if self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']):
            self.winner = True
            self.render()
        if self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']):
            self.winner = True
            self.render()
        if self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']):
            self.winner = True
            self.render()
        if self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']):
            self.winner = True
            self.render()
        if self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']):
            self.winner = True
            self.render()
        if self.board['c1'] and (self.board['c1'] == self.board['b2'] == self.board['a3']):
            self.winner = True
            self.render()
        
            
    
    def check_for_tie(self):
        if not self.winner:
            if not None in self.board.values():
                self.tie = True

    def switch_turn(self):
        if not self.winner:
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"




game_instance = Game()
game_instance.play_game()

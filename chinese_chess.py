from chess_board import ChessBoard
from player import Player
from side import Side


class ChineseChess:

    def __init__(self):
        self.chess_board = None
        self.red_player = Player(Side.RED)
        self.black_player = Player(Side.BLACK)
        self.current_player = self.red_player
        self.game_over = False
        self.winner = None

    def start(self):
        print('Game Start')
        print('init a new game')
        self.winner = None
        self.game_over = False
        self.current_player = self.red_player
        self.chess_board = ChessBoard()
        self.chess_board.init_game()
        print('end of init')

    def move_chess(self, from_point, to_point):
        if not self.can_be_select(from_point):
            return False
        if not self.chess_board.move_chess(from_point, to_point):
            return False
        return True

    def check_winner(self):
        side_getting_check = Side.RED
        if self.current_player.side == Side.RED:
            side_getting_check = Side.BLACK

        if not self.chess_board.is_game_over(side_getting_check):
            return
        self.game_over = True
        self.winner = self.current_player

    def can_be_select(self, point):
        selected_piece = self.chess_board.find_chess(point)
        if selected_piece is None:
            return False
        if selected_piece.side != self.current_player.side:
            return False
        return True

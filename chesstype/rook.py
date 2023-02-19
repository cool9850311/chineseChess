from chess import Chess


class Rook(Chess):

    def validate_movement(self, to_point: tuple, ChessBoard):
        from_point = self.point
        if to_point == from_point:
            return False
        if not self.is_in_board(to_point):
            return False
        if self.has_chess(to_point, ChessBoard) and not self.is_opponant(
                to_point, ChessBoard):
            return False
        chess_count = self.count_chess_in_line(self.point, to_point,
                                               ChessBoard)
        if chess_count != 1 and (chess_count != 2
                                 or not self.has_chess(to_point, ChessBoard)):
            return False
        return True

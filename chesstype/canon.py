from chess import Chess


class Canon(Chess):

    def validate_movement(self, to_point: tuple, ChessBoard):
        if to_point == self.point:
            return False
        if not self.is_in_board(to_point):
            return False
        chess_count = self.count_chess_in_line(self.point, to_point,
                                               ChessBoard)

        if self.has_chess(to_point, ChessBoard) and not self.is_opponant(
                to_point, ChessBoard):
            return False
        if (chess_count != 3 or
                not self.has_chess(to_point, ChessBoard)) and chess_count != 1:
            return False
        return True

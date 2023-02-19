from chess import Chess
from side import Side


class Advisor(Chess):

    def validate_movement(self, to_point: tuple, ChessBoard):
        from_point = self.point
        if to_point == from_point:
            return False
        if not self.is_in_side_board(to_point, self.side):
            return False
        if abs(from_point[0] - to_point[0]) != 1 or abs(from_point[1] -
                                                        to_point[1]) != 1:
            return False
        if self.has_chess(to_point, ChessBoard) and not self.is_opponant(
                to_point, ChessBoard):
            return False
        return True

    def is_in_side_board(self, to_point, side):
        if to_point[0] > 8 or to_point[0] < 0:
            return False
        if side == Side.RED:
            if to_point[1] > 2 or to_point[1] < 0 or to_point[
                    0] < 3 or to_point[0] > 5:
                return False
        if side == Side.BLACK:
            if to_point[1] > 9 or to_point[1] < 7 or to_point[
                    0] < 3 or to_point[0] > 5:
                return False
        return True

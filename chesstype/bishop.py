from chess import Chess
from side import Side


class Bishop(Chess):

    def validate_movement(self, to_point: tuple, ChessBoard):
        from_point = self.point
        if to_point == from_point:
            return False
        if not self.is_in_side_board(to_point, self.side):
            return False
        if abs(from_point[0] - to_point[0]) != 2 or abs(from_point[1] -
                                                        to_point[1]) != 2:
            return False
        elephant_eye_point = (((from_point[0] + to_point[0]) / 2),
                              ((from_point[1] + to_point[1]) / 2))
        if self.has_chess(elephant_eye_point, ChessBoard):
            return False
        if self.has_chess(to_point, ChessBoard) and not self.is_opponant(
                to_point, ChessBoard):
            return False
        return True

    def is_in_side_board(self, to_point, side):
        if to_point[0] > 8 or to_point[0] < 0:
            return False
        if side == Side.RED and (to_point[1] > 4 or to_point[1] < 0):
            return False
        if side == Side.BLACK and (to_point[1] > 9 or to_point[1] < 5):
            return False
        return True

from chess import Chess
from side import Side


class Pawn(Chess):

    def validate_movement(self, to_point: tuple, ChessBoard):
        from_point = self.point
        if to_point == from_point:
            return False
        if not self.is_in_board(to_point):
            return False
        if abs(from_point[0] - to_point[0]) + abs(from_point[1] -
                                                  to_point[1]) != 1:
            return False
        if self.side == Side.RED:
            if from_point[1] - to_point[1] == 1:  # 後退
                return False
            # 過河左右走
            if (from_point[1] == 3 or from_point[1]
                    == 4) and abs(from_point[0] - to_point[0]) != 0:
                return False
        else:
            if from_point[1] - to_point[1] == -1:  # 後退
                return False
            # 過河左右走
            if (from_point[1] == 5 or from_point[1]
                    == 6) and abs(from_point[0] - to_point[0]) != 0:
                return False
        if self.has_chess(to_point, ChessBoard) and not self.is_opponant(
                to_point, ChessBoard):
            return False
        return True

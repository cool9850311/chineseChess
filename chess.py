from abc import ABCMeta, abstractmethod

from side import Side


class Chess(metaclass=ABCMeta):

    def __init__(self, point: tuple, side: Side):
        self._point = point
        self._side = side

    def is_opponant(self, point, ChessBoard):
        current_point_side = self.side
        for chess in ChessBoard.chess_list:
            if chess.point == point and chess.side != current_point_side:
                return True
        return False

    def has_chess(self, point, ChessBoard):
        for chess in ChessBoard.chess_list:
            if chess.point == point:
                return True
        return False

    def count_chess_in_line(self, from_point, to_point, ChessBoard):
        min_x, max_x = min(to_point[0],
                           from_point[0]), max(to_point[0], from_point[0])
        min_y, max_y = min(to_point[1],
                           from_point[1]), max(to_point[1], from_point[1])

        if max_x - min_x != 0 and max_y - min_y != 0:
            return None
        i_range = range(min_x, max_x + 1)
        j_range = range(min_y, max_y + 1)

        middle_chess_count = 0
        for i in i_range:
            for j in j_range:
                if self.has_chess((i, j), ChessBoard):
                    middle_chess_count += 1
        return middle_chess_count

    def is_in_board(self, to_point):
        if to_point[0] > 8 or to_point[0] < 0:
            return False
        if to_point[1] > 9 or to_point[1] < 0:
            return False
        return True

    def validate_king_is_check(self):
        pass

    @abstractmethod
    def validate_movement(self, to_point: tuple, ChessBoard):
        pass

    @property
    def side(self):
        return self._side

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, point):
        self._point = point

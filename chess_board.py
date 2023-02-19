from chesstype.advisor import Advisor
from chesstype.bishop import Bishop
from chesstype.canon import Canon
from chesstype.king import King
from chesstype.knight import Knight
from chesstype.pawn import Pawn
from chesstype.rook import Rook
from side import Side
import copy


class ChessBoard:

    def __init__(self):
        self._chess_list = []

    def init_game(self):
        # Red side
        self._chess_list.append(King((4, 0), Side.RED))
        self._chess_list.append(Advisor((3, 0), Side.RED))
        self._chess_list.append(Advisor((5, 0), Side.RED))
        self._chess_list.append(Bishop((2, 0), Side.RED))
        self._chess_list.append(Bishop((6, 0), Side.RED))
        self._chess_list.append(Knight((1, 0), Side.RED))
        self._chess_list.append(Knight((7, 0), Side.RED))
        self._chess_list.append(Rook((0, 0), Side.RED))
        self._chess_list.append(Rook((8, 0), Side.RED))
        self._chess_list.append(Canon((1, 2), Side.RED))
        self._chess_list.append(Canon((7, 2), Side.RED))
        self._chess_list.append(Pawn((0, 3), Side.RED))
        self._chess_list.append(Pawn((2, 3), Side.RED))
        self._chess_list.append(Pawn((4, 3), Side.RED))
        self._chess_list.append(Pawn((6, 3), Side.RED))
        self._chess_list.append(Pawn((8, 3), Side.RED))
        # Black side
        self._chess_list.append(King((4, 9), Side.BLACK))
        self._chess_list.append(Advisor((3, 9), Side.BLACK))
        self._chess_list.append(Advisor((5, 9), Side.BLACK))
        self._chess_list.append(Bishop((2, 9), Side.BLACK))
        self._chess_list.append(Bishop((6, 9), Side.BLACK))
        self._chess_list.append(Knight((1, 9), Side.BLACK))
        self._chess_list.append(Knight((7, 9), Side.BLACK))
        self._chess_list.append(Rook((0, 9), Side.BLACK))
        self._chess_list.append(Rook((8, 9), Side.BLACK))
        self._chess_list.append(Canon((1, 7), Side.BLACK))
        self._chess_list.append(Canon((7, 7), Side.BLACK))
        self._chess_list.append(Pawn((0, 6), Side.BLACK))
        self._chess_list.append(Pawn((2, 6), Side.BLACK))
        self._chess_list.append(Pawn((4, 6), Side.BLACK))
        self._chess_list.append(Pawn((6, 6), Side.BLACK))
        self._chess_list.append(Pawn((8, 6), Side.BLACK))

    @property
    def chess_list(self):
        return self._chess_list

    @chess_list.setter
    def chess_list(self, chess_list):
        self._chess_list = chess_list

    def move_chess(self, from_point, to_point):
        chess_to_move = self.find_chess(from_point)
        if chess_to_move is None:
            return False
        if not chess_to_move.validate_movement(to_point, self):
            return False
        chess_list_temp = copy.deepcopy(self.chess_list)
        # actual move
        chess_to_remove = self.find_chess(to_point)
        if chess_to_remove:
            self.remove_chess(to_point)
        chess_to_move.point = to_point

        if self.is_getting_check(chess_to_move.side):
            self.chess_list = chess_list_temp
            return False
        return True

    def is_getting_check(self, side):
        # 王對王
        red_king = self.find_king(Side.RED)
        black_king = self.find_king(Side.BLACK)
        if red_king.point[0] == black_king.point[0]:
            if red_king.count_chess_in_line(red_king.point, black_king.point,
                                            self) == 2:
                return True
        # 王以外
        king_to_check = red_king
        if side == Side.BLACK:
            king_to_check = black_king

        for i in self.chess_list:
            if i.validate_movement(king_to_check.point, self):
                return True
        return False

    def is_game_over(self, side):
        # 困斃rule DON'T have to check is_in_check

        # king_to_check = self.find_king(side)
        # piece_checking_king_list = []
        # for i in self.chess_board.chess_list:
        #     if i.validate_movement(king_to_check.point, self.chess_board):
        #         piece_checking_king_list.append(i)

        # if not is_in_check:  # not getting check
        #     return False

        # move every single move u can go
        # if one of them escape the check then return False
        # king face king rule confirm required
        # may have to use the same way as chessboard's movement
        # move verify and undo
        # may have to implement undo method in chessboard
        final_chess_list_temp = copy.deepcopy(self.chess_list)
        # DON'T USE self.chess_list to iter it cuz fetal error
        for i in final_chess_list_temp:
            if i.side != side:
                continue
            for x in range(0, 9):
                for y in range(0, 10):
                    if not i.validate_movement((x, y), self):
                        continue
                    # move
                    # actual move
                    chess_to_remove = self.find_chess((x, y))
                    if chess_to_remove:
                        self.remove_chess((x, y))
                    chess_to_move = self.find_chess(i.point)
                    chess_to_move.point = (x, y)

                    # verify
                    if not self.is_getting_check(side):
                        self.chess_list = copy.deepcopy(final_chess_list_temp)
                        return False
                    # undo
                    self.chess_list = copy.deepcopy(final_chess_list_temp)

        return True

    def find_king(self, side):
        for i in self._chess_list:
            if i.side == side and isinstance(i, King):
                return i
        return None

    # TODO:找到兩顆應該回NONE？ 或實作chess count method
    def find_chess(self, point):
        for i in self._chess_list:
            if i.point == point:
                return i
        return None

    def remove_chess(self, point):
        self._chess_list[:] = [x for x in self._chess_list if x.point != point]

from chess import Chess


class Knight(Chess):

    def validate_movement(self, to_point: tuple, ChessBoard):
        from_point = self.point
        if to_point == from_point:
            return False
        if not self.is_in_board(to_point):
            return False
        if abs(from_point[0] - to_point[0]) + abs(from_point[1] -
                                                  to_point[1]) != 3:
            return False
        if abs(from_point[0] - to_point[0]) == 0 or abs(from_point[1] -
                                                        to_point[1]) == 0:
            return False
        horse_foot = from_point
        if abs(from_point[0] - to_point[0]) == 2:
            horse_foot = (horse_foot[0] + (to_point[0] - from_point[0]) / 2,
                          horse_foot[1])
        else:
            horse_foot = (horse_foot[0],
                          horse_foot[1] + (to_point[1] - from_point[1]) / 2)
        if self.has_chess(horse_foot, ChessBoard):
            return False
        if self.has_chess(to_point, ChessBoard) and not self.is_opponant(
                to_point, ChessBoard):
            return False
        return True

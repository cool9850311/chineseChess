import unittest

from chess_board import ChessBoard


class CanonTestCase(unittest.TestCase):

    # 每一個testcase開始前都會被呼叫 -> 前置作業
    def setUp(self):
        self.ChessBoard = ChessBoard()
        self.ChessBoard.init_game()

    # 每一個testcase結束後會被呼叫 -> 清理善後作業
    def tearDown(self):
        self.ChessBoard = None

    def test_canon01(self):
        expected = True
        result = self.ChessBoard.move_chess((1, 2), (1, 9))
        self.assertEqual(expected, result)

    def test_canon02(self):
        expected = True
        result = self.ChessBoard.move_chess((1, 2), (3, 2))
        self.assertEqual(expected, result)

    def test_canon03(self):
        expected = False
        result = self.ChessBoard.move_chess((1, 2), (1, 7))
        self.assertEqual(expected, result)

    def test_canon04(self):
        expected = False
        result = self.ChessBoard.move_chess((1, 2), (8, 2))
        self.assertEqual(expected, result)

    def test_canon08(self):  # 跑過頭
        expected = False
        result = self.ChessBoard.move_chess((7, 2), (6, 2))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((6, 2), (6, 7))
        self.assertEqual(expected, result)


class BishopTestCase(unittest.TestCase):

    def setUp(self):
        self.ChessBoard = ChessBoard()
        self.ChessBoard.init_game()

    # 每一個testcase結束後會被呼叫 -> 清理善後作業
    def tearDown(self):
        self.ChessBoard = None

    def test_bishop01(self):
        expected = True
        result = self.ChessBoard.move_chess((2, 0), (4, 2))
        self.assertEqual(expected, result)

    def test_bishop02(self):
        expected = False
        result = self.ChessBoard.move_chess((2, 0), (2, 1))
        self.assertEqual(expected, result)

    def test_bishop03(self):  # elephant eye
        expected = False
        # Given
        self.ChessBoard.move_chess((1, 2), (1, 1))
        # Then
        result = self.ChessBoard.move_chess((2, 0), (0, 2))
        self.assertEqual(expected, result)

    def test_bishop04(self):  # cross river
        expected = False
        # Given
        self.ChessBoard.move_chess((2, 0), (4, 2))
        self.ChessBoard.move_chess((4, 2), (2, 4))

        # Then
        result = self.ChessBoard.move_chess((2, 4), (4, 6))
        self.assertEqual(expected, result)

    def test_bishop05(self):
        expected = True
        # Given
        self.ChessBoard.move_chess((2, 0), (4, 2))
        self.ChessBoard.move_chess((4, 2), (2, 4))

        # Then
        result = self.ChessBoard.move_chess((2, 4), (0, 2))
        self.assertEqual(expected, result)

    def test_bishop06(self):
        expected = False
        # Given
        self.ChessBoard.move_chess((1, 2), (4, 2))

        # Then
        result = self.ChessBoard.move_chess((2, 0), (4, 2))
        self.assertEqual(expected, result)


class AdvisorTestCase(unittest.TestCase):

    # 每一個testcase開始前都會被呼叫 -> 前置作業
    def setUp(self):
        self.ChessBoard = ChessBoard()
        self.ChessBoard.init_game()

    # 每一個testcase結束後會被呼叫 -> 清理善後作業
    def tearDown(self):
        self.ChessBoard = None

    def test_advisor01(self):  # 原地
        expected = False
        result = self.ChessBoard.move_chess((3, 0), (3, 0))
        self.assertEqual(expected, result)

    def test_advisor02(self):  # 走直
        expected = False
        result = self.ChessBoard.move_chess((3, 0), (3, 1))
        self.assertEqual(expected, result)

    def test_advisor03(self):  # 走斜
        expected = True
        result = self.ChessBoard.move_chess((3, 0), (4, 1))
        self.assertEqual(expected, result)

    def test_advisor04(self):  # 走兩步
        expected = False
        result = self.ChessBoard.move_chess((3, 0), (3, 2))
        self.assertEqual(expected, result)

    def test_advisor05(self):  # 走兩步(黑)
        expected = False
        result = self.ChessBoard.move_chess((3, 9), (3, 7))
        self.assertEqual(expected, result)

    def test_advisor06(self):  # 超出範圍
        expected = False
        result = self.ChessBoard.move_chess((3, 0), (2, 1))
        self.assertEqual(expected, result)

    def test_advisor07(self):  # 超出範圍(黑)
        expected = False
        result = self.ChessBoard.move_chess((3, 9), (2, 8))
        self.assertEqual(expected, result)

    def test_advisor08(self):  # 友軍位置
        expected = False
        result = self.ChessBoard.move_chess((3, 0), (4, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((5, 0), (4, 1))
        self.assertEqual(expected, result)


class KingTestCase(unittest.TestCase):

    # 每一個testcase開始前都會被呼叫 -> 前置作業
    def setUp(self):
        self.ChessBoard = ChessBoard()
        self.ChessBoard.init_game()

    # 每一個testcase結束後會被呼叫 -> 清理善後作業
    def tearDown(self):
        self.ChessBoard = None

    def test_king01(self):  # 原地
        expected = False
        result = self.ChessBoard.move_chess((4, 0), (4, 0))
        self.assertEqual(expected, result)

    def test_king02(self):  # 走直
        expected = True
        result = self.ChessBoard.move_chess((4, 0), (4, 1))
        self.assertEqual(expected, result)

    def test_king03(self):  # 走斜
        expected = False
        result = self.ChessBoard.move_chess((4, 0), (3, 1))
        self.assertEqual(expected, result)

    def test_king04(self):  # 走兩步
        expected = False
        result = self.ChessBoard.move_chess((4, 0), (4, 2))
        self.assertEqual(expected, result)

    def test_king05(self):  # 走兩步(黑)
        expected = False
        result = self.ChessBoard.move_chess((4, 9), (4, 7))
        self.assertEqual(expected, result)

    def test_king06(self):  # 超出範圍
        expected = False
        result = self.ChessBoard.move_chess((4, 0), (4, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 1), (3, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((3, 1), (2, 1))
        self.assertEqual(expected, result)

    def test_king07(self):  # 超出範圍(黑)
        expected = False
        result = self.ChessBoard.move_chess((4, 9), (4, 8))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 8), (3, 8))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((3, 8), (2, 8))
        self.assertEqual(expected, result)

    def test_king08(self):  # 友軍位置
        expected = False
        result = self.ChessBoard.move_chess((4, 0), (3, 0))
        self.assertEqual(expected, result)


class PawnTestCase(unittest.TestCase):

    # 每一個testcase開始前都會被呼叫 -> 前置作業
    def setUp(self):
        self.ChessBoard = ChessBoard()
        self.ChessBoard.init_game()

    # 每一個testcase結束後會被呼叫 -> 清理善後作業
    def tearDown(self):
        self.ChessBoard = None

    def test_pawn01(self):  # 原地
        expected = False
        result = self.ChessBoard.move_chess((4, 3), (4, 3))
        self.assertEqual(expected, result)

    def test_pawn02(self):  # 走直
        expected = True
        result = self.ChessBoard.move_chess((4, 3), (4, 4))
        self.assertEqual(expected, result)

    def test_pawn03(self):  # 走斜
        expected = False
        result = self.ChessBoard.move_chess((4, 3), (3, 4))
        self.assertEqual(expected, result)

    def test_pawn04(self):  # 走兩步
        expected = False
        result = self.ChessBoard.move_chess((4, 3), (4, 5))
        self.assertEqual(expected, result)

    def test_pawn05(self):  # 走兩步(黑)
        expected = False
        result = self.ChessBoard.move_chess((4, 6), (4, 4))
        self.assertEqual(expected, result)

    def test_pawn06(self):  # 超出範圍
        expected = False
        result = self.ChessBoard.move_chess((0, 3), (-1, 3))
        self.assertEqual(expected, result)

    def test_pawn07(self):  # 超出範圍(黑)
        expected = False
        result = self.ChessBoard.move_chess((0, 6), (-1, 6))
        self.assertEqual(expected, result)

    def test_pawn08(self):  # 友軍位置
        expected = False
        result = self.ChessBoard.move_chess((1, 2), (1, 4))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((1, 4), (2, 4))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((2, 3), (2, 4))
        self.assertEqual(expected, result)

    def test_pawn09(self):  # 不能後退
        expected = False
        result = self.ChessBoard.move_chess((4, 3), (4, 2))
        self.assertEqual(expected, result)

    def test_pawn10(self):  # 不能後退(黑)
        expected = False
        result = self.ChessBoard.move_chess((4, 6), (4, 7))
        self.assertEqual(expected, result)

    def test_pawn11(self):  # 過河左右走
        expected = True
        result = self.ChessBoard.move_chess((4, 3), (4, 4))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 4), (4, 5))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 5), (3, 5))
        self.assertEqual(expected, result)

    def test_pawn12(self):  # 過河左右走(黑)
        expected = True
        result = self.ChessBoard.move_chess((4, 6), (4, 5))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 5), (4, 4))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 4), (3, 4))
        self.assertEqual(expected, result)

    def test_pawn13(self):  # 過河前左右走
        expected = False
        result = self.ChessBoard.move_chess((4, 3), (3, 3))
        self.assertEqual(expected, result)


class KnightTestCase(unittest.TestCase):

    # 每一個testcase開始前都會被呼叫 -> 前置作業
    def setUp(self):
        self.ChessBoard = ChessBoard()
        self.ChessBoard.init_game()

    # 每一個testcase結束後會被呼叫 -> 清理善後作業
    def tearDown(self):
        self.ChessBoard = None

    def test_knight01(self):  # 原地
        expected = False
        result = self.ChessBoard.move_chess((1, 0), (1, 0))
        self.assertEqual(expected, result)

    def test_knight02(self):  # 走直
        expected = False
        result = self.ChessBoard.move_chess((1, 0), (1, 3))
        self.assertEqual(expected, result)

    def test_knight03(self):  # 走斜
        expected = True
        result = self.ChessBoard.move_chess((1, 0), (2, 2))
        self.assertEqual(expected, result)

    def test_knight04(self):  # 卡馬腳
        expected = False
        result = self.ChessBoard.move_chess((1, 0), (3, 1))
        self.assertEqual(expected, result)

    def test_knight05(self):  # 超出範圍
        expected = False
        result = self.ChessBoard.move_chess((1, 0), (0, 2))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((0, 2), (-1, 0))
        self.assertEqual(expected, result)

    def test_knight06(self):  # 友軍位置
        expected = False
        result = self.ChessBoard.move_chess((1, 0), (2, 2))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((2, 2), (3, 0))
        self.assertEqual(expected, result)


class RookTestCase(unittest.TestCase):

    # 每一個testcase開始前都會被呼叫 -> 前置作業
    def setUp(self):
        self.ChessBoard = ChessBoard()
        self.ChessBoard.init_game()

    # 每一個testcase結束後會被呼叫 -> 清理善後作業
    def tearDown(self):
        self.ChessBoard = None

    def test_rook01(self):  # 原地
        expected = False
        result = self.ChessBoard.move_chess((0, 0), (0, 0))
        self.assertEqual(expected, result)

    def test_rook02(self):  # 走直
        expected = True
        result = self.ChessBoard.move_chess((0, 0), (0, 1))
        self.assertEqual(expected, result)

    def test_rook03(self):  # 走斜
        expected = False
        result = self.ChessBoard.move_chess((0, 0), (1, 1))
        self.assertEqual(expected, result)

    def test_rook04(self):  # 有擋路的
        expected = False
        result = self.ChessBoard.move_chess((0, 0), (0, 6))
        self.assertEqual(expected, result)

    def test_rook05(self):  # 超出範圍
        expected = False
        result = self.ChessBoard.move_chess((0, 0), (-1, 0))
        self.assertEqual(expected, result)

    def test_rook06(self):  # 友軍位置
        expected = False
        result = self.ChessBoard.move_chess((0, 0), (1, 0))
        self.assertEqual(expected, result)

    def test_rook07(self):  # 吃子
        expected = True
        result = self.ChessBoard.move_chess((0, 0), (0, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((0, 1), (3, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((3, 1), (3, 9))
        self.assertEqual(expected, result)

    def test_rook08(self):  # 跑過頭
        expected = False
        result = self.ChessBoard.move_chess((0, 0), (0, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((0, 1), (1, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((1, 2), (0, 2))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((1, 1), (1, 8))
        self.assertEqual(expected, result)


class CheckTestCase(unittest.TestCase):

    # 每一個testcase開始前都會被呼叫 -> 前置作業
    def setUp(self):
        self.ChessBoard = ChessBoard()
        self.ChessBoard.init_game()

    # 每一個testcase結束後會被呼叫 -> 清理善後作業
    def tearDown(self):
        self.ChessBoard = None

    def test_check01(self):  # 王對王(紅)
        expected = False
        result = self.ChessBoard.move_chess((4, 0), (4, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 9), (4, 8))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 8), (3, 8))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 1), (3, 1))
        self.assertEqual(expected, result)

    def test_check02(self):  # 王對王(黑)
        expected = False
        result = self.ChessBoard.move_chess((4, 0), (4, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 9), (4, 8))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 1), (3, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 8), (3, 8))
        self.assertEqual(expected, result)

    def test_check03(self):  # 王以外(紅)
        expected = False
        result = self.ChessBoard.move_chess((4, 0), (4, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((0, 9), (0, 8))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((0, 8), (3, 8))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 1), (3, 1))
        self.assertEqual(expected, result)

    def test_check04(self):  # 王以外(黑)
        expected = False
        result = self.ChessBoard.move_chess((4, 9), (4, 8))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((0, 0), (0, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((0, 1), (3, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 8), (3, 8))
        self.assertEqual(expected, result)

    def test_check05(self):  # 不能走需要恢復
        expected = False
        result = self.ChessBoard.move_chess((4, 0), (4, 1))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((0, 9), (0, 8))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((0, 8), (3, 8))
        self.assertEqual(True, result)
        result = self.ChessBoard.move_chess((4, 1), (3, 1))
        self.assertEqual(expected, result)
        result = self.ChessBoard.move_chess((4, 1), (5, 1))
        self.assertEqual(True, result)


def suite():
    suite = unittest.TestSuite()

    suite.addTest((unittest.TestLoader().loadTestsFromTestCase(CanonTestCase)))
    suite.addTest(
        (unittest.TestLoader().loadTestsFromTestCase(BishopTestCase)))
    suite.addTest(
        (unittest.TestLoader().loadTestsFromTestCase(AdvisorTestCase)))
    suite.addTest((unittest.TestLoader().loadTestsFromTestCase(KingTestCase)))
    suite.addTest((unittest.TestLoader().loadTestsFromTestCase(PawnTestCase)))
    suite.addTest(
        (unittest.TestLoader().loadTestsFromTestCase(KnightTestCase)))
    suite.addTest((unittest.TestLoader().loadTestsFromTestCase(RookTestCase)))
    suite.addTest((unittest.TestLoader().loadTestsFromTestCase(CheckTestCase)))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())

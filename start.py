import pygame
import math
from chinese_chess import ChineseChess
from gui.piece_sprite import PieceSprite


def covert_point_to_position(point):
    x = point[0] * 57 + 33
    y = 548 - point[1] * 57
    return (x, y)


def fix_position(point):
    x, y = covert_point_to_position(point)
    return (x - 28, y - 28)


def covert_position_to_point(position):

    for x in range(0, 9):
        for y in range(0, 10):
            x_position = x * 57 + 33
            y_position = 548 - y * 57
            if math.hypot(position[0] - x_position,
                          position[1] - y_position) <= 28:
                return (x, y)
    return None


# 初始化 Pygame
pygame.init()

FPS = 60
# 521 * 577
# 57 * 57
# piece size also 57
# 33 548 equal 0 0
background = pygame.image.load('./gui/img/wood_board.GIF')
# 創建視窗
screen = pygame.display.set_mode(background.get_size())

# 設定視窗標題
pygame.display.set_caption("Chinese Chess Game")
main_clock = pygame.time.Clock()
# 創建 sprite 群組
all_sprites = pygame.sprite.Group()

background = background.convert()
screen.blit(background, (0, 0))
pygame.display.update()

# 創建棋子
# /gui/img/
pieces = [
    PieceSprite("./gui/img/black_rook.GIF", fix_position((0, 9))),
    PieceSprite("./gui/img/black_rook.GIF", fix_position((8, 9))),
    PieceSprite("./gui/img/black_knight.GIF", fix_position((1, 9))),
    PieceSprite("./gui/img/black_knight.GIF", fix_position((7, 9))),
    PieceSprite("./gui/img/black_bishop.GIF", fix_position((2, 9))),
    PieceSprite("./gui/img/black_bishop.GIF", fix_position((6, 9))),
    PieceSprite("./gui/img/black_advisor.GIF", fix_position((3, 9))),
    PieceSprite("./gui/img/black_advisor.GIF", fix_position((5, 9))),
    PieceSprite("./gui/img/black_cannon.GIF", fix_position((1, 7))),
    PieceSprite("./gui/img/black_cannon.GIF", fix_position((7, 7))),
    PieceSprite("./gui/img/black_king.GIF", fix_position((4, 9))),
    PieceSprite("./gui/img/black_pawn.GIF", fix_position((0, 6))),
    PieceSprite("./gui/img/black_pawn.GIF", fix_position((2, 6))),
    PieceSprite("./gui/img/black_pawn.GIF", fix_position((4, 6))),
    PieceSprite("./gui/img/black_pawn.GIF", fix_position((6, 6))),
    PieceSprite("./gui/img/black_pawn.GIF", fix_position((8, 6))),
    PieceSprite("./gui/img/red_rook.GIF", fix_position((0, 0))),
    PieceSprite("./gui/img/red_rook.GIF", fix_position((8, 0))),
    PieceSprite("./gui/img/red_knight.GIF", fix_position((1, 0))),
    PieceSprite("./gui/img/red_knight.GIF", fix_position((7, 0))),
    PieceSprite("./gui/img/red_bishop.GIF", fix_position((2, 0))),
    PieceSprite("./gui/img/red_bishop.GIF", fix_position((6, 0))),
    PieceSprite("./gui/img/red_advisor.GIF", fix_position((3, 0))),
    PieceSprite("./gui/img/red_advisor.GIF", fix_position((5, 0))),
    PieceSprite("./gui/img/red_cannon.GIF", fix_position((1, 2))),
    PieceSprite("./gui/img/red_cannon.GIF", fix_position((7, 2))),
    PieceSprite("./gui/img/red_king.GIF", fix_position((4, 0))),
    PieceSprite("./gui/img/red_pawn.GIF", fix_position((0, 3))),
    PieceSprite("./gui/img/red_pawn.GIF", fix_position((2, 3))),
    PieceSprite("./gui/img/red_pawn.GIF", fix_position((4, 3))),
    PieceSprite("./gui/img/red_pawn.GIF", fix_position((6, 3))),
    PieceSprite("./gui/img/red_pawn.GIF", fix_position((8, 3)))
]

# 將棋子加入 sprite 群組
for piece in pieces:
    all_sprites.add(piece)
# init game
game = ChineseChess()
game.start()
# 遊戲主迴圈
running = True
selected_piece = None
game_over = False
while running:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                continue
            if selected_piece:
                from_position_x, from_position_y = selected_piece.get_position(
                )
                from_point = covert_position_to_point(
                    (from_position_x + 28, from_position_y + 28))
                to_point = covert_position_to_point(event.pos)
                to_piece = None
                if to_point is None or not game.move_chess(
                        from_point, to_point):
                    selected_piece.unselect()
                    selected_piece = None
                    continue

                for piece in all_sprites:
                    if piece.rect.collidepoint(event.pos):
                        to_piece = piece
                        break
                if to_piece:
                    to_piece.kill()
                to_position = fix_position(to_point)
                selected_piece.move(to_position[0], to_position[1])
                selected_piece.unselect()
                selected_piece = None
                game.check_winner()

                if game.current_player == game.red_player:
                    game.current_player = game.black_player
                else:
                    game.current_player = game.red_player

            else:
                for piece in all_sprites:
                    if piece.rect.collidepoint(event.pos):
                        if not game.can_be_select(
                                covert_position_to_point(event.pos)):
                            break
                        selected_piece = piece
                        selected_piece.select()
                        break

    # 更新畫面
    if not game_over:
        all_sprites.clear(screen, background)
        all_sprites.update()
        all_sprites.draw(screen)
    if game.game_over:
        msg = ''
        if game.winner == game.red_player:
            msg = 'Game Over Red Won'
        else:
            msg = 'Game Over Black Won'
        font = pygame.font.Font(pygame.font.get_default_font(), 36)

        # now print the text
        text_surface = font.render(msg, False, pygame.Color('blue'))
        screen.blit(text_surface, dest=(75, 0))
        game_over = True
    pygame.display.update()
    main_clock.tick(FPS)

# 釋放 Pygame
pygame.quit()

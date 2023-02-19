
from chinese_chess import ChineseChess
import re

from side import Side

if __name__ == "__main__":
    game = ChineseChess()
    game.start()
    while True:
        if game.current_player.side == Side.RED:
            print('Red Player\'s turn Please input your move')
        else:
            print('Black Player\'s turn Please input your move')
        move_input = input()
        if not re.search('^\\d{4}$', move_input):
            print('Wrong Move Try Again')
            continue
        if not game.move_chess((int(move_input[0]), int(move_input[1])), (
                int(move_input[2]),
                int(move_input[3]),
        )):
            print('Wrong Move Try Again')
            continue
        game.check_winner()
        if game.game_over:
            break
        if game.current_player == game.red_player:
            game.current_player = game.black_player
        else:
            game.current_player = game.red_player
    if game.winner == game.red_player:
        print('Game Over Red Won')
    else:
        print('Game Over Black Won')

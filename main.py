import random
from game_logic import game








if __name__ == "__main__":
    game_now=game.init_game()
    while len(game_now['player_1']['hand']) and len(game_now['player_2']['hand']):
        game.play_round(game_now['player_1'], game_now['player_2'])
    print(game_now['player_1']['name'],len(game_now['player_1']['won_pile']))
    print(game_now['player_2']['name'],len(game_now['player_2']['won_pile']))
    if len(game_now['player_2']['won_pile']) > len(game_now['player_1']['won_pile']):
        print(game_now['player_2']['name'],'winner')
    elif len(game_now['player_1']['won_pile']) > len(game_now['player_2']['won_pile']):
        print(game_now['player_1']['name'],'winner')
    else:
        print('draw')





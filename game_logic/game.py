from utils import deck





def create_player(name:str='Ai') -> dict:
    player={'name':name,'hand':[],'won_pile':[]}
    return player



def init_game()->dict:
    players=[]

    players.append(create_player())
    players.append(create_player(input('Please enter your name.')))
    deck1=deck.create_deck()
    deck1=deck.shuffle(deck1)
    for i in range(52):
        if i < 26:
            players[1]['hand'].append(deck1[i])
        else:
            players[0]['hand'].append(deck1[i])
    return players





def  play_round(p1:dict,p2:dict):
    pass


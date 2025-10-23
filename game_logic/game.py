from utils import deck





def create_player(name:str='Ai') -> dict:
    player={'name':name,'hand':[],'won_pile':[]}
    return player



def init_game()->dict:

    p2=create_player()
    p1=create_player(input('Please enter your name'))
    deck1=deck.create_deck()
    deck1=deck.shuffle(deck1)
    for i in range(52):
        if i < 26:
           p1['hand'].append(deck1[i])
        else:
            p2['hand'].append(deck1[i])
    players={"player_1":p1,'player_2':p2,'deck':deck1}

    return players





def  play_round(p1:dict,p2:dict):
    p1_rotation = p1["hand"].pop(-1)
    p2_rotation = p2["hand"].pop(-1)
    if p1_rotation['value'] > p2_rotation['value']:
        p1['won_pile'].append(p1_rotation)
        p1['won_pile'].append(p2_rotation)
        print(p1['name'],'winner',p1_rotation)
    elif p2_rotation['value'] > p1_rotation['value']:
        p2['won_pile'].append(p1_rotation)
        p2['won_pile'].append(p2_rotation)
        print(p2['name'],'winner',p2_rotation)
    else:
         print('draw',p1_rotation)






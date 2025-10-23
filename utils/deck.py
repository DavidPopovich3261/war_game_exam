



def create_card(rank:str,suite:str) -> dict:
    value_cards={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
    card={"rank":rank,"suite":suite,'value':value_cards[rank]}
    return card



def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        result="p1"
    elif p2_card['value'] > p1_card['value']:
        result='p2'
    else:
        result="WAR"
    return result


def create_deck() -> list[dict]:
    pass

def shuffle(deck:list[dict]) -> list[dict]:
    pass

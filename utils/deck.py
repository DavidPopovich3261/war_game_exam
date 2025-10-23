



def create_card(rank:str,suite:str) -> dict:
    value_cards={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
    card={"rank":rank,"suite":suite,'value':value_cards[rank]}


def compare_cards(p1_card:dict, p2_card:dict) -> str:
    pass


def create_deck() -> list[dict]:
    pass

def shuffle(deck:list[dict]) -> list[dict]:
    pass

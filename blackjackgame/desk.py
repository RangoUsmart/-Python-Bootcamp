suits = ['♠', '♣', '♦', '♥']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def generate_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    desk_string = ''
    for card in deck:
        desk_string += card[0] + card[1] + ' '
        if card[0] == 'K':
            desk_string += '\n'
    return desk_string

desk = generate_deck()
print(desk)

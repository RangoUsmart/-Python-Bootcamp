suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

cards = [f'{rank}{suit}' for suit in suits for rank in ranks]

for card in cards:
    print(card, end=' ')

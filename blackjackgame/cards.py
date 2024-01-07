suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

cards = [f'{rank}{suit}' for suit in suits for rank in ranks]

def build_card_image(cards):
    for card in cards:
        print(f'┌─────┐', end=' ')
    print()
    for card in cards:
        print(f'| {card[0]:<2}  |', end=' ')
    print()
    for card in cards:
        print(f'|     |', end=' ')
    print()
    for card in cards:
        print(f'|  {card[1]}  |', end=' ')
    print()
    for card in cards:
        print(f'|     |', end=' ')
    print()
    for card in cards:
        print(f'|  {card[0]:>2} |', end=' ')
    print()
    for card in cards:
        print(f'└─────┘', end=' ')
    print()

for card in cards:
    print(card, end=' ')
print()
build_card_image(cards[0:10])

def build_card_image(card):
    print(f'┌─────┐')
    print(f'| {card.rank:<2}  |')
    print(f'|     |')
    print(f'|  {card.suit}  |')
    print(f'|     |')
    print(f'|  {card.rank:>2} |')
    print(f'└─────┘')
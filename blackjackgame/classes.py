import random 

suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
values = {
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8, 
        '9':9,
        '10':10,
        'J':10,
        'Q':10,
        'K':10,
        'A':11
        }
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' ' + self.suit
  
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
            # pass
    
    def __str__(self):
        deck_str = ""
        for card in self.deck:
            deck_str += str(card) + "\n"
        return deck_str
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        car=self.deck.pop(0)
        return car
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        
    def __str__(self):
        hand_str = ""
        for card in self.cards:
            hand_str += str(card) + "\n"
        return hand_str
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
    
    def adjust_for_ace(self):
        pass
    
    def build_card_image(self, hide_second=False):
        cards = self.cards
        for card in cards:
            print(f'┌─────┐', end=' ')
        print()
        
        for card in cards:
            if hide_second and card == cards[1]:
                print(f'|  X  |', end=' ')
            else:
                print(f'| {card.rank:<2}  |', end=' ')
        print()
        
        
        for card in cards:
            print(f'|     |', end=' ')
        print()

        for card in cards:
            if hide_second and card == cards[1]:
                print(f'|  X  |', end=' ')
            else:
                print(f'|  {card.suit}  |', end=' ')
        print()

        for card in cards:
            print(f'|     |', end=' ')
        print()
        
        for card in cards:
            if hide_second and card == cards[1]:
                print(f'|  X  |', end=' ')
            else:
                print(f'|  {card.rank:>2} |', end=' ')
        print()
        
        for card in cards:
            print(f'└─────┘', end=' ')
        print()

    
class Chips:
    def __init__(self, total=0, bet=0):
        self.total = total # This can be set to a default value or supplied by a user input
        self.bet = bet
        
    def win_bet(self):
        self.total += int(self.bet*1.5)
        return self.total
        # pass
    
    def lose_bet(self):
        self.total -= int(self.bet)
        return self.total
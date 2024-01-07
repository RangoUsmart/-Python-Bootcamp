import random 
import classes as cl  

cassino_money = 1000
player_money = 100
playing = True

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
    
    def adjust_for_ace(self):
        pass
    
class Chips:
    
    def __init__(self):
        self.total = player_money  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet*1.5
        # pass
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet():
    print(f"Ваш баланс: {player_money}")  
    try:
        bet = int(input("Ваша ставка: "))
        return bet
    except ValueError:
        print("Введіть число")
        take_bet()

while True:
    # Print an opening statement
    print("Гра в блекджек!")
    koloda=Deck()
    koloda.shuffle()
    # print(koloda)
    
    
    # Create & shuffle the deck, deal two cards to each player
    computer_hand = Hand()
    player_hand = Hand()

    for _ in range(2):
        computer_hand.add_card(koloda.deal())
        player_hand.add_card(koloda.deal())
    # Set up the Player's chips
    chips=Chips()
    # Prompt the Player for their bet
    # print(koloda)
    chips.bet=take_bet()
    
    
    # Show cards (but keep one dealer card hidden)
    print("карти казино {} інша карта чекає ???".format(computer_hand.cards[0]))
    print("карти гравця {} інша карта {}".format(player_hand.cards[0],player_hand.cards[1]))
    # print(computer_hand.cards[0]+ " " + "???")
    # print(player_hand.cards[0]+ " " + player_hand.cards[1])
    break
    playing = True
    while playing:  # recall this variable from our hit_or_stand function
            print("щось там")

        
        # Prompt for Player to Hit or Stand
        
        
        # Show cards (but keep one dealer card hidden)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        
            # playing = False
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    
        # Show all cards
    
        # Run different winning scenarios
        
    
    # Inform Player of their chips total 
    
    # Ask to play again

        # break
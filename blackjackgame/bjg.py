
from classes import Deck, Hand, Chips   
import time

cassino_money = 1000
player_money = 100
playing = True

    

def draw_table(coins=0, prob=Deck(), bank=0):
    print("_"*12)
    print("банк: {}$    ".format(bank))
    print("вірогідність: {:.2f}%    ".format(prob*100))
    print(" "*12)
    print(" "*12)
    print("_"*12)   

def take_bet():
    print(f"Ваш баланс: {player_money}")  
    try:
        bet = int(input("Ваша ставка: "))
        return bet
    except ValueError:
        print("Введіть число")
        take_bet()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    ask=input("Ваш хід: ")
    if ask == "hit":
        hand.add_card(deck.deal())
        if hand.value >= 21:
            playing = False 
    elif ask == "stand":
        playing = False
    
def calculate_probability(cards):
    total = 0
    count = 0

    for card in cards:
        if card.rank != 'A':
            total += card.value
        else:
            count += 1

    if count > 0:
        for _ in range(count):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1

    probability = (21 - total) / (len(cards) * 13 - len(cards))
    return probability

        
while True:
    # Print an opening statement
    print("Гра в блекджек!")
    koloda=Deck()
    koloda.shuffle()
    
    # Create & shuffle the deck, deal two cards to each player
    computer_hand = Hand()
    player_hand = Hand()

    for _ in range(2):
        computer_hand.add_card(koloda.deal())
        player_hand.add_card(koloda.deal())
    # Set up the Player's chips
    comp_chips=Chips()
    comp_chips.total=1000
    player_chips=Chips()
    player_chips.total=100

    player_chips.bet=take_bet()
    playing = True
    while playing:  # recall this variable from our hit_or_stand function
        
        computer_hand.build_card_image( hide_second=True)
        print("карти казино ")
        draw_table(prob=calculate_probability(player_hand.cards),
                   bank=player_chips.bet*1.5)
        print("карти гравця ")
        player_hand.build_card_image()
        print("Для продовження введіть hit або stand")
        hit_or_stand(koloda,player_hand)
        if player_hand.value>21:
            comp_chips.win_bet()
            player_chips.lose_bet()
    
    while calculate_probability(computer_hand.cards)>0.20 or (21>=player_hand.value>computer_hand.value ):
            computer_hand.add_card(koloda.deal())
            computer_hand.build_card_image()
            print("карти казино ")
            draw_table(prob=calculate_probability(computer_hand.cards),
                       bank=player_chips.bet*1.5)
            print("карти гравця ")
            player_hand.build_card_image()
            time.sleep(1)
            
    computer_hand.build_card_image()
    print("карти казино ")
    print("карти гравця ")
    player_hand.build_card_image()
      
    if player_hand.value<computer_hand.value <=21 or player_hand.value>21:
        print("Казино виграло!")
        comp_chips.win_bet()
        player_chips.lose_bet()
    elif computer_hand.value < player_hand.value<=21 or computer_hand.value>21:
        print("Ви виграли!")
        player_chips.win_bet()
        comp_chips.lose_bet()
    else:
        print("Нічия!")        
    
    # Inform Player of their chips total 
    
    # Ask to play again

    break
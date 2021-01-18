import random

# Creating references to the suits, ranks and values to use throughout
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    # Removing a card from the player's cards
    def remove_one(self):
        return self.all_cards.pop(0)
    
    # Adding either a single card or array of cards to player's stack
    def add_cards(self, new_cards):
        if type(new_cards) == type([]): # dealing with multiple cards
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return 'Player {} has {} cards'.format(self.name, len(self.all_cards))
    

    # GAME SETUP

    # Declaring two instances of the Player class
    player_one = Player('One')
    player_two = Player('Two')

    # creating a new deck and shuffling it
    new_deck = Deck()
    new_deck.shuffle()

    # splitting the deck in half for each player
    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())
    
    game_on = True
    round_num = 0

    # BEGINNING OF GAME LOGIC
    while game_on:
        round_num += 1
        print('Round {}'.format(round_num))

        if len(player_one.all_cards) == 0:
            print('Player One is out of cards. \nPlayer Two wins!')
            game_on = False
            break
            
        if len(player_two.all_cards) == 0:
            print('Player Two is out of cards. \nPlayer One wins!')
            game_on = False
            break

        # STARTING A NEW ROUND
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        # ENABLING THE 'WAR' FEATURE
        at_war = True

        while at_war:
            # Checking if Player 1's last card beats Player 2
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False
            
            # Checking if Player 2's last card beats Player 1
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False
        
        else:
            print('WAR!')
            
            # Checking if Player 1 is unable to go to war
            # Player 1 has less than 5 cards, thus losing the game
            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war.")
                print("Player Two wins!")
                game_on = False
                break
            
            # Checking if Player 2 is unable to go to war
            # PLayer 2 has less than 5 cards, thus losing the game
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war.")
                print("Player One wins!")
                game_on = False
                break
            
            # Otherwise, add 5 cards to each player's 'WAR' stack
            # Compare the last card in the next iteration of the while loop
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
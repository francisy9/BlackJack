#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


# In[3]:


class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'


# In[4]:


class Deck():
    
    
    def __init__(self):
        self.card_list = []
        for everysuit in suits:
            for everyrank in ranks:
                self.card_list.append(Card(everysuit,everyrank))
                
    def __str__(self):
        deck_string = ''
        for card in self.card_list:
            deck_string += '\n' + card.__str__()
        return 'Remaining cards:' + deck_string
    
    def shuffle_deck(self):
        random.shuffle(self.card_list)
        
    def deal(self):
        dealt_card = self.card_list.pop()
        return dealt_card
        


# In[5]:


class Player():
    
    
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0
        
    def add(self,card):
        self.hand.append(card)
        self.value += card.value
        
    def with_aces(self):
        while self.value > 21 and self.aces > 0:
            self.value -=10
            self.aces -=1


# In[6]:


def checkbust(player):
    
    player.with_aces()
    
    if player.value > 21:
        return True
    else: 
        return False


# In[7]:


class playermoney():
    
    total = 1000
    
    def __init__(self):
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# In[8]:


def take_bet(playermoney):
        try:
            playermoney.bet = int(input('How much are you betting?'))
        except ValueError:
            print('Please enter an interger.')
        else:
            if playermoney.bet > playermoney.total:
                print(f'Insufficient funds. You have {playermoney.total} left')


# In[9]:


def draw(deck,player):
    
    player.add(deck.deal())
    player.with_aces()


# In[10]:


def keep_hitting(deck,player):
    global playing 
    
    while True:
        hit = input('Hit? (y or n)')
        
        if hit == 'y':
            draw(deck,player)
            
        elif hit == 'n':
            print('Player stands. Dealer is playing.')
            playing = False
        
        else:
            print('Sorry, please enter y or n.')
            continue
        break


# In[11]:


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.hand[1])  
    print("\nPlayer's Hand:", *player.hand, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.hand, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.hand, sep='\n ')
    print("Player's Hand =",player.value)


# In[12]:


def player_busts(money):
    print("Player busts!")
    money.lose_bet()

def player_wins(money):
    print("Player wins!")
    money.win_bet()

def dealer_busts(money):
    print("Dealer busts!")
    money.win_bet()
    
def dealer_wins(money):
    print("Dealer wins!")
    money.lose_bet()
    
def push():
    print("Dealer and Player tie! It's a push.")


# In[13]:


def repeat():
    play = ''
    while play not in ['y','n']:
        play = input('Keep playing? (y,n)')
    if play == 'y':
        return True 
    else:
        return False


# In[17]:


money = playermoney()
while True:
    
    deck = Deck()
    deck.shuffle_deck()
    playing = True
    
    player = Player()
    player.add(deck.deal())
    player.add(deck.deal())
    
    dealer = Player()
    dealer.add(deck.deal())
    
    dealer.add(deck.deal())
    
    
    print(f'You have {money.total} left.')
    
    take_bet(money)
        
    show_some(player,dealer)
    
    
    while playing:
        
        keep_hitting(deck,player)
        
        if not playing:
            break
        
        show_some(player,dealer)
    
        
        if player.value > 21:
            player_busts(money)
            break
            
    while not playing:
        show_all(player,dealer)
        while dealer.value < 17:
            dealer.add(deck.deal())
            print('Dealer hits.')
            show_all(player,dealer)
        if dealer.value > 21:
            dealer_busts(money)
            break
            
        if dealer.value == player.value:
            push()
            break
        elif dealer.value < player.value:
            player_wins(money)
            break
        else:
            dealer_wins(money)
            break
    
    if repeat():
        continue
    else:
        break
        
    break


# In[ ]:




